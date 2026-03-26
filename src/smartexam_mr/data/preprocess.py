import pandas as pd
import string
import re


def handle_missing_and_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Removes duplicates and fills missing text answers with empty strings."""
    df = df.drop_duplicates().copy()

    # Fill missing answers
    if "student_answer" in df.columns:
        df["student_answer"] = df["student_answer"].fillna("")
    if "reference_answer" in df.columns:
        df["reference_answer"] = df["reference_answer"].fillna("")

    return df


def normalize_text(text: str) -> str:
    """Lowercases, strips leading/trailing space, collapses internal space."""
    if not isinstance(text, str):
        return ""

    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Collapse multiple whitespaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Applies basic cleaning and text normalization."""
    df = handle_missing_and_duplicates(df)

    if "student_answer" in df.columns:
        df["student_answer_clean"] = df["student_answer"].apply(normalize_text)
    if "reference_answer" in df.columns:
        df["reference_answer_clean"] = df["reference_answer"].apply(normalize_text)

    return df
