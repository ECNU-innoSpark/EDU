"""
TeaCH 推理主脚本
用法示例：
  # 跑单个模型
  python run.py --models claude-sonnet-4-6

  # 同时跑多个模型（并行）
  python run.py --models claude-sonnet-4-6 gemini-2.5-pro gpt-4o

  # 只跑指定数据集
  python run.py --models claude-sonnet-4-6 --datasets s1 s2

  # 断点续跑（默认行为，已完成的题自动跳过）
  python run.py --models claude-sonnet-4-6

  # 强制重跑所有题
  python run.py --models claude-sonnet-4-6 --force

输出路径：results/{model_name}/{dataset_name}.jsonl
每条记录 = 原始题目字段 + model_response（模型原始输出）
"""

import base64
import os
import sys
import time

from openai import OpenAI

from config import DATASET_DIR

# ── 路径 ─────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPTS_DIR)

from config import API_KEY, API_BASE
from inference.api_configs import MODEL_API_CONFIGS
from inference.api_configs import resolve_api_key
from inference.prompts import format_question

"""
所有待测模型的配置。

字段说明：
  multimodal  : 是否支持图片输入（含图题会附带图片）
  api_base    : 若为 None，使用 config.py 里的统一代理 API_BASE
                若指定，使用该模型自己的 API endpoint
  api_key_env : 若为 None，使用 config.py 里的 API_KEY
                若指定，从该环境变量读取 API key
                （也可在 config.py 里直接写 key，见下方说明）
"""

# ── 模型名称常量 ─────────────────────────────────────────────
class ModelName:
    # 本地测试
    MOCK                      = "mock"
    # Claude
    CLAUDE_HAIKU_4_5          = "claude-haiku-4-5"
    CLAUDE_SONNET_4_5         = "claude-sonnet-4-5"
    CLAUDE_SONNET_4_6         = "claude-sonnet-4-6"
    CLAUDE_OPUS_4_5           = "claude-opus-4-5"
    CLAUDE_OPUS_4_6           = "claude-opus-4-6"
    # Gemini
    GEMINI_2_0_FLASH          = "gemini-2.0-flash"
    GEMINI_2_5_FLASH          = "gemini-2.5-flash"
    GEMINI_2_5_PRO            = "gemini-2.5-pro"
    GEMINI_3_FLASH_PREVIEW    = "gemini-3-flash-preview"
    GEMINI_3_PRO_PREVIEW      = "gemini-3-pro-preview"
    GEMINI_3_1_PRO_PREVIEW    = "gemini-3.1-pro-preview"
    # GPT
    GPT_4O                    = "gpt-4o"
    GPT_4_1                   = "gpt-4.1"
    GPT_5                     = "gpt-5"
    GPT_5_2                   = "gpt-5.2"
    # Doubao
    DOUBAO_SEED_1_6_THINKING  = "doubao-seed-1-6-thinking-250715"
    # DeepSeek
    DEEPSEEK_CHAT             = "deepseek-chat"
    DEEPSEEK_REASONER         = "deepseek-reasoner"
    # Kimi
    # KIMI_K2_5                 = "kimi-k2.5"
    KIMI_K25                  = "Kimi-K25"
    # GLM
    GLM_5                     = "glm-5"
    GLM_4_6V                  = "glm-4.6v"
    # Qwen
    QWEN3_5_397B              = "qwen3.5-397b"
    QWEN3_6_35B               = "qwen3.6-35b"
    MINI_MAX_M_2_7                  = "MiniMax-M2.7"


# Keep the historical dict interface used by run.py and scoring scripts.
MODELS = {
    model_name: model_config.to_legacy_dict()
    for model_name, model_config in MODEL_API_CONFIGS.items()
}

# ── 客户端抽象 ───────────────────────────────────────────────

class BaseMLLM:
    @classmethod
    def create(cls, model_name: str) -> "BaseMLLM":
        """工厂方法：根据模型名返回对应的客户端实例"""
        cfg = MODELS.get(model_name, {})
        base = cfg.get("api_base") or API_BASE
        key_env = cfg.get("api_key_env")
        if key_env:
            key = resolve_api_key(key_env)
            if not key:
                raise ValueError(
                    f"模型 {model_name} 需要 {key_env}，"
                    f"请在 config.py 里填写 {key_env} = 'your-key'"
                )
        else:
            key = API_KEY
        if model_name == ModelName.MOCK:
            key = key or "mock"
        return OpenAIMLLM(
            OpenAI(api_key=key, base_url=base),
            api_key=key,
            base_url=base,
            api_model=cfg.get("api_model"),
        )

    def call_with_content_list(self, model_name: str, content: list,
                               is_streaming: bool = False, disable_thinking=None) -> tuple[str, str | None]:
        """返回 (response_text, reasoning_text | None)"""
        raise NotImplementedError

    def call_model(self, model_name: str, question: dict,
                   multimodal: bool, is_streaming: bool = False) -> tuple[str, str | None, str]:
        """调用模型，返回 (response, reasoning, prompt)。失败时 response 为 '[ERROR] ...'"""
        prompt = format_question(question)
        content: list = []

        # 含图题：附上图片（仅多模态模型）
        if multimodal and question.get("has_image") and question.get("img"):
            img_path = os.path.join(DATASET_DIR, question["img"])
            with open(img_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
            })

        content.append({"type": "text", "text": prompt})

        for attempt in range(1, 4):
            try:
                response, reasoning = self.call_with_content_list(
                    model_name, content, is_streaming=is_streaming, disable_thinking=attempt > 1
                )
                return response, reasoning, prompt
            except Exception as e:
                err = str(e)
                print(f"    [{model_name}] 第{attempt}次失败：{type(e).__name__}: {err[:80]}")
                if attempt < 3:
                    time.sleep(5)
        return "[ERROR] 重试3次仍失败", None, prompt


class OpenAIMLLM(BaseMLLM):
    def __init__(self, openai_client: OpenAI, api_key: str = "", base_url: str = "", api_model: str | None = None):
        self._client = openai_client
        self._api_key = api_key
        self._base_url = base_url
        self._api_model = api_model

    def call_with_content_list(self, model_name: str, content: list, is_streaming=False, disable_thinking=None) -> tuple[str, str | None]:
        if is_streaming:
            streaming_result = self._call_openai_with_llm_evals(
                model_name=self._api_model or model_name,
                prompt=content,
                timeout=120,
                disable_thinking=disable_thinking,
                stream=True,
            )
            if streaming_result is not None:
                return streaming_result

        non_streaming_result = self._call_openai_with_llm_evals(
            model_name=self._api_model or model_name,
            prompt=content,
            timeout=120,
            disable_thinking=disable_thinking,
            stream=False,
        )
        if non_streaming_result is not None:
            return non_streaming_result

        request_kwargs = {
            "model": self._api_model or model_name,
            "messages": [{"role": "user", "content": content}],
            "timeout": 120,
        }
        if disable_thinking:
            request_kwargs["extra_body"] = {
                "thinking": {"type": "disabled"},
                "chat_template_kwargs": {"enable_thinking": False},
                "enable_thinking": False,
            }
        resp = self._client.chat.completions.create(**request_kwargs)
        msg = resp.choices[0].message
        return msg.content, getattr(msg, "reasoning_content", None)

    @staticmethod
    def _split_content(content: list) -> tuple[str, list[str]]:
        text_parts = []
        image_data_urls = []
        for part in content:
            if part.get("type") == "text":
                text_parts.append(part.get("text", ""))
            elif part.get("type") == "image_url":
                image_url = part.get("image_url") or {}
                url = image_url.get("url")
                if url:
                    image_data_urls.append(url)
        return "\n".join(text for text in text_parts if text), image_data_urls

    @staticmethod
    def _ensure_llm_evals_path():
        llm_evals_path = os.environ.get("LLM_EVALS_PATH", "/Users/l/klee_code/git_repos/llm_evals")
        if llm_evals_path and os.path.isdir(llm_evals_path) and llm_evals_path not in sys.path:
            sys.path.insert(0, llm_evals_path)

    def _call_openai_with_llm_evals(
            self,
            model_name: str,
            prompt: str | list,
            timeout: float,
            disable_thinking=None,
            stream: bool = True,
    ) -> tuple[str, str | None] | None:
        if model_name == ModelName.MOCK:
            text = next(
                (
                    "mock response with prompt: " + part.get("text", "")
                    for part in prompt
                    if isinstance(part, dict) and part.get("type") == "text"
                ),
                "",
            ) if isinstance(prompt, list) else "mock response with prompt: " + prompt
            return text, None

        try:
            self._ensure_llm_evals_path()
            from llm_common.llm_infer.call_by_single_instance import call_openai
            from llm_common.llm_infer.api_info.dataclass_ import ApiConfig
            from llm_common.llm_infer.instances import ChatCompletionRequest
            from llm_common.llm_infer.instances import LLMInferInputRecord
        except Exception:
            return None

        out = call_openai(LLMInferInputRecord(
                prompt=prompt,
                api=ApiConfig(
                        api_key=self._api_key,
                        base_url=self._base_url,
                        model=model_name,
                ),
                chat_completion_request=ChatCompletionRequest(
                        model=model_name,
                        stream=stream,
                ),
                timeout=timeout,
                do_print_one_response_per_line=False,
                disable_thinking=bool(disable_thinking),
        ))
        return out.llm_response, out.reasoning

            #
            #
test_png = '/Users/l/klee_code/git_repos/TeaCH-main/dataset/images/dummies_math_0018.png'
def main(*_args, **_kwargs):
    """测试 call_model：用统一 mock 调用路径覆盖各题型。"""
    sample_questions = [
        {"id": "q1", "type": "单项选择题",
         "question": "下列属于新课程改革核心理念的是？",
         "options": {"A": "知识本位", "B": "以学生发展为本", "C": "应试教育", "D": "教师中心"}},
        {"id": "q2", "type": "简答题",
         "question": '简述维果斯基"最近发展区"的含义及教育意义。'},
        {"id": "q3", "type": "材料分析题",
         "material": "某教师上课时发现学生注意力涣散……",
         "sub_questions": ["分析该教师课堂管理存在哪些问题？", "请提出改进建议。"]},
        {"id": "q4", "type": "教学设计题",
         "question": "请为初中数学《一元一次方程》设计一节课的教学方案。"},
        {"id": "q5", "type": "结构化面试",
         "question": "如果班级中有学生长期被同学孤立，你作为班主任会如何处理？"},
    ]

    # ── 多模态能力验证：用真实带图题调用 GEMINI_2_5_FLASH ──────────
    print("\n── 多模态测试 (GEMINI_2_5_FLASH) ─────────────────")
    test_img_q = {
        "id": "s3_senior_art_2013d_31",
        "type": "案例分析题",
        "sub_questions": [
            "(1)从教学目标、教学安排与教学方法三方面分析，张老师的教学存在哪些问题?(12 分)",
            "(2)张老师对读错字的解释合适吗?请作出判断，并说出你的建议。(8 分)",
        ],
        "has_image": True,
        "img": "images/s3_senior_art_2013d_31.jpg",
    }
    try:
        mm_client = BaseMLLM.create(ModelName.GEMINI_2_5_FLASH)
        response, reasoning, prompt = mm_client.call_model(
            ModelName.GEMINI_2_5_FLASH, test_img_q, multimodal=True
        )
        if response.startswith("[ERROR]"):
            print(f"  [FAIL] 多模态调用失败: {response}")
        else:
            print(f"  [PASS] 多模态调用成功，response前80字: {response[:80].replace(chr(10),' ')!r}")
    except Exception as e:
        print(f"  [SKIP] 多模态测试跳过（{type(e).__name__}: {e}）")
    print()


    client = BaseMLLM.create(ModelName.MOCK)
    passed = 0
    for q in sample_questions:
        response, reasoning, prompt = client.call_model("mock", q, multimodal=False)
        ok = response == "mock response with prompt: " + prompt and reasoning is None
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"  [{status}] {q['id']} ({q['type']})")
        print(f"         prompt前50字: {prompt[:50].replace(chr(10),' ')!r}")
        print(f"         response前50字: {response[:50].replace(chr(10),' ')!r}")

    print(f"\ncall_model 测试完成：{passed}/{len(sample_questions)} 通过")


if __name__ == "__main__":
    main()
