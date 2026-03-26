import os

files = [
    "src/smartexam_mr/__init__.py",
    "src/smartexam_mr/config.py",
    "src/smartexam_mr/data/__init__.py",
    "src/smartexam_mr/data/load_data.py",
    "src/smartexam_mr/data/preprocess.py",
    "src/smartexam_mr/data/feature_engineering.py",
    "src/smartexam_mr/models/__init__.py",
    "src/smartexam_mr/models/grading.py",
    "src/smartexam_mr/pipeline/__init__.py",
    "src/smartexam_mr/pipeline/build_pipeline.py",
    "src/smartexam_mr/utils/__init__.py",
    "src/smartexam_mr/utils/text_utils.py",
    "src/smartexam_mr/visualization/__init__.py",
    "src/smartexam_mr/visualization/charts.py",
    "app/streamlit_app.py",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "tests/__init__.py",
    "tests/test_preprocess.py",
    "tests/test_grading.py",
]

notebook_content = (
    '{\n "cells": [],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 5\n}'
)

for f in files:
    os.makedirs(os.path.dirname(f), exist_ok=True)
    with open(f, "w", encoding="utf-8") as file:
        file.write(
            '"""Placeholder"""\n' if f.endswith(".py") and "__init__" not in f else ""
        )

os.makedirs("notebooks", exist_ok=True)
with open(
    "notebooks/01_preprocessing_and_grading_demo.ipynb", "w", encoding="utf-8"
) as f:
    f.write(notebook_content)

print("Scaffolding complete.")
