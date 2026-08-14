"""
TeaCH 推理进度统计 (CLI 版)

功能：
  - 统计各模型在各数据集上的推理完成情况
  - 基于唯一题目 ID 统计，防止由于重复记录导致的百分比超过 100%
  - 自动剔除 [ERROR] 记录
"""

import os
import sys
import json
import argparse
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path


# ── 路径配置 ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # scripts/monitor
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)               # scripts
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)                 # Jiaozikaoshi
sys.path.insert(0, SCRIPTS_DIR)

from config import DATASET_DIR

RESULTS_DIR = os.path.join(ROOT_DIR, "results")

# 待监控的模型列表
MODELS = [
    # ("GLM-4.6V", "glm-4.6v"),
    # ("Gemini 3.1-Pro", "gemini-3.1-pro-preview"),
    # ("Claude Sonnet 4.6", "claude-sonnet-4-6"),
    # ("Gemini 3.0-Flash", "gemini-3-flash-preview"),
    # ("GPT-5.2", "gpt-5.2"),
    # ("Kimi K2.5", "Kimi-K25"),
    # ("Qwen 3.5-397B", "qwen3.5-397b"),
]


def discover_models():
    """Return configured models, or scan results/ when MODELS is empty."""
    if MODELS:
        return MODELS

    results_path = Path(RESULTS_DIR)
    if not results_path.exists():
        return []

    models = []
    for model_dir in sorted(results_path.iterdir(), key=lambda p: p.name.lower()):
        if not model_dir.is_dir() or model_dir.name.startswith("."):
            continue
        has_result_file = any(
            f.is_file()
            and f.suffix == ".jsonl"
            and "_scored" not in f.name
            and ".bak" not in f.name
            and "_dedup" not in f.name
            for f in model_dir.glob("*.jsonl")
        )
        if has_result_file:
            models.append((model_dir.name, model_dir.name))
    return models


def load_dataset_id_sets(use_filter=True):
    """加载各数据集题目 ID 集合（按唯一 ID 统计）"""
    from input_datasets.load import DATASET_GROUPS
    from input_datasets.load import load_dataset_group

    id_sets = {}
    id_to_groups = {}
    for group_name in DATASET_GROUPS:
        if "capes" in group_name or (
                'qts' in group_name
        ):
            continue
        # if 'praxis' not in group_name:
        #     continue
        unique_ids = {
            qid
            for record in load_dataset_group(group_name, use_filter=use_filter)
            if (qid := (record.get("id") or record.get("question_id")))
        }
        id_sets[group_name] = unique_ids
        for qid in unique_ids:
            id_to_groups.setdefault(qid, set()).add(group_name)
    return id_sets, id_to_groups


def load_result_unique_count(model_id):
    """加载某模型已完成的唯一题目数"""
    model_dir = os.path.join(RESULTS_DIR, model_id)
    unique_ids = set()
    if not os.path.exists(model_dir):
        return 0

    for f in Path(model_dir).glob("*.jsonl"):
        # 排除评分文件和备份文件
        if "_scored" in f.name or ".bak" in f.name or "_dedup" in f.name:
            continue
        try:
            with open(f, "r", encoding="utf-8") as fh:
                for line in fh:
                    if line.strip():
                        try:
                            data = json.loads(line)
                            qid = data.get("id") or data.get("question_id")
                            if qid:
                                # 剔除错误记录
                                resp = str(data.get("model_response", ""))
                                if not resp.startswith("[ERROR]"):
                                    unique_ids.add(qid)
                        except: continue
        except: continue
    return len(unique_ids)


def load_result_unique_counts_by_group(model_id, dataset_id_sets, id_to_groups):
    """加载某模型已完成题目数，并按 dataset group 分开统计。"""
    model_dir = os.path.join(RESULTS_DIR, model_id)
    completed_by_group = {group_name: set() for group_name in dataset_id_sets}
    unknown_ids = set()
    if not os.path.exists(model_dir):
        return completed_by_group, unknown_ids

    group_names = set(dataset_id_sets)
    for f in Path(model_dir).glob("*.jsonl"):
        if "_scored" in f.name or ".bak" in f.name or "_dedup" in f.name:
            continue
        from inference.remove_erroring_results import purge_errors
        purge_errors(f)

        file_group = f.stem if f.stem in group_names else None
        try:
            with open(f, "r", encoding="utf-8") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        qid = data.get("id") or data.get("question_id")
                        if not qid:
                            continue
                        resp = str(data.get("model_response", ""))
                        if resp.startswith("[ERROR]"):
                            continue

                        if file_group:
                            if qid in dataset_id_sets[file_group]:
                                completed_by_group[file_group].add(qid)
                            continue

                        matched_groups = id_to_groups.get(qid)
                        if matched_groups:
                            for group_name in matched_groups:
                                completed_by_group[group_name].add(qid)
                        else:
                            unknown_ids.add(qid)
                    except: continue
        except: continue
    return completed_by_group, unknown_ids


def count_errors(model_id):
    """统计某模型结果中 ERROR 记录数"""
    model_dir = os.path.join(RESULTS_DIR, model_id)
    errors = 0
    if not os.path.exists(model_dir):
        return errors

    for f in Path(model_dir).glob("*.jsonl"):
        if "_scored" in f.name or ".bak" in f.name or "_dedup" in f.name:
            continue
        try:
            with open(f, "r", encoding="utf-8") as fh:
                for line in fh:
                    try:
                        rec = json.loads(line)
                        resp = str(rec.get("model_response", ""))
                        if resp.startswith("[ERROR]"):
                            errors += 1
                    except: pass
        except: pass
    return errors


def count_errors_by_group(model_id, dataset_id_sets, id_to_groups):
    """统计某模型结果中 ERROR 记录数，并按 dataset group 分开统计。"""
    model_dir = os.path.join(RESULTS_DIR, model_id)
    errors_by_group = {group_name: 0 for group_name in dataset_id_sets}
    unknown_errors = 0
    if not os.path.exists(model_dir):
        return errors_by_group, unknown_errors

    group_names = set(dataset_id_sets)
    for f in Path(model_dir).glob("*.jsonl"):
        if "_scored" in f.name or ".bak" in f.name or "_dedup" in f.name:
            continue

        file_group = f.stem if f.stem in group_names else None
        try:
            with open(f, "r", encoding="utf-8") as fh:
                for line in fh:
                    try:
                        rec = json.loads(line)
                        resp = str(rec.get("model_response", ""))
                        if not resp.startswith("[ERROR]"):
                            continue
                        qid = rec.get("id") or rec.get("question_id")
                        if file_group:
                            if qid in dataset_id_sets[file_group]:
                                errors_by_group[file_group] += 1
                        elif qid and qid in id_to_groups:
                            for group_name in id_to_groups[qid]:
                                errors_by_group[group_name] += 1
                        else:
                            unknown_errors += 1
                    except: pass
        except: pass
    return errors_by_group, unknown_errors


def make_bar(pct, bar_len=15):
    filled = int(bar_len * pct / 100)
    return "#" * filled + "." * (bar_len - filled)

@dataclass(frozen=True)
class InferenceProgress:
    display_name: str
    model_id: str
    completed: int
    total: int
    missing: int
    percentage: float
    errors: int | None = None

    def to_dict(self) -> dict:
        data = asdict(self)
        if data["errors"] is None:
            data.pop("errors")
        return data

def main():

    parser = argparse.ArgumentParser(description="TeaCH 推理进度统计")
    parser.add_argument("--detail", action="store_true", help="按数据集展开", default=False)
    parser.add_argument("--errors", action="store_true", help="统计错误记录数")
    parser.add_argument("--no-filter", action="store_true", help="关闭 dataset blacklist 过滤")
    from input_datasets.load import LOG_PROGRESS_PATH
    parser.add_argument("--json-output", help="把总览进度写入指定 JSON 文件", default=LOG_PROGRESS_PATH)
    args = parser.parse_args()

    use_filter = not args.no_filter
    models = discover_models()
    dataset_id_sets, id_to_groups = load_dataset_id_sets(use_filter=use_filter)
    dataset_counts = {group_name: len(ids) for group_name, ids in dataset_id_sets.items()}
    total_questions = sum(dataset_counts.values())
    total_datasets = len(dataset_counts)

    print("=" * 85)
    print(f"TeaCH 推理进度统计 (CLI - 唯一 ID 去重版)")
    print(f"Blacklist filter: {'yes' if use_filter else 'no'}")
    print(f"数据集: {total_datasets} 个 | 总题目: {total_questions} 题 | 模型: {len(models)} 个")
    print("=" * 85)

    # ── 总览 ──
    print(f"\n{'模型':<25} {'已完成':>8} {'总题目':>8} {'进度条':>12} {'百分比':>8} {'缺失':>8}", end="")
    if args.errors:
        print(f" {'错误':>8}", end="")
    print()
    print("-" * 85)
    # if empty, scan over all subdirs under results/
    progress_rows: list[InferenceProgress] = []
    for display_name, model_id in models:
        completed_by_group, unknown_ids = load_result_unique_counts_by_group(model_id, dataset_id_sets, id_to_groups)
        # len(dataset_id_sets['praxis'])
        # Out[8]: 554
        # 'praxis_elem_multiple_subjects_q003' in completed_by_group['praxis']
        # Out[12]: True

        completed = sum(len(ids) for ids in completed_by_group.values())
        missing = max(0, total_questions - completed)
        pct = 100 * completed / total_questions if total_questions else 0

        bar = make_bar(pct)

        line = f"{display_name:<25} {completed:>8} {total_questions:>8} [{bar}] {pct:7.1f}% {missing:>8}"
        err = None
        if args.errors:
            err = count_errors(model_id)
            line += f" {err:>8}"
        print(line)
        progress_rows.append(
            InferenceProgress(
                display_name=display_name,
                model_id=model_id,
                completed=completed,
                total=total_questions,
                missing=missing,
                percentage=round(pct, 4),
                errors=err,
            )
        )

    print("-" * 85)

    if args.json_output:
        output_path = Path(args.json_output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "blacklist_filter": use_filter,
            "total_datasets": total_datasets,
            "total_questions": total_questions,
            "models": [row.to_dict() for row in progress_rows],
        }
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Progress JSON saved: {output_path}")

    if args.detail:
        print("\n按 dataset group 展开:")
        for display_name, model_id in models:
            completed_by_group, unknown_ids = load_result_unique_counts_by_group(model_id, dataset_id_sets, id_to_groups)
            errors_by_group = {}
            unknown_errors = 0
            if args.errors:
                errors_by_group, unknown_errors = count_errors_by_group(model_id, dataset_id_sets, id_to_groups)

            print(f"\n[{display_name}]")
            print(f"{'group':<18} {'已完成':>8} {'总题目':>8} {'进度条':>12} {'百分比':>8} {'缺失':>8}", end="")
            if args.errors:
                print(f" {'错误':>8}", end="")
            print()
            print("-" * 85)

            for group_name, total in dataset_counts.items():
                completed = len(completed_by_group.get(group_name, set()))
                missing = max(0, total - completed)
                pct = 100 * completed / total if total else 0
                bar = make_bar(pct, bar_len=12)
                line = f"{group_name:<18} {completed:>8} {total:>8} [{bar}] {pct:7.1f}% {missing:>8}"
                if args.errors:
                    line += f" {errors_by_group.get(group_name, 0):>8}"
                print(line)

            if unknown_ids or unknown_errors:
                print(f"{'(unknown)':<18} {len(unknown_ids):>8} {'-':>8} {'-':>14} {'-':>8} {'-':>8}", end="")
                if args.errors:
                    print(f" {unknown_errors:>8}", end="")
                print()

if __name__ == "__main__":
    main()
