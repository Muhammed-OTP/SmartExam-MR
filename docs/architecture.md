# Architecture

SmartExam-MR employs a layered architecture suited for the Mauritanian university context logic while decoupled from the UI.

## Layers

1. **Data Layer**
   - Resides in `data/raw/` and `data/processed/`.
   - Managed as flat files (CSV, JSON).

2. **Preprocessing Layer** (`src/smartexam_mr/data/`)
   - Uses `scikit-learn` Pipelines and `ColumnTransformer`.
   - Normalizes text, extracts features, and handles dataset irregularities.
   - Saves fitted pipelines to disk using `joblib`.

3. **Grading/Model Layer** (`src/smartexam_mr/models/`)
   - Uses TF-IDF vectorization and cosine similarity as a fast, reliable baseline for short-answer grading.
   - Computes similarity metrics securely (handles missing data, bounds checks).
   - Maps similarity to a grading scale (e.g., 0 to max_score) and provides interpretable feedback.
   - *Future Work*: Encapsulates advanced embedding logic (like `sentence-transformers`) as an optional fallback or enhancement.

4. **UI Layer** (`app/`)
   - A robust Streamlit dashboard.
   - Connects to the Preprocessing and Grading layers to run inferences interactively on user input.
## Data Pipeline (Phase 2)
1. **Data Ingestion**: Standard file I/O loading the raw dataset.
2. **Preprocessing**: Functional programming strategy that strictly drops duplicates and lowercases missing/excessive textual noise.
3. **Feature Engineering**: Derives `question_length`, `reference_answer_length`, `student_answer_length`, `answer_missing` boolean flag, and calculates an initial `word_overlap_ratio`.
4. **Sklearn Integration**: Final transformation routes numerical variables (lengths, score) through a `StandardScaler`, and categorical strings (`course`, `question_type`) through a `OneHotEncoder` via `ColumnTransformer`. The finalized pipeline is serialized using `joblib`.
