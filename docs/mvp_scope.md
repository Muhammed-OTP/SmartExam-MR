# MVP Scope

## In-Scope
1. **Synthetic Dataset**: A small, imperfect dataset containing mock reference answers and student answers for typical CS courses (NLP, ML, CV).
2. **Preprocessing Pipeline**: 
    - Handling missing values and duplicates.
    - Basic text normalization (lowercasing, punctuation removal).
    - Feature engineering (length ratios, word overlap).
3. **Similarity Grading Baseline**:
    - **TF-IDF + Cosine Similarity**: Fast, lightweight baseline (Implemented).
    - **Sentence-Transformers**: A denser vector mapping baseline (Planned future work as fallback/enhancement).
4. **Streamlit UI**:
    - Dataset exploration page.
    - Live grading interface (Reference vs. Student answer).

## Out-of-Scope
- Complex generative grading (e.g., Llama 3/GPT-4 feedback generation).
- User Authentication (Login/Roles for teachers and students).
- Relational Database integration (PostgreSQL, MySQL).
- REST/GraphQL API layer (FastAPI/Django).
- Containerization (Docker) and Cloud orchestrations (Kubernetes).
