# Agent Instructions for SmartExam-MR

This document provides explicit guidelines for any AI coding agents assisting with the SmartExam-MR project.

## Project Purpose
SmartExam-MR is an academic project at the Master 1 level. We are building a lightweight AI assessment platform.

## Architecture Rules
1. **No External Paid APIs**: The project relies on local compute and lightweight open-source models (TF-IDF, sentence-transformers).
2. **Frameworks**: Use Streamlit for UI, scikit-learn for models/pipelines, pandas for data. Do not introduce heavy backends like FastAPI or Docker unless explicitly requested.
3. **Layered Design**: The core logic (`src/smartexam_mr/`) must be cleanly decoupled from the UI (`app/`).

## Coding Standards
1. Use **Python 3.11+**.
2. Include type hints for function signatures.
3. Include docstrings for all classes and vital functions.
4. Favor readability and functional predictability over premature optimization.

## Branch & Testing Rules
1. Main branch acts as the production baseline.
2. For any feature, write lightweight `pytest` unit tests (especially for data processing and grading logic).

## What NOT to Change
- Do not modify the underlying project architecture or introduce massive dependency shifts without explicit user approval.
- Do not discard the Mauritanian project context.

## Commit Discipline
Use conventional commits (e.g., `feat:`, `chore:`, `fix:`, `docs:`). Make small, focused pull requests if working collaboratively.

## Definition of Done
A feature is complete when it includes:
- Clean code passing `ruff` and `black`.
- Unit tests validating core logic.
- An updated Streamlit visualization (if applicable).
