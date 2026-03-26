# Dataset Plan

## Origin
For the MVP, we will generate a realistic synthetic dataset mimicking short-answer exam submissions in computer science courses at a Mauritanian university.

## Structure
The CSV dataset will include columns such as:
- `student_id`: Unique identifier
- `course`: E.g., NLP, Machine Learning, Computer Vision
- `question`: The text of the exam question
- `reference_answer`: The expected correct answer
- `student_answer`: The actual submitted answer
- `difficulty`: Categorical (Easy, Medium, Hard)
- `score`: Placeholder for the actual grade out of 10 or 100

## Intentional Imperfections
To demonstrate the preprocessing pipeline, we will incorporate:
- **Missing Values**: Empty rows or `NaN` student answers.
- **Duplicates**: Accidental double submissions.
- **Inconsistencies**: Variations in casing, punctuation, and leading/trailing spaces.

## Future Expansion
Post-MVP, this could be expanded to include real anonymized student answers, or integrated with an OCR pipeline for handwritten exams.
