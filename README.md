[//]: # (# add a readme, note to clone https://github.com/kleeeeea/llm_common and https://github.com/kleeeeea/parse_evaluation and add its path to python path)

# EDU 1.0

Benchmark data and evaluation pipeline for measuring the professional
educational competence of foundation models on teacher-certification
examinations from three countries.

The released question set contains **10,013 questions** — 8,868 selected-response
and 1,145 constructed-response — drawn from the Chinese NTCE, the U.S. Praxis and
the Indian KVS recruitment examinations.

| Country | Selected response | Constructed response | Total |
|---|---:|---:|---:|
| China (NTCE) | 3,660 | 1,028 | 4,688 |
| India (KVS) | 3,421 | 0 | 3,421 |
| U.S. (Praxis) | 1,787 | 117 | 1,904 |
| **Total** | **8,868** | **1,145** | **10,013** |

## Setup

Two helper libraries are kept in separate repositories and are **not** installable
from PyPI. Clone them and put them on `PYTHONPATH` before running anything here:

```bash
git clone https://github.com/kleeeeea/llm_common
git clone https://github.com/kleeeeea/parse_evaluation
export PYTHONPATH="$PWD/llm_common:$PWD/parse_evaluation:$PYTHONPATH"
```

`llm_common` supplies the per-model API configuration used by inference and
scoring (`llm_common.llm_infer.api_info.dataclass_`); `parse_evaluation` supplies
the shared response-type constants used by the scoring rules.

Remaining dependencies are ordinary packages:

```bash
pip install openai pandas
```

Set the API credentials as environment variables — see
[Configuration](#configuration) before your first run:

```bash
export INNOSPARK_API_KEY=...
```

## Layout

```
dataset/            released questions, one <dataset>.jsonl + <dataset>.csv per source
input_datasets/     dataset loading, model registry, token pricing
inference/          run models over the questions
scoring/            LLM-as-judge scoring of constructed responses
monitor/            progress inspection for long-running jobs
config.py           paths and API endpoints
```

### `dataset/`

Twenty datasets, each shipped as a JSON Lines file and an equivalent CSV. Every
record is one question; the field set varies by examination family, but `id`,
`type`, `question` and `answer` are always present. Structured values (`options`,
`sub_questions`, …) are objects in the JSONL and JSON-encoded strings in the CSV.

| Group | Datasets |
|---|---|
| China | `s1`, `s2`, `s3`, `interview`, `shijian` |
| U.S. | `praxis`, `barrons`, `dummies`, `cliffs_ss`, `cliffs0511`, `kaplan`, `kaplan2017`, `ppst_cliffs`, `learningexpress`, `mometrix`, `math0061`, `allen`, `plt_selected_response`, `evaluation_records_plt_constructed_response` |
| India | `india` |

## Usage

Run inference for one or more models over one or more datasets:

```bash
python inference/run.py --models qwen3.5-397b --datasets s1 s2 --workers 8
```

`--limit` caps the number of questions per dataset (useful for a smoke test),
`--force` re-runs questions that already have a stored answer, and
`--disable_thinking` turns off extended reasoning for models that support it.

Score constructed responses with a single judge, or with every configured judge:

```bash
python scoring/run_scoring.py --model qwen3.5-397b --dataset s2 --judge Kimi-K25
python scoring/run_all_judges.py --model qwen3.5-397b --dataset s2 --parallel
```

Selected-response questions are graded by exact match and need no judge.

Watch a long run:

```bash
python monitor/cli_progress.py
```

## Configuration

`config.py` holds API endpoints and dataset paths. Two things to check before
running:

- **Credentials.** `API_KEY` reads from `INNOSPARK_API_KEY`, but
  `EXTRACT_API_KEY` is currently a literal string in the file. Replace it with an
  environment lookup and rotate the key before publishing or sharing this
  repository — a committed key must be treated as compromised.
- **Paths.** `DATA_ROOT` points at the raw examination archive, which is not part
  of this release; only `DATASET_DIR` (the `dataset/` directory above) is needed
  to reproduce inference and scoring.

## Notes on the released set

The questions here are the ones that actually enter the reported results. Items
excluded upstream by the quality blacklist are not included, and neither are 79
fill-in-the-blank items that were answered by the models but never entered any
reported aggregate. Counts in this README therefore match the paper exactly
rather than the larger raw collection.
