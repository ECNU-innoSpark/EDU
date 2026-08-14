import csv
import json
import os


def jsonl_to_csv(jsonl_path: str):
    """把 JSONL 结果文件重新写成同名 CSV（列顺序：id 在前，model_response/reasoning 在后）"""
    if not os.path.exists(jsonl_path):
        return
    rows = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
    if not rows:
        return
    priority = ["id", "model"]
    tail = ["model_response", "reasoning"]
    all_keys = list(dict.fromkeys(
        priority
        + [k for k in rows[0] if k not in priority and k not in tail]
        + [k for k in tail if k in rows[0]]
    ))
    csv_path = jsonl_path.replace(".jsonl", ".csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=all_keys, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

