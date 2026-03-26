# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

### Fixed
- Feature typing correction: Moved `difficulty` from numeric to categorical features in pipeline builder.
- Import paths correction: Fixed internal module import statements in `build_pipeline.py`.
- Robustness: Added safe NaN handling `str(ref or "")` for text feature engineering functions.

### Added
- Baseline intelligent grading for short answers (`smartexam_mr.models.grading`) using TF-IDF and cosine similarity.
- Initial project structure scaffold.
- Root documentation files (`README.md`, `AGENTS.md`, `CHANGELOG.md`).
- Git ignoring and dependency management (`.gitignore`, `requirements.txt`, `pyproject.toml`).
- Detailed markdown documentation for architecture, scope, workflow, and dataset.
- GitHub workflow for CI and issue/PR templates.
- Python package layout in `src/smartexam_mr/`.
- Phase 2: Synthetic data generator script `scripts/generate_synthetic_data.py` producing robust MVP data.
- Phase 2: Core modules for loading (`load_data.py`), preprocessing (`preprocess.py`), and feature engineering (`feature_engineering.py`).
- Phase 2: Final numerical and categorical pipelining via Scikit-Learn `ColumnTransformer` (`build_pipeline.py`).
- Unit tests validating duplicate removal, missing value handling, and engineered features in `test_preprocess.py`.

### Changed
- Checked off Phase 2 in the project Roadmap.
