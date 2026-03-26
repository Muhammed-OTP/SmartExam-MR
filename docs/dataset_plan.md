# Dataset Plan

## Schema
- `student_id`: Unique identifier for the student.
- `course`: The academic subject (e.g., NLP, Computer Vision, Machine Learning, Project Management).
- `question`: The simulated exam question.
- `reference_answer`: The correct or expected answer.
- `student_answer`: The actual text submitted by the student.
- `question_type`: Analytical format (definition, explanation, comparison, etc.).
- `difficulty`: Rated difficulty of the question on a scale of 1 to 5.
- `score`: The evaluated grade, scoring from 0 to 10.

## Simulated Anomalies (MVP)
The `data/raw/student_exam_answers.csv` dataset explicitly models real-world noise:
* **Missing Values**: Simulates blank tests or unsubmitted segments.
* **Duplicate Rows**: Duplicated telemetry or pipeline errors.
* **Inconsistent Formatting**: Simulates mobile input with extra whitespaces, varying punctuation patterns, and extreme casing.
