"""
各国各科目的评分规则：满分分数、评分细则等

数据来源：
  - 中国：NTCE官方评分标准、workplan.md
  - 美国：Praxis官方评分框架、edTPA手册
  - 法国：CAPES官方评分标准
  - 印度：100% MCQ，不需要主观题评分
"""
from input_datasets.load import plt_constructed_response_dataset_id
from parse_evaluation.dataclass_ import EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE

# ═════════════════════════════════════════════════════════════════════════
# 中国 NTCE 评分规则
# ═════════════════════════════════════════════════════════════════════════

CHINA_SCORING_RULES = {
    "s1": {
        "科目": "综合素质",
        "题型": {
            "单项选择题": {"满分": 58, "题数": 29, "单题分": 2, "评分方式": "accuracy"},
            "材料分析题": {"满分": 42, "题数": 3, "单题分": 14, "评分方式": "judge"},
        },
        "总分": 100,
        "评分维度": {
            "要点覆盖度": "是否包含参考答案中的关键要点",
            "论述准确性": "表述是否准确、无事实错误",
            "理论运用": "是否恰当运用教育理论和法律法规",
            "逻辑清晰": "论证逻辑是否严密、结构是否清晰",
        }
    },

    "s2": {
        "科目": "教育知识与能力",
        "题型": {
            "单项选择题": {"满分": 42, "题数": 21, "单题分": 2, "评分方式": "accuracy"},
            "辨析题": {"满分": 32, "题数": 4, "单题分": 8, "评分方式": "judge"},
            "简答题": {"满分": 32, "题数": 4, "单题分": 8, "评分方式": "judge"},
            "材料分析题": {"满分": 40, "题数": 2, "单题分": 20, "评分方式": "judge"},
        },
        "总分": 100,
        "评分维度": {
            "理论理解": "教育学、心理学基本理论的理解准确性",
            "理论应用": "将理论应用于分析教育现象的能力",
            "论述完整": "回答是否全面、要点是否完整",
            "表述规范": "表述是否专业、逻辑是否清晰",
        }
    },

    "s3_senior": {
        "科目": "学科知识与教学能力（高中）",
        "题型": {
            "单项选择题": {"满分": 50, "题数": 25, "单题分": 2, "评分方式": "accuracy"},
            "案例分析题": {"满分": 30, "题数": "若干", "单题分": 20, "评分方式": "judge"},
            "教学设计题": {"满分": 20, "题数": "1", "单题分": 20, "评分方式": "judge"},
        },
        "总分": 100,
        "评分维度": {
            "学科知识掌握": "对学科核心知识和概念的理解",
            "教学法应用": "学科教学法的恰当应用",
            "教学设计": "教学目标、重难点、教学环节的设计",
            "学生理解": "是否能从学生角度出发考虑教学",
            "表述专业": "用语是否准确、规范",
        }
    },

    "interview_structured": {
        "科目": "结构化面试",
        "评分维度": {
            "职业认知": {"满分": 5, "评分方式": "judge"},
            "心理素质": {"满分": 5, "评分方式": "judge"},
            "言语表达": {"满分": 15, "评分方式": "judge"},
            "思维品质": {"满分": 15, "评分方式": "judge"},
        },
        "总分": 40,  # 官方满分50分，但仪表仪态LLM无法评
        "说明": "仪表仪态(5分)无法通过LLM评分，故可评分总计40分",
    },

    "interview_demo": {
        "科目": "试讲",
        "评分维度": {
            "教学设计": {"满分": 10, "评分方式": "judge"},
            "教学实施": {"满分": 35, "评分方式": "judge"},
            "教学评价": {"满分": 10, "评分方式": "judge"},
        },
        "总分": 55,
        "说明": "根据NTCE官方标准，教案设计(10分) + 现场表现(40分)，其中现场表现包含教学实施(35分) + 教学评价(10分)，但实际合计为55分可评",
    },
}

# ═════════════════════════════════════════════════════════════════════════
# 美国 Praxis 评分规则
# ═════════════════════════════════════════════════════════════════════════

USA_PRAXIS_SCORING_RULES = {
    "praxis_core": {
        "科目": "Praxis Core（基础学术技能）",
        "模块": {
            "reading": {"满分": 100, "题数": "约50", "评分方式": "accuracy"},
            "writing": {"满分": 100, "题数": "约50", "评分方式": "accuracy"},
            "math": {"满分": 100, "题数": "约50", "评分方式": "accuracy"},
        },
        "说明": "Core为通用基础科目，不分学科，全为MCQ"
    },

    "praxis_plt": {
        "科目": "Praxis PLT（教学原理与实践）",
        "评分方式": "accuracy",
        "满分": 100,
        "说明": "PLT（7-12年级版本为5624）考查教学理论，主要为选择题和案例分析题"
    },

    "praxis_subject": {
        "科目": "Praxis 学科评估",
        "评分方式": "accuracy",
        "满分": 100,
        "说明": "各学科独立评估，考查学科内容知识和教学应用",
    },

    "edtpa": {
        "科目": "edTPA（教学表现评估）",
        "tasks": {
            "task_1_planning": {
                "名称": "Task 1: Planning（教学规划）",
                "满分": 20,
                "rubrics": 5,
                "单项分": "1-5分制",
                "评分维度": [
                    "Content and Curricular Goals",
                    "Understanding Students",
                    "Learning Objectives",
                    "Instructional Strategies",
                    "Resources and Adaptation"
                ]
            },
            "task_2_instruction": {
                "名称": "Task 2: Instruction（教学实施）",
                "满分": 20,
                "rubrics": 5,
                "单项分": "1-5分制",
                "评分维度": [
                    "Alignment of Instruction to Outcomes",
                    "Quality of Teacher Explanations",
                    "Engagement of Students in Learning",
                    "Lesson Pacing",
                    "Responsiveness to Students"
                ]
            },
            "task_3_assessment": {
                "名称": "Task 3: Assessment（学生评估）",
                "满分": 20,
                "rubrics": 5,
                "单项分": "1-5分制",
                "评分维度": [
                    "Design of Assessments",
                    "Interpretation of Assessment Data",
                    "Student Readiness/Misconceptions",
                    "Adjustment of Instruction",
                    "Student Self-Assessment"
                ]
            }
        },
        "总分": 60,
        "说明": "edTPA为表现性评估，基于教学视频、教案、学生作品等"
    }
}

# ═════════════════════════════════════════════════════════════════════════
# 法国 CAPES 评分规则
# ═════════════════════════════════════════════════════════════════════════

FRANCE_CAPES_SCORING_RULES = {
    "capes": {
        "科目": "CAPES（法国国家教师选拔考试）",
        "考试类型": "concours externe（外部竞争性考试）笔试",
        "满分": 20,
        "评分标准": {
            "题目回应的切合度": {
                "满分": 20,
                "说明": "作答是否准确回应题目要求，是否围绕核心问题展开"
            },
            "学科知识的掌握": {
                "满分": 20,
                "说明": "对学科核心概念、理论和方法的掌握与运用是否准确"
            },
            "论证的逻辑性": {
                "满分": 20,
                "说明": "论证结构是否清晰有序，推理是否严密，论据是否充分"
            },
            "分析的深度": {
                "满分": 20,
                "说明": "对材料/文本/问题的分析是否深入，是否有多层次解读"
            },
            "批判性思维": {
                "满分": 20,
                "说明": "是否能独立思考，提出有见地的观点和判断"
            },
            "表达与规范性": {
                "满分": 20,
                "说明": "书面表达是否准确流畅，术语使用是否规范，语法拼写是否正确"
            }
        },
        "评分范围": {
            "16-20": "优秀（Très bien）",
            "12-15": "良好（Bien）",
            "8-11": "及格（Assez bien）",
            "0-7": "不及格（Insuffisant），低于5分淘汰",
        },
        "说明": "6项标准综合评分，0-20分制。适用于数学、物理化学、生物、历史地理、哲学、文献、法文、美术、音乐等所有学科。"
    }
}

# ═════════════════════════════════════════════════════════════════════════
# 印度评分规则（仅MCQ，不需主观题评分）
# ═════════════════════════════════════════════════════════════════════════

INDIA_SCORING_RULES = {
    "india_ntqe": {
        "科目": "印度教师资格考试（NTCE）",
        "评分方式": "accuracy（100% MCQ）",
        "满分": 100,
        "说明": "印度教师资格考试为全选择题，不含主观题，无需LLM评分"
    }
}

# ═════════════════════════════════════════════════════════════════════════
# 综合评分规则（按数据集名称前缀快速查找）
# ═════════════════════════════════════════════════════════════════════════

SCORING_RULES = {
    **CHINA_SCORING_RULES,
    **USA_PRAXIS_SCORING_RULES,
    **FRANCE_CAPES_SCORING_RULES,
    **INDIA_SCORING_RULES,
}


def _extract_score_from_text(question_text: str) -> int:
    """
    从题目文本中提取总分值

    查找模式：
      - "（本大题共1小题，共15分）" → 15
      - "（20分）" → 取所有分值之和
      - "共XX分" → XX
    """
    import re
    if not question_text:
        return None

    # 1. 优先匹配 "共XX分"（通常是大题总分）
    m = re.search(r'共\s*(\d+)\s*分', question_text)
    if m:
        return int(m.group(1))

    # 2. 收集所有 "（XX分）" 形式的小题分值，求和
    sub_scores = re.findall(r'[（(]\s*(\d+)\s*分\s*[）)]', question_text)
    if sub_scores:
        return sum(int(s) for s in sub_scores)

    return None


# s3 各题型的默认分值（题目文本无法提取时的回退值）
_S3_DEFAULT_SCORES = {
    "案例分析题": 20, "教学设计题": 20, "材料分析题": 20,
    "分析题": 15, "教学情境分析题": 20, "课例点评题": 15, "案例点评题": 15,
    "诊断题": 15,
    "简答题": 10, "问答题": 10, "解答题": 10, "论述题": 15, "辨析题": 10,
    "计算题": 10,
    "编创题": 10, "音乐编创题": 10, "音乐作品分析题": 15,
}


def get_max_score(dataset: str, question_type: str, question_text: str = None) -> int:
    """
    根据数据集名称和题型，查询单题满分分数

    参数：
        dataset: 数据集名称，如 "s1_2024u", "s1", "praxis_plt_7_12"
        question_type: 题型，如 "材料分析题", "单项选择题"（可能是乱码）
        question_text: （可选）题目原文，用于从文本中动态提取分值

    返回：
        单题满分分数（int），或 None 如果找不到
    """
    # 中国科目一
    from input_datasets.load import US_DATASETS
    if dataset == "s1" or dataset.startswith("s1_"):
        # 题型可能是乱码，用关键词匹配
        if "材料" in question_type or "分析" in question_type or len(question_type) < 10:
            return CHINA_SCORING_RULES["s1"]["题型"]["材料分析题"]["单题分"]

    # 中国科目二
    elif dataset == "s2" or dataset.startswith("s2_"):
        s2_types = CHINA_SCORING_RULES["s2"]["题型"]
        # 先尝试精确匹配
        if question_type in s2_types:
            return s2_types[question_type].get("单题分")
        # 再尝试关键词匹配
        if "材料" in question_type:
            return s2_types["材料分析题"].get("单题分")
        elif "辨析" in question_type:
            return s2_types["辨析题"].get("单题分")
        elif "简答" in question_type:
            return s2_types["简答题"].get("单题分")

    # 中国科目三 —— 题型多、分值不固定，优先从题目文本提取
    elif dataset == "s3" or dataset.startswith("s3_"):
        # 1) 先尝试从题目文本动态提取
        if question_text:
            extracted = _extract_score_from_text(question_text)
            if extracted:
                return extracted
        # 2) 查默认分值表
        if question_type in _S3_DEFAULT_SCORES:
            return _S3_DEFAULT_SCORES[question_type]
        # 3) 关键词模糊匹配
        for key, score in _S3_DEFAULT_SCORES.items():
            if key[:2] in question_type:
                return score
        # 4) 最终回退
        return 20

    # 中国面试（结构化）
    elif dataset == "interview" or dataset.startswith("structured_interview_"):
        # 结构化面试可评4个维度共40分（仪表仪态10分LLM无法评）
        return CHINA_SCORING_RULES["interview_structured"]["总分"]

    # 中国试讲（排除 shijian_capes）
    elif dataset == "shijian" or (dataset.startswith("shijian_") and "capes" not in dataset):
        # 试讲返回总分
        return CHINA_SCORING_RULES["interview_demo"]["总分"]

    # 美国 Praxis / Barrons / Kaplan 等主观题
    elif any(x in dataset for x in US_DATASETS):
        # 根据考试类型返回对应的官方满分分数
        # PLT (5622/5623/5624): 每题0-2分，满分2分
        # 学科考试 (5086/5089/5205): 每题0-3分，满分3分
        # Core Writing (5722/5723): 每篇1-6分，满分6分
        # 注：5001/5081/5625的"Constructed-Response"实际是MCQ误标，不应到这里
        if question_type in ["案例分析题", "材料分析题", "Constructed-Response"]:
            return 2   # PLT构造题0/1/2分制
        elif question_type == "写作题":
            return 6   # Core Writing 1-6分holistic
        elif question_type == "填空题":
            return 5   # Numeric-Entry 填空题默认5分
        elif question_type == EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE:
            return 2   # Numeric-Entry 填空题默认5分
        # return None

    # 法国 CAPES
    elif dataset == "capes" or dataset.startswith("extract_capes_") or dataset.startswith("shijian_capes_") or "capes" in dataset:
        return FRANCE_CAPES_SCORING_RULES["capes"]["满分"]

    # 印度
    elif dataset.startswith("india_"):
        # 印度全是MCQ
        return None

    return None


# ═════════════════════════════════════════════════════════════════════════
# 核心数据集映射配置（从脚本迁移至此处）
# ═════════════════════════════════════════════════════════════════════════

# 各数据集的主观题题型定义
SUBJECTIVE_TYPES = {
    "s1": ["材料分析题"],
    "s2": ["辨析题", "简答题", "材料分析题"],
    "s3": ["案例分析题", "教学设计题", "简答题", "解答题", "论述题",
           "材料分析题", "问答题", "分析题", "编创题", "课例点评题",
           "教学情境分析题", "音乐作品分析题", "诊断题", "音乐编创题",
           "计算题", "辨析题", "案例点评题"],
    "interview": ["结构化面试"],
    "shijian": ["试讲"],
    "capes": ["problem", "材料分析题", "论述题"], # 法国CAPES笔试（type=problem）
    "shijian_capes": ["CAPES考试"], # 法国CAPES考试题
    "praxis": ["案例分析题", "材料分析题", "写作题"], # 美国Praxis主观题
    #     , "填空题"
    #     , "填空题"
    "barrons": ["写作题"], # 美国Barrons主观题
    "kaplan": ["案例分析题"], # 美国Kaplan主观题
    plt_constructed_response_dataset_id: [EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE], # 美国Kaplan主观题
}

# 数据集到国家/科目的映射关系
DATASET_META = {
    "s1": {"country": "china", "subject": "s1"},
    "s2": {"country": "china", "subject": "s2"},
    "s3": {"country": "china", "subject": "s3"},
    "interview": {"country": "china", "subject": "interview"},
    "shijian": {"country": "china", "subject": "shijian"},
    "capes": {"country": "france", "subject": "capes"},
    "shijian_capes": {"country": "france", "subject": "capes"},
    "praxis": {"country": "usa", "subject": "praxis"},
    "barrons": {"country": "usa", "subject": "praxis"},
    "kaplan": {"country": "usa", "subject": "praxis"},
    plt_constructed_response_dataset_id: {"country": "usa", "subject": "praxis"},
}


def get_scoring_rules(dataset: str) -> dict:
    """
    获取某个数据集的完整评分规则

    参数：
        dataset: 数据集名称，如 "s1_2024u" 或 "s1"

    返回：
        评分规则字典，或 None 如果找不到
    """
    if dataset == "s1" or dataset.startswith("s1_"):
        return CHINA_SCORING_RULES.get("s1")
    elif dataset == "s2" or dataset.startswith("s2_"):
        return CHINA_SCORING_RULES.get("s2")
    elif dataset == "s3" or dataset.startswith("s3_"):
        return CHINA_SCORING_RULES.get("s3_senior")
    elif dataset == "interview" or dataset.startswith("structured_interview_"):
        return CHINA_SCORING_RULES.get("interview_structured")
    elif dataset == "shijian" or dataset.startswith("shijian_"):
        return CHINA_SCORING_RULES.get("interview_demo")
    elif "praxis" in dataset or dataset in ("barrons", "kaplan"):
        return USA_PRAXIS_SCORING_RULES.get("praxis_subject")
    elif dataset.startswith("extract_capes_") or dataset.startswith("shijian_capes_") or "capes" in dataset:
        return FRANCE_CAPES_SCORING_RULES.get("capes")
    elif dataset.startswith("india_") or "india" in dataset:
        return INDIA_SCORING_RULES.get("india_ntqe")

    return None
