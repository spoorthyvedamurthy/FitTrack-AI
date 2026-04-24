import streamlit as st

st.title("🤖 Prediction Page")

score = st.slider("Health Score", 0, 100, 75)

if score >= 80:
    st.success("High Probability of Goal Achievement")
elif score >= 60:
    st.warning("Moderate Probability")
else:
    st.error("Low Probability - Improve Routine")

st.info("Prediction based on health metrics and user inputs.")