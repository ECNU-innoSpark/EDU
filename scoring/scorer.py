"""
LLM-as-Judge 评分执行器

使用指定的LLM模型对主观题进行评分，支持多个国家的教师认证考试。
"""

import json
import re
import logging
import os
import sys
from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod

from llm_common.llm_infer.instances import LLMInferResultRecord
from .judge_prompts import get_judge_prompt
from .scoring_rules import get_max_score

logger = logging.getLogger(__name__)


# ═════════════════════════════════════════════════════════════════════════
# 数据结构
# ═════════════════════════════════════════════════════════════════════════

@dataclass
class ScoringContext:
    """评分所需上下文：由题目直接确定，model_response 填入前的中间状态。"""
    question_id: str
    country: str
    subject: str
    question_type: str
    dataset: str
    max_score: float
    model_response: str
    scoring_prompt_without_model_response: str  # {model_response} 仍为占位符


@dataclass
class ScoringResult:
    """评分结果数据结构"""
    question_id: str
    score: float
    max_score: float
    percentage: float  # 得分百分比 (score / max_score * 100)
    judge_model: str  # 用于评分的LLM模型名称
    judge_response: str  # 评分模型的完整回复
    reasoning: str  # 评分理由（从响应中提取）
    country: str  # 国家代码 (china/usa/france/india)
    subject: str  # 科目 (s1/s2/s3/praxis/capes等)
    question_type: str  # 题型 (材料分析题/教学设计题等)
    dataset: str  # 数据集名称

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return asdict(self)

    def to_json(self) -> str:
        """转换为JSON字符串"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


# ═════════════════════════════════════════════════════════════════════════
# LLM客户端接口
# ═════════════════════════════════════════════════════════════════════════

class LLMClient(ABC):
    """LLM客户端抽象基类"""

    def __init__(self, model: str, api_base: Optional[str] = None, api_key: Optional[str] = None):
        self.model = model
        self.api_base = api_base
        self.api_key = api_key

    @abstractmethod
    def call(self, prompt: str, max_tokens: int = 8192) -> str:
        """
        调用LLM API获取评分结果

        参数：
            prompt: 完整的评分提示词
            max_tokens: 最大输出token数

        返回：
            LLM的文本响应
        """
        pass


class MockLLMClient(LLMClient):
    """本地测试用客户端，从 prompt 中提取满分，返回固定60%得分字符串，不发 HTTP 请求。"""
    RATIO = 0.6

    def __init__(self):
        super().__init__(model="mock")

    def call(self, prompt: str, max_tokens: int = 8192) -> str:
        # 从格式化后的 prompt 里提取满分（中文：满分：X 分 / 英文：out of X）
        m = re.search(r'满分[：:]\s*(\d+(?:\.\d+)?)', prompt)
        if not m:
            m = re.search(r'out of\s+(\d+(?:\.\d+)?)', prompt, re.IGNORECASE)
        max_score = float(m.group(1)) if m else 10.0
        score = round(max_score * self.RATIO, 1)
        return f"得分：{score}\n理由：mock评分（测试用，固定返回满分的{int(self.RATIO * 100)}%）"


class OpenAICompatibleClient(LLMClient):
    """兼容OpenAI API的客户端（Claude、Gemini、GPT等）"""

    def __init__(self, model: str, api_base: Optional[str] = None, api_key: Optional[str] = None):
        super().__init__(model, api_base, api_key)
        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=api_key or "",
                base_url=api_base
            )
        except ImportError:
            logger.error("openai库未安装，请运行: pip install openai")
            raise

    def call(self, prompt: str, max_tokens: int = 16384) -> str:
        """调用兼容OpenAI API的LLM"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一位专业的教师资格证阅卷教师，擅长按照标准评分。"},
                    {"role": "user", "content": prompt}
                ],
                # max_tokens=5000,
                temperature=0.3,  # 较低温度以获得更一致的评分
            )
            # 打印原始响应，方便调试
            import sys
            print(f"\n{'='*60}", file=sys.stderr)
            print(f"[RAW RESPONSE] model={self.model}", file=sys.stderr)
            print(f"choices数量: {len(response.choices)}", file=sys.stderr)
            msg = response.choices[0].message
            print(f"msg.role: {msg.role}", file=sys.stderr)
            print(f"msg.content: {repr(msg.content)[:200]}", file=sys.stderr)
            print(f"msg.content类型: {type(msg.content)}", file=sys.stderr)
            # 检查所有可能的字段
            for attr in ['reasoning_content', 'reasoning', 'tool_calls', 'function_call', 'refusal']:
                val = getattr(msg, attr, 'NOT_FOUND')
                if val != 'NOT_FOUND':
                    print(f"msg.{attr}: {repr(val)[:200]}", file=sys.stderr)
            # 打印finish_reason
            print(f"finish_reason: {response.choices[0].finish_reason}", file=sys.stderr)
            print(f"{'='*60}\n", file=sys.stderr)

            content = msg.content or ""
            # 思考模型（如Qwen3.5）可能把内容放在reasoning_content里
            reasoning = getattr(msg, "reasoning_content", None) or ""
            # 优先用content，content为空则用reasoning_content
            return content if content.strip() else reasoning
        except Exception as e:
            logger.error(f"调用LLM API失败: {e}")
            raise


# ═════════════════════════════════════════════════════════════════════════
# 评分提取器
# ═════════════════════════════════════════════════════════════════════════

class ScoreExtractor:
    """从LLM响应中提取评分和理由"""

    @staticmethod
    def extract_score(response: str, max_score: float) -> Optional[float]:
        """
        从评分响应中提取数字分数

        支持多种格式，并优先处理回复开头的内容
        """
        if not response:
            return None

        # 清洗掉一些可能干扰的字符（如粗体 **、花括号 {1} → 1）
        clean_response = response.replace("**", "").strip()
        # 处理 LLM 输出 Score: {1} 或 得分：{8} 等带花括号的格式
        clean_response = re.sub(r'\{(\d+(?:\.\d+)?)\}', r'\1', clean_response)

        # 1. 优先尝试匹配开头的数字（针对我们新加的"第一行给出得分"的要求）
        # 匹配：得分：15 或 15分 或 开头直接是 15
        first_line = clean_response.split('\n')[0].strip()
        first_line_match = re.search(r'(?:得分|分数|Score|评分)[：:]?\s*(\d+(?:\.\d+)?)', first_line)
        if first_line_match:
            score = float(first_line_match.group(1))
            return min(score, max_score)

        # 2. 如果第一行没找到，但在全文中找到了明确的格式
        patterns = [
            r"得分[：:]\s*(\d+(?:\.\d+)?)",
            r"分数[：:]\s*(\d+(?:\.\d+)?)",
            r"[Ss]core[：:]\s*(\d+(?:\.\d+)?)",
            r"评分[：:]\s*(\d+(?:\.\d+)?)",
            r"(\d+(?:\.\d+)?)\s*分",
        ]

        for pattern in patterns:
            match = re.search(pattern, clean_response)
            if match:
                score = float(match.group(1))
                if 0 <= score <= max_score * 1.2:  # 容忍一定的偏差
                    return min(score, max_score)

        return None

    @staticmethod
    def extract_reasoning(response: str) -> str:
        """
        从评分响应中提取理由

        查找"理由"、"原因"、"说明"等字段后的内容
        """
        patterns = [
            r"理由[：:]\s*(.+?)(?=\n\n|$)",
            r"原因[：:]\s*(.+?)(?=\n\n|$)",
            r"说明[：:]\s*(.+?)(?=\n\n|$)",
            r"[Rr]easoning[：:]\s*(.+?)(?=\n\n|$)",
        ]

        for pattern in patterns:
            match = re.search(pattern, response, re.DOTALL)
            if match and match.group(1):
                reasoning = match.group(1).strip()
                # 限制理由长度
                return reasoning[:500]

        # 如果没有找到明确的理由字段，返回前300个字符
        return response[:300]


# ═════════════════════════════════════════════════════════════════════════
# 核心评分器
# ═════════════════════════════════════════════════════════════════════════

def _build_question_text(record: dict, dataset_group: str) -> str:
    """根据数据集类型，从记录中组装题目文本"""
    # 试讲类数据：字段是 lesson_title / content / requirements，没有 question
    if dataset_group in ("shijian", "shijian_capes"):
        parts = []
        if record.get("lesson_title"):
            parts.append(f"课题：{record['lesson_title']}")
        if record.get("subject"):
            parts.append(f"学科：{record['subject']}")
        if record.get("content"):
            parts.append(f"教学内容：\n{record['content']}")
        if record.get("requirements"):
            reqs = record["requirements"]
            if isinstance(reqs, list):
                reqs = "\n".join(f"  {i+1}. {r}" for i, r in enumerate(reqs))
            parts.append(f"教学要求：\n{reqs}")
        return "\n".join(parts)

    # 法国 CAPES 笔试数据：字段是 question_text
    if dataset_group == "capes":
        parts = []
        if record.get("subject"):
            parts.append(f"学科：{record['subject']}")
        if record.get("question_text"):
            parts.append(f"题目：\n{record['question_text']}")
        return "\n".join(parts)

    # 面试类数据
    if dataset_group == "interview":
        return record.get("question") or record.get("content") or ""

    # 常规笔试
    return record.get("question") or record.get("material", "")


def _build_reference_answer(record: dict, dataset_group: str) -> str:
    """根据数据集类型，从记录中组装参考答案"""
    def _to_str(val):
        """确保返回值为字符串"""
        if isinstance(val, list):
            return ", ".join(str(v) for v in val)
        return str(val) if val is not None else ""

    if dataset_group in ("shijian", "shijian_capes"):
        return _to_str(record.get("reference_plan") or record.get("answer", ""))
    # 法国 CAPES 笔试：参考答案在 report_analysis 字段
    if dataset_group == "capes":
        return _to_str(record.get("report_analysis") or record.get("reference_answer") or record.get("answer", ""))
    return _to_str(record.get("reference_answer") or record.get("answer", ""))


def _build_question_context(
        template: str,
    question: str,
    reference_answer: str,
    max_score: float,
    material: Optional[str] = None,
    dimensions: Optional[str] = None,
    reference_standards: Optional[str] = None,
) -> str:
    """
    第一步：填入由题目直接确定的字段，{model_response} 保留为占位符。

    可在不知道模型回答的情况下预先构建，便于缓存或批量复用。
    """
    replacements = {
        "{question}": question,
        "{reference_answer}": reference_answer,
        "{max_score}": str(max_score),
        "{得分数字}": "",  # 输出占位符，由LLM填写
        "{简要说明}": "",  # 输出占位符，由LLM填写
    }
    if material:
        replacements["{material}"] = material
    if dimensions:
        replacements["{dimensions}"] = dimensions
    if reference_standards:
        replacements["{reference_standards}"] = reference_standards

    prompt = template
    for key, value in replacements.items():
        if key in prompt:
            prompt = prompt.replace(key, value)
    return prompt


def get_scoring_context(dataset_group: str, record: dict) -> ScoringContext:
    from scoring.scoring_rules import DATASET_META
    meta = DATASET_META.get(dataset_group, {"country": "china", "subject": dataset_group})
    qtype = record.get("type", "")
    qid = record.get("id", "")
    question = _build_question_text(record, dataset_group)
    ref_answer = _build_reference_answer(record, dataset_group)
    has_reference = bool(ref_answer and str(ref_answer).strip())
    source_exam = record.get("source_exam", "")
    question_type_original = record.get("question_type_original", "")
    question_id = qid
    country = meta["country"]
    subject = meta["subject"]
    question_type = qtype
    dataset = dataset_group
    question = question
    model_response = record.get("model_response", "")
    reference_answer = ref_answer
    material = record.get("material")
    has_reference = has_reference
    source_exam = source_exam
    question_type_original = question_type_original
    max_score = get_max_score(dataset, question_type, question_text=question)
    if max_score is None:
        error_msg = f"无法获取满分: dataset={dataset}, question_type={question_type}"
        logger.warning(error_msg)
        raise ValueError(error_msg)

    # 2. 获取评分提示词模板
    judge_prompt_template = get_judge_prompt(country, subject, question_type, has_reference=has_reference,
                                             source_exam=source_exam, question_type_original=question_type_original)
    if judge_prompt_template is None:
        error_msg = f"无法获取提示词: country={country}, subject={subject}, question_type={question_type}"
        logger.warning(error_msg)
        raise ValueError(error_msg)

    # 3. 格式化提示词
    try:
        scoring_prompt_without_model_response = _build_question_context(
                judge_prompt_template, question, reference_answer, max_score,
                material, None, None,
        )
    except KeyError as e:
        logger.error(f"提示词格式化失败: {e}")
        raise e

    return ScoringContext(
        question_id=question_id,
        country=country,
        subject=subject,
        question_type=question_type,
        dataset=dataset,
        max_score=max_score,
        model_response=model_response,
        scoring_prompt_without_model_response=scoring_prompt_without_model_response,
    )


JUDGES_NAME = [
        "Kimi-K25",
        "qwen3.5-397b",
        "glm-4.6v",
]
    # ["qwen3.5-397b", "Kimi-K25", "glm-4.6v"]

class TeachScorer:
    """
    TeaCH基准教师认证考试评分器

    支持：
    - 中国 NTCE（科目一/二/三、结构化/试讲）
    - 美国 Praxis/edTPA
    - 法国 CAPES
    - 印度 NTCE（MCQ-only，无需评分）
    """

    def __init__(
        self,
        judge_model: str,
        api_base: Optional[str] = None,
        api_key: Optional[str] = None,
        max_retries: int = 3,
        use_direct_call_openai: bool = True,
    ):
        """
        初始化评分器

        参数：
            judge_model: 用于评分的模型名称 (如 "kimi-k2.5", "qwen3.5-397b")
            api_base: API基础URL（可选，默认使用代理）
            api_key: API密钥（可选，从环境变量读取）
            max_retries: 失败重试次数
        """
        self.judge_model = judge_model
        self.max_retries = max_retries
        self.api_base = api_base
        self.api_key = api_key
        self.use_direct_call_openai = use_direct_call_openai and judge_model != "mock"
        self.llm_client = self._create_llm_client(judge_model, api_base, api_key)
        self.score_extractor = ScoreExtractor()

    def _create_llm_client(
        self,
        model: str,
        api_base: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> LLMClient:
        """创建合适的LLM客户端"""
        # 这里可以根据模型类型选择不同的客户端
        # 目前所有模型都使用OpenAI兼容接口
        return OpenAICompatibleClient(model, api_base, api_key)

    @staticmethod
    def _ensure_llm_evals_path() -> None:
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        llm_evals_path = os.environ.get(
            "LLM_EVALS_PATH",
            os.path.join(project_root, "dependencies", "llm_evals"),
        )
        if llm_evals_path and os.path.isdir(llm_evals_path) and llm_evals_path not in sys.path:
            sys.path.insert(0, llm_evals_path)

    def _call_judge_llm(self, prompt: str, do_stream=False) -> LLMInferResultRecord:
        if not self.use_direct_call_openai:
            return self.llm_client.call(prompt)

        self._ensure_llm_evals_path()
        from llm_common.llm_infer.api_info.dataclass_ import ApiConfig
        from llm_common.llm_infer.call_by_single_instance import call_openai
        from llm_common.llm_infer.instances import ChatCompletionRequest
        from llm_common.llm_infer.instances import LLMInferInputRecord

        result = call_openai(LLMInferInputRecord(
            prompt=prompt,
            system_input="你是一位专业的教师资格证阅卷教师，擅长按照标准评分。",
            api=ApiConfig(
                api_key=self.api_key or "",
                base_url=self.api_base or "",
                model=self.judge_model,
            ),
            chat_completion_request=ChatCompletionRequest(
                model=self.judge_model,
                stream=do_stream,
            ),
            timeout=120,
            do_print_one_response_per_line=False,
        ))
        return result

    def score_question(
        self,
        record: dict, dataset_group: str,
        # question_id: str,
        # country: str,
        # subject: str,
        # question_type: str,
        # dataset: str,
        # question: str,
        # model_response: str,
        # reference_answer: str,
        # material: Optional[str] = None,
        # dimensions: Optional[str] = None,
        # reference_standards: Optional[str] = None,
        # has_reference: bool = True,
        # source_exam: str = "",
        # question_type_original: str = "",
        do_stream=None,
    ) -> Optional[ScoringResult]:
        """
        对单个问题进行评分

        参数：
            question_id: 问题ID
            country: 国家代码 ("china", "usa", "france", "india")
            subject: 科目 ("s1", "s2", "s3", "praxis", "capes" 等)
            question_type: 题型 ("材料分析题", "教学设计题" 等)
            dataset: 数据集名称
            question: 题目文本
            model_response: 模型的作答
            reference_answer: 参考答案或评分标准
            material: （可选）材料/背景信息
            dimensions: （可选）评分维度
            reference_standards: （可选）参考标准
            has_reference: 是否有参考答案（影响prompt选择）
            source_exam: （可选）数据来源考试编号（如 "praxis_5623"）
            question_type_original: （可选）原始题型标记

        返回：
            ScoringResult 对象，如果评分失败则返回 None
        """
        # 1. 获取评分规则（满分）

        ctx = get_scoring_context(dataset_group, record)
        country, dataset, max_score, model_response, question_id, question_type, scoring_prompt_without_model_response, subject = (
            ctx.country, ctx.dataset, ctx.max_score, ctx.model_response,
            ctx.question_id, ctx.question_type, ctx.scoring_prompt_without_model_response, ctx.subject,
        )

        try:
            formatted_prompt = scoring_prompt_without_model_response.replace("{model_response}", model_response)
        except KeyError as e:
            logger.error(f"提示词格式化失败: {e}")
            return None


        # 4. 调用LLM进行评分（带重试）
        last_error = None
        logger.debug(f"[{question_id}] 开始调用LLM, 模型={self.judge_model}, 提示词长度={len(formatted_prompt)}")

        for attempt in range(self.max_retries):
            try:
                # judge_response = self.llm_client.call(formatted_prompt)
                result = self._call_judge_llm(formatted_prompt, do_stream)
                if not result.llm_response:
                    logger.warning(f"[{question_id}] LLM返回空字符串")
                    continue
                break
            except Exception as e:
                last_error = str(e)
                logger.warning(f"[{question_id}] 评分尝试 {attempt + 1}/{self.max_retries} 失败: {e}")
                if attempt == self.max_retries - 1:
                    error_msg = f"LLM调用失败({self.max_retries}次): {last_error[:100]}"
                    logger.error(f"问题 {question_id} {error_msg}")
                    raise RuntimeError(error_msg)

        if result.llm_response is None or not result.llm_response.strip():
            raise RuntimeError(f"LLM返回为空或只有空白（长度={len(result.llm_response) if result.llm_response else 0}）")

        # 5. 从响应中提取评分和理由
        score = self.score_extractor.extract_score(result.llm_response, max_score)
        if score is None:
            error_msg = f"无法提取分数 (回复前200字: {result.llm_response[:200]})"
            logger.warning(f"{error_msg} (问题ID: {question_id})")
            raise ValueError(error_msg)

        reasoning = self.score_extractor.extract_reasoning(result.llm_response) + '\n---\n' + (result.reasoning or '')

        # 6. 构建结果对象
        percentage = (score / max_score * 100) if max_score > 0 else 0

        return ScoringResult(
            question_id=question_id,
            score=score,
            max_score=max_score,
            percentage=percentage,
            judge_model=self.judge_model,
            judge_response=result.llm_response,
            reasoning=reasoning,
            country=country,
            subject=subject,
            question_type=question_type,
            dataset=dataset,
        )

    def score_batch(
        self,
        questions: list[Dict[str, Any]],
    ) -> list[Optional[ScoringResult]]:
        """
        批量评分多个问题

        参数：
            questions: 问题列表，每个问题是包含以下字段的字典：
                - question_id: str
                - country: str
                - subject: str
                - question_type: str
                - dataset: str
                - question: str
                - model_response: str
                - reference_answer: str
                - material: Optional[str]
                - dimensions: Optional[str]
                - reference_standards: Optional[str]

        返回：
            ScoringResult 列表（失败的项为 None）
        """
        results = []
        for i, q in enumerate(questions):
            logger.info(f"评分进度: {i + 1}/{len(questions)}")
            result = self.score_question(**q)
            results.append(result)

        return results


# ═════════════════════════════════════════════════════════════════════════
# Mock 评分器（本地测试用，不发起真实 API 调用）
# ═════════════════════════════════════════════════════════════════════════

class MockTeachScorer(TeachScorer):
    """
    本地测试用评分器：走完整 score_question() 路径，仅替换 LLM HTTP 调用。

    命中路径：get_max_score → get_judge_prompt → _format_prompt → MockLLMClient.call
              → ScoreExtractor.extract_score → ScoringResult
    """

    def __init__(self):
        self.judge_model = "mock"
        self.max_retries = 1
        self.api_base = None
        self.api_key = None
        self.use_direct_call_openai = False
        self.score_extractor = ScoreExtractor()
        self.llm_client = MockLLMClient()
