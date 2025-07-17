
import streamlit as st

st.set_page_config(page_title="ML in der Prozessautomation", layout="wide")
st.title("🤖 Machine Learning in der Prozessautomation und -steuerung")
st.markdown("Interaktive Lernplattform für Hochschullehre")

# === Kapitel 2 ===
with st.expander("📘 2. Grundlagen des Maschinellen Lernens"):
    st.subheader("2.1 Einführung in Maschinelles Lernen (ML)")
    st.markdown("""
    - Arten des Lernens: Überwachtes, Unüberwachtes, Bestärkendes Lernen  
    - Grundkonzepte: Features, Labels, Trainings-/Testdaten  
    - Evaluierungsmetriken: MSE, R², F1-Score usw.  
    - Overfitting/Underfitting, Kreuzvalidierung  
    """)

    st.subheader("2.2 Datenerfassung und Vorverarbeitung")
    st.markdown("""
    - Datenquellen: Sensoren, Historian, LIMS  
    - Datenreinigung: Fehlwerte, Rauschen, Ausreißer  
    - Feature Engineering: Zeitreihen, Domänenwissen  
    - Zeitreihenanalyse: Autokorrelation, gleitende Durchschnitte  
    """)

    st.subheader("2.3 Überwachtes Lernen")
    st.markdown("**Regression:**")
    st.markdown("""
    - Lineare / Polynomiale Regression  
    - Support Vector Regression (SVR)  
    - Random Forest, XGBoost, LightGBM  
    - Neuronale Netze  
    """)
    st.markdown("**Klassifikation:**")
    st.markdown("""
    - Logistische Regression  
    - SVM, KNN, Random Forest  
    - Neuronale Netze  
    """)

    st.subheader("2.4 Unüberwachtes Lernen")
    st.markdown("""
    - Clustering: K-Means, DBSCAN, Hierarchisches Clustering  
    - Dimensionsreduktion: PCA, Autoencoder  
    """)

    st.subheader("2.5 Reinforcement Learning")
    st.markdown("""
    - Grundlagen: Agent, Aktion, Zustand, Belohnung  
    - Q-Learning, SARSA, DQN  
    - PPO, SAC, Actor-Critic  
    - Sicherheit, Stabilität, Exploration vs. Exploitation  
    """)

# === Kapitel 3 ===
with st.expander("🧭 3. Machine Learning Control (MLC)"):
    st.subheader("3.1 Grundlagen der MLC")
    st.markdown("""
    - ML-Modelle im Regelkreis  
    - Lernende Regler vs. Regler mit lernenden Komponenten  
    - Herausforderungen: Stabilität, Interpretierbarkeit, Sicherheit  
    """)

    st.subheader("3.2 Modellprädiktive Regelung (MPC)")
    st.markdown("""
    - ML-Modelle in MPC: Neuronale Netze, Gauß-Prozesse  
    - Hybride Modelle: physikalisch + ML  
    - NMPC mit ML, Beispiel: Destillationskolonnen  
    """)

    st.subheader("3.3 RL in der Prozessregelung")
    st.markdown("""
    - Direkte RL-Regler (DQN, PPO, SAC)  
    - Belohnungsdesign, hierarchisches RL  
    - Offline- & Safe RL  
    """)

    st.subheader("3.4 Hybride Ansätze")
    st.markdown("""
    - Modellbasiertes RL  
    - Adaptive PID-Regler  
    - Fehlerkompensation, Regler-Tuning mit ML  
    """)

# Quiz-Modul
st.markdown("---")
st.header("📝 Quiz: Kapitel 3 – Machine Learning Control")

with st.expander("Quiz jetzt starten"):
    score = 0
    total = 5

    st.markdown("Beantworte folgende Fragen zum Thema **Machine Learning Control (MLC)**:")

    q1 = st.radio("1️⃣ Welche Aussage beschreibt Machine Learning Control (MLC) am besten?",
                  ["Ein rein physikalisches Regelkonzept ohne Datenbezug",
                   "Ein Verfahren zur Integration von ML-Modellen in Regelkreise",
                   "Ein Tool zur grafischen Visualisierung von Regelalgorithmen"])
    if q1 == "Ein Verfahren zur Integration von ML-Modellen in Regelkreise":
        score += 1

    q2 = st.radio("2️⃣ Was ist eine typische Herausforderung bei ML-basierten Regelungen?",
                  ["Zu wenig Rechenleistung", "Stabilität und Sicherheit", "Niedrige Temperatur"])
    if q2 == "Stabilität und Sicherheit":
        score += 1

    q3 = st.radio("3️⃣ Welche Methode wird typischerweise für Modellprädiktive Regelung (MPC) mit Unsicherheitsquantifizierung verwendet?",
                  ["Support Vector Machines", "Gauß-Prozesse", "K-Means Clustering"])
    if q3 == "Gauß-Prozesse":
        score += 1

    q4 = st.radio("4️⃣ Was ist der Unterschied zwischen modellfreiem und modellbasiertem Reinforcement Learning?",
                  ["Es gibt keinen Unterschied", 
                   "Modellfrei nutzt keine Prozessmodelle, modellbasiert schon",
                   "Modellfrei ist deterministisch, modellbasiert nicht"])
    if q4 == "Modellfrei nutzt keine Prozessmodelle, modellbasiert schon":
        score += 1

    q5 = st.radio("5️⃣ Wofür steht PPO in der Prozesssteuerung?",
                  ["Proximal Policy Optimization", "Process Path Operation", "Parallel Planning Optimization"])
    if q5 == "Proximal Policy Optimization":
        score += 1

    if st.button("🎯 Auswertung anzeigen"):
        st.success(f"Du hast {score} von {total} Punkten erreicht.")
        if score == 5:
            st.balloons()
            st.markdown("✅ **Perfekt! Du hast alle Fragen korrekt beantwortet.**")
        elif score >= 3:
            st.markdown("👍 **Gute Arbeit – du hast das Wesentliche verstanden.**")
        else:
            st.warning("🧐 Vielleicht wiederholst du Kapitel 3 noch einmal.")
