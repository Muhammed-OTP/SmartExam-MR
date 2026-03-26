# Architecture

SmartExam-MR employs a layered architecture suited for the Mauritanian university context logic while decoupled from the UI.

## Data Pipeline (Phase 2)
1. **Data Ingestion**: Standard file I/O loading the raw dataset.
2. **Preprocessing**: Functional programming strategy that strictly drops duplicates and lowercases missing/excessive textual noise.
3. **Feature Engineering**: Derives `question_length`, `reference_answer_length`, `student_answer_length`, `answer_missing` boolean flag, and calculates an initial `word_overlap_ratio`.
4. **Sklearn Integration**: Final transformation routes numerical variables (lengths, score) through a `StandardScaler`, and categorical strings (`course`, `question_type`) through a `OneHotEncoder` via `ColumnTransformer`. The finalized pipeline is serialized using `joblib`.
