"""
评分结果清理与去重工具

功能：
  - 扫描 results/ 下所有的 _scored.jsonl 文件
  - 优先保留 scored=True 的记录
  - 剔除所有包含 score_error 或 scored=False 的错误记录（以便重试）
  - 原位覆盖旧文件
"""

import os
import json
from pathlib import Path

# ── 路径配置 ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # scripts/scoring
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR)) # Jiaozikaoshi
RESULTS_DIR = os.path.join(ROOT_DIR, "results")

def clean_file(file_path):
    if not file_path.name.endswith("_scored.jsonl"):
        return
    
    records_map = {} # id -> record
    removed_errors = 0
    duplicates = 0
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip(): continue
                try:
                    data = json.loads(line)
                    qid = data.get("id") or data.get("question_id")
                    if not qid: continue
                    
                    # 1. 剔除错误记录
                    if data.get("scored") is False or "score_error" in data:
                        removed_errors += 1
                        continue
                    
                    # 2. 去重逻辑
                    if qid in records_map:
                        duplicates += 1
                        # 优先保留有分数的
                        if "score" not in records_map[qid] and "score" in data:
                            records_map[qid] = data
                    else:
                        records_map[qid] = data
                except:
                    continue
        
        if removed_errors > 0 or duplicates > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                for rec in records_map.values():
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"  [CLEANED] {file_path.name}: 删去错误 {removed_errors} 条, 合并重复 {duplicates} 条")
            
    except Exception as e:
        print(f"  [ERROR] 处理 {file_path} 失败: {e}")

def main():
    print(f"开始清理评分结果: {RESULTS_DIR}\n")
    for model_dir in Path(RESULTS_DIR).iterdir():
        if model_dir.is_dir():
            for f in model_dir.glob("*_scored.jsonl"):
                clean_file(f)
    print("\n清理完成！")

if __name__ == "__main__":
    main()
