import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFGrader:
    """
    A lightweight, local baseline grading system for SmartExam-MR.
    Uses TF-IDF vectorization and cosine similarity to compare student
    answers against a reference answer, scaling the result to a 0-20 point system.
    """

    def __init__(self):
        # Initialize vectorizer. We don't fit it globally, but rather pair-wise for simplicity
        # or corpus-wise if preferred. For baseline MVP, pair-wise is robust enough.
        pass

    def grade_answer(self, reference_answer: str, student_answer: str) -> float:
        """
        Grades a single student answer against a reference answer.

        Args:
            reference_answer (str): The correct/reference answer.
            student_answer (str): The student's submitted answer.

        Returns:
            float: A score between 0.0 and 20.0, rounded to 2 decimal places.
        """
        # Handle empty/null answers
        if (
            not student_answer
            or not isinstance(student_answer, str)
            or not student_answer.strip()
        ):
            return 0.0
        if (
            not reference_answer
            or not isinstance(reference_answer, str)
            or not reference_answer.strip()
        ):
            return 0.0

        corpus = [reference_answer, student_answer]
        vectorizer = TfidfVectorizer()

        try:
            tfidf_matrix = vectorizer.fit_transform(corpus)
        except ValueError:
            # Raised if vocab is completely empty (e.g. only stop words if english, or single letter texts)
            return 0.0

        # tfidf_matrix[0] is reference, tfidf_matrix[1] is student
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        # Scale to Mauritanian 0-20 point system
        score = similarity * 20.0
        return round(score, 2)

    def grade_batch(
        self,
        df: pd.DataFrame,
        ref_col: str = "reference_answer_cleaned",
        student_col: str = "student_answer_cleaned",
    ) -> pd.DataFrame:
        """
        Convenience method to grade a batch of answers represented in a DataFrame.

        Args:
            df (pd.DataFrame): Dataset containing the answers.
            ref_col (str): Column name containing the cleaned reference answers.
            student_col (str): Column name containing the cleaned student answers.

        Returns:
            pd.DataFrame: A copy of the DataFrame with an appended 'score_out_of_20' column.
        """
        df_graded = df.copy()

        # Apply the grade_answer function to every row in the dataframe
        df_graded["score_out_of_20"] = df_graded.apply(
            lambda row: self.grade_answer(
                str(row[ref_col]) if pd.notna(row[ref_col]) else "",
                str(row[student_col]) if pd.notna(row[student_col]) else "",
            ),
            axis=1,
        )

        return df_graded


if __name__ == "__main__":
    grader = TFIDFGrader()
    print("Testing TFIDFGrader locally...")
    ref = "un modèle de calcul inspiré du cerveau humain"
    ans1 = "un modèle algorithmique inspiré par le fonctionnement du cerveau"
    ans2 = "une base de données relationnelle utilisant des tables"

    print(f"Reference: '{ref}'")
    print(
        f"Answer 1 (Correct): '{ans1}' -> Score: {grader.grade_answer(ref, ans1)} / 20.0"
    )
    print(
        f"Answer 2 (Incorrect): '{ans2}' -> Score: {grader.grade_answer(ref, ans2)} / 20.0"
    )
