"""Score single- and multiple-choice model responses without an LLM judge.

This is the self-contained release counterpart of
``scripts/stage3_gather_responses/mcq_is_correct.py``.  Run this file directly
to execute its unit tests::

    python scoring/score_selected_response.py
"""

from __future__ import annotations

import ast
import re
import unittest
from dataclasses import dataclass
from typing import Any, Mapping, Optional


_MISSING_ANSWERS = frozenset({"", "none", "nan", "null"})


def normalize_answer(answer: Any) -> Optional[str]:
    """Normalize a reference answer or extracted choice to a compact string."""
    if answer is None:
        return None

    if isinstance(answer, (list, tuple, set)):
        return "".join(sorted(str(item).strip().upper() for item in answer))

    text = str(answer).strip()
    if text.lower() in _MISSING_ANSWERS:
        return None

    # Serialized answer lists occur in CSV inputs, for example ``['A', 'C']``.
    if text.startswith("["):
        try:
            parsed = ast.literal_eval(text)
        except (SyntaxError, ValueError):
            parsed = None
        if isinstance(parsed, list):
            return "".join(
                sorted(str(item).strip().upper() for item in parsed)
            )

    # Comma-delimited multiple-choice keys: ``A, C, D`` -> ``ACD``.
    if "," in text:
        parts = [part.strip().upper() for part in text.split(",")]
        if all(len(part) == 1 and part.isalpha() for part in parts):
            return "".join(sorted(parts))

    if re.fullmatch(r"[A-E]", text, flags=re.IGNORECASE):
        return text.upper()
    return text


def extract_choice(response: Any) -> Optional[str]:
    """Extract the selected A--E option letters from a model response."""
    if response is None or not str(response).strip():
        return None
    response = str(response).strip()
    if response.startswith("[ERROR]"):
        return None

    separated_choices = (
        r"[A-E](?:(?:\s*[,，、/]\s*|\s*(?:和|及|与)\s*|\s+)[A-E])+"
    )
    choice_sequence = rf"(?:{separated_choices}|[A-E]+)"

    def compact(value: str) -> str:
        return "".join(re.findall(r"[A-E]", value.upper()))

    # English answer markers, including ``Final answer: A, C``.
    match = re.search(
        rf"(?:the\s+)?(?:correct\s+|final\s+)?"
        rf"answer(?:\s+is)?(?:\s*[:=])?\s*[\(（]?"
        rf"({choice_sequence})",
        response,
        flags=re.IGNORECASE,
    )
    if match:
        return compact(match.group(1))

    # Chinese answer markers, including ``【答案】BC``.
    match = re.search(
        rf"(?:【\s*)?(?:正确答案|答案)(?:\s*】)?"
        rf"(?:\s*[:：=])?\s*[\(（]?({choice_sequence})",
        response,
        flags=re.IGNORECASE,
    )
    if match:
        return compact(match.group(1))

    match = re.search(
        rf"<\|begin_of_box\|>\s*({choice_sequence})"
        rf"\s*<\|end_of_box\|>",
        response,
        flags=re.IGNORECASE,
    )
    if match:
        return compact(match.group(1))

    last_line = response.splitlines()[-1].strip()
    if re.fullmatch(r"\(?[A-E]+\)?", last_line, flags=re.IGNORECASE):
        return re.search(r"[A-E]+", last_line, flags=re.IGNORECASE).group().upper()

    match = re.fullmatch(
        rf"\s*[\(（\[]?\s*({separated_choices})"
        rf"\s*[\)）\]]?\s*[。.]?\s*",
        last_line,
        flags=re.IGNORECASE,
    )
    if match:
        return compact(match.group(1))

    # Match the final independent option sequence as the original scorer does.
    matches = re.findall(r"(?:^|[^A-Za-z])([A-E]+)(?:[^A-Za-z]|$)", response)
    return matches[-1].upper() if matches else "Z"


def check_answer(model_choice: Optional[str], standard: Optional[str]) -> bool:
    """Use exact match for multiple choice and the original single-choice rule."""
    if not model_choice or not standard:
        return False
    if len(standard) < 2:
        return model_choice in standard or model_choice == standard
    return sorted(model_choice) == sorted(standard)


def get_standard_answer(reference: Mapping[str, Any]) -> Any:
    """Prefer ``answer_options`` and fall back to ``answer``."""
    return reference.get("answer_options", reference.get("answer"))


@dataclass(frozen=True)
class SelectedResponseScore:
    """Auditable result of grading one selected-response model output."""

    model_output: str
    extracted_choice: Optional[str]
    standard_answer: Optional[str]
    is_correct: bool


def score_selected_response(
    model_output: Any,
    reference: Mapping[str, Any],
) -> SelectedResponseScore:
    """Grade one model output against a selected-response reference record."""
    output = "" if model_output is None else str(model_output)
    standard = normalize_answer(get_standard_answer(reference))
    choice = extract_choice(normalize_answer(output))
    return SelectedResponseScore(
        model_output=output,
        extracted_choice=choice,
        standard_answer=standard,
        is_correct=check_answer(choice, standard),
    )


class FixedOutputModel:
    """Small deterministic model stub used by the self-contained unit test."""

    def __init__(self, output: str):
        self.output = output

    def generate(self, prompt: str) -> str:
        del prompt
        return self.output


class SelectedResponseScoringTest(unittest.TestCase):
    def test_model_output_to_multiple_choice_score(self) -> None:
        model = FixedOutputModel(
            "<think>I compared each statement.</think>\nFinal answer: C, A"
        )
        output = model.generate("Select every correct option.")
        score = score_selected_response(
            output,
            {"answer": "B", "answer_options": ["A", "C"]},
        )

        self.assertEqual(score.extracted_choice, "CA")
        self.assertEqual(score.standard_answer, "AC")
        self.assertTrue(score.is_correct)

    def test_single_choice(self) -> None:
        score = score_selected_response("The correct answer is D.", {"answer": "d"})
        self.assertEqual(score.extracted_choice, "D")
        self.assertTrue(score.is_correct)

    def test_multiple_choice_requires_exact_set(self) -> None:
        score = score_selected_response("答案：A, C", {"answer": "A, B, C"})
        self.assertFalse(score.is_correct)

    def test_error_output_is_incorrect(self) -> None:
        score = score_selected_response("[ERROR] timeout", {"answer": "A"})
        self.assertIsNone(score.extracted_choice)
        self.assertFalse(score.is_correct)


if __name__ == "__main__":
    unittest.main()
