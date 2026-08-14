"""
主观题评分统一入口脚本（LLM-as-Judge）

功能：
  - 对 results/{model}/{dataset}.jsonl 中的主观题进行评分
  - 支持并发评分、断点续评
  - 统一调用 scoring 包中的逻辑

用法：
    python -m scripts.scoring.run_scoring                    # 对所有模型所有数据集评分
    python -m scripts.scoring.run_scoring --model qwen3.5-397b  # 指定被评分的模型
    python -m scripts.scoring.run_scoring --dataset s1 s2      # 指定被评分的数据集
    python -m scripts.scoring.run_scoring --limit 10          # 每组限制评分数量
    python -m scripts.scoring.run_scoring --workers 8         # 指定每个数据集评分线程数
    python -m scripts.scoring.run_scoring --force             # 强制重跑已评过的题

输出：
    results/{model}/{dataset}_scored.jsonl
"""

import argparse
import json
import logging
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# ── 路径配置 ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from scoring.scorer import JUDGES_NAME
from scoring.scorer import TeachScorer, MockTeachScorer
from scoring.scoring_rules import SUBJECTIVE_TYPES
import config as cfg

# ── 配置 ──────────────────────────────────────────────────────────────
RESULTS_DIR = os.path.join(ROOT_DIR, "results")
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)
LOG_PATH = f"{os.path.abspath(__file__)}.log"


def _ensure_realtime_file_logging() -> str:
    """Mirror logger output to ``<this script>.log`` without buffering lines."""
    normalized_log_path = os.path.abspath(LOG_PATH)
    for handler in logger.handlers:
        if (
                isinstance(handler, logging.FileHandler)
                and os.path.abspath(handler.baseFilename) == normalized_log_path
        ):
            return normalized_log_path

    file_handler = logging.FileHandler(
            normalized_log_path,
            mode="a",
            encoding="utf-8",
            delay=False,
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
            logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    )
    logger.addHandler(file_handler)
    return normalized_log_path

judge_response_field = "judge_response"
judge_reasoning_field = "reasoning"
judge_percentage_field = "percentage"
judge_score_field = "score"
judge_max_score_field = "max_score"
judger_model_field = "judge_model"

JUDGE_FIELDS = [
    judger_model_field,
    judge_percentage_field,
    judge_score_field,
    judge_reasoning_field,
    judge_response_field,
]
# ── 核心逻辑 ──────────────────────────────────────────────────────────

def get_judge_scorer(judge_model: str):
    """创建评分器，自动获取API配置"""


    from llm_common.llm_infer.api_info.dataclass_ import apiconfig_for_model
    if judge_model == "mock":
        return MockTeachScorer()
    # if judge_model == "qwen3.5-397b":
    #     api_base = cfg.QWEN_BASE
    #     api_key = cfg.QWEN_KEY
    # elif judge_model in ["Kimi-K25", "kimi-k2.5"]:
    #     api_base = cfg.KIMI_BASE
    #     api_key = cfg.KIMI_KEY
    #     judge_model = cfg.KIMI_MODEL
    # elif judge_model == "glm-4.6v":
    #     api_base = cfg.GLM46V_BASE
    #     api_key = cfg.GLM46V_KEY
    else:
        apiconfig = apiconfig_for_model(judge_model)
        # cfg_model = MODELS.get(judge_model, {})
        # api_base = cfg_model.get("api_base") or cfg.API_BASE
        # key_env = cfg_model.get("api_key_env")
        # if key_env:
        #     api_key = getattr(cfg, key_env, None) or os.environ.get(key_env)
        # else:
        api_key = cfg.API_KEY

    return TeachScorer(apiconfig.model, api_base=apiconfig.base_url, api_key=apiconfig.api_key)

def is_subjective(record: dict) -> bool:
    """判断记录是否为主观题"""
    qtype = record.get("type", "")
    for subjective_list in SUBJECTIVE_TYPES.values():
        if qtype in subjective_list:
            # 额外检查：Praxis中部分"Constructed-Response"标记的题实际是MCQ
            # 如果answer字段是单字母(A/B/C/D等)，说明是选择题误标，不是构造题
            # 这个是抽取错误
            # answer_raw = record.get("answer", "")
            # 处理列表类型的答案（如 ['A', 'D']）
            # if isinstance(answer_raw, list):
            #     if all(str(a).upper() in ["A","B","C","D","E","F"] for a in answer_raw):
            #         return False
            # else:
            #     answer = str(answer_raw)
            #     if answer and len(answer) <= 3 and answer.upper() in ["A","B","C","D","E","F","AB","AC","AD","BC","BD","CD"]:
            #         return False
            return True
    return False

def get_dataset_group(jsonl_path: str) -> str:
    """从文件名推导数据集分组"""
    fname = os.path.basename(jsonl_path)
    for group_name in SUBJECTIVE_TYPES.keys():
        if fname.startswith(group_name):
            return group_name
    return None


def get_score_workers(judge_model: str) -> int:
    """Per-dataset scoring concurrency for one judge.

    The outer --parallel controls how many model/dataset tasks run at once.
    GLM is less stable under concurrent chat requests, so keep its inner
    per-dataset worker count at 1 even when outer parallelism is higher.
    """
    judge = judge_model.lower()
    if judge_model == "mock":
        return 1
    if "glm" in judge:
        return 1
    if "qwen" in judge:
        return 1
    if "kimi" in judge.lower():
        return 1
    return 3


def score_record(scorer: TeachScorer, record: dict, dataset_group: str, do_stream=None) -> dict:
    """对单条记录进行评分"""
    if record.get("scored"):
        return record

    try:
        # max_score = get_max_score(dataset_group, qtype, question_text=question)
        # if max_score is None:
        #     record["scored"] = False
        #     record["score_error"] = f"获取满分失败: dataset={dataset_group}, qtype={qtype}"
        #     return record

        result = scorer.score_question(
                record=record,
                dataset_group=dataset_group,
                do_stream=do_stream,
        )

        if result:
            record["scored"] = True
            record[judge_score_field] = result.score
            record[judge_max_score_field] = result.max_score
            record[judge_percentage_field] = result.percentage
            record[judger_model_field] = result.judge_model


            record[judge_response_field] = result.judge_response
            record[judge_reasoning_field] = result.reasoning

    except Exception as e:
        record["scored"] = False
        record["score_error"] = str(e)
        breakpoint()

    # 打印结果（单独try，不影响评分结果）
    # try:
    #     if record.get("scored"):
    #         print(f"      [OK] {qid:<15} | {record['score']:>4}/{record['max_score']:<4} | {str(record.get('reasoning',''))[:50]}", flush=True)
    #     elif record.get("score_error"):
    #         print(f"      [ERR] {qid:<15} | {record['score_error'][:50]}", flush=True)
    # except Exception:
    #     pass

    return record

def process_dataset(
        model_name: str,
        dataset_group: str,
        judge_model: str,
        force: bool = False,
        limit: int = None,
        workers: int = None,
):
    """处理单个模型的单个数据集"""
    model_inference_file_path = os.path.join(RESULTS_DIR, model_name, f"{dataset_group}.jsonl")
    # 修改点：文件名包含 judge_model，实现独立存档
    output_path = get_scoring_output(model_name, dataset_group, judge_model)

    if not os.path.exists(model_inference_file_path):
        return 0

    # 加载数据
    records = []
    with open(model_inference_file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                from input_datasets.blacklist_reason import get_blacklisted_reason
                r = json.loads(line)
                from input_datasets.load import normalize_record_for_filter
                if get_blacklisted_reason(normalize_record_for_filter(r, dataset=dataset_group, ispreparingblacklist=1)):
                    continue

                records.append(r)

    # 过滤出主观题
    subjective_records = [r for r in records if is_subjective(r)]
    if not subjective_records:
        return 0

    id2model_response = {}
    id2subjective_record = {}
    duplidated_response_id2count = {}
    for r in subjective_records:
        id_ = (r.get("id"))
        if id_ in id2model_response:
            if id_ in duplidated_response_id2count:
                duplidated_response_id2count[id_]  += 1
            else:
                duplidated_response_id2count[id_] = 2
        id2model_response[id_] = r.get("model_response")
        id2subjective_record[r.get("id")] = r
    # 输入 JSONL 也是 append-only；同一 ID 仅评分最后生成的回答。

    # 加载已评分数据（断点续评）
    subjective_records = list(id2subjective_record.values())
    deprecated_ids = set()
    if os.path.exists(output_path) and not force:
        with open(output_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    if r.get("scored"):
                        record_id = r.get("id")
                        if record_id not in id2model_response:
                            continue
                        original_response = id2model_response.get(record_id)
                        scored_response = r.get("model_response")
                        # record_id not in id2model_response
                        if (
                                scored_response != original_response and bool(scored_response)
                        ):
                            # depcreate
                            print(model_inference_file_path)
                            print(scored_response[-100:])
                            print(original_response[-100:])
                            deprecated_ids.add(record_id)
                        # also make sure the 'model_response' field is the same as the one in record with the same id
    if deprecated_ids:
        print('*' * 50 + f'''\n{len(records),deprecated_ids}\n^^^(len(records),deprecated_ids)^^^\n''' + '''\nat:\nscripts/scoring/run_scoring.py:238\n''' + '*' * 50)

        # write to output_path with the new file without deprecated_ids
        temporary_output_path = f"{output_path}.remove-deprecated.tmp"
        try:
            with open(output_path, "r", encoding="utf-8") as source_file, open(
                    temporary_output_path,
                    "w",
                    encoding="utf-8",
            ) as temporary_file:
                for line in source_file:
                    if not line.strip():
                        continue
                    scored_record = json.loads(line)
                    if scored_record.get("id") in deprecated_ids:
                        continue
                    temporary_file.write(line)
            os.replace(temporary_output_path, output_path)
        finally:
            if os.path.exists(temporary_output_path):
                os.remove(temporary_output_path)


    id2scored_response = {}
    if os.path.exists(output_path) and not force:
        with open(output_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    if r.get("scored"):
                        id2scored_response[r.get('id')] = r

    to_score = []
    for r in subjective_records:
        if (
                not force
                and id2scored_response.get(r.get("id"), None)
        ):
            continue
        to_score.append(r)

    if limit:
        to_score = to_score[:limit]

    if not to_score:
        logger.info(f"  [SKIPPED] {model_name}/{dataset_group}/{judge_model}: 没有需要评分的题目")
        return 0

    # force 模式下清空输出文件，避免 append 造成重复
    if force and os.path.exists(output_path):
        open(output_path, "w").close()

    scorer = get_judge_scorer(judge_model)
    scored_count = 0

    # 使用线程池并发评分，逐条追加写入（实时可见进度）
    write_lock = threading.Lock()
    max_workers = workers or get_score_workers(judge_model)
    # log to __file__.log, in real time , as fast as printing to console
    _ensure_realtime_file_logging()
    logger.info(
        f"  [START] {model_name}/{dataset_group}: 待评分 {len(to_score)} 题 "
        f"(judge={judge_model}, workers={max_workers}) duplidated_response_id2count {duplidated_response_id2count}， {model_inference_file_path}-model_inference_file_path"
    )
    do_stream = max_workers == 1
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_record = {executor.submit(score_record, scorer, r, dataset_group, do_stream): r for r in to_score}
        for future in as_completed(future_to_record):
            source_record = future_to_record[future]
            try:
                result = future.result()
            except Exception as e:
                qid = source_record.get("id") or source_record.get("question_id")
                logger.exception(f"  [ERROR] {model_name}/{dataset_group}/{qid}: scoring future failed")
                result = dict(source_record)
                result["scored"] = False
                result["score_error"] = str(e)
            scored_count += 1
            # 逐条追加写入，进度监控可实时看到
            with write_lock:
                with open(output_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(result, ensure_ascii=False) + "\n")

    logger.info(f"  [DONE] {model_name}/{dataset_group}: 已保存至 {os.path.basename(output_path)}")
    return len(to_score)


def get_scoring_output(model_name: str, dataset_group: str, judge_model: str=JUDGES_NAME[0]) -> str:
    output_path = os.path.join(RESULTS_DIR, model_name, f"{dataset_group}_scored_by_{judge_model}.jsonl")
    return output_path


def _process_task(task_args):
    """供进程池调用的包装函数"""
    model_name, dataset_group, judge_model, force, limit, workers = task_args
    try:
        return model_name, dataset_group, process_dataset(
                model_name, dataset_group, judge_model, force, limit, workers
        )
    except Exception as e:
        logger.exception(f"  [FAIL] {model_name}/{dataset_group}")
        logger.error(f"  [FAIL] {model_name}/{dataset_group}: {e}")
        return model_name, dataset_group, 0


def main():
    _ensure_realtime_file_logging()
    parser = argparse.ArgumentParser(description="主观题评分脚本")
    from input_datasets.load import current_models
    from input_datasets.load import large_t1t2_models
    parser.add_argument("--model", nargs="+", help="被评分的模型名 (文件夹名)",
                        default=current_models[:]
                        )
    parser.add_argument("--dataset", nargs="+", help="数据集分组名 (如 s1 s2)",
                        default=[
                                # "s2"
                        ]
                        )
    from llm_common.llm_infer.api_info.dataclass_ import QWEN35_397B_CURRENT
    from llm_common.llm_infer.api_info.dataclass_ import KIMI_K25_CURRENT
    parser.add_argument("--judge", nargs="+", default=[
            QWEN35_397B_CURRENT.model_alias,
            KIMI_K25_CURRENT.model_alias,
    ],
                        help="评分模型名；'mock' = 本地测试，不调用API，固定返回满分60%%")
    parser.add_argument("--limit", type=int, help="限制每组评分数量")
    parser.add_argument("--force", action="store_true", help="强制重跑")
    parser.add_argument("--parallel", type=int, default=1,
                        help="同时评分的 (模型×数据集) 组合数 (默认1)")
    parser.add_argument("--workers", type=int,
                        help="每个数据集内部评分线程数；不指定时按 judge 自动选择")
    args = parser.parse_args()
    for judge in args.judge:
        if args.workers is not None and args.workers < 1:
            parser.error("--workers 必须是正整数")

        models = args.model or [d for d in os.listdir(RESULTS_DIR) if os.path.isdir(os.path.join(RESULTS_DIR, d))]
        datasets = args.dataset or [
                d for d in list(SUBJECTIVE_TYPES.keys()) if 'capes' not in d
        ]

        # 构建所有 (model, dataset) 任务
        tasks = [(m, d, judge, args.force, args.limit, args.workers) for m in models for d in datasets]
        workers_text = args.workers if args.workers is not None else f"auto({get_score_workers(judge)})"
        logger.info(
            f"共 {len(tasks)} 个任务 (模型×数据集), 并行度={args.parallel}, "
            f"judge={judge}, workers={workers_text}"
        )
        while True:
            total_scored = 0
            if args.parallel <= 1:
                for task in tasks:
                    model_name, dataset_group, count = _process_task(task)
                    total_scored += count
            else:
                from concurrent.futures import ProcessPoolExecutor
                with ProcessPoolExecutor(max_workers=args.parallel) as pool:
                    for model_name, dataset_group, count in pool.map(_process_task, tasks):
                        total_scored += count
            if total_scored == 0:
                break
            from time import sleep
            sleep(300)
        logger.info(f"所有任务完成！总计评分: {total_scored}")

if __name__ == "__main__":
    main()

