# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

### Fixed
- Feature typing correction: Moved `difficulty` from numeric to categorical features in pipeline builder.
- Import paths correction: Fixed internal module import statements in `build_pipeline.py`.
- Robustness: Added safe NaN handling `str(ref or "")` for text feature engineering functions.

### Added
- Phase 2: Synthetic data generator script `scripts/generate_synthetic_data.py` producing robust MVP data.
- Phase 2: Core modules for loading (`load_data.py`), preprocessing (`preprocess.py`), and feature engineering (`feature_engineering.py`).
- Phase 2: Final numerical and categorical pipelining via Scikit-Learn `ColumnTransformer` (`build_pipeline.py`).
- Unit tests validating duplicate removal, missing value handling, and engineered features in `test_preprocess.py`.

### Changed
- Checked off Phase 2 in the project Roadmap.
