"""
TeaCH subjective scoring progress monitor (CLI).

This follows scripts/monitor/cli_progress.py, but tracks LLM-as-Judge scoring
outputs created by scripts/scoring/run_scoring.py:

  results/<model>/<dataset>_scored_by_<judge>.jsonl
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
sys.path.insert(0, SCRIPTS_DIR)
LLM_EVALS_PATH = os.environ.get("LLM_EVALS_PATH", os.path.join(ROOT_DIR, "dependencies", "llm_evals"))
if os.path.isdir(LLM_EVALS_PATH) and LLM_EVALS_PATH not in sys.path:
    sys.path.insert(0, LLM_EVALS_PATH)

from scoring.run_scoring import is_subjective
from scoring.scoring_rules import SUBJECTIVE_TYPES


RESULTS_DIR = Path(ROOT_DIR) / "results"

MODELS = [
    # ("Gemini 3.1-Pro", "gemini-3.1-pro-preview"),
    # ("GLM-4.6V", "glm-4.6v"),
    # ("Claude Sonnet 4.6", "claude-sonnet-4-6"),
    # ("Gemini 3.0-Flash", "gemini-3-flash-preview"),
    # ("GPT-5.2", "gpt-5.2"),
    # ("Kimi K2.5", "Kimi-K25"),
    # ("Qwen 3.5-397B", "qwen3.5-397b"),
]


def discover_models() -> list[tuple[str, str]]:
    """Return configured models, or scan results/ when MODELS is empty."""
    if MODELS:
        return MODELS
    if not RESULTS_DIR.exists():
        return []

    models = []
    for model_dir in sorted(RESULTS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not model_dir.is_dir() or model_dir.name.startswith("."):
            continue
        has_input_jsonl = any(
            path.is_file()
            and path.suffix == ".jsonl"
            and "_scored" not in path.name
            and ".bak" not in path.name
            and "_dedup" not in path.name
            for path in model_dir.glob("*.jsonl")
        )
        if has_input_jsonl:
            models.append((model_dir.name, model_dir.name))
    return models


def make_bar(pct: float, bar_len: int = 15) -> str:
    filled = int(bar_len * pct / 100)
    return "#" * filled + "." * (bar_len - filled)


def safe_read_jsonl(path: Path):
    if not path.exists():
        return
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def get_qid(record: dict) -> str | None:
    return record.get("id") or record.get("question_id")


def load_target_subjective_ids(model_id: str, dataset_group: str) -> set[str]:
    input_path = RESULTS_DIR / model_id / f"{dataset_group}.jsonl"
    ids = set()
    for record in safe_read_jsonl(input_path) or []:
        qid = get_qid(record)
        if qid and is_subjective(record):
            ids.add(qid)
    return ids


def load_scored_ids(model_id: str, dataset_group: str, judge: str, target_ids: set[str]) -> tuple[set[str], int]:
    scored_path = RESULTS_DIR / model_id / f"{dataset_group}_scored_by_{judge}.jsonl"
    scored_ids = set()
    error_count = 0
    for record in safe_read_jsonl(scored_path) or []:
        qid = get_qid(record)
        if not qid or qid not in target_ids:
            continue
        if record.get("scored") is True:
            scored_ids.add(qid)
        elif record.get("score_error") or record.get("scored") is False:
            error_count += 1
    return scored_ids, error_count


def collect_progress(models: list[tuple[str, str]], datasets: list[str], judges: list[str]):
    progress = {}
    targets_by_model_group = {}
    for display_name, model_id in models:
        for dataset_group in datasets:
            target_ids = load_target_subjective_ids(model_id, dataset_group)
            targets_by_model_group[(model_id, dataset_group)] = target_ids
            for judge in judges:
                scored_ids, errors = load_scored_ids(model_id, dataset_group, judge, target_ids)
                progress[(model_id, dataset_group, judge)] = {
                    "scored_ids": scored_ids,
                    "errors": errors,
                }
    return targets_by_model_group, progress


def print_overview(models, datasets, judges, targets_by_model_group, progress, show_errors: bool) -> None:
    print(f"\n{'被评模型':<25} {'judge':<18} {'已评分':>8} {'总题目':>8} {'进度条':>17} {'百分比':>8} {'缺失':>8}", end="")
    if show_errors:
        print(f" {'错误':>8}", end="")
    print()
    print("-" * 100)

    for display_name, model_id in models:
        total = sum(len(targets_by_model_group[(model_id, dataset_group)]) for dataset_group in datasets)
        for judge in judges:
            scored = sum(len(progress[(model_id, dataset_group, judge)]["scored_ids"]) for dataset_group in datasets)
            errors = sum(progress[(model_id, dataset_group, judge)]["errors"] for dataset_group in datasets)
            missing = max(0, total - scored)
            pct = 100 * scored / total if total else 0
            line = f"{display_name:<25} {judge:<18} {scored:>8} {total:>8} [{make_bar(pct)}] {pct:7.1f}% {missing:>8}"
            if show_errors:
                line += f" {errors:>8}"
            print(line)


def print_detail(models, datasets, judges, targets_by_model_group, progress, show_errors: bool) -> None:
    print("\n按 dataset group 展开:")
    for display_name, model_id in models:
        print(f"\n[{display_name}]")
        header = f"{'group':<18} {'judge':<18} {'已评分':>8} {'总题目':>8} {'进度条':>14} {'百分比':>8} {'缺失':>8}"
        if show_errors:
            header += f" {'错误':>8}"
        print(header)
        print("-" * 100)

        for dataset_group in datasets:
            total = len(targets_by_model_group[(model_id, dataset_group)])
            if total == 0:
                continue
            for judge in judges:
                item = progress[(model_id, dataset_group, judge)]
                scored = len(item["scored_ids"])
                missing = max(0, total - scored)
                pct = 100 * scored / total if total else 0
                line = f"{dataset_group:<18} {judge:<18} {scored:>8} {total:>8} [{make_bar(pct, 12)}] {pct:7.1f}% {missing:>8}"
                if show_errors:
                    line += f" {item['errors']:>8}"
                print(line)


PROGRESS_DIR = Path(SCRIPT_DIR) / "progress"


def serialize_progress(models, datasets, judges, targets_by_model_group, progress) -> Path:
    """Snapshot the progress stats as JSON under scripts/scoring/progress/."""
    generated_at = datetime.now()
    snapshot = {
        "generated_at": generated_at.isoformat(timespec="seconds"),
        "datasets": datasets,
        "judges": judges,
        "total_targets": sum(len(ids) for ids in targets_by_model_group.values()),
        "models": [],
    }
    for display_name, model_id in models:
        total = sum(len(targets_by_model_group[(model_id, dataset_group)]) for dataset_group in datasets)
        model_entry = {"model": model_id, "display_name": display_name, "total": total, "judges": {}}
        for judge in judges:
            scored = sum(len(progress[(model_id, dataset_group, judge)]["scored_ids"]) for dataset_group in datasets)
            errors = sum(progress[(model_id, dataset_group, judge)]["errors"] for dataset_group in datasets)
            groups = {}
            for dataset_group in datasets:
                group_total = len(targets_by_model_group[(model_id, dataset_group)])
                if group_total == 0:
                    continue
                item = progress[(model_id, dataset_group, judge)]
                groups[dataset_group] = {
                    "scored": len(item["scored_ids"]),
                    "total": group_total,
                    "missing": max(0, group_total - len(item["scored_ids"])),
                    "errors": item["errors"],
                }
            model_entry["judges"][judge] = {
                "scored": scored,
                "total": total,
                "missing": max(0, total - scored),
                "pct": round(100 * scored / total, 2) if total else 0.0,
                "errors": errors,
                "groups": groups,
            }
        snapshot["models"].append(model_entry)

    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROGRESS_DIR / f"progress_{generated_at:%Y%m%d_%H%M%S}.json"
    output_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    (PROGRESS_DIR / "latest.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    return output_path


def print_net_change(models, datasets, judges, targets_by_model_group, progress) -> None:
    """Diff against the most recent snapshot in PROGRESS_DIR, in the overview format."""
    previous_files = sorted(PROGRESS_DIR.glob("progress_*.json"))
    if not previous_files:
        return
    previous = json.loads(previous_files[-1].read_text(encoding="utf-8"))
    previous_stats = {}
    for model_entry in previous.get("models", []):
        for judge, stats in model_entry.get("judges", {}).items():
            previous_stats[(model_entry["model"], judge)] = stats

    lines = []
    for display_name, model_id in models:
        total = sum(len(targets_by_model_group[(model_id, dataset_group)]) for dataset_group in datasets)
        for judge in judges:
            scored = sum(len(progress[(model_id, dataset_group, judge)]["scored_ids"]) for dataset_group in datasets)
            errors = sum(progress[(model_id, dataset_group, judge)]["errors"] for dataset_group in datasets)
            missing = max(0, total - scored)
            prev = previous_stats.get((model_id, judge), {})
            delta_scored = scored - prev.get("scored", 0)
            delta_total = total - prev.get("total", 0)
            delta_missing = missing - prev.get("missing", 0)
            delta_errors = errors - prev.get("errors", 0)
            if not any((delta_scored, delta_total, delta_missing, delta_errors)):
                continue
            pct = 100 * scored / total if total else 0
            prev_pct = prev.get("pct", 0.0)
            lines.append(f"{display_name:<25} {judge:<18} {delta_scored:>+8} {delta_total:>+8} "
                         f"{'':>17} {pct - prev_pct:>+7.1f}% {delta_missing:>+8} {delta_errors:>+8}")

    print(f"\n与上次快照的净变化 (自 {previous.get('generated_at', '?')}):")
    if not lines:
        print("  无变化")
        return
    print(f"{'被评模型':<25} {'judge':<18} {'Δ已评分':>8} {'Δ总题目':>8} {'':>17} {'Δ百分比':>8} {'Δ缺失':>8} {'Δ错误':>8}")
    print("-" * 100)
    for line in lines:
        print(line)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TeaCH 主观题 LLM-as-Judge 评分进度统计")
    parser.add_argument("--model", nargs="+", help="只统计指定被评模型 folder name")
    parser.add_argument("--dataset", nargs="+", default=[
            d for d in list(SUBJECTIVE_TYPES.keys()) if 'capes' not in d
    ],
                        help="数据集 group，默认使用 run_scoring.py 的 SUBJECTIVE_TYPES keys")
    parser.add_argument("--judge", nargs="+", default=[
            "Kimi-K25", 'qwen3.5-397b'], help="评分模型，默认统计所有 JUDGES_NAME")
    parser.add_argument("--detail", action="store_true", help="按 dataset group 展开"
                        # , default=True
                        )
    parser.add_argument("--errors", action="store_true", help="显示 score_error/scored=False 数量")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selected_model_ids = set(args.model or [])
    discovered_models = discover_models()
    models = [m for m in discovered_models if not selected_model_ids or m[1] in selected_model_ids]
    known_model_ids = {m[1] for m in models}
    for model_id in sorted(selected_model_ids - known_model_ids):
        models.append((model_id, model_id))

    targets_by_model_group, progress = collect_progress(models, args.dataset, args.judge)
    total_targets = sum(len(ids) for ids in targets_by_model_group.values())

    print("=" * 100)
    print("TeaCH 主观题评分进度统计 (CLI - 唯一 ID 去重版)")
    print(f"数据集: {len(args.dataset)} 个 | 被评模型: {len(models)} 个 | judges: {len(args.judge)} 个 | 总待评分题次: {total_targets}")
    print("=" * 100)

    print_overview(models, args.dataset, args.judge, targets_by_model_group, progress, args.errors)
    # must diff before serialize_progress writes the new snapshot
    print_net_change(models, args.dataset, args.judge, targets_by_model_group, progress)

    snapshot_path = serialize_progress(models, args.dataset, args.judge, targets_by_model_group, progress)
    print("-" * 100)
    print(f"进度快照已保存: {snapshot_path}")

    if args.detail:
        print_detail(models, args.dataset, args.judge, targets_by_model_group, progress, args.errors)


if __name__ == "__main__":
    main()
#
