"""
所有模块的路径配置和基本参数
"""

import os
from pathlib import Path

# 凭据一律从 .env 读，不写进源码 —— 本仓库要开源，写死的 key 等于公开泄露。
# .env 已列入 .gitignore；参照 .env.example 复制一份填进去即可。
try:
    from dotenv import load_dotenv
except ImportError:                      # 没装 python-dotenv 就只用环境变量
    load_dotenv = None
else:
    load_dotenv(Path(__file__).resolve().parent / ".env")


def _required_env(name: str) -> str | None:
    """读取凭据；缺失时返回 None，由调用方在真正要用时报错。

    这里不直接抛异常：很多脚本（比如只做数据统计的）根本不碰 API，
    import config 时就崩掉会很难用。
    """
    return os.environ.get(name)


# API 配置 —— 统一代理（Claude / Gemini / GPT / Doubao）
API_KEY = _required_env("INNOSPARK_API_KEY")
API_BASE = os.environ.get("INNOSPARK_API_BASE", "https://api.innospark.cn/v1")

# PDF 题目提取用（Vision 模型）
EXTRACT_MODEL = os.environ.get("EXTRACT_MODEL", "Kimi-K25")  # Vision 能力最好
EXTRACT_API_KEY = _required_env("EXTRACT_API_KEY")
EXTRACT_API_BASE = os.environ.get("EXTRACT_API_BASE", "")

# 推理用的模型配置（开源免费）。原先这里写死过 KIMI / QWEN / GLM46V 的
# key 与 endpoint，现已移除；需要时在 .env 里定义同名变量。
KIMI_MODEL = os.environ.get("KIMI_MODEL", "kimi-k2.5")
KIMI_KEY = _required_env("KIMI_KEY")
KIMI_BASE = os.environ.get("KIMI_BASE", "")

QWEN_MODEL = os.environ.get("QWEN_MODEL", "qwen3.5-397b")
QWEN_KEY = _required_env("QWEN_KEY")
QWEN_BASE = os.environ.get("QWEN_BASE", "")

GLM46V_KEY = _required_env("GLM46V_KEY")
GLM46V_BASE = os.environ.get("GLM46V_BASE", "")

# MinerU PDF 转 Markdown API


# 项目根目录
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_ROOT = os.path.join(ROOT, "教资考试真题")
DATASET_DIR = os.path.join(ROOT, "dataset")

# ── 笔试 ──────────────────────────────────────────────────────────────

WRITTEN = os.path.join(DATA_ROOT, "笔试")

# 科目一（综合素质，中学通用）
S1_PDF_DIR  = os.path.join(WRITTEN, "1.《综合素质》历年真题（2011下-2025上）", "中学综合素质PDF（真题）（推荐打印）")
S1_ANS_DIR  = os.path.join(WRITTEN, "1.《综合素质》历年真题（2011下-2025上）", "中学（综合素质）参考答案及解析")

# 科目二（教育知识与能力，中学通用）
S2_PDF_DIR  = os.path.join(WRITTEN, "2.《教育知识与能力》历年真题（2011下-2025上）", "中学知识与能力PDF（真题）（推荐打印）")
S2_ANS_DIR  = os.path.join(WRITTEN, "2.《教育知识与能力》历年真题（2011下-2025上）", "中学（知识与能力）参考答案及解析")

# 科目三 — 高中语文
S3_CHINESE_PDF_DIR = os.path.join(WRITTEN, "高中语文", "历年真题")
S3_CHINESE_ANS_DIR = os.path.join(WRITTEN, "高中语文", "答案解析")

# 科目三 — 高中数学
S3_MATH_PDF_DIR = os.path.join(WRITTEN, "（高中）数学", "（高中）数学", "【02】历年真题", "高中数学", "历年真题")
S3_MATH_ANS_DIR = os.path.join(WRITTEN, "（高中）数学", "（高中）数学", "【02】历年真题", "高中数学", "答案解析")

# 科目三 — 高中美术
S3_ART_PDF_DIR = os.path.join(WRITTEN, "（高中）美术", "（高中）美术", "【02】历年真题", "高中美术", "高中美术真题2014-2024上", "【01】高中美术真题（2013下-2024上）")
S3_ART_ANS_DIR = os.path.join(WRITTEN, "（高中）美术", "（高中）美术", "【02】历年真题", "高中美术", "高中美术真题2014-2024上", "【02】高中美术真题解析（2013下-2024上）")

# 科目三 — 高中历史
S3_HISTORY_PDF_DIR = os.path.join(WRITTEN, "（高中）历史", "（高中）历史", "【02】历年真题", "高中历史真题14上-24上", "历年真题")
S3_HISTORY_ANS_DIR = os.path.join(WRITTEN, "（高中）历史", "（高中）历史", "【02】历年真题", "高中历史真题14上-24上", "答案解析")

# 科目三 — 高中地理
S3_GEOGRAPHY_PDF_DIR = os.path.join(WRITTEN, "高中地理", "历年真题")
S3_GEOGRAPHY_ANS_DIR = os.path.join(WRITTEN, "高中地理", "答案解析")

# 科目三 — 高中信息技术
S3_IT_PDF_DIR = os.path.join(WRITTEN, "高中信息技术", "历年真题")
S3_IT_ANS_DIR = os.path.join(WRITTEN, "高中信息技术", "答案解析")

# 科目三 — 高中生物
S3_BIOLOGY_PDF_DIR = os.path.join(WRITTEN, "（高中）生物", "（高中）生物", "【02】历年真题", "高中生物", "高中生物真题12下-24上", "【01】高中生物真题（2012下-2024上）")
S3_BIOLOGY_ANS_DIR = os.path.join(WRITTEN, "（高中）生物", "（高中）生物", "【02】历年真题", "高中生物", "高中生物真题12下-24上", "【02】高中生物真题解析（2012下-2024上）")

# 科目三 — 高中物理
S3_PHYSICS_PDF_DIR = os.path.join(WRITTEN, "（高中）物理", "（高中）物理", "【02】历年真题", "高中物理", "高中物理真题16下-24上", "高中物理真题")
S3_PHYSICS_ANS_DIR = os.path.join(WRITTEN, "（高中）物理", "（高中）物理", "【02】历年真题", "高中物理", "高中物理真题16下-24上", "高中物理真题解析")

# 科目三 — 高中思想品德（政治）
S3_POLITICS_PDF_DIR = os.path.join(WRITTEN, "（高中）思想品德", "（高中）思想品德", "【02】历年真题", "高中政治", "9.高中政治真题15下-24上", "高中政治真题")
S3_POLITICS_ANS_DIR = os.path.join(WRITTEN, "（高中）思想品德", "（高中）思想品德", "【02】历年真题", "高中政治", "9.高中政治真题15下-24上", "高中政治真题解析")

# 科目三 — 高中化学
S3_CHEMISTRY_PDF_DIR = os.path.join(WRITTEN, "（高中）化学", "（高中）化学", "【02】历年真题", "高中化学", "高中化学真题15-24上", "历年真题")
S3_CHEMISTRY_ANS_DIR = os.path.join(WRITTEN, "（高中）化学", "（高中）化学", "【02】历年真题", "高中化学", "高中化学真题15-24上", "答案解析")

# 科目三 — 高中体育与健康
S3_PE_PDF_DIR = os.path.join(WRITTEN, "（高中）体育与健康", "（高中）体育与健康", "【02】历年真题", "高中体育", "高中体育真题15-24上", "历年真题")
S3_PE_ANS_DIR = os.path.join(WRITTEN, "（高中）体育与健康", "（高中）体育与健康", "【02】历年真题", "高中体育", "高中体育真题15-24上", "答案解析")

# 科目三 — 高中英语
S3_ENGLISH_PDF_DIR = os.path.join(WRITTEN, "高中英语", "历年真题")
S3_ENGLISH_ANS_DIR = os.path.join(WRITTEN, "高中英语", "答案解析")

# 科目三 — 高中音乐
S3_MUSIC_PDF_DIR = os.path.join(WRITTEN, "高中音乐", "【01】高中音乐真题（2015上-2024上）")
S3_MUSIC_ANS_DIR = os.path.join(WRITTEN, "高中音乐", "【02】高中音乐真题解析（2015上-2024上）")

# ── 面试 ──────────────────────────────────────────────────────────────

INTERVIEW = os.path.join(DATA_ROOT, "面试")

# 结构化面试（中小学通用）
STRUCT_DIR  = os.path.join(INTERVIEW, "结构化", "中小学")

# 试讲（按学段/学科）
SHIJIAN_DIR = os.path.join(INTERVIEW, "教案", "试讲（分科目发送）")

# ── 各模块题型说明 ────────────────────────────────────────────────────

MODULE_INFO = {
    "s1": {
        "name": "综合素质",
        "level": "中学",
        "mcq_count": 29,
        "mcq_score": 58,
        "subjective_types": ["材料分析题"],
    },
    "s2": {
        "name": "教育知识与能力",
        "level": "中学",
        "mcq_count": 21,
        "mcq_score": 42,
        "subjective_types": ["辨析题", "简答题", "材料分析题"],
    },
    "s3_chinese": {
        "name": "高中语文学科知识与教学能力",
        "level": "高中",
        "subject": "语文",
        "mcq_count": 25,
        "mcq_score": 50,
        "subjective_types": ["案例分析题", "教学设计题"],
    },
    "s3_math": {
        "name": "高中数学学科知识与教学能力",
        "level": "高中",
        "subject": "数学",
        "mcq_count": 25,
        "mcq_score": 50,
        "subjective_types": ["案例分析题", "教学设计题"],
        "has_image": True,   # 含公式图片，需多模态处理
    },
}
