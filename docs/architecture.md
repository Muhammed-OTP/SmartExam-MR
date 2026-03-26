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
   - Encapsulates embedding logic (TF-IDF or sentence-transformers).
   - Computes similarity metrics.
   - Maps similarity to a discrete or continuous grading scale.

4. **UI Layer** (`app/`)
   - A robust Streamlit dashboard.
   - Connects to the Preprocessing and Grading layers to run inferences interactively on user input.
