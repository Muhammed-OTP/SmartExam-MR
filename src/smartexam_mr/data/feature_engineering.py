import pandas as pd

def compute_word_overlap_ratio(ref: str, stu: str) -> float:
    """Computes basic word overlap ratio between reference and student answer."""
    ref = str(ref or "")
    stu = str(stu or "")
    
    ref_words = set(ref.split())
    stu_words = set(stu.split())
    
    if len(ref_words) == 0:
        return 0.0
        
    overlap = ref_words.intersection(stu_words)
    return len(overlap) / len(ref_words)

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Engineers lengths, missing flag, and word overlap features."""
    df = df.copy()
    
    # Missing flag
    df['answer_missing'] = (df['student_answer_clean'] == "").astype(int)
    
    # Lengths
    if 'question' in df.columns:
        df['question_length'] = df['question'].astype(str).str.len()
    
    df['reference_answer_length'] = df['reference_answer_clean'].str.len()
    df['student_answer_length'] = df['student_answer_clean'].str.len()
    
    # Word overlap
    df['word_overlap_ratio'] = df.apply(
        lambda row: compute_word_overlap_ratio(row['reference_answer_clean'], row['student_answer_clean']),
        axis=1
    )
    
    return df
