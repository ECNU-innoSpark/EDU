"""
结果文件清理与去重工具

功能：
  - 扫描 results/ 下所有的 .jsonl 和 _scored.jsonl 文件
  - 对每个文件按 'id' 进行去重
  - 针对 _scored 文件：
    1. 优先保留 scored=True 的记录
    2. 剔除所有包含 score_error 或 scored=False 的错误记录（以便重试）
  - 原位覆盖旧文件，并备份一份 .bak
"""

import os
import json
import shutil
from pathlib import Path

RESULTS_DIR = "E:/ECNU/Chuangzhi/Jiaozikaoshi/results"

def clean_file(file_path):
    if not os.path.exists(file_path):
        return
    
    is_scored_file = file_path.name.endswith("_scored.jsonl")
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
                    
                    # 如果是评分文件，执行特殊清洗逻辑
                    if is_scored_file:
                        # 1. 剔除错误记录
                        if data.get("scored") is False or "score_error" in data:
                            removed_errors += 1
                            continue
                        
                        # 2. 去重逻辑：如果已存在，只有当前记录更好时才替换
                        if qid in records_map:
                            duplicates += 1
                            # 如果存着的没分，现在的有分，替换
                            if "score" not in records_map[qid] and "score" in data:
                                records_map[qid] = data
                        else:
                            records_map[qid] = data
                    else:
                        # 普通回答文件，简单去重
                        if qid in records_map:
                            duplicates += 1
                        records_map[qid] = data
                        
                except Exception:
                    continue
        
        if removed_errors == 0 and duplicates == 0:
            return # 没有变化，不操作
            
        # 备份并回写
        # shutil.copy(file_path, str(file_path) + ".bak")
        with open(file_path, "w", encoding="utf-8") as f:
            for rec in records_map.values():
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        
        print(f"  [CLEANED] {file_path.relative_to(RESULTS_DIR)}: 删去错误 {removed_errors} 条, 合并重复 {duplicates} 条")
        
    except Exception as e:
        print(f"  [ERROR] 处理 {file_path} 失败: {e}")

def main():
    print(f"开始清理结果目录: {RESULTS_DIR}\n")
    results_path = Path(RESULTS_DIR)
    
    # 递归查找所有 jsonl
    files = list(results_path.rglob("*.jsonl"))
    for file in files:
        clean_file(file)
    
    print("\n清理完成！现在你可以重新运行进度检查脚本了。")

if __name__ == "__main__":
    main()
