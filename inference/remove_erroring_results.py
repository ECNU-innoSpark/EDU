import json
import os


def purge_errors(out_path: str):
    """把输出文件里的 [ERROR] 记录删除，为重试腾位置"""
    if not os.path.exists(out_path):
        return
    with open(out_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    kept = []
    removed = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
            if str(r.get("model_response", "")).startswith("[ERROR]"):
                removed += 1
            else:
                kept.append(line)
        except Exception:
            kept.append(line)
    if removed:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(kept) + "\n")
        print(f"  [清理] 移除 {removed} 条 ERROR 记录 → {out_path}")
