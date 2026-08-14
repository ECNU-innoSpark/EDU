"""
一键启动三个 Judge 模型并行评分

用法：
    python -m scripts.scoring.run_all_judges                       # 所有模型、所有数据集
    python -m scripts.scoring.run_all_judges --model gpt-5.2       # 指定被评模型
    python -m scripts.scoring.run_all_judges --dataset s1 s3       # 指定数据集
    python -m scripts.scoring.run_all_judges --parallel 6          # 每个judge内部并行度
    python -m scripts.scoring.run_all_judges --force               # 强制重评

功能：
  - 同时启动 qwen3.5-397b / Kimi-K25 / glm-4.6v 三个评分进程
  - 每个进程内部再并行评多个 (模型×数据集) 组合
  - 日志独立输出到 logs/ 目录，UTF-8 编码
  - Ctrl+C 一键终止全部
"""

import argparse
import subprocess
import sys
import os
import time
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOG_DIR = os.path.join(ROOT_DIR, "logs")




def main():
    parser = argparse.ArgumentParser(description="一键启动三个 Judge 并行评分")
    parser.add_argument("--model", nargs="+", help="被评分的模型名")
    parser.add_argument("--dataset", nargs="+", help="数据集名")
    parser.add_argument("--limit", type=int, help="每组限制评分数量")
    parser.add_argument("--force", action="store_true", help="强制重跑")
    parser.add_argument("--parallel", type=int, default=4,
                        help="每个 judge 内部并行度 (默认4)")
    parser.add_argument("--judges", nargs="+", default=JUDGES,
                        help=f"评分模型列表 (默认: {' '.join(JUDGES)})")
    args = parser.parse_args()

    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 构建各 judge 的子进程命令
    processes = {}
    for judge in args.judges:
        cmd = [
            sys.executable, "-X", "utf8",
            "-m", "scripts.scoring.run_scoring",
            "--judge", judge,
            "--parallel", str(args.parallel),
        ]
        if args.model:
            cmd += ["--model"] + args.model
        if args.dataset:
            cmd += ["--dataset"] + args.dataset
        if args.limit:
            cmd += ["--limit", str(args.limit)]
        if args.force:
            cmd += ["--force"]

        log_file = os.path.join(LOG_DIR, f"scoring_{judge}_{timestamp}.log")
        log_fh = open(log_file, "w", encoding="utf-8")

        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"

        proc = subprocess.Popen(
            cmd,
            cwd=ROOT_DIR,
            stdout=log_fh,
            stderr=subprocess.STDOUT,
            env=env,
        )
        processes[judge] = {"proc": proc, "log_file": log_file, "log_fh": log_fh}
        print(f"  [STARTED] {judge}  (PID={proc.pid})")

    print(f"\n{'='*60}")
    print(f"  3 个 Judge x {args.parallel} 路并行 已启动")
    print(f"  日志目录: logs/")
    print(f"  监控进度: python scripts/monitor/check_zhuguan_progress.py")
    print(f"{'='*60}\n")

    # 等待所有进程完成
    try:
        while True:
            all_done = True
            status_parts = []
            for judge, info in processes.items():
                ret = info["proc"].poll()
                if ret is None:
                    all_done = False
                    status_parts.append(f"{judge}: running")
                else:
                    status_parts.append(f"{judge}: done(rc={ret})")

            print(f"  [{datetime.now().strftime('%H:%M:%S')}] {' | '.join(status_parts)}", flush=True)

            if all_done:
                break
            time.sleep(60)

    except KeyboardInterrupt:
        print("\n\n  [INTERRUPTED] 正在终止所有评分进程...")
        for judge, info in processes.items():
            if info["proc"].poll() is None:
                info["proc"].terminate()
                print(f"    terminated {judge} (PID={info['proc'].pid})")
        sys.exit(1)
    finally:
        for info in processes.values():
            info["log_fh"].close()

    # 汇总
    print(f"\n{'='*60}")
    print("  所有评分完成！")
    for judge, info in processes.items():
        rc = info["proc"].returncode
        status = "SUCCESS" if rc == 0 else f"FAILED(rc={rc})"
        print(f"    {judge}: {status}  log={os.path.basename(info['log_file'])}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
