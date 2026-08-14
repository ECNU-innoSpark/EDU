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

import argparse
import base64
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from inference.prompts import get_prompt_candidates
from input_datasets.load import US_DATASETS

# ── 路径 ─────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPTS_DIR)

from inference import RESULTS_DIR
from inference.prompts import extract_prompt_fields
from config import API_BASE
from config import API_KEY
from config import DATASET_DIR


def _ensure_llm_evals_on_path():
    """Put the llm_evals package on sys.path (idempotent) and return it."""
    project_root = os.path.dirname(SCRIPTS_DIR)
    llm_evals_path = os.environ.get(
            "LLM_EVALS_PATH",
            os.path.join(project_root, "dependencies", "llm_evals"),
    )
    if not os.path.isdir(llm_evals_path):
        raise ImportError(f"LLM_EVALS_PATH 目录不存在: {llm_evals_path}")
    if llm_evals_path not in sys.path:
        sys.path.insert(0, llm_evals_path)
    return llm_evals_path


# ── 数据集定义 ───────────────────────────────────────────────
# name → glob pattern（相对于 dataset/）


def append_jsonl(record: dict, out_path: str):
    """追加一条记录到 JSONL 文件"""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# def merge_results_csv(models: list[str], dataset_names: list[str]):
#     """每个模型生成一个 results/{model}/all_results.csv，汇总该模型所有数据集"""
#     priority = ["id", "dataset", "model"]
#     tail = ["model_response", "reasoning"]
#     for model_name in models:
#         rows = []
#         for gname in dataset_names:
#             path = os.path.join(RESULTS_DIR, model_name, f"{gname}.jsonl")
#             if not os.path.exists(path):
#                 continue
#             with open(path, "r", encoding="utf-8") as f:
#                 for line in f:
#                     line = line.strip()
#                     if line:
#                         try:
#                             r.setdefault("dataset", gname)
#                             rows.append(r)
#                         except Exception:
#                             pass
#         if not rows:
#             continue
#         all_keys = list(dict.fromkeys(
#             priority
#             + [k for k in rows[0] if k not in priority and k not in tail]
#             + [k for k in tail if k in rows[0]]
#         ))
#         out = os.path.join(RESULTS_DIR, model_name, "all_results.csv")
#         with open(out, "w", encoding="utf-8", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=all_keys, extrasaction="ignore")
#             writer.writeheader()
#             writer.writerows(rows)
#         print(f"汇总 CSV → {out}  ({len(rows)} 条)")


def run_one(model_name: str, group_name: str, records: list[dict],
            force: bool = False, workers: int = 4, enrich: bool = False,
            is_streaming: bool = False, disable_thinking=None, log_frequency = 1) -> int:
    """
    对一个数据集跑一个模型的推理，断点续跑，多线程并行。
    返回本次新完成的题目数。
    """
    out_path = os.path.join(RESULTS_DIR, model_name + ('_nothink' if disable_thinking else ''), f"{group_name}.jsonl")
    print('*' * 50 + f'''\n{out_path}\n^^^(out_path)^^^\n''' + '''\nat:\nscripts/inference/run.py:114\n''' + '*' * 50)

    if not force:
        from inference.remove_erroring_results import purge_errors
        purge_errors(out_path)
    from inference.get_finished_results import load_done_ids
    done_ids = set() if force else load_done_ids(out_path)
    todo = [r for r in records if r.get("id", "") not in done_ids]

    if not todo:
        print(f"  [{model_name}/{group_name}] 全部 {len(records)} 题已完成，跳过")
        return 0

    streaming_text = "，streaming" if is_streaming else ""
    print(f"  [{model_name}/{group_name}] {len(todo)}/{len(records)} 题待跑（{workers}线程{streaming_text}）")

    try:
        _ensure_llm_evals_on_path()
        from llm_common.llm_infer.call_by_single_instance import call_openai
        from llm_common.llm_infer.api_info.dataclass_ import ApiConfig
        from llm_common.llm_infer.api_info.dataclass_ import config_for_model
        from llm_common.llm_infer.api_info.dataclass_ import model_is_multimodal
        from llm_common.llm_infer.instances import ChatCompletionRequest
        from llm_common.llm_infer.instances import LLMInferInputRecord
    except (AttributeError, ImportError) as error:
        print(f"  [SKIP] 无法加载 llm_evals: {error}")
        return 0

    multimodal = model_is_multimodal(model_name)

    # 用 llm_evals 的注册表解析 base_url / api_key / model，按真实 model 名与
    # model_alias 两路查找（如 Kimi-K25→kimi-k2.5、qwen3.6-35b→qwen）。
    api_config = config_for_model(model_name)
    if api_config is not None:
        api_base = api_config.base_url or API_BASE
        api_key = api_config.api_key or API_KEY
        api_model = api_config.model or model_name
    else:
        # 代理类模型（claude-*/gpt-*/部分 gemini-*/doubao-*/mock）走统一代理。
        api_base = API_BASE
        api_key = API_KEY
        api_model = model_name

    if model_name == "mock":
        api_key = api_key or "mock"
    elif not api_key:

        print(f"  [SKIP] 模型 {model_name} 缺少 API key")
        return 0

    completed = 0

    def process(q):
        prompt_candidates = get_prompt_candidates(q, model_name=model_name)
        content = []
        if multimodal and q.get("has_image") and q.get("img"):
            img_path = os.path.join(DATASET_DIR, q["img"])
            with open(img_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode()
            content.append({
                    "type"     : "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
            })

        response = "[ERROR] 重试3次仍失败"
        reasoning = None
        for attempt in range(1, 4):
            for prompt in prompt_candidates:
                try:
                    result = call_openai(
                            LLMInferInputRecord(
                                    prompt=content + [{"type": "text", "text": prompt}],
                                    api=ApiConfig(
                                            api_key=api_key,
                                            base_url=api_base,
                                            model=api_model,
                                    ),
                                    chat_completion_request=ChatCompletionRequest(
                                            model=api_model,
                                            stream=is_streaming,
                                            max_tokens=4096 if disable_thinking or 'qwen' in api_model.lower() else None,
                                    ),
                                    timeout=120,
                                    do_print_one_response_per_line=False,
                                    disable_thinking=disable_thinking or attempt > 1,
                            )
                    )
                    response = result.llm_response
                    reasoning = result.reasoning
                    break
                except Exception as error:
                    print(
                            f"    [{model_name}] 第{attempt}次失败："
                            f"{type(error).__name__}: {str(error)[:80]}"
                    )
                    if attempt < 3:
                        time.sleep(5)

        record = dict(q)
        record["model"] = model_name
        record["prompt"] = prompt
        if enrich:
            record.update(extract_prompt_fields(q))
        record["model_response"] = response
        record["reasoning"] = reasoning
        record.pop("_source_file", None)
        return record

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(process, q): q for q in todo}
        for fut in as_completed(futures):
            try:
                rec = fut.result()
                append_jsonl(rec, out_path)
                completed += 1
                if completed % log_frequency == 0 or completed == len(todo):
                    print(f"    [{model_name}/{group_name}] {completed}/{len(todo)} 完成")
            except Exception as e:
                q = futures[fut]
                print(f"    [{model_name}/{group_name}] 题 {q.get('id', '')} 异常：{e}")

    from inference.jsonl_to_csv import jsonl_to_csv
    jsonl_to_csv(out_path)
    print(f"  [{model_name}/{group_name}] 完成 {completed} 题 → {out_path}")
    return completed


def run_models(models: list[str], datasets: dict[str, list],
               force: bool = False, workers: int = 4,
               model_workers: int = 3, enrich: bool = False, disable_thinking=None) -> int:
    is_streaming = workers == 1
    if is_streaming:
        print("[INFO] model_workers=1，启用 streaming 调用")

    def run_model(current_model_name):
        done = 0
        current_model_disable_think  = disable_thinking
        from input_datasets.model_names import NO_THINK_SUFFIX
        if current_model_name.endswith(NO_THINK_SUFFIX):
            current_model_name = current_model_name[:-len(NO_THINK_SUFFIX)]
            current_model_disable_think  = True
        for gname, records in datasets.items():
            try:
                # if model name is like InternVL3_5-14B_nothink,
                done += run_one(current_model_name, gname, records,
                                force=force, workers=workers, enrich=enrich,
                                is_streaming=is_streaming, disable_thinking=current_model_disable_think)
            except Exception as e1:
                print(f"[ERROR] {current_model_name}/{gname} 失败：{e1}")
        return done

    total = 0
    with ThreadPoolExecutor(max_workers=model_workers) as pool:
        futures = {pool.submit(run_model, m): m for m in models}
        for fut in as_completed(futures):
            model_name = futures[fut]
            try:
                total += fut.result()
            except Exception as e:
                print(f"[ERROR] {model_name} 失败：{e}")
    return total


# ── 主入口 ───────────────────────────────────────────────────

def main():
    # --models mock --limit 1
    parser = argparse.ArgumentParser(description="TeaCH 推理跑分")
    from input_datasets.load import large_t1t2_models
    parser.add_argument("--models", nargs="+", default=["claude-sonnet-4-6"], help="模型名称，可指定多个（并行跑）")
    from input_datasets.load import DATASET_GROUPS
    parser.add_argument("--datasets", nargs="+",
                        default=[
                                "barrons"
                        ],
                        help=f"数据集组名，可选：{list(DATASET_GROUPS.keys())}")
    parser.add_argument("--force", action="store_true",
                        help="强制重跑，忽略已有结果")
    parser.add_argument("--disable_thinking", action="store_true",
                        help="强制disable_thinking", default=None)
    parser.add_argument("--limit", type=int, default=None,
                        help="每个数据集只跑前N题（测试用）")
    parser.add_argument("--workers", type=int, default=1,
                        help="每个模型的并发线程数（默认4）")
    parser.add_argument("--model_workers", type=int, default=1,
                        help="同时跑几个模型（默认3）")
    args = parser.parse_args()


    # 检查模型名（用 llm_evals 的注册表，替代本地 MODELS 表）
    try:
        _ensure_llm_evals_on_path()
        from llm_common.llm_infer.api_info.dataclass_ import is_known_model
        unknown = [m for m in args.models if not is_known_model(m)]
    except ImportError as error:
        print(f"[WARN] 无法加载 llm_evals 校验模型名：{error}")
        unknown = []
    if unknown:
        print(f"[WARN] 未知模型（仍会尝试调用）：{unknown}")

    from input_datasets.load import load_datasets
    datasets = load_datasets(args.datasets, limit=args.limit)
    total_questions = sum(len(v) for v in datasets.values())
    print(f"\n共 {len(datasets)} 个数据集，{total_questions} 题，{len(args.models)} 个模型\n")

    total_done = run_models(args.models, datasets,
                            force=args.force, workers=args.workers,
                            model_workers=args.model_workers, disable_thinking=args.disable_thinking)
    print(f"\n全部完成，本次新跑 {total_done} 题")
    # merge_results_csv(args.models, list(datasets.keys()))


if __name__ == "__main__":
    main()
