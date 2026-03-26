import pandas as pd
import numpy as np
from src.smartexam_mr.data.preprocess import preprocess_data, normalize_text
from src.smartexam_mr.data.feature_engineering import (
    engineer_features,
    compute_word_overlap_ratio,
)


def test_missing_values_handled():
    df = pd.DataFrame(
        {"student_answer": ["Answer 1", np.nan], "reference_answer": [np.nan, "Ref 2"]}
    )

    df_clean = preprocess_data(df)

    assert df_clean["student_answer"].isnull().sum() == 0
    assert df_clean["reference_answer"].isnull().sum() == 0
    assert df_clean.iloc[1]["student_answer"] == ""
    assert df_clean.iloc[0]["reference_answer"] == ""


def test_duplicates_removed():
    df = pd.DataFrame(
        {
            "student_answer": ["Ans 1", "Ans 1", "Ans 2"],
            "reference_answer": ["Ref 1", "Ref 1", "Ref 2"],
        }
    )
    df_clean = preprocess_data(df)
    assert len(df_clean) == 2


def test_text_normalization():
    text = "  HELLO, world!  This is    a Test.  "
    clean_text = normalize_text(text)
    assert clean_text == "hello world this is a test"


def test_feature_engineering_created():
    df = pd.DataFrame(
        {
            "question": ["Q1?"],
            "student_answer": ["student ans"],
            "reference_answer": ["reference ans"],
        }
    )
    df_clean = preprocess_data(df)
    df_features = engineer_features(df_clean)

    assert "question_length" in df_features.columns
    assert "student_answer_length" in df_features.columns
    assert "reference_answer_length" in df_features.columns
    assert "answer_missing" in df_features.columns
    assert "word_overlap_ratio" in df_features.columns


def test_word_overlap_ratio():
    ref = "this is a test answer"
    stu1 = "this is a test answer"
    stu2 = "completely different string"
    stu3 = "this is something else"

    assert compute_word_overlap_ratio(ref, stu1) == 1.0
    assert compute_word_overlap_ratio(ref, stu2) == 0.0
    overlap_partial = compute_word_overlap_ratio(ref, stu3)
    assert 0.0 < overlap_partial < 1.0
