"""
"""
import json
import os
import sys
from dataclasses import dataclass
from typing import Any

from input_datasets.model_names import prettify_model_id
from llm_common.llm_infer.api_info.dataclass_ import GLM46V_API
from llm_common.llm_infer.api_info.dataclass_ import KIMI_K25_QZ_API
from llm_common.llm_infer.api_info.dataclass_ import claude_opus_4_6_API

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from config import DATASET_DIR
from inference.prompts import extract_prompt_fields
from inference.prompts import format_question

LOG_PROGRESS_PATH = os.path.join(ROOT_DIR, "log", "teach_inference_progress.json")

BASE_MODELS_V0 = [
        "gemini-3-flash-preview",
        "gemini-3.1-pro-preview",
        "claude-sonnet-4-6",
        "glm-4.6v",
        "gpt-5.2",
        "Kimi-K25",
        "qwen3.5-397b",
]

BASE_MODEL_SHORT_V0 = {
        "claude-sonnet-4-6"     : "Claude Sonnet 4.6",
        "gemini-3-flash-preview": "Gemini 3 Flash",
        "gemini-3.1-pro-preview": "Gemini 3.1 Pro",
        "glm-4.6v"              : "GLM-4.6V",
        "gpt-5.2"               : "GPT-5.2",
        "Kimi-K25"              : "Kimi-K25",
        "qwen3.5-397b"          : "Qwen3.5-397B",
}

# enforce this order
BASE_MODEL_SHORT_V1 = {
        "claude-opus-4-6"        : "Claude Opus 4.6",
        "claude-sonnet-4-6"      : "Claude Sonnet 4.6",
        "gemini-3.1-pro-preview" : "Gemini 3.1 Pro",
        "gemini-3-flash-preview" : "Gemini 3 Flash",
        "gpt-5.2"                : "GPT 5.2",
        "Kimi-K25"               : "Kimi K2.5",
        "qwen3.5-397b"           : "Qwen3.5 397B",
        "glm-4.6v"               : "GLM-4.6V",
        "gemma-4-12B-it"         : "Gemma 4 12B",
        "gemma-4-26B-A4B-it"     : "Gemma 4 26B-A4B",
        "gemma-4-31B-it"         : "Gemma 4 31B",
        "gemma-4-E2B-it"         : "Gemma 4 E2B",
        "InternVL3_5-14B"        : "InternVL3.5 14B",
        "InternVL3_5-2B"         : "InternVL3.5 2B",
        "InternVL3_5-4B"         : "InternVL3.5 4B",
        "InternVL3_5-8B"         : "InternVL3.5 8B",
        "Kimi-VL-A3B-Instruct"   : "Kimi-VL A3B",
        "MiMo-VL-7B-SFT"         : "MiMo-VL 7B SFT",
        "ministral-3-14b"        : "Ministral 3 14B",
        "ministral-3-3b"         : "Ministral 3 3B",
        "ministral-3-8b"         : "Ministral 3 8B",
        "Molmo2-8B"              : "Molmo2 8B",
        "Phi-3.5-vision-instruct": "Phi-3.5 Vision",
        "Qwen3.5-4B"             : "Qwen3.5 4B",
        "qwen3.5-9b"             : "Qwen3.5 9B",
        "qwen3.6-27b"            : "Qwen3.6 27B",
        "qwen3.6-35b"            : "Qwen3.5 35B",
        "qwen3.6-35b-latest"     : "Qwen3.6 35B",
        "Step3-VL-10B"           : "Step3-VL 10B",
}


def _load_progress_model_rows(path: str = LOG_PROGRESS_PATH) -> list[dict[str, Any]]:
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []

    rows = payload.get("models", [])
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict) and row.get("model_id")]



thinking_model = """
Step3-VL 10B-No Think
MiMo-VL 7B SFT-No Think
"""


def _extend_models_from_progress(
        base_models: list[str],
        base_model_short: dict[str, str],
        progress_rows: list[dict[str, Any]],
) -> tuple[list[str], dict[str, str]]:
    models = list(base_models)
    model_short = dict(base_model_short)
    seen = set(models)

    for row in progress_rows:
        model_id = str(row["model_id"])
        if model_id not in seen:
            models.append(model_id)
            seen.add(model_id)
        model_short.setdefault(model_id, prettify_model_id(str(row.get("display_name") or model_id)))

    return models, model_short


def _model_order_key(model_id: str, order_index: dict[str, int]) -> tuple[int, int, str]:
    no_think_suffix = "_nothink"
    if model_id in order_index:
        return order_index[model_id], 0, model_id
    if model_id.endswith(no_think_suffix):
        base_id = model_id[:-len(no_think_suffix)]
        if base_id in order_index:
            return order_index[base_id], 1, model_id
    return len(order_index), 0, model_id


def _models_from_progress_in_order(
        ordered_model_short: dict[str, str],
        progress_rows: list[dict[str, Any]],
) -> tuple[list[str], dict[str, str]]:
    order_index = {model_id: idx for idx, model_id in enumerate(ordered_model_short)}
    progress_model_ids = [
            str(row["model_id"])
            for row in progress_rows
            if row.get("model_id")
    ]

    if progress_model_ids:
        models = list(dict.fromkeys(progress_model_ids))
    else:
        models = list(ordered_model_short)

    models.sort(key=lambda model_id: _model_order_key(model_id, order_index))

    model_short = dict(ordered_model_short)
    for row in progress_rows:
        model_id = str(row["model_id"])
        model_short.setdefault(model_id, prettify_model_id(str(row.get("display_name") or model_id)))

    return models, model_short


# enforce the order as in BASE_MODEL_SHORT_V1
MODELS, MODEL_SHORT = _models_from_progress_in_order(
        BASE_MODEL_SHORT_V1,
        _load_progress_model_rows(),
)

from llm_common.llm_infer.api_info.dataclass_ import qwen_3_5_397_b
large_t1t2_models = [
        'qwen3.5-397b',
        'Kimi-K25',
        'gemini-3-flash-preview'
        ,
        "gemini-3.1-pro-preview"
        ,
        "claude-sonnet-4-6"
        ,
        claude_opus_4_6_API.model,
        "gpt-5.2",
        'glm-4.6v',
] + '''
qwen3.6-27b
qwen3.6-27b_nothink
qwen3.6-35b
qwen3.6-35b_nothink
'''.split()
current_models = '''
gemini-3-flash-preview
Kimi-K25
claude-opus-4-6
claude-sonnet-4-6
gemini-3.1-pro-preview
gemma-4-12B-it_nothink
gemma-4-26B-A4B-it_nothink
gemma-4-31B-it_nothink
gemma-4-E2B-it_nothink
glm-4.6v
gpt-5.2
InternVL3_5-2B_nothink
InternVL3_5-4B_nothink
InternVL3_5-8B_nothink
InternVL3_5-14B_nothink
Kimi-VL-A3B-Instruct_nothink
Llama-3.2-11B-Vision-Instruct_nothink
MiMo-VL-7B-SFT_nothink
ministral-3-3b
ministral-3-8b
ministral-3-14b
Molmo2-8B_nothink
Phi-3.5-vision-instruct
Qwen3.5-4B
Qwen3.5-4B_nothink
qwen3.5-9b
qwen3.5-9b_nothink
qwen3.5-397b
qwen3.5-397b_nothink
qwen3.6-27b
qwen3.6-27b_nothink
qwen3.6-35b
qwen3.6-35b-latest
qwen3.6-35b-latest_nothink
qwen3.6-35b_nothink
Step3-VL-10B_nothink
    '''.split()

JUDGES = ["glm-4.6v", "Kimi-K25", "qwen3.5-397b"]

plt_constructed_response_dataset_id = "evaluation_records_plt_constructed_response"
plt_selected_response_dataset_id = 'plt_selected_response'
US_DATASET_GROUPS = {

        # ─── 美国 Praxis ───
        "praxis"                           : "praxis_*.jsonl",
        "barrons"                          : "barrons_*.jsonl",
        "mometrix"                         : "mometrix_*.jsonl",
        "kaplan"                           : "kaplan_*.jsonl",
        "kaplan2017"                       : "kaplan2017_*.jsonl",
        "dummies"                          : "dummies_*.jsonl",
        "allen"                            : "allen_*.jsonl",
        "learningexpress"                  : "learningexpress_*.jsonl",
        "cliffs0511"                       : "cliffs0511.jsonl",
        "cliffs_ss"                        : "cliffs_ss_*.jsonl",  # 新增：Cliffs SS
        "math0061"                         : "math0061.jsonl",
        "ppst_cliffs"                      : "ppst_cliffs.jsonl",
        plt_constructed_response_dataset_id: "evaluation_records_plt_constructed_response.jsonl",
        plt_selected_response_dataset_id   : "evaluation_selected_response_plt.jsonl",
}

US_DATASETS = list(US_DATASET_GROUPS.keys())

NTCE_DATASET = {

        "s1"       : "s1_*.jsonl",
        "s2"       : "s2_*.jsonl",
        "s3"       : "s3_senior_*.jsonl",
        "shijian"  : "shijian_senior_*.jsonl",  # 新增：中国试讲
        "interview": "structured_interview_*.jsonl",
}
DATASET_GROUPS = {
        "india"        : "india_sed_*.jsonl",  # 新增：印度
        # ─── 中国 NTCE ───
        **NTCE_DATASET,
        # ─── 法国 CAPES ───
        "capes"        : "extract_capes_*.jsonl",  # 新增：法国CAPES笔试
        "shijian_capes": "shijian_capes_france_*.jsonl",  # 新增：法国试讲
        #
        # # ─── 印度 ───

        # ─── 英国 QTS ───
        "qts"          : "qts_*.jsonl",  # 新增：英国QTS

        **US_DATASET_GROUPS
}
finished_dataset = [d for d in list(DATASET_GROUPS.keys()) if d not in ['capes', 'shijian_capes', 'qts']]
INCLUDED_DATASETS = [
        l for l in list(DATASET_GROUPS.keys()) if l not in {
                "capes", "shijian_capes", "qts"
        }
]

# 数据集来源分类
DATASET_SOURCE = {
        "praxis"         : "ETS Official",
        "barrons"        : "Barrons",
        "mometrix"       : "Mometrix",
        "kaplan"         : "Kaplan",
        "kaplan2017"     : "Kaplan 2017",
        "dummies"        : "Dummies",
        "allen"          : "Allen",
        "learningexpress": "LearningExpress",
        "cliffs0511"     : "CliffsNotes 5081",
        "cliffs_ss"      : "CliffsNotes SS",
        "math0061"       : "Math 0061",
        "ppst_cliffs"    : "PPST CliffsNotes",
}
question_field = 'question'
BLACKLIST_REASON_FIELD = "blacklist_reason"
PROMPT_FIELD_NAME = 'prompt'
ANSWER_FIELD = 'answer'


@dataclass(frozen=True)
class EvaluationRecordRow:
    value: dict[str, Any]

    @classmethod
    def from_json_line(
            cls,
            line: str,
            dataset: str | None = None,
            source_file: str | None = None,
            model_name: str | None = None,
            include_blacklist_reason: bool = True,
    ) -> "EvaluationRecordRow":
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError("evaluation result row must be a JSON object")
        r = normalize_record_for_filter(
                row,
                dataset=dataset,
                source_file=source_file,
                model_name=model_name,
        )
        r.setdefault(BLACKLIST_REASON_FIELD, "")
        return cls(
                r
        )

    def to_record(self) -> dict[str, Any]:
        return dict(self.value)


def normalize_record_for_filter(
        record: dict,
        dataset: str | None = None,
        source_file: str | None = None,
        model_name: str | None = None,
ispreparingblacklist=None) -> dict:
    normalized = dict(record)
    if dataset is not None:
        normalized.setdefault(SOURCE_DATASET_FIELD, dataset)
    if source_file is not None:
        normalized.setdefault(SOURCE_FILE_FIELD, source_file)
    try:
        fields = extract_prompt_fields(normalized)
    except Exception as e:
        fields = ''
    normalized.update(fields)
    if not normalized.get("prompt"):
        try:
            normalized["prompt"] = format_question(normalized, model_name=model_name)
        except Exception as e:
            if ispreparingblacklist:
                pass
            else:
                raise e
    return normalized



SOURCE_FILE_FIELD = "_source_file"
SOURCE_DATASET_FIELD = 'dataset'


def load_dataset_group(group_name: str, use_filter: bool = True) -> list[dict]:
    """加载一组数据集文件，合并为题目列表"""
    import glob as _glob
    pattern = os.path.join(DATASET_DIR, DATASET_GROUPS[group_name])
    files = sorted(_glob.glob(pattern))
    if not files:
        print(f"  [WARN] 找不到匹配文件：{pattern}")
        return []
    records = []
    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        r = EvaluationRecordRow.from_json_line(
                                line,
                                dataset=group_name,
                                source_file=os.path.basename(fp),
                                include_blacklist_reason=use_filter,
                        ).to_record()
                    except (ValueError, FileNotFoundError):
                        if use_filter:
                            continue
                        raise
                    if use_filter:
                        if r[BLACKLIST_REASON_FIELD]:
                            continue
                    records.append(r)
    return records


# ── 共享流程 ─────────────────────────────────────────────────
def load_datasets(dataset_names: list[str], limit: int | None = None,
                  use_filter: bool = True) -> dict[str, list]:
    print("正在加载数据集...")
    print(f"Blacklist filter: {'yes' if use_filter else 'no'}")
    datasets: dict[str, list] = {}
    for gname in dataset_names:
        if gname not in DATASET_GROUPS:
            print(f"[WARN] 未知数据集组：{gname}，跳过")
            continue
        records = load_dataset_group(gname, use_filter=use_filter)
        if limit:
            records = records[:limit]
        print(f"  {gname}: {len(records)} 题")
        datasets[gname] = records
    return datasets


def get_record_by_id(id):
    """Load all dataset groups and return the first record with the given id."""
    target_id = str(id)
    import glob as _glob

    for group_name, file_pattern in DATASET_GROUPS.items():
        pattern = os.path.join(DATASET_DIR, file_pattern)
        for fp in sorted(_glob.glob(pattern)):
            with open(fp, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        raw = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if str(raw.get("id", "")) != target_id:
                        continue
                    return EvaluationRecordRow.from_json_line(
                            line,
                            dataset=group_name,
                            source_file=os.path.basename(fp),
                            include_blacklist_reason=False,
                    ).to_record()
    raise KeyError(f"record id not found: {target_id}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="TeaCH 数据集加载示例")
    parser.add_argument("--datasets", nargs="+",
                        default=list(DATASET_GROUPS.keys())[:],
                        help=f"数据集组名，可选：{list(DATASET_GROUPS.keys())}")
    parser.add_argument("--limit", type=int, default=1,
                        help="每个数据集只取前N题（测试用）")
    parser.add_argument("--no-filter", action="store_true",
                        help="关闭 blacklist 过滤")
    args = parser.parse_args()

    datasets = load_datasets(args.datasets, limit=args.limit, use_filter=not args.no_filter)
    total_questions = sum(len(v) for v in datasets.values())
    print(f"\n共 {len(datasets)} 个数据集，{total_questions} 题")
    for gname, records in datasets.items():
        if records:
            print(f"\n  [{gname}] 第一题示例:")
            print(f"    id   : {records[0].get('id', 'N/A')}")
            print(f"    type : {records[0].get('type', 'N/A')}")


if __name__ == '__main__':
    main()
