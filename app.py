import streamlit as st

st.set_page_config(page_title="FitTrack AI", layout="wide")

st.title("🏋️ FitTrack AI")
st.subheader("Intelligent Health Analytics & Prediction Platform")

st.markdown("""
Welcome to FitTrack AI – a final year Data Science project designed to analyze user health metrics, visualize trends, and predict fitness outcomes.

### Features:
- Multi-page dashboard
- BMI & calorie analysis
- Health score system
- Workout analytics
- Prediction engine
- Professional UI
""")

col1, col2, col3 = st.columns(3)
import streamlit as st

st.set_page_config(
    page_title="FitTrack AI",
    layout="wide",
    page_icon="📊"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
section[data-testid="stSidebar"] {
    background-color: #111827;
}
section[data-testid="stSidebar"] * {
    color: white;
}
div[data-testid="metric-container"] {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 15px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏋️ FitTrack AI")
st.subheader("Intelligent Health Analytics & Prediction Platform")

st.markdown("""
Welcome to a multi-page final year Data Science application built for health monitoring,
analytics, and prediction using Python.
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("📊 Analytics Dashboard")

with c2:
    st.info("📈 Trend Monitoring")

with c3:
    st.info("🤖 Prediction Engine")

st.success("Use the sidebar to navigate across modules.")
col1.info("📊 Data Analytics")
col2.info("📈 Trend Monitoring")
col3.info("🤖 Smart Prediction")

st.success("Use the sidebar to navigate between pages.")