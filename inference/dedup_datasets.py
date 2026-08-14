"""
TeaCH 数据集去重

扫描 dataset/ 中所有 JSONL 文件，按 id 字段去重，原地覆盖。

用法：
  python scripts/inference/dedup_datasets.py           # 预览（不修改）
  python scripts/inference/dedup_datasets.py --apply    # 执行去重
"""

import os
import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATASET_DIR


def dedup_file(filepath, apply=False):
    """对单个 JSONL 文件按 id 去重，返回 (原始行数, 去重后行数)"""
    seen_ids = set()
    unique_records = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                rid = r.get("id", "")
                if rid not in seen_ids:
                    seen_ids.add(rid)
                    unique_records.append(line)
            except json.JSONDecodeError:
                unique_records.append(line)

    original = sum(1 for _ in open(filepath, "r", encoding="utf-8"))
    deduped = len(unique_records)

    if apply and deduped < original:
        with open(filepath, "w", encoding="utf-8") as f:
            for line in unique_records:
                f.write(line + "\n")

    return original, deduped


def main():
    parser = argparse.ArgumentParser(description="数据集去重")
    parser.add_argument("--apply", action="store_true", help="执行去重（默认只预览）")
    args = parser.parse_args()

    print("=" * 70)
    print(f"TeaCH 数据集去重 {'[执行模式]' if args.apply else '[预览模式]'}")
    print("=" * 70)

    total_before = 0
    total_after = 0
    changed_files = 0

    for f in sorted(Path(DATASET_DIR).glob("*.jsonl")):
        original, deduped = dedup_file(f, apply=args.apply)
        total_before += original
        total_after += deduped

        if original != deduped:
            changed_files += 1
            removed = original - deduped
            print(f"  {f.name:<50s} {original:>6d} -> {deduped:>6d}  (-{removed})")

    print("-" * 70)
    print(f"  Total: {total_before} -> {total_after}  (removed {total_before - total_after})")
    print(f"  Files with duplicates: {changed_files}")

    if not args.apply and total_before != total_after:
        print(f"\n  [提示] 以上为预览，执行去重请加 --apply")


if __name__ == "__main__":
    main()
