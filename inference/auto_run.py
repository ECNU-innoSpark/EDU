"""
TeaCH 自动补跑 - 找到未完成的数据集，自动启动推理

run.py 本身会跳过已完成的题目，所以直接启动即可。
本脚本同时启动所有模型，实时打印各进程输出。

用法：
  python scripts/inference/auto_run.py              # 启动所有6个模型
  python scripts/inference/auto_run.py --models Kimi-K25 qwen3.5-397b  # 只启动指定模型
"""

import os
import sys
import subprocess
import threading
import time
from pathlib import Path

# 修复 Windows 终端中文乱码
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    os.system("chcp 65001 > nul 2>&1")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATASET_DIR

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ALL_MODELS = {
    "Kimi-K25": "Kimi",
    "qwen3.5-397b": "Qwen",
    "qwen3.6-35b": "Qwen36",
    "claude-sonnet-4-6": "Claude",
    "gemini-3-flash-preview": "Flash",
    "gemini-3.1-pro-preview": "Pro",
    "gpt-5.2": "GPT",
    "glm-4.6v": "GLM",
}


def get_all_datasets():
    """获取 run.py 支持的聚合数据集名称"""
    return [
        "s1", "s2", "s3", "shijian", "interview",
        "praxis", "barrons", "mometrix", "kaplan", "kaplan2017",
        "dummies", "allen", "learningexpress", "cliffs0511", "cliffs_ss",
        "math0061", "ppst_cliffs",
        "capes", "shijian_capes",
        "india",
        "qts",
    ]


def stream_output(proc, tag):
    """实时打印子进程输出"""
    while True:
        line = proc.stdout.readline()
        if not line and proc.poll() is not None:
            break
        if line:
            print(f"  [{tag}] {line.strip()}", flush=True)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="+", default=list(ALL_MODELS.keys()),
                        help="要运行的模型列表")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--model-workers", type=int, default=3)
    args = parser.parse_args()

    datasets = get_all_datasets()
    datasets_str = " ".join(datasets)

    print("=" * 70)
    print(f"TeaCH 自动补跑")
    print(f"工作目录: {PROJECT_ROOT}")
    print(f"数据集: {len(datasets)} 个 | 模型: {len(args.models)} 个")
    print("=" * 70)

    processes = {}
    threads = []

    for model_id in args.models:
        tag = ALL_MODELS.get(model_id, model_id[:6])

        cmd = [
            sys.executable, "scripts/inference/run.py",
            "--models", model_id,
            "--datasets", *datasets_str.split(),
            "--workers", str(args.workers),
            "--model-workers", str(args.model_workers),
        ]

        print(f"\n[START] {tag} ({model_id})")

        proc = subprocess.Popen(
            cmd,
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        processes[model_id] = proc

        t = threading.Thread(target=stream_output, args=(proc, tag), daemon=True)
        t.start()
        threads.append(t)

        time.sleep(3)  # 间隔启动

    print(f"\n[OK] {len(processes)} 个模型已启动，等待完成...\n")

    # 等待所有进程结束
    try:
        while True:
            all_done = True
            for model_id, proc in processes.items():
                if proc.poll() is None:
                    all_done = False
            if all_done:
                break
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[STOP] Ctrl+C，正在终止所有进程...")
        for proc in processes.values():
            proc.terminate()
        sys.exit(0)

    print("\n" + "=" * 70)
    print("[DONE] 所有模型已完成")
    print("=" * 70)

    # 打印最终统计
    for model_id, proc in processes.items():
        tag = ALL_MODELS.get(model_id, model_id)
        code = proc.returncode
        status = "OK" if code == 0 else f"ERROR (code={code})"
        print(f"  {tag:<10} {status}")


if __name__ == "__main__":
    main()
