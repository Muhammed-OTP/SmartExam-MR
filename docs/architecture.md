# System Architecture

The MVP follows a layered, decoupled design while keeping deployment simple.

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
