import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_tfidf_similarity(reference_answer: str, student_answer: str) -> float:
    """
    Computes the cosine similarity between a reference answer and a student answer using TF-IDF.
    Returns a score between 0.0 and 1.0.
    """
    if not isinstance(reference_answer, str) or not isinstance(student_answer, str):
        return 0.0
        
    ref = reference_answer.strip()
    student = student_answer.strip()
    
    if not ref or not student:
        return 0.0
        
    vectorizer = TfidfVectorizer()
    try:
        # Ignore warnings about empty vocabulary which we catch right after
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            tfidf_matrix = vectorizer.fit_transform([ref, student])
            
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return max(0.0, min(1.0, float(similarity)))
    except ValueError:
        # This can happen if the text contains no valid words (e.g., only stop words or punctuation)
        # resulting in an empty vocabulary.
        return 0.0

def map_similarity_to_grade(similarity: float, max_score: float = 10.0) -> float:
    """
    Maps a similarity score [0, 1] linearly to a suggested grade [0, max_score].
    """
    similarity = max(0.0, min(1.0, similarity))
    return round(similarity * max_score, 2)

def grade_short_answer(reference_answer: str, student_answer: str, max_score: float = 10.0) -> dict:
    """
    Computes similarity, calculates a suggested score, and provides a short explanation.
    
    Args:
        reference_answer: The expected answer text.
        student_answer: The answer provided by the student.
        max_score: Maximum possible score for this question (default 10.0).
        
    Returns:
        dict: containing 'similarity_score', 'suggested_score', and 'feedback'
    """
    similarity = compute_tfidf_similarity(reference_answer, student_answer)
    suggested_score = map_similarity_to_grade(similarity, max_score)
    
    if similarity >= 0.8:
        feedback = "High semantic overlap with the reference answer."
    elif similarity >= 0.4:
        feedback = "Moderate overlap; partial correctness detected."
    else:
        feedback = "Low overlap; answer may be incomplete or incorrect."
        
    return {
        "similarity_score": similarity,
        "suggested_score": suggested_score,
        "feedback": feedback
    }
