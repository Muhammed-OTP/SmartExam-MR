# SmartExam-MR
**Plateforme Intelligente d’Évaluation Académique Assistée par IA**

## Description
SmartExam-MR is an intelligent academic assessment platform adapted to the Mauritanian university context. Built as a Master 1 AI project, this MVP aims to streamline the grading process for short answers by demonstrating automated data ingestion, advanced preprocessing, and a baseline intelligent grading system.

## Problem Context
In Mauritania, university class sizes are growing and grading handwritten or short-text exams manually is time-consuming. SmartExam-MR tackles this by offering a local, lightweight, and efficient AI-based assessment proof-of-concept.

## MVP Features
1. **Dataset Ingestion**: Handling student exam answers iteratively.
2. **Preprocessing Pipeline**: Cleaning textual data and engineering relevant features.
3. **Intelligent Grading Baseline**: Using NLP metrics (TF-IDF/sentence-transformers) to calculate similarity scores between student and reference answers.
4. **Streamlit Showcase**: A professional, dynamic demo interface.

## Project Structure
```text
SmartExam-MR/
├── app/                  # Streamlit application
├── data/                 # Raw and processed datasets
├── docs/                 # Project documentation
├── notebooks/            # Jupyter notebooks for exploration
├── src/smartexam_mr/     # Core library package
└── tests/                # Unit tests
```

## Local Setup
1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Unix: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## How to Run Streamlit
Provide a command to run the Streamlit demo once developed:
```bash
streamlit run app/streamlit_app.py
```

## Team
- **Developer**: Muhammad Salem (Master 1 AI)

## Roadmap
- [x] Phase 1: Repository architecture and initial scaffold
- [ ] Phase 2: Synthetic dataset generation and preprocessing pipeline
- [ ] Phase 3: Intelligent grading baseline
- [ ] Phase 4: Streamlit MVP implementation

## Limitations
This MVP is an academic prototype and does not leverage large parameter LLMs or paid external APIs in order to ensure local execution viability.
