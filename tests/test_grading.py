import pytest
import pandas as pd
from smartexam_mr.models.grading import TFIDFGrader


def test_exact_match_score():
    """Verify that identical texts score exactly 20.0 points."""
    grader = TFIDFGrader()
    text = "un modèle de calcul inspiré du cerveau humain"
    score = grader.grade_answer(text, text)
    assert score == 20.0


def test_non_overlapping_score():
    """Verify that completely disjoint vocabularies score 0.0 points."""
    grader = TFIDFGrader()
    reference = "pomme banane cerise"
    student = "voiture chien chat"
    score = grader.grade_answer(reference, student)
    assert score == 0.0


def test_empty_strings():
    """Verify that empty or null strings are handled gracefully with a 0.0 score."""
    grader = TFIDFGrader()
    assert grader.grade_answer("texte", "") == 0.0
    assert grader.grade_answer("", "texte") == 0.0
    assert grader.grade_answer(None, "texte") == 0.0


def test_batch_grading():
    """Verify that the batch grader successfully applies scores to a DataFrame."""
    grader = TFIDFGrader()
    data = [
        {
            "ref": "chat pomme cerise",
            "stud": "chat pomme cerise",
        },  # Exact match -> 20.0
        {"ref": "chat pomme cerise", "stud": "voiture chien loup"},  # Disjoint -> 0.0
    ]
    df = pd.DataFrame(data)

    df_scored = grader.grade_batch(df, ref_col="ref", student_col="stud")

    assert "score_out_of_20" in df_scored.columns
    assert df_scored.iloc[0]["score_out_of_20"] == 20.0
    assert df_scored.iloc[1]["score_out_of_20"] == 0.0
