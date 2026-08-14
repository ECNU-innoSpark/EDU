"""
各国各科目的 LLM-as-Judge 评分提示词模板

支持的国家：
  - "china"  : 中国 NTCE (科目一/二/三/结构化/试讲)
  - "usa"    : 美国 Praxis/edTPA
  - "france" : 法国 CAPES RAEP
"""

# ═════════════════════════════════════════════════════════════════════════
# 中国 NTCE 评分提示词
# ═════════════════════════════════════════════════════════════════════════

CHINA_S1_JUDGE_PROMPT = """你是中国教师资格证（NTCE）笔试的资深阅卷教师，现在需要对"科目一·综合素质"的材料分析题进行评分。评分时请保持严格标准。

【题目与材料】
{question}

{material}

【参考答案与评分要点】
{reference_answer}

【考生作答】
{model_response}

【评分说明】
满分：{max_score} 分

【请严格按以下要求输出】
1. 必须在回复的第一行给出得分，格式为：得分：XX
2. 第二行及以后再写理由。
3. 理由请言简意赅，不要重复题目内容。

【评分标准】（严格标准）
- 高分（12-14分）：理论准确，引用2-3个具体理论，分析全面，与材料结合紧密，逻辑严密，表述规范
- 中等偏上（10-11分）：理论基本正确，引用1-2个理论，分析较全面，逻辑基本清晰，表述基本规范
- 中等（7-9分）：理论理解基本，理论引用不足，分析不够全面，有逻辑缺陷
- 低分（4-6分）：理论理解有误，缺乏理论支撑，分析片面，表述不规范
- 极低分（0-3分）：完全错误或答非所问

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

CHINA_S2_JUDGE_PROMPT_ANALYSIS = """你是中国教师资格证（NTCE）笔试的资深阅卷教师，现在需要对"科目二·教育知识与能力"的材料分析题进行评分。评分时请保持严格标准。

【题目与材料】
{question}

{material}

【参考答案与评分要点】
{reference_answer}

【考生作答】
{model_response}

【评分说明】
满分：{max_score} 分

【请严格按以下要求输出】
1. 必须在回复的第一行给出得分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过150字。

【评分标准】（严格标准）
- 高分（17-20分）：理论准确，引用2-3个具体理论，分析全面深入，与现象结合紧密，逻辑严密，表述规范专业
- 中等偏上（14-16分）：理论基本正确，引用1-2个理论，分析较全面，逻辑基本清晰，表述基本规范
- 中等（10-13分）：理论理解基本，引用理论不足，分析不够全面，有逻辑缺陷
- 低分（6-9分）：理论理解有误，缺乏理论支撑，分析片面，表述不规范
- 极低分（0-5分）：完全错误或答非所问

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

# ── 中国 S2 辨析题专用prompt ──────────────────────────────────────
CHINA_S2_JUDGE_PROMPT_DISCRIMINATION = """你是中国教师资格证（NTCE）笔试的资深阅卷教师，现在需要对"科目二·教育知识与能力"的辨析题进行评分。评分时请保持严格标准。

【重要】辨析题的评分逻辑：必须先判断正误，再分析理由。判断错误则整题低分（0-2分），即使后续分析有一定道理。

【题目】
{question}

【参考答案与评分要点】
{reference_answer}

【考生作答】
{model_response}

【评分说明】
满分：{max_score} 分

【请严格按以下要求输出】
1. 必须在回复的第一行给出得分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过150字。

【评分标准】（严格标准）
- 高分（7-8分）：判断正确，理论分析准确全面，表述规范
- 中等偏上（6分）：判断正确，理论分析基本准确但不够全面
- 中等（4-5分）：判断正确，但理论分析有偏差或不够深入
- 低分（2-3分）：判断正确但分析严重不足；或判断错误但分析有部分道理
- 极低分（0-1分）：判断错误且分析混乱，或答非所问

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

CHINA_S3_JUDGE_PROMPT_TEACHING_DESIGN = """你是中国教师资格证（NTCE）笔试的资深阅卷教师，现在需要对"科目三·学科知识与教学能力"的教学设计题进行评分。评分时请保持严格标准。

【题目要求】
{question}

【参考答案与评分要点】
{reference_answer}

【考生作答】
{model_response}

【评分说明】
满分：{max_score} 分

【请严格按以下要求输出】
1. 必须在回复的第一行给出得分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过200字。

【评分标准】（严格标准）
- 高分（17-20分）：目标明确具体、重难点准确、方法恰当专业、环节完整、体现学生中心、评价科学
- 中等偏上（14-16分）：目标基本明确、重难点基本准确、方法基本恰当、环节基本完整、基本体现学生中心
- 中等（10-13分）：目标和重难点有偏差、方法不够专业、环节不够完整、理念体现不充分
- 低分（6-9分）：目标把握不准、设计有明显问题、逻辑不清晰、专业性欠缺
- 极低分（0-5分）：严重不符合要求、逻辑混乱

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

CHINA_S3_JUDGE_PROMPT_GENERAL = """你是中国教师资格证（NTCE）笔试的资深阅卷教师，现在需要对"科目三·学科知识与教学能力"的主观题进行评分。评分时请保持严格标准。

【题目要求】
{question}

【参考答案与评分要点】
{reference_answer}

【考生作答】
{model_response}

【评分说明】
满分：{max_score} 分

【请严格按以下要求输出】
1. 必须在回复的第一行给出得分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过200字。

【评分标准】（严格标准）
- 高分（85-100%满分）：要点覆盖全面，学科知识准确，分析/解答深入，论证有理有据，表述规范专业
- 中等偏上（70-84%满分）：要点基本完整，知识基本准确，分析/解答较充分，逻辑基本清晰
- 中等（50-69%满分）：要点有遗漏，知识有偏差，分析/解答不够深入，表述不够规范
- 低分（25-49%满分）：要点严重遗漏，知识有明显错误，分析片面，逻辑不清
- 极低分（0-24%满分）：完全错误或答非所问

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

# ═════════════════════════════════════════════════════════════════════════
# 面试评分提示词
# ═════════════════════════════════════════════════════════════════════════

CHINA_STRUCTURED_INTERVIEW_JUDGE_PROMPT = """你是中国教师资格证面试的评委，现在需要对考生的结构化面试回答进行评分。

【面试题目】
{question}

【参考答案/评分要点】
{reference_answer}

【考生回答】
{model_response}

【评分说明】
满分：{max_score} 分

【评分维度】（共40分，仪表仪态10分LLM无法评分，故仅评以下4个维度）
- 职业认知（5分）：对教师职业的理解是否深刻，教育理念是否正确
- 心理素质（5分）：情绪是否稳定，应对压力是否得当，态度是否积极
- 言语表达（15分）：语言是否清晰流畅，逻辑是否严密，表达是否得体
- 思维品质（15分）：分析是否全面深入，是否有创新观点，应变能力如何

【请严格按以下要求输出】
1. 必须在回复的第一行给出总分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过200字。

【评分标准】
- 高分（34-40分）：职业认知深刻，心理素质佳，表达流畅专业，思维敏捷有深度
- 中等偏上（26-33分）：认知基本正确，情绪稳定，表达基本清晰，思维较有条理
- 中等（18-25分）：认知一般，情绪尚可，表达有瑕疵，思维不够深入
- 低分（10-17分）：认知有偏差，情绪不稳定，表达欠佳，思维混乱
- 极低分（0-9分）：严重偏离要求或答非所问

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

CHINA_INTERVIEW_JUDGE_PROMPT = """你是中国教师资格证面试的评委，现在需要对考生的试讲进行评分。

【试讲题目与要求】
{question}

【教案格式参考】
{reference_answer}

【考生试讲实录】
{model_response}

【评分说明】
满分：{max_score} 分

【评分维度】
- 教学设计（10分）：教学目标明确、重难点把握准确、教学环节合理
- 教学实施（35分）：讲解清晰、师生互动充分、教学方法恰当、课堂掌控力强
- 教学评价（10分）：关注学生反馈、及时调整教学、有教学反思意识

【请严格按以下要求输出】
1. 必须在回复的第一行给出总分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过200字。

【评分标准】
- 高分（45-55分）：教学设计完整科学，讲解准确生动，师生互动自然，教学艺术性强
- 中等偏上（35-44分）：设计基本合理，讲解基本清晰，有一定互动，教学流程完整
- 中等（25-34分）：设计有缺陷，讲解不够清晰，互动不足，流程不完整
- 低分（15-24分）：设计有明显问题，讲解有错误，缺乏互动
- 极低分（0-14分）：严重偏离要求或内容空洞

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

# ═════════════════════════════════════════════════════════════════════════
# 美国 Praxis 评分提示词（英文）
# ═════════════════════════════════════════════════════════════════════════

# ── Praxis PLT 构造题（0/1/2分制，来源：5623 Study Companion General Scoring Guide）──
USA_PRAXIS_PLT_JUDGE_PROMPT = """You are a Praxis exam grader. Please score the following constructed-response question using the ETS official scoring guide.

【Question】
{question}

【Reference Answer】
{reference_answer}

【Student Response】
{model_response}

【Scoring Rubric】
Max Score: {max_score} points (0-2 scale)

Use the ETS General Scoring Guide for Praxis PLT constructed-response questions:

Score of 2 — A response in this category:
• Demonstrates a thorough understanding of the aspects of the case that are relevant to the question
• Responds appropriately to all parts of the question
• Provides a strong explanation, when required, that is well supported by relevant evidence
• Demonstrates a strong knowledge of pedagogical concepts, theories, facts, procedures, or methodologies relevant to the question

Score of 1 — A response in this category:
• Demonstrates a basic understanding of the aspects of the case that are relevant to the question
• Responds appropriately to one portion of the question
• Provides a weak explanation, when required, that is supported by relevant evidence
• Demonstrates some knowledge of pedagogical concepts, theories, facts, procedures, or methodologies relevant to the question

Score of 0 — A response in this category:
• Demonstrates misunderstanding of the aspects of the case that are relevant to the question
• Fails to respond appropriately to the question
• Is not supported by relevant evidence
• Demonstrates little knowledge of pedagogical concepts, theories, facts, procedures, or methodologies relevant to the question

No credit is given for a blank or off-topic response.

【Please provide score in this format】
Score: {0, 1, or 2}
Reasoning: {brief explanation, max 100 words}
"""

# ── Praxis 学科考试构造题（0/1/2/3分制，来源：5089/5205 Study Companion Scoring Guide）──
USA_PRAXIS_SUBJECT_CR_JUDGE_PROMPT = """You are a Praxis exam grader. Please score the following constructed-response question using the ETS official scoring guide.

【Question】
{question}

【Reference Answer】
{reference_answer}

【Student Response】
{model_response}

【Scoring Rubric】
Max Score: {max_score} points (0-3 scale)

Use the ETS Scoring Guide for Praxis subject assessment constructed-response questions:

Score of 3 — A response in this category:
• Shows a thorough understanding of the stimulus (where appropriate)
• Provides an accurate and complete response
• Demonstrates a thorough understanding of the subject matter relevant to the question

Score of 2 — A response in this category:
• Shows an adequate understanding of the stimulus (where appropriate)
• Provides a mostly accurate and complete response
• Demonstrates general understanding of the subject matter relevant to the question

Score of 1 — A response in this category:
• Shows little understanding of the stimulus (where appropriate)
• Provides a basically inaccurate and incomplete response
• Demonstrates weak or limited understanding of the subject matter relevant to the question

Score of 0 — A response in this category:
• A totally or almost completely incorrect response; or simply rephrases the question
• Demonstrates no understanding of the subject matter relevant to the question

【Please provide score in this format】
Score: {0, 1, 2, or 3}
Reasoning: {brief explanation, max 100 words}
"""

# ── Praxis Core Writing 构造题（1-6分holistic制，来源：Barron's Praxis Core + Core Study Guide Rubric）──
USA_PRAXIS_WRITING_JUDGE_PROMPT = """You are a Praxis exam grader. Please score the following essay/writing response using the ETS holistic scoring method and constructed response rubric.

【Question】
{question}

【Reference Answer】
{reference_answer}

【Student Response】
{model_response}

【Scoring Rubric】
Max Score: {max_score} points (1-6 holistic scale)

Each essay is graded holistically by raters using a 6-point scale (1=lowest, 6=highest). Evaluate the response on these four domains:

1. **Content Knowledge** — The response directly addresses every part of the prompt; demonstrates independent knowledge of the topic; discusses the topic at an appropriate depth.
2. **Organization** — The response introduces the topic with a thesis statement; directly addresses the prompt; answer is supported by logical arguments or evidence; restates the main idea in the conclusion.
3. **Arguments and Examples** — The response provides a reasonable answer; supported by strong reasoning or evidence; develops ideas logically and connects ideas; reasoning supports a unified main idea.
4. **Language and Usage** — Effective grammar and varied sentence structure; correct spelling, punctuation, and capitalization; strong and varied vocabulary relevant to the topic.

Scoring Standards (1-6 scale):
- 6: Outstanding — excels in all four domains; thorough, well-organized, compelling, polished
- 5: Strong — strong in most domains; well-developed with minor weaknesses
- 4: Adequate — adequate in most domains; reasonably organized and supported
- 3: Limited — limited in one or more domains; some development but significant gaps
- 2: Weak — weak in most domains; poorly organized, little support, many errors
- 1: Inadequate — fails to address the prompt; incoherent or extremely brief

【Please provide score in this format】
Score: {1, 2, 3, 4, 5, or 6}
Reasoning: {brief explanation referencing the 4 domains, max 150 words}
"""

# ── 美国 Praxis 无参考答案通用评分提示词（4维度，来源：Core Study Guide Constructed Response Rubric）──
USA_PRAXIS_NO_REF_JUDGE_PROMPT = """You are a Praxis exam grader. The question below does not have a reference answer, so you must evaluate the response based on general educational standards and professional rubrics.

【Question】
{question}

【Student Response】
{model_response}

【Scoring Rubric】
Max Score: {max_score} points

Evaluate the response on the following dimensions, each equally weighted:

1. **Content Knowledge** — Are the facts, concepts, and pedagogical principles stated correctly? Does the response directly address every part of the prompt? Does it demonstrate independent knowledge of the topic?
2. **Organization** — Is the response well-structured, coherent, and clearly communicated? Does it introduce the topic, support with logical arguments, and conclude effectively?
3. **Arguments and Examples** — Does the response provide reasonable answers supported by strong reasoning or evidence? Are ideas developed logically and connected to one another?
4. **Language and Usage** — Is the grammar correct with varied sentence structure? Are spelling, punctuation, and vocabulary appropriate?

【Scoring Standards】
- 90-100%: Exceptional — comprehensive, insightful, flawlessly applies theory
- 70-89%: Proficient — solid understanding, accurate application, minor gaps
- 50-69%: Basic — addresses the prompt but with inaccuracies, superficial analysis
- 30-49%: Below Expectations — significant errors, largely misses the point
- 0-29%: Inadequate — off-topic, factually wrong, or no substantive response

【Please provide score in this format】
Score: {score}
Reasoning: {brief explanation referencing the 4 dimensions, max 150 words}
"""

# ═════════════════════════════════════════════════════════════════════════
# 法国 CAPES 评分提示词（中文）
# ═════════════════════════════════════════════════════════════════════════

FRANCE_CAPES_JUDGE_PROMPT = """你是法国CAPES（Certificat d'Aptitude au Professorat de l'Enseignement du Second Degré）考试的资深阅卷教师，现在需要对考生的学科笔试作答进行评分。该考试为法国国家教师选拔的外部竞争性考试（concours externe），涵盖数学、物理化学、生物、历史地理、哲学、文献、法文、美术、音乐等学科。

【题目与材料】
{question}

【参考答案/评委评析】
{reference_answer}

【考生作答】
{model_response}

【评分说明】
满分：{max_score} 分（0-20分制）

评分依据：
1. 法国官方规定所有考试统一0-20分制（"Les épreuves sont notées de 0 à 20"）
2. 评委会在评分时考虑考生对法语的书面掌握程度（词汇、语法、动词变位、标点、拼写）
3. 总分低于5分淘汰（"Une note globale égale ou inférieure à 5 est éliminatoire"）

本研究基于各学科Rapports du jury提炼的6维度综合评价框架（非法国教育部统一规定）：
1. 题目回应的切合度：作答是否准确回应题目要求，是否围绕核心问题展开
2. 学科知识的掌握：对学科核心概念、理论和方法的掌握与运用是否准确
3. 论证的逻辑性：论证结构是否清晰有序，推理是否严密，论据是否充分
4. 分析的深度：对材料/文本/问题的分析是否深入，是否有多层次解读
5. 批判性思维：是否能独立思考，提出有见地的观点和判断
6. 表达与规范性：书面表达是否准确流畅，术语使用是否规范，语法拼写是否正确

【评分标准】（严格标准）
- 优秀（16-20分）：所有标准均达到或超过预期，学科知识扎实，论证严密，分析深入
- 良好（12-15分）：大多数标准达到预期，知识基本准确，论证较清晰
- 及格（8-11分）：部分标准达到预期，知识有偏差，论证有欠缺
- 不及格（0-7分）：未达到预期，知识有重大错误或答非所问

【请严格按以下要求输出】
1. 必须在回复的第一行给出得分，格式为：得分：XX
2. 第二行及以后再写理由，总字数不要超过200字。

【请按以下格式给出评分结果】
得分：{得分数字}
理由：{简要说明，不超过150字}
"""

# ═════════════════════════════════════════════════════════════════════════
# 提示词模板字典
# ═════════════════════════════════════════════════════════════════════════

JUDGE_PROMPT_TEMPLATES = {
    # 中国科目一
    "china_s1_analysis": CHINA_S1_JUDGE_PROMPT,

    # 中国科目二
    "china_s2_analysis": CHINA_S2_JUDGE_PROMPT_ANALYSIS,
    "china_s2_discrimination": CHINA_S2_JUDGE_PROMPT_DISCRIMINATION,

    # 中国科目三
    "china_s3_teaching_design": CHINA_S3_JUDGE_PROMPT_TEACHING_DESIGN,
    "china_s3_general": CHINA_S3_JUDGE_PROMPT_GENERAL,

    # 中国面试
    "china_structured_interview": CHINA_STRUCTURED_INTERVIEW_JUDGE_PROMPT,
    "china_interview": CHINA_INTERVIEW_JUDGE_PROMPT,

    # 美国 Praxis（按考试类型细分）
    "usa_praxis_plt": USA_PRAXIS_PLT_JUDGE_PROMPT,
    "usa_praxis_subject_cr": USA_PRAXIS_SUBJECT_CR_JUDGE_PROMPT,
    "usa_praxis_writing": USA_PRAXIS_WRITING_JUDGE_PROMPT,
    "usa_praxis_no_ref": USA_PRAXIS_NO_REF_JUDGE_PROMPT,
    # 保留旧key的兼容映射（指向新版prompt）
    "usa_praxis": USA_PRAXIS_PLT_JUDGE_PROMPT,
    "usa_praxis_no_ref_old": USA_PRAXIS_NO_REF_JUDGE_PROMPT,
    "france_capes": FRANCE_CAPES_JUDGE_PROMPT,
}


def get_judge_prompt(country: str, subject: str, question_type: str, has_reference: bool = True,
                     source_exam: str = "", question_type_original: str = "") -> str:
    """
    获取相应国家、科目、题型的评分提示词模板

    参数：
        country: "china", "usa", "france"
        subject: "s1", "s2", "s3", "praxis", "capes", "interview" 等
        question_type: "材料分析题", "教学设计题", "case_analysis" 等
        has_reference: 是否有参考答案（美国无参考答案时用通用标准prompt）
        source_exam: 数据来源考试编号（如 "praxis_5623", "barrons_core_writing_5722"）
        question_type_original: 原始题型标记（如 "Constructed-Response"）

    返回：
        对应的提示词模板（str）或 None 如果找不到
    """
    # 构建键
    if country == "china":
        if subject == "s1":
            if "材料" in question_type or "分析" in question_type or len(question_type) < 10:
                return JUDGE_PROMPT_TEMPLATES.get("china_s1_analysis")
        elif subject == "s2":
            if "辨析" in question_type:
                return JUDGE_PROMPT_TEMPLATES.get("china_s2_discrimination")
            elif "材料" in question_type or "分析" in question_type:
                return JUDGE_PROMPT_TEMPLATES.get("china_s2_analysis")
            elif "简答" in question_type:
                return JUDGE_PROMPT_TEMPLATES.get("china_s2_analysis")
        elif subject == "s3":
            if "教学设计" in question_type or "设计" in question_type:
                return JUDGE_PROMPT_TEMPLATES.get("china_s3_teaching_design")
            else:
                return JUDGE_PROMPT_TEMPLATES.get("china_s3_general")
        elif "interview" in subject or "shijian" in subject:
            if "结构化" in question_type or subject == "interview":
                return JUDGE_PROMPT_TEMPLATES.get("china_structured_interview")
            return JUDGE_PROMPT_TEMPLATES.get("china_interview")

    elif country == "usa":
        # 根据考试编号和题型选择对应的评分prompt
        exam_id = source_exam.lower() if source_exam else ""

        # Core Writing (5722/5723): 1-6分holistic
        if "5722" in exam_id or "5723" in exam_id or "writing" in exam_id:
            if has_reference:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_writing")
            else:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_no_ref")

        # PLT (5622/5623/5624): 0/1/2分制
        if any(x in exam_id for x in ["5622", "5623", "5624"]):
            if has_reference:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_plt")
            else:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_no_ref")

        # 学科考试 (5086/5089/5205/5001/5081): 0/1/2/3分制
        if any(x in exam_id for x in ["5001", "5081", "5086", "5089", "5205"]):
            if has_reference:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_subject_cr")
            else:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_no_ref")

        # Kaplan PLT: 0/1/2分制
        if "kaplan" in exam_id or "5624" in exam_id:
            if has_reference:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_plt")
            else:
                return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_no_ref")

        # Barrons Writing: 1-6分holistic
        if "barrons" in exam_id:
            if "writing" in exam_id or "5722" in exam_id:
                if has_reference:
                    return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_writing")
                else:
                    return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_no_ref")

        # 通用回退：有参考答案用PLT prompt，无参考答案用NO_REF prompt
        if has_reference:
            return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_plt")
        else:
            return JUDGE_PROMPT_TEMPLATES.get("usa_praxis_no_ref")

    elif country == "france" and subject == "capes":
        return JUDGE_PROMPT_TEMPLATES.get("france_capes")

    return None
