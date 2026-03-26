import pytest
import pandas as pd
from smartexam_mr.pipeline.build_pipeline import (
    generate_synthetic_data,
    clean_text,
    build_preprocessing_pipeline,
)


def test_synthetic_data_schema():
    """Verify the generated DataFrame contains the expected mock data and columns."""
    df = generate_synthetic_data()
    assert isinstance(df, pd.DataFrame)

    expected_columns = ["student_id", "question", "reference_answer", "student_answer"]
    for col in expected_columns:
        assert col in df.columns, f"Missing expected column: {col}"

    assert len(df) > 0, "DataFrame should not be empty"


def test_clean_text():
    """Verify the text cleaner properly lowercases, strips punctuation, and trims spaces."""
    raw_text = "L'apprentissage supervisé, C'EST super! 100%"
    # 'l', 'apprentissage', 'supervisé', 'c', 'est', 'super'
    expected_cleaned = "l apprentissage supervisé c est super"
    assert clean_text(raw_text) == expected_cleaned

    # Handle None or non-string inputs gracefully
    assert clean_text(None) == ""


def test_preprocessing_pipeline():
    """Verify the scikit-learn pipeline correctly transforms the input DataFrame."""
    raw_df = generate_synthetic_data()
    pipeline = build_preprocessing_pipeline()

    processed_df = pipeline.fit_transform(raw_df)

    # Pipeline should have added cleaned versions of the text columns
    assert "student_answer_cleaned" in processed_df.columns
    assert "reference_answer_cleaned" in processed_df.columns

    # Verify a transformation happened
    sample_text = processed_df.iloc[0]["student_answer_cleaned"]
    assert sample_text == sample_text.lower()
    assert "?" not in sample_text
