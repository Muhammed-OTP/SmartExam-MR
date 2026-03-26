import pandas as pd
import numpy as np
import os


def generate_synthetic_data(num_records=150):
    np.random.seed(42)

    courses = ["NLP", "Computer Vision", "Machine Learning", "Project Management"]
    question_types = ["definition", "explanation", "comparison"]

    # Base data
    data = []
    for i in range(1, num_records + 1):
        course = np.random.choice(courses)
        q_type = np.random.choice(question_types)
        difficulty = np.random.randint(1, 6)  # 1 to 5
        score = np.random.randint(0, 11)  # 0 to 10

        # Simulating some text
        ref_ans = (
            f"This is the reference answer for a {q_type} in {course}."
            * np.random.randint(1, 4)
        )
        stu_ans = f"This is the student answer regarding {course}." * np.random.randint(
            1, 4
        )

        # Inject formatting anomalies
        if np.random.rand() > 0.8:
            stu_ans = "   " + stu_ans.upper() + "   "
        if np.random.rand() > 0.8:
            ref_ans = ref_ans.lower() + "   \n "

        data.append(
            {
                "student_id": f"STU{i:03d}",
                "course": course,
                "question": f"Explain the main concept of {course}?",
                "reference_answer": ref_ans,
                "student_answer": stu_ans,
                "question_type": q_type,
                "difficulty": difficulty,
                "score": score,
            }
        )

    df = pd.DataFrame(data)

    # Inject missing values
    missing_idx = np.random.choice(df.index, size=int(num_records * 0.1), replace=False)
    df.loc[missing_idx, "student_answer"] = np.nan

    # Inject duplicates
    duplicates = df.sample(n=int(num_records * 0.05), random_state=42)
    df = pd.concat([df, duplicates], ignore_index=True)

    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save
    out_dir = "data/raw"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "student_exam_answers.csv")
    df.to_csv(out_path, index=False)
    print(f"Generated synthetic data: {out_path} with {len(df)} records.")


if __name__ == "__main__":
    generate_synthetic_data()
