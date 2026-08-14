"""
各题型的 Prompt 模板。
每个函数接收一道题的 dict，返回发给模型的 user message 字符串。

数据字段说明：
  选择题：question + options
  主观题（简答/辨析）：question
  材料分析题：material + sub_questions（list of str）
  教学设计题：question
  结构化面试：question
"""
from typing import Optional

from config import DATASET_DIR
from parse_evaluation.dataclass_ import EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE
from parse_evaluation.dataclass_ import EVALUATIONRECORD_SELECTED_RESPONSE_TYPE


def fmt_question_text(q: dict) -> str:
    """统一取题干文本，兼容 question / question_text / material+sub_questions 三种结构"""

    if "question" in q and q["question"]:  # 没有处理空字符
        return q["question"]
    # 法国 CAPES 数据：题干在 question_text 字段
    if "question_text" in q and q["question_text"]:
        return q["question_text"]
    # 材料分析题结构：material + sub_questions
    parts = []
    if q.get("material"):
        parts.append(q["material"])
    if q.get("sub_questions"):
        subs = q["sub_questions"]
        if isinstance(subs, list):
            for i, sq in enumerate(subs, 1):
                parts.append(f"（{i}）{sq}")
        else:
            parts.append(str(subs))
    if not parts:
        raise ValueError(f"题目缺少题干字段（question/question_text/material）: id={q.get('id')}")
    return "\n".join(parts)


def fmt_selected_response_cn(q: dict) -> str:
    """单项/多项选择题"""
    lines = [fmt_question_text(q), ""]
    if q.get("options"):
        for k, v in q["options"].items():
            lines.append(f"{k}. {v}")
    lines += [
            "",
            "请直接给出答案字母（如：A 或 AB），不需要解释。",
    ]
    return "\n".join(lines)


def fmt_selected_response_en(q: dict) -> str:
    """单项/多项选择题"""
    lines = [fmt_question_text(q), ""]
    if q.get("options"):
        for k, v in q["options"].items():
            lines.append(f"{k}. {v}")
    lines += [
            "",
            "Please provide only the letter(s) of the answer (e.g., A or AB); no explanation is required.",
    ]
    return "\n".join(lines)


def fmt_short_answer_s3(q: dict) -> str:
    """简答题 / 辨析题"""
    lines = [
            "你是一名参加中小学教师资格考试科目三（学科知识与教学能力）的考生，",
            "【题目】",
            fmt_question_text(q),
            "",
            "请结合相关学科知识与教育学及心理学知识，给出完整、准确的回答。",
    ]
    return "\n".join(lines)


def fmt_short_answer_cn(q: dict) -> str:
    """简答题 / 辨析题"""
    lines = [
            "【题目】",
            fmt_question_text(q),
            "",
            "请根据教育学和心理学知识，给出完整、准确的回答。",
    ]

    return "\n".join(lines)


def fmt_writing_en(q: dict) -> str:
    """简答题 / 辨析题"""
    lines = [
            "[Quesion]",
            fmt_question_text(q),
            "",
            "Write your essay here.",
    ]
    return "\n".join(lines)


def fmt_passage_constructed_response_en(q: dict) -> str:
    #    {'id': 'parse_evaluation_plt_1_001',
    # 'question': "1. What would be the best way for Ms. Morris to respond to the note she has received from her student's parent?",
    # 'answer': "1. First, Ms. Morris should not be judgmental of the parent or Alicja based on the note's contents and composition flaws. She should reflect on the purpose of the note, the context of the situation, and what this all means in regard to Alicja's education and her role in it. As a first-year teacher, Ms. Morris may want to bring the note to her administrator and/or school social worker before responding to the parent or talking with Alicja. Administrators and social workers usually understand the needs of the community in which the school resides and can shed some light on the situation. Also, if Ms. Morris is unfamiliar with the community environment, family circumstances, and economic conditions that might warrant Alicja babysitting while her parent works, the administrator or social worker can help her think about how to respond. Second, this note might be a cause for Ms. Morris to reflect on just how much and the purpose for the homework she is assigning each night. Homework should not be busy work. It should be purposeful. It might be best to change the homework routine or to talk with Alicja about other times during the school day she has available to work on homework. Perhaps she is not using a study hall time advantageously to complete her homework before she even gets home. Respectful reflection, discussion, and planning should help solve this dilemma.\n",
    # 'passage': "## PLT Case History 5.1\n\nDirections: Read the following case history, then answer the three short-answer questions that follow. You are not expected to include citations of specific texts, authors, or theories in your responses. Your answers will be evaluated, however, based on your use of professionally accepted practices and principles in learning and teaching. Some questions have multiple parts, so be sure your response addresses all components of each question.\n\n## Ms. Morris\n\n## Scenario\n\nAnn Morris is a first-year teacher who is fresh out of her university undergraduate program. She was happy to get a position two months after graduation as a ninth-grade teacher in an inner-city school. Ms. Morris is looking forward to working with the 135 underprivileged adolescents who will pass through her Earth Science class each day. She is committed to her students' learning and to the professional services she can offer her students and their families. She believes she understands the magnitude of the responsibility inherent in teaching.\n\nOne week into the school year, one of Ms. Morris's students brings her a note from home. The handwritten note contains many unconventional spellings and incorrect grammar. Ms. Morris can barely believe the note is from a parent, based on the quality of the writing. In the note, the parent questions Ms. Morris's practice of giving homework to the students every night. She writes:\n\nAlicja can't do no for hour a work evry nite. She got to watch the kids so I be to work.\n\nMs. Morris interpreted the message to read, Alicja can't do four hours of work every night. She has to watch the kids so I can go to work.\n\n## PLT Case History 5.1 Questions",
    # 'explanation': '',
    # 'module': '',
    # 'subject': '',
    # 'type': 'constructed_response',
    # 'language': 'en',
    # 'source_exam': 'plt_1_question.pdf-db462577-447b-473d-ab8f-e4adc15d61b8',
    # 'source_exam_pdf': 'plt_1_answer.pdf-3e5f76c0-4dcc-4e9d-9d73-709ac14a4c4d',
    # 'has_image': False,
    # 'options': None,
    # 'dataset': 'evaluation_records_plt_constructed_response',
    # '_source_file': 'evaluation_records_plt_constructed_response.jsonl',
    # 'question_text': "1. What would be the best way for Ms. Morris to respond to the note she has received from her student's parent?"}
    lines = [
            "[Question]",
            q['question'],
            "Write your essay here.",
    ]

    passage = q.get('passage')
    if passage:
        lines = [
                        "[Material]",
                        passage,
                        "", ] + lines
    return "\n".join(lines)


def fmt_passage_selected_response_en(q: dict) -> str:
    #    {'id': 'parse_evaluation_plt_1_001',
    # 'question': "1. What would be the best way for Ms. Morris to respond to the note she has received from her student's parent?",
    # 'answer': "1. First, Ms. Morris should not be judgmental of the parent or Alicja based on the note's contents and composition flaws. She should reflect on the purpose of the note, the context of the situation, and what this all means in regard to Alicja's education and her role in it. As a first-year teacher, Ms. Morris may want to bring the note to her administrator and/or school social worker before responding to the parent or talking with Alicja. Administrators and social workers usually understand the needs of the community in which the school resides and can shed some light on the situation. Also, if Ms. Morris is unfamiliar with the community environment, family circumstances, and economic conditions that might warrant Alicja babysitting while her parent works, the administrator or social worker can help her think about how to respond. Second, this note might be a cause for Ms. Morris to reflect on just how much and the purpose for the homework she is assigning each night. Homework should not be busy work. It should be purposeful. It might be best to change the homework routine or to talk with Alicja about other times during the school day she has available to work on homework. Perhaps she is not using a study hall time advantageously to complete her homework before she even gets home. Respectful reflection, discussion, and planning should help solve this dilemma.\n",
    # 'passage': "## PLT Case History 5.1\n\nDirections: Read the following case history, then answer the three short-answer questions that follow. You are not expected to include citations of specific texts, authors, or theories in your responses. Your answers will be evaluated, however, based on your use of professionally accepted practices and principles in learning and teaching. Some questions have multiple parts, so be sure your response addresses all components of each question.\n\n## Ms. Morris\n\n## Scenario\n\nAnn Morris is a first-year teacher who is fresh out of her university undergraduate program. She was happy to get a position two months after graduation as a ninth-grade teacher in an inner-city school. Ms. Morris is looking forward to working with the 135 underprivileged adolescents who will pass through her Earth Science class each day. She is committed to her students' learning and to the professional services she can offer her students and their families. She believes she understands the magnitude of the responsibility inherent in teaching.\n\nOne week into the school year, one of Ms. Morris's students brings her a note from home. The handwritten note contains many unconventional spellings and incorrect grammar. Ms. Morris can barely believe the note is from a parent, based on the quality of the writing. In the note, the parent questions Ms. Morris's practice of giving homework to the students every night. She writes:\n\nAlicja can't do no for hour a work evry nite. She got to watch the kids so I be to work.\n\nMs. Morris interpreted the message to read, Alicja can't do four hours of work every night. She has to watch the kids so I can go to work.\n\n## PLT Case History 5.1 Questions",
    # 'explanation': '',
    # 'module': '',
    # 'subject': '',
    # 'type': 'constructed_response',
    # 'language': 'en',
    # 'source_exam': 'plt_1_question.pdf-db462577-447b-473d-ab8f-e4adc15d61b8',
    # 'source_exam_pdf': 'plt_1_answer.pdf-3e5f76c0-4dcc-4e9d-9d73-709ac14a4c4d',
    # 'has_image': False,
    # 'options': None,
    # 'dataset': 'evaluation_records_plt_constructed_response',
    # '_source_file': 'evaluation_records_plt_constructed_response.jsonl',
    # 'question_text': "1. What would be the best way for Ms. Morris to respond to the note she has received from her student's parent?"}

    lines = [
            "[Question]",
            q['question'],
            "Please diretly give answer letter (e.g. A or AB). No explanation needed.",
    ]

    passage = q.get('passage')
    if passage:
        lines = [
                        "[Material]",
                        passage,
                        "", ] + lines
    return "\n".join(lines)


def fmt_case_analysis_cn(q: dict) -> str:
    """材料分析题 / 案例分析题"""
    text = fmt_question_text(q)
    lines = [
            "【材料】",
            text,
            "",
            "请结合材料，运用相关教育理论进行深入分析，回答须有理有据、层次清晰。",
    ]
    return "\n".join(lines)


def fmt_teaching_design_cn(q: dict) -> str:
    """教学设计题"""
    lines = [
            "【教学设计任务】",
            fmt_question_text(q),
            "",
            "请设计一份完整的教学方案，包括：教学目标（三维目标）、教学重难点、"
            "教学过程（导入—新授—练习—小结—作业）、教学方法说明。",
    ]
    return "\n".join(lines)


def fmt_structured_interview_cn(q: dict) -> str:
    """结构化面试题"""
    lines = [
            "【面试情境】",
            fmt_question_text(q),
            "",
            "请以教师应聘者的身份，给出你的回答。要求：观点明确，逻辑清晰，"
            "体现教育情怀与职业素养。",
    ]
    return "\n".join(lines)


def fmt_teaching_demo_cn(q: dict) -> str:
    """试讲题"""
    parts = []
    if q.get("lesson_title"):
        parts.append(f"课题：{q['lesson_title']}")
    if q.get("subject"):
        parts.append(f"学科：{q['subject']}")
    if q.get("level"):
        parts.append(f"学段：{q['level']}")
    if q.get("content"):
        parts.append(f"\n【教学内容】\n{q['content']}")
    if q.get("requirements"):
        reqs = q["requirements"]
        if isinstance(reqs, list):
            reqs = "\n".join(f"  {i + 1}. {r}" for i, r in enumerate(reqs))
        parts.append(f"\n【教学要求】\n{reqs}")

    lines = [
            "【试讲任务】",
            "\n".join(parts),
            "",
            "请根据以上内容完成一份完整的试讲稿，包括：",
            "1. 导入环节：创设情境，引出课题",
            "2. 新授环节：讲解核心知识，注意师生互动",
            "3. 巩固练习：设计练习或讨论活动",
            "4. 小结与作业：总结要点，布置课后任务",
            "要求：语言自然流畅，体现师生互动，符合课标理念。",
    ]
    return "\n".join(lines)


def fmt_capes_written_exam(q: dict) -> str:
    """法国CAPES written exam（数学/物理等学科解题）"""
    subject = q.get("subject", "")
    lines = [
            f"【CAPES {subject}笔试题】" if subject else "【CAPES笔试题】",
            format_question(q),
            "",
            "Please solve the problem step by step in French or Chinese. "
            "Show your reasoning clearly and provide complete proofs or calculations where required.",
    ]
    return "\n".join(lines)


def fmt_capes_teaching_demo(q: dict) -> str:
    """法国CAPES考试题（多学科笔试/口试，shijian_capes数据集）"""
    subject = q.get("subject") or ""
    parts = []
    if q.get("lesson_title"):
        parts.append(f"考试：{q['lesson_title']}")
    if subject:
        parts.append(f"学科：{subject}")
    if q.get("content"):
        parts.append(f"\n【考试内容】\n{q['content']}")
    if q.get("requirements"):
        reqs = q["requirements"]
        if isinstance(reqs, list):
            reqs = "\n".join(f"  {i + 1}. {r}" for i, r in enumerate(reqs))
        parts.append(f"\n【考试要求】\n{reqs}")

    lines = [
            f"【CAPES法国教师选拔考试 - {subject}】" if subject else "【CAPES法国教师选拔考试】",
            "\n".join(parts),
            "",
            "This is a French national teaching certification exam (CAPES). "
            "Please answer the question thoroughly in French or Chinese, "
            "demonstrating your subject knowledge, analytical depth, and logical argumentation.",
    ]
    return "\n".join(lines)


# 题型 → 该 formatter 使用的中间字段列表
TYPE_SCHEMA: dict[str, list[str]] = {
        # question_text = _get_question_text 的归一化结果；question 是大多数题型的原始字段
        "单项选择题"          : ["question", "question_text", "material", "sub_questions", "options"],
        "多项选择题"          : ["question", "question_text", "material", "sub_questions", "options"],
        "Selected Response"   : ["question", "question_text", "material", "sub_questions", "options"],
        "简答题"              : ["question", "question_text", "material", "sub_questions"],
        "辨析题"              : ["question", "question_text", "material", "sub_questions"],
        "材料分析题"          : ["question", "question_text", "material", "sub_questions"],
        "案例分析题"          : ["question", "question_text", "material", "sub_questions"],
        "Constructed-Response": ["question", "question_text", "material", "sub_questions"],
        "教学设计题"          : ["question", "question_text", "material", "sub_questions"],
        "结构化面试"          : ["question", "question_text", "material", "sub_questions"],
        "试讲"                : ["lesson_title", "subject", "level", "content", "requirements"],
        "CAPES考试"           : ["subject", "lesson_title", "content", "requirements"],
        "problem"             : ["subject", "question_text"],  # CAPES 原始字段即 question_text
}


def extract_prompt_fields(q: dict) -> dict:
    """按题型提取 format_question 用到的中间字段；未使用的字段值为 None。"""
    import os as _os
    img_size = None
    if q.get("has_image"):
        if not q.get("img"):
            raise ValueError(f"has_image=True 但 img 字段为空 (题目 id={q.get('id')})")
        img_path = _os.path.join(DATASET_DIR, q["img"])
        if not _os.path.exists(img_path):
            raise FileNotFoundError(f"图片文件不存在: {img_path}  (题目 id={q.get('id')})")
        img_size = _os.path.getsize(img_path)
    qtype = q.get("type", "")
    schema = TYPE_SCHEMA.get(qtype, ["question_text"])
    result = {}
    for field in schema:
        if field == "question_text":
            result["question_text"] = fmt_question_text(q)
        else:
            result[field] = q.get(field)
    if img_size is not None:
        result["img_size"] = img_size
    return result


# 题型 → 格式化函数映射
TYPE_TO_REPRESENTITIVE_FMT = {
        "单项选择题"                              : fmt_selected_response_cn,
        "多项选择题"                              : fmt_selected_response_cn,
        "简答题"                                  : fmt_short_answer_cn,
        "辨析题"                                  : fmt_short_answer_cn,
        "材料分析题"                              : fmt_case_analysis_cn,
        "案例分析题"                              : fmt_case_analysis_cn,
        "教学设计题"                              : fmt_teaching_design_cn,
        "结构化面试"                              : fmt_structured_interview_cn,
        "试讲"                                    : fmt_teaching_demo_cn,
        "CAPES考试"                               : fmt_capes_teaching_demo,  # 法国CAPES考试（多学科笔试/口试）
        "problem"                                 : fmt_capes_written_exam,  # 法国CAPES笔试学科题
        # Praxis 英文题型
        EVALUATIONRECORD_SELECTED_RESPONSE_TYPE   : fmt_selected_response_cn,
        "Constructed-Response"                    : fmt_case_analysis_cn,
        EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE: fmt_passage_constructed_response_en,
}

TYPE_TO_FMT_FNS = {
        "单项选择题"                              : [fmt_selected_response_cn, fmt_selected_response_en],
        "多项选择题"                              : [fmt_selected_response_cn, fmt_selected_response_en],
        "简答题"                                  : [fmt_short_answer_cn, fmt_passage_constructed_response_en],
        "辨析题"                                  : [fmt_short_answer_cn, fmt_passage_constructed_response_en],
        "材料分析题"                              : [fmt_case_analysis_cn, fmt_passage_constructed_response_en],
        "案例分析题"                              : [fmt_case_analysis_cn, fmt_passage_constructed_response_en],
        "教学设计题"                              : [fmt_teaching_design_cn, fmt_passage_constructed_response_en],
        "结构化面试"                              : [fmt_structured_interview_cn, fmt_passage_constructed_response_en],
        '写作题'                                  : [fmt_writing_en, fmt_passage_constructed_response_en],
        "试讲"                                    : [fmt_teaching_demo_cn, fmt_passage_constructed_response_en],
        "CAPES考试"                               : [fmt_capes_teaching_demo, fmt_passage_constructed_response_en],  # 法国CAPES考试（多学科笔试/口试）
        "problem"                                 : [fmt_capes_written_exam, fmt_passage_constructed_response_en],  # 法国CAPES笔试学科题
        # Praxis 英文题型
        EVALUATIONRECORD_SELECTED_RESPONSE_TYPE   : [fmt_selected_response_cn, fmt_selected_response_en],
        "Constructed-Response"                    : [fmt_passage_constructed_response_en, fmt_case_analysis_cn],
        EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE: [fmt_passage_constructed_response_en, fmt_selected_response_en],
}


def format_question(q: dict, model_name: Optional[str] = None) -> str:
    """根据题型自动选择格式化函数"""
    qtype = q.get("type", "")
    #
    fmt_fn = TYPE_TO_REPRESENTITIVE_FMT.get(qtype, fmt_short_answer_cn)

    from input_datasets.load import SOURCE_FILE_FIELD

    #    {'id': 'praxis_core_math_q003',
    # 'exam_year': None,
    # 'module': '科目一',
    # 'module_name': 'Praxis Core Academic Skills: Mathematics',
    # 'level': '高中',
    # 'type': '单项选择题',
    # 'number': 3,
    # 'question': 'A soft drink company surveyed a random sample of 1,240 people between the ages of 18 and 24 and found that 5 out of 8 of those surveyed liked the company’s new soft drink. Based on the results of the survey, if 200,000 people ages 18 to 24 were to try the new drink, which of the following statements would most likely be true?',
    # 'options': {'A': 'Between 90,000 and 100,000 people would like the new drink.',
    #  'B': 'Between 100,000 and 110,000 people would like the new drink.',
    #  'C': 'Between 110,000 and 120,000 people would like the new drink.',
    #  'D': 'Between 120,000 and 130,000 people would like the new drink.',
    #  'E': 'Between 130,000 and 140,000 people would like the new drink.'},
    # 'answer': 'D',
    # 'explanation': 'Option (D) is correct. Of the 200,000 people, the number of people that would like the new drink is approximately 5/8 × 200,000, or 125,000. Since 125,000 is between 120,000 and 130,000, the answer is choice (D).',
    # 'has_image': False,
    # 'language': 'en',
    # 'source_exam': 'praxis_5733',
    # 'content_category': None,
    # 'question_type_original': 'Selected-Response',
    # '_source_file': 'praxis_core_math.jsonl',
    # 'question_text': 'A soft drink company surveyed a random sample of 1,240 people between the ages of 18 and 24 and found that 5 out of 8 of those surveyed liked the company’s new soft drink. Based on the results of the survey, if 200,000 people ages 18 to 24 were to try the new drink, which of the following statements would most likely be true?',
    # 'material': None,
    # 'sub_questions': None}
    from input_datasets.load import SOURCE_DATASET_FIELD
    from input_datasets.load import US_DATASETS
    from input_datasets.load import large_t1t2_models
    if q[SOURCE_DATASET_FIELD] in US_DATASETS:
        if model_name in large_t1t2_models:
            fmt_fn = {
                    '单项选择题'                              : fmt_selected_response_cn,
                    '多项选择题'                              : fmt_selected_response_cn,
                    '写作题'                                  : fmt_writing_en,
                    '案例分析题'                              : fmt_question_text,
                    '材料分析题'                              : fmt_question_text,
                    '填空题'                                  : fmt_question_text,
                    EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE: fmt_passage_constructed_response_en,
                    EVALUATIONRECORD_SELECTED_RESPONSE_TYPE   : fmt_passage_selected_response_en,
            }[qtype]
        else:
            fmt_fn = {
                    '单项选择题'                              : fmt_selected_response_cn,
                    '多项选择题'                              : fmt_selected_response_cn,
                    '写作题'                                  : fmt_writing_en,
                    '案例分析题'                              : fmt_case_analysis_cn,
                    '材料分析题'                              : fmt_case_analysis_cn,
                    '填空题'                                  : fmt_short_answer_cn,
                    EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE: fmt_passage_constructed_response_en,
                    EVALUATIONRECORD_SELECTED_RESPONSE_TYPE   : fmt_passage_selected_response_en,
            }[qtype]
    if q.get(SOURCE_FILE_FIELD, '').startswith('s3') and model_name not in large_t1t2_models:
        # In [1]: q
        # Out[1]:
        # {'exam_year': '2013下',
        #  'module': '科目三',
        #  'module_name': '高中美术学科知识与教学能力',
        #  'level': '高中',
        #  'subject': '美术',
        #  'id': 's3_senior_art_2013d_27',
        #  'type': '简答题',
        #  'number': 27,
        #  'question': '徐悲鸿对现代美术教育有哪些贡献?',
        #  'answer': '徐悲鸿是中国现代美术教育家中的重要代表，在美术教育上建立了一套较为明确而富有特色的美术创作、美术教育理论并且影响重大。综览其理论框架主要是：(1)科学主义的理性精神。以科学主义为思想的美术教学原则，建立规范化与理性的美术教学体系，是徐悲鸿美术教育思想的一贯核心。他坚持以素描作为造型艺术学习的基础和主要手段，强调素描教学对其他艺术教学的主导作用，在美术教学中建立一套科学的逻辑规则，使艺术具有理性特征。并且，这种以科学主义为理论基础的美术教育思想在其具体的教育实践中日臻完善。(2)写实主义的教学原则。把西方写实艺术原则融入美术教学的始终是徐悲鸿美术教育思想的主要基点。他明确提出“素描为一切造型艺术之基础”，引进西方绘画的写实手法，建立有别于传统教育观念的新型教学体系。(3)现实主义的创作观念。徐悲鸿在绘画思想、创作手法、教育主旨中处处求“真”， 以他执着的态度倡真求实，他反复强调“真”在艺术中的重要性同他的绘画创作一样具有鲜明的现实主义精神，他的“真”在新时代背景下被赋予新的生命。',
        #  'has_image': False,
        #  '_source_file': 's3_senior_art_2013d.jsonl',
        #  'question_text': '徐悲鸿对现代美术教育有哪些贡献?',
        #  'material': None,
        #  'sub_questions': None}
        fmt_fn = {
                fmt_short_answer_cn: fmt_short_answer_s3
        }.get(fmt_fn, fmt_fn)
    return fmt_fn(q)


def get_prompt_candidates(q: dict, model_name: Optional[str] = None) -> str:
    qtype = q.get("type", "")
    fmt_fns = TYPE_TO_FMT_FNS.get(qtype, fmt_short_answer_cn)
    from input_datasets.load import SOURCE_DATASET_FIELD
    from input_datasets.load import NTCE_DATASET
    if q[SOURCE_DATASET_FIELD] in NTCE_DATASET:

        if q[SOURCE_DATASET_FIELD] in {'s3'}:
            fmt_fns = {
                    "简答题": [fmt_short_answer_s3, fmt_passage_constructed_response_en],
                    "辨析题": [fmt_short_answer_s3, fmt_passage_constructed_response_en],
            }.get(fmt_fns, fmt_fns)
    else:
        fmt_fns = {
                '案例分析题'                              : [fmt_question_text, fmt_case_analysis_cn, ],
                '材料分析题'                              : [fmt_question_text, fmt_case_analysis_cn, ],
                EVALUATIONRECORD_CONSTRUCTED_RESPONSE_TYPE: [fmt_passage_constructed_response_en, fmt_selected_response_cn, ],
                EVALUATIONRECORD_SELECTED_RESPONSE_TYPE   : [fmt_passage_selected_response_en, fmt_selected_response_cn, ],
        }.get(qtype, fmt_fns)
    return [fmt_fn(q) for fmt_fn in fmt_fns]
