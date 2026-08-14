"""
清理 results 目录：删除不在 dataset 中的结果记录

用法：
  python clean_results.py          # 预览模式，只统计
  python clean_results.py --apply  # 实际执行清理
"""

import json
import glob
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SCRIPT_DIR, "..", "..")
DATASET_DIR = os.path.join(PROJECT_DIR, "dataset")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")


def load_dataset_ids():
    """加载 dataset 中所有题目 ID"""
    ids = set()
    for f in glob.glob(os.path.join(DATASET_DIR, "*.jsonl")):
        for line in open(f, "r", encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                ids.add(json.loads(line)["id"])
            except Exception:
                pass
    return ids


def clean_results(apply=False):
    dataset_ids = load_dataset_ids()
    print(f"Dataset IDs: {len(dataset_ids)}")
    print()

    total_kept = 0
    total_removed = 0

    for model_dir in sorted(glob.glob(os.path.join(RESULTS_DIR, "*"))):
        if not os.path.isdir(model_dir):
            continue
        model = os.path.basename(model_dir)
        model_kept = 0
        model_removed = 0

        for rf in sorted(glob.glob(os.path.join(model_dir, "*.jsonl"))):
            fname = os.path.basename(rf)
            kept = []
            removed = 0

            for line in open(rf, "r", encoding="utf-8"):
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                    if r.get("id") in dataset_ids:
                        kept.append(line)
                    else:
                        removed += 1
                except Exception:
                    removed += 1

            if removed > 0:
                print(f"  {model}/{fname}: {len(kept)} keep, {removed} remove")
                if apply:
                    with open(rf, "w", encoding="utf-8") as f:
                        for line in kept:
                            f.write(line + "\n")

            model_kept += len(kept)
            model_removed += removed

        if model_kept + model_removed > 0:
            print(f"  [{model}] total: {model_kept} keep, {model_removed} remove")
            print()

        total_kept += model_kept
        total_removed += model_removed

    print(f"{'APPLIED' if apply else 'PREVIEW'}: {total_kept} keep, {total_removed} remove")


if __name__ == "__main__":
    apply = "--apply" in sys.argv
    clean_results(apply)
