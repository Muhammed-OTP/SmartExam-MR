import pytest
from smartexam_mr.models.grading import (
    compute_tfidf_similarity,
    map_similarity_to_grade,
    grade_short_answer
)

def test_identical_answers():
    ref = "Machine learning is a subset of artificial intelligence."
    student = "Machine learning is a subset of artificial intelligence."
    result = grade_short_answer(ref, student)
    
    assert result["similarity_score"] > 0.99
    assert result["suggested_score"] == 10.0
    assert "High semantic overlap" in result["feedback"]

def test_very_different_answers():
    ref = "The capital of France is Paris."
    student = "Photosynthesis is the process by which plants make food."
    result = grade_short_answer(ref, student)
    
    assert result["similarity_score"] < 0.2
    assert "Low overlap" in result["feedback"]

def test_empty_student_answer():
    ref = "This is a reference answer."
    result = grade_short_answer(ref, "")
    
    assert result["similarity_score"] == 0.0
    assert result["suggested_score"] == 0.0
    assert "Low overlap" in result["feedback"]

def test_empty_reference():
    result = grade_short_answer("", "student wrote this")
    assert result["similarity_score"] == 0.0

def test_none_answers():
    result = grade_short_answer(None, "student wrote this")
    assert result["similarity_score"] == 0.0

def test_punctuation_only_student_answer():
    result = grade_short_answer("The Earth is round.", ".,?!")
    assert result["similarity_score"] == 0.0

def test_moderately_similar_answers():
    ref = "Artificial Intelligence is the simulation of human intelligence by machines."
    student = "AI is the simulation of human intelligence."
    result = grade_short_answer(ref, student)
    
    # They share words but not perfectly
    assert 0.4 <= result["similarity_score"] < 1.0
    assert result["suggested_score"] > 4.0
    assert "overlap" in result["feedback"]

def test_bounds():
    # Test that mapping strictly enforces bounds
    assert map_similarity_to_grade(1.5, 10.0) == 10.0
    assert map_similarity_to_grade(-0.5, 10.0) == 0.0
    assert map_similarity_to_grade(0.5, 10.0) == 5.0
