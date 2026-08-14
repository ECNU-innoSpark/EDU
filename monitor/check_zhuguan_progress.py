"""
主观题评分进度检查脚本 (精确去重版)

功能：
  - 统计每个 Judge 对每个数据集的批改进度
  - 基于 question_id 进行精确去重，确保总数和进度百分比真实可靠
"""

import os
import json
import sys
from pathlib import Path
from collections import defaultdict

# ── 路径配置 ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # scripts/scoring
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR)) # Jiaozikaoshi
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))

RESULTS_DIR = os.path.join(ROOT_DIR, "results")

def is_subjective(record):
    """判定是否为主观题：非单项选择题"""
    return record.get("type", "") != "单项选择题"

def check_progress():
    print("\n[Scoring Monitor] 正在扫描主观题评分进度 (基于唯一 ID 统计)...")
    
    # 结构: {(model, dataset): {total_ids: set(), judge_counts: {judge_name: set()}}}
    stats = defaultdict(lambda: {"total_ids": set(), "judges": defaultdict(set)})

    if not os.path.exists(RESULTS_DIR):
        print(f"错误: 找不到目录 {RESULTS_DIR}")
        return

    # 遍历模型
    for model_name in sorted(os.listdir(RESULTS_DIR)):
        model_path = os.path.join(RESULTS_DIR, model_name)
        if not os.path.isdir(model_path): continue
            
        # 1. 扫描原始文件，确定主观题 ID 集合
        for raw_file in Path(model_path).glob("*.jsonl"):
            if "_scored" in raw_file.name or "_dedup" in raw_file.name or ".bak" in raw_file.name:
                continue
            
            dataset_name = raw_file.stem
            try:
                with open(raw_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip(): continue
                        data = json.loads(line)
                        qid = data.get("id") or data.get("question_id")
                        if qid and is_subjective(data):
                            stats[(model_name, dataset_name)]["total_ids"].add(qid)
            except: continue

        # 2. 扫描评分文件，统计各 Judge 完成的 ID 集合
        for scored_file in Path(model_path).glob("*_scored_by_*.jsonl"):
            parts = scored_file.stem.split("_scored_by_")
            if len(parts) != 2: continue
            
            dataset_name = parts[0]
            judge_name = parts[1]
            
            try:
                with open(scored_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip(): continue
                        data = json.loads(line)
                        qid = data.get("id") or data.get("question_id")
                        if qid and data.get("scored") is True:
                            stats[(model_name, dataset_name)]["judges"][judge_name].add(qid)
            except: continue

    # 过滤掉没有任何主观题的数据集
    report_data = {k: v for k, v in stats.items() if v["total_ids"]}

    if not report_data:
        print("未发现任何主观题评分数据。")
        return

    print("\n" + "="*120)
    print(f"{'被评模型':<22} | {'数据集':<12} | {'总题数':>6} | {'各 Judge 评分进度 (唯一ID)'}")
    print("-" * 120)
    
    for (m, d), s in sorted(report_data.items()):
        total = len(s["total_ids"])
        judge_list = []
        
        for j, scored_set in sorted(s["judges"].items()):
            # 这里的逻辑：已评分 ID 必须在原始 ID 集合中才算有效进度
            valid_scored = scored_set.intersection(s["total_ids"])
            count = len(valid_scored)
            pct = (count / total * 100) if total > 0 else 0
            judge_list.append(f"{j}: {count}/{total} ({pct:.1f}%)")
        
        judges_str = " | ".join(judge_list) if judge_list else "未开始"
        print(f"{m:<22} | {d:<12} | {total:>6} | {judges_str}")
    
    print("="*120 + "\n")

if __name__ == "__main__":
    check_progress()
