"""
走完完整推理流程（默认 mock 模型），结果含 prompt 中间字段，按题型分 CSV 输出。

用法：
  python split_by_type.py                          # mock 模型，全部数据集
  python split_by_type.py --models gpt-4o          # 真实模型
  python split_by_type.py --limit 1 --force        # 快速测试
"""

import csv
import os
import sys

from analysis.model_output.split_by_type import HEAD
from analysis.model_output.split_by_type import TAIL

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))

from inference.prompts import TYPE_SCHEMA


def write_split_by_type_result(by_type: dict[str, list[dict]], model: str, out_dir: str):
    for qtype, rows in by_type.items():
        schema_fields = TYPE_SCHEMA.get(qtype, ["question_text"])
        base = set(HEAD + schema_fields + TAIL)
        extra = list(dict.fromkeys(k for r in rows for k in r if k not in base))
        fieldnames = HEAD + schema_fields + extra + TAIL
        safe = qtype.replace("/", "-").replace(" ", "_")
        out = os.path.join(out_dir, f"{safe}.csv")
        with open(out, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"  [{model}] {qtype}: {len(rows)} 条 → {out}")
