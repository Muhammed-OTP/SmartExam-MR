import re
import pandas as pd
from typing import Any  # Changed to Any just in case, but let's check if we actually need typing. 
# Actually, the file used List in type hints but let's see.
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


def generate_synthetic_data() -> pd.DataFrame:
    """
    Generates a synthetic pandas DataFrame of student exam answers simulating a Master 1 CS exam.
    The text is strictly in French, suited for the Mauritanian university context.
    """
    data = [
        {
            "student_id": "S001",
            "question": "Qu'est-ce qu'un réseau de neurones ?",
            "reference_answer": "Un modèle de calcul inspiré du cerveau humain, composé de couches de neurones artificiels.",
            "student_answer": "C'est un modèle algorithmique inspiré par le fonctionnement du cerveau biologique.",
        },
        {
            "student_id": "S002",
            "question": "Qu'est-ce qu'un réseau de neurones ?",
            "reference_answer": "Un modèle de calcul inspiré du cerveau humain, composé de couches de neurones artificiels.",
            "student_answer": "C'est une base de données relationnelle utilisant des tables.",
        },
        {
            "student_id": "S003",
            "question": "Quelle est la différence entre l'apprentissage supervisé et non supervisé ?",
            "reference_answer": "L'apprentissage supervisé utilise des données étiquetées, tandis que le non supervisé trouve des motifs dans des données non étiquetées.",
            "student_answer": "Dans le supervisé, on donne les réponses attendues pour entraîner le modèle. Dans le non supervisé, le modèle se débrouille tout seul avec des données brut.",
        },
    ]
    return pd.DataFrame(data)


def clean_text(text: str) -> str:
    """
    Cleans text by lowercasing, removing digits, and stripping out punctuation.

    Args:
        text (str): The raw text to clean.

    Returns:
        str: The cleaned text string.
    """
    if not isinstance(text, str):
        return ""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation using regex, leaving only letters and spaces
    text = re.sub(r"[^\w\s]", " ", text)
    # Remove digits
    text = re.sub(r"\d+", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _clean_series(X: pd.DataFrame) -> pd.DataFrame:
    """
    Helper function for the FunctionTransformer to clean multiple DataFrame columns.
    """
    X_clean = X.copy()
    columns_to_clean = ["student_answer", "reference_answer"]

    for col in columns_to_clean:
        if col in X_clean.columns:
            X_clean[col + "_cleaned"] = X_clean[col].apply(clean_text)

    return X_clean


def build_preprocessing_pipeline() -> Pipeline:
    """
    Builds and returns a scikit-learn Pipeline that encapsulates all text preprocessing.
    """
    return Pipeline(
        steps=[
            ("text_cleaner", FunctionTransformer(_clean_series, validate=False)),
        ]
    )


if __name__ == "__main__":
    import os

    print("Generating synthetic data...")
    raw_df = generate_synthetic_data()

    print("Building preprocessing pipeline...")
    pipeline = build_preprocessing_pipeline()

    print("Executing pipeline...")
    processed_df = pipeline.fit_transform(raw_df)

    # Assure directories exist
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Save data
    print("Saving data to disk...")
    raw_df.to_csv("data/raw/synthetic_data.csv", index=False)
    processed_df.to_csv("data/processed/cleaned_data.csv", index=False)

    print("Pipeline compilation and execution completed successfully!")
