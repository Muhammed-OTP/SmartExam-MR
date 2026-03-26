# Project Brief: SmartExam-MR

## Context
In Mauritanian universities, large class sizes and limited grading resources present a significant challenge for ongoing student assessment. Manual evaluation of open-ended and short-answer questions is labor-intensive and error-prone.

## Objective
The SmartExam-MR project (Master 1 level) aims to create a proof-of-concept AI assessment platform. By using NLP techniques, the system will semi-automate the grading of short text answers.

## Key Features
- **Data Ingestion**: Import student answers via CSV/JSON.
- **Preprocessing Pipeline**: Clean text, handle missing values, and extract logical features.
- **Intelligent Grading**: Use lightweight similarity measures (TF-IDF, sentence-transformers) to calculate a grade based on a reference answer.
- **Interactive Dashboard**: A Streamlit UI to visualize data, test the pipeline interactively, and display results.

## Constraints
- **Resource Limits**: Must run locally without heavy GPU dependence.
- **No Paid APIs**: Rely strictly on open-source libraries (scikit-learn, HuggingFace).
- **Simplicity**: No complex microservices, Dockerization, or dedicated databases for the MVP.
