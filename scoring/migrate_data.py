"""
数据迁移脚本：将混杂的 _scored.jsonl 拆分为按 Judge 命名的独立文件
"""

import os
import json
from pathlib import Path
from collections import defaultdict

RESULTS_DIR = "E:/ECNU/Chuangzhi/Jiaozikaoshi/results"

def migrate():
    print(f"正在扫描并拆分混杂的评分数据...")
    
    for model_dir in Path(RESULTS_DIR).iterdir():
        if not model_dir.is_dir(): continue
        
        # 找老的混杂文件
        for old_file in model_dir.glob("*_scored.jsonl"):
            # 排除掉已经是新格式的文件
            if "_scored_by_" in old_file.name: continue
            
            dataset_name = old_file.stem.replace("_scored", "")
            
            # 按 judge 缓存记录
            judge_buckets = defaultdict(list)
            
            try:
                with open(old_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip(): continue
                        data = json.loads(line)
                        if data.get("scored"):
                            judge = data.get("judge_model", "Unknown")
                            judge_buckets[judge].append(data)
                
                # 写入新文件
                for judge, records in judge_buckets.items():
                    new_filename = f"{dataset_name}_scored_by_{judge}.jsonl"
                    new_path = model_dir / new_filename
                    
                    # 追加模式，防止丢失
                    with open(new_path, "a", encoding="utf-8") as nf:
                        for r in records:
                            nf.write(json.dumps(r, ensure_ascii=False) + "\n")
                    
                    print(f"  [MIGRATED] {model_dir.name}/{old_file.name} -> {new_filename} ({len(records)} 条)")
                
                # 迁移完后，重命名旧文件作为备份
                old_file.rename(str(old_file) + ".bak")
                
            except Exception as e:
                print(f"  [ERROR] 迁移 {old_file} 失败: {e}")

if __name__ == "__main__":
    migrate()
