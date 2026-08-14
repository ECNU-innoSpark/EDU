import json
import os


# ── 断点续跑 ─────────────────────────────────────────────────

def load_done_ids(out_path: str) -> set:
    """读取已成功完成的题目 id 集合（[ERROR] 记录不算完成，会被重试）"""
    if not os.path.exists(out_path):
        return set()
    done = set()
    with open(out_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    r = json.loads(line)
                    resp = r.get("model_response", "")
                    if not str(resp).startswith("[ERROR]"):
                        done.add(r.get("id", ""))
                except Exception:
                    pass
    return done


def main(*_args, **_kwargs):
    import argparse
    from inference import RESULTS_DIR
    from input_datasets.load import DATASET_GROUPS

    parser = argparse.ArgumentParser(description="查看推理已完成题目数")
    parser.add_argument("--models", nargs="+",
                        help="模型名称，可指定多个", default=['qwen3.5-397b'])
    parser.add_argument("--datasets", nargs="+",
                        default=list(DATASET_GROUPS.keys()),
                        help=f"数据集组名，可选：{list(DATASET_GROUPS.keys())}")
    args = parser.parse_args()

    for model_name in args.models:
        for gname in args.datasets:
            out_path = os.path.join(RESULTS_DIR, model_name, f"{gname}.jsonl")
            done_ids = load_done_ids(out_path)
            if done_ids:
                print(f"  {model_name}/{gname}: {len(done_ids)} 题已完成")


if __name__ == "__main__":
    main()
