import os
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Add the project's src directory to sys path if running directly
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from smartexam_mr.data.load_data import load_raw_data, save_processed_data
from smartexam_mr.data.preprocess import preprocess_data
from smartexam_mr.data.feature_engineering import engineer_features


def create_sklearn_pipeline() -> ColumnTransformer:
    """Creates the final numerical/categorical transformation stage."""
    numeric_features = [
        "score",
        "question_length",
        "reference_answer_length",
        "student_answer_length",
        "word_overlap_ratio",
    ]
    categorical_features = ["course", "question_type", "difficulty"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ],
        remainder="drop",
    )
    return preprocessor


def build_and_save_pipeline(
    input_path: str, output_data_path: str, output_pipeline_path: str
):
    """Executes the full pipeline and saves the outputs."""
    print(f"Loading raw data from {input_path}")
    df = load_raw_data(input_path)

    print("Applying pandas preprocessing...")
    df_clean = preprocess_data(df)

    print("Applying feature engineering...")
    df_features = engineer_features(df_clean)

    # Save the cleaned and enriched CSV
    os.makedirs(os.path.dirname(output_data_path), exist_ok=True)
    save_processed_data(df_features, output_data_path)
    print(f"Saved processed data to {output_data_path}")

    print("Fitting sklearn ColumnTransformer...")
    preprocessor = create_sklearn_pipeline()

    # Fit the pipeline on the enriched dataframe
    X_transformed = preprocessor.fit_transform(df_features)

    # Save pipeline
    os.makedirs(os.path.dirname(output_pipeline_path), exist_ok=True)
    joblib.dump(preprocessor, output_pipeline_path)
    print(f"Saved sklearn preprocessing pipeline to {output_pipeline_path}")


if __name__ == "__main__":
    build_and_save_pipeline(
        input_path="data/raw/student_exam_answers.csv",
        output_data_path="data/processed/student_exam_answers_processed.csv",
        output_pipeline_path="data/processed/preprocessing_pipeline.joblib",
    )
