import streamlit as st
import graphviz

st.subheader("🧠 Inhaltsübersicht – Machine Learning Control")

dot = graphviz.Digraph()
dot.node("MLC", "Machine Learning Control")
dot.edge("MLC", "MPC")
dot.edge("MLC", "RL")
dot.edge("MLC", "Hybride Systeme")
dot.edge("MPC", "NN-Modelle")
dot.edge("MPC", "Gauß-Prozesse")
dot.edge("RL", "DQN")
dot.edge("RL", "PPO")
dot.edge("Hybride Systeme", "PID mit ML")
dot.edge("Hybride Systeme", "Fehlerkompensation")

st.graphviz_chart(dot)
