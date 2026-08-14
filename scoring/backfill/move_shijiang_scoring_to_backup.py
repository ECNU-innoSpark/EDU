# add .bak suffix to like
# /Users/l/other_git_repos/TeaCH-main/results/gemini-3.1-pro-preview/shijian_scored_by_qwen3.5-397b.jsonl
# /Users/l/other_git_repos/TeaCH-main/results/{other}/shijian_scored_by_qwen3.5-397b.jsonl
# just write the file, but don't execute it

from __future__ import annotations

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
RESULTS_DIR = REPO_ROOT / "results"

SCORING_FILENAME = "shijian_scored_by_Kimi-K25.jsonl"
# shijian_scored_by_qwen3.5-397b.jsonl

def main() -> None:
    parser = argparse.ArgumentParser(
            description=f"Rename results/*/{SCORING_FILENAME} to *.jsonl.bak")
    parser.add_argument("--apply", action="store_true",
                        help="actually rename; default is a dry run that only prints")
    args = parser.parse_args()

    targets = sorted(RESULTS_DIR.glob(f"*/{SCORING_FILENAME}"))
    if not targets:
        print(f"no {SCORING_FILENAME} found under {RESULTS_DIR}")
        return

    renamed = skipped = 0
    for path in targets:
        backup = path.with_suffix(path.suffix + ".bak")
        if backup.exists():
            print(f"SKIP (backup already exists): {backup}")
            skipped += 1
            continue
        print(f"{'mv' if args.apply else 'would mv'} {path} -> {backup.name}")
        if args.apply:
            path.rename(backup)
        renamed += 1

    mode = "renamed" if args.apply else "would rename"
    print(f"\n{mode} {renamed} file(s), skipped {skipped}"
          + ("" if args.apply else "  (dry run; pass --apply to execute)"))


if __name__ == "__main__":
    main()
