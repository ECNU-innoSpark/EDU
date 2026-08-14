"""
评分模块：LLM-as-Judge 评分脚本和提示词库
"""

from .judge_prompts import get_judge_prompt, JUDGE_PROMPT_TEMPLATES
from .scoring_rules import get_max_score, SCORING_RULES, get_scoring_rules
from .scorer import TeachScorer, ScoringResult, ScoreExtractor

__all__ = [
    "get_judge_prompt",
    "JUDGE_PROMPT_TEMPLATES",
    "get_max_score",
    "get_scoring_rules",
    "SCORING_RULES",
    "TeachScorer",
    "ScoringResult",
    "ScoreExtractor",
]
