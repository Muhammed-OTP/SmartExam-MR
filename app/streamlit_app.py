import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from smartexam_mr.models.grading import TFIDFGrader
from smartexam_mr.pipeline.build_pipeline import (
    generate_synthetic_data,
    build_preprocessing_pipeline,
)

# 1. Page Configuration & Aesthetic Setup
st.set_page_config(
    page_title="SmartExam-MR | AI Assessment",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Custom CSS for "Premium" Rich Aesthetics (Glassmorphism & Gradients)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }

    .stApp {
        background: transparent;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: transform 0.2s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
    }

    h1, h2, h3 {
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    .sidebar .sidebar-content {
        background: rgba(15, 23, 42, 0.95);
    }
    </style>
    """,
    unsafe_allow_stdio=True,
    unsafe_allow_html=True,
)


# 3. Application Brain
@st.cache_resource
def load_grader():
    return TFIDFGrader()


@st.cache_data
def get_data():
    processed_path = "data/processed/cleaned_data.csv"

    if os.path.exists(processed_path):
        return pd.read_csv(processed_path)

    # Fallback to generating on the fly if files missing
    df = generate_synthetic_data()
    pipeline = build_preprocessing_pipeline()
    return pipeline.fit_transform(df)


grader = load_grader()
data = get_data()

# 4. Sidebar Content
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=80)
    st.title("SmartExam-MR")
    st.info(
        "**MVP Académique (Master 1 AI)** \n\n Plateforme d’évaluation automatique adaptée au contexte Mauritanien."
    )

    st.divider()
    st.subheader("⚙️ Paramètres Système")
    st.write("**Modèle**: TF-IDF + Cosine Similarity")
    st.write("**Langue**: Français")
    st.write("**Échelle**: 0 - 20")

    st.divider()
    st.caption("Développé par Muhammad Salem")

# 5. Dashboard Layout
st.title("Tableau de Bord d'Évaluation")

tab1, tab2, tab3 = st.tabs(
    ["🎯 Grading Sandbox", "📊 Data Insights", "📜 Documentation"]
)

# --- Tab 1: Sandbox ---
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Bac à sable d'Évaluation Interactive")
    st.write(
        "Testez le moteur de notation en saisissant une réponse de référence et une réponse étudiant."
    )

    col1, col2 = st.columns(2)
    with col1:
        ref_input = st.text_area(
            "Réponse de Référence",
            placeholder="Saisissez la réponse correcte attendue...",
            value="Un réseau de neurones est un modèle de calcul inspiré du cerveau humain.",
        )
    with col2:
        student_input = st.text_area(
            "Réponse de l'Étudiant",
            placeholder="Saisissez ce que l'étudiant a écrit...",
        )

    if st.button("Calculer la Note"):
        if ref_input and student_input:
            score = grader.grade_answer(ref_input, student_input)

            # Dynamic Score Display
            st.divider()
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                st.metric(label="Note Finale", value=f"{score} / 20.0")
                if score >= 10:
                    st.success("Admis (Mention)")
                else:
                    st.warning("Ajourné")

                # Progress bar visualization
                st.progress(score / 20.0)
        else:
            st.error("Veuillez remplir les deux champs.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Tab 2: Data Insights ---
with tab2:
    st.subheader("Analyse de Données Mock (Synthétique)")

    # Grade everything in the mock data
    scored_data = grader.grade_batch(data)

    # Summary Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Nb. Examens", len(scored_data))
    m2.metric("Note Moyenne", round(scored_data["score_out_of_20"].mean(), 2))
    m3.metric(
        "Taux de Réussite",
        f"{round((scored_data['score_out_of_20'] >= 10).mean() * 100, 1)}%",
    )

    col_chart, col_table = st.columns([1, 1])

    with col_chart:
        st.write("**Distribution des Notes**")
        fig, ax = plt.subplots(figsize=(10, 6))
        # Style the plot for Dark Mode
        plt.style.use("dark_background")
        ax.hist(
            scored_data["score_out_of_20"],
            bins=10,
            color="#3b82f6",
            edgecolor="white",
            alpha=0.7,
        )
        ax.set_xlabel("Note / 20")
        ax.set_ylabel("Fréquence")
        st.pyplot(fig)

    with col_table:
        st.write("**Aperçu des Données Scores**")
        st.dataframe(
            scored_data[["question", "score_out_of_20"]].style.highlight_max(
                axis=0, color="#1e3a8a"
            )
        )

        # Download button
        csv = scored_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Télécharger les résultats (CSV)",
            data=csv,
            file_name="resultats_scores.csv",
            mime="text/csv",
        )

# --- Tab 3: Documentation ---
with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("""
    ### Comment ça marche ?
    
    Le système utilise une approche de **Traitement du Langage Naturel (NLP)** basée sur :
    1. **Preprocessing (Phase 2)**: Nettoyage du texte (suppression de la ponctuation, mise en minuscule, etc.).
    2. **Vectorisation TF-IDF (Phase 3)**: Conversion du texte en vecteurs mathématiques basés sur l'importance des mots.
    3. **Similarité Cosinus**: Calcul de l'angle entre le vecteur de l'étudiant et celui de la référence pour déterminer la proximité sémantique.
    
    ### Limites de l'MVP
    - Ce prototype n'utilise pas de LLMs coûteux.
    - La performance dépend de la qualité de la réponse de référence.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
