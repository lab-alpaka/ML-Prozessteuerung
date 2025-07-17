

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
    - Zeitreihenanalyse: Autokorrelation, MA  
    """)

### expander not allowed on nested form of other expanders!     with st.expander("📈 2.3 Überwachtes Lernen"):
        st.markdown("**Regression:**")
        st.markdown("- Lineare / Polynomiale Regression")
        st.markdown("- Support Vector Regression (SVR)")
        st.markdown("- Random Forest, XGBoost, LightGBM")
        st.markdown("- Neuronale Netze")

        st.markdown("**Klassifikation:**")
        st.markdown("- Logistische Regression")
        st.markdown("- SVM, KNN, Random Forest")
        st.markdown("- Neuronale Netze")

    with st.expander("🔍 2.4 Unüberwachtes Lernen"):
        st.markdown("- Clustering: K-Means, DBSCAN, Hierarchisch")
        st.markdown("- Dimensionsreduktion: PCA, Autoencoder")

    with st.expander("🎮 2.5 Reinforcement Learning"):
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
    - Herausforderungen: Stabilität, Interpretierbarkeit  
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

# === Kapitel 4 ===
with st.expander("🏭 4. Anwendungen & Fallstudien"):
    st.markdown("**4.1 Prozessoptimierung**")
    st.markdown("- Echtzeit-Optimierung, Prädiktive Wartung")

    st.markdown("**4.2 Fehlerdiagnose & Prognose**")
    st.markdown("- Anomalieerkennung (Isolation Forest, Autoencoder)")
    st.markdown("- RUL, Alarmmanagement")

    st.markdown("**4.3 Qualitätskontrolle**")
    st.markdown("- Prädiktion & Regelung von Produktqualität")

    st.markdown("**4.4 Energieeffizienz**")
    st.markdown("- Lastmanagement, Prädiktive Steuerung")

    st.markdown("**4.5 Branchen**")
    st.markdown("- Chemie, Energie, Pharma, Wasserwirtschaft")

# === Kapitel 5 ===
with st.expander("🛠️ 5. Implementierung & Integration"):
    st.markdown("**5.1 Software & Tools**")
    st.markdown("- Python, MATLAB, TensorFlow, PyTorch")
    st.markdown("- OpenAI Gym, gPROMS, InfluxDB")

    st.markdown("**5.2 Integration**")
    st.markdown("- OPC UA, PLC, Docker, Kubernetes")

    st.markdown("**5.3 Sicherheit & Zuverlässigkeit**")
    st.markdown("- Model Drift, Redundanz, Cybersecurity")

    st.markdown("**5.4 Ethik & Regulierung**")
    st.markdown("- Datenschutz, Mensch-KI-Interaktion")

# === Kapitel 6 ===
with st.expander("🔮 6. Forschung & Zukunftstrends"):
    st.markdown("**6.1 Explainable AI (XAI)**")
    st.markdown("- SHAP, LIME, Modellvisualisierung")

    st.markdown("**6.2 Edge AI & Verteilte Systeme**")
    st.markdown("- Federated Learning, Edge Computing")

    st.markdown("**6.3 Digitale Zwillinge**")
    st.markdown("- Simulation, KI-basierte Wartung, Realtime-Modellierung")

# === GitHub-Beispielbox ===
st.sidebar.title("🔗 Beispiel-Repos & Ressourcen")

if st.sidebar.button("Beispiel-Repositories anzeigen"):
    st.sidebar.markdown("**📦 Supervised Learning (Regression)**")
    st.sidebar.markdown("[Scikit-learn Beispiele](https://github.com/scikit-learn/scikit-learn/tree/main/examples)")
    st.sidebar.markdown("[XGBoost Regression](https://github.com/dmlc/xgboost/tree/master/demo/regression)")

    st.sidebar.markdown("**📦 Reinforcement Learning**")
    st.sidebar.markdown("[OpenAI Baselines](https://github.com/openai/baselines)")
    st.sidebar.markdown("[CleanRL (PPO, DQN)](https://github.com/vwxyzjn/cleanrl)")

    st.sidebar.markdown("**📦 MPC + ML**")
    st.sidebar.markdown("[MPC mit NN (PyTorch)](https://github.com/eziosie/DeepMPC)")
    st.sidebar.markdown("[Gaussian Process MPC](https://github.com/henniggroup/gp-mpc)")

    st.sidebar.markdown("**📦 Anomaly Detection**")
    st.sidebar.markdown("[Autoencoder für Anomalien](https://github.com/guansongpang/DeepAD)")


# === Kapitel 3 Quiz-Modul ===
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

## ▶️ Schritt 3: App starten
