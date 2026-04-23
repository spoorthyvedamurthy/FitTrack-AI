import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FitTrack AI",
    layout="wide",
    page_icon="📊"
)

# ---------------------------
# HEADER / HOME SECTION
# ---------------------------

st.markdown(
"""
# 🏋️ FitTrack AI  
### Intelligent Health Analytics & Prediction System
A final year Data Science project that analyzes personal health metrics, visualizes trends, and predicts fitness outcomes.
"""
)

st.markdown("---")

# ---------------------------
# FEATURE CARDS
# ---------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.info("📊 Health Metrics Analysis")

with c2:
    st.info("📈 Workout Trend Monitoring")

with c3:
    st.info("🤖 Goal Prediction Engine")

st.markdown("---")

# ---------------------------
# SIDEBAR INPUTS
# ---------------------------

st.sidebar.title("FitTrack AI")
st.sidebar.caption("Final Year Data Science Project")

st.sidebar.header("Enter User Details")

age = st.sidebar.slider("Age", 18, 60, 21)
height = st.sidebar.slider("Height (cm)", 140, 210, 160)
weight = st.sidebar.slider("Weight (kg)", 35, 150, 55)
workout = st.sidebar.slider("Workout Minutes", 0, 120, 30)
sleep = st.sidebar.slider("Sleep Hours", 0, 10, 7)
water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 2.5)

# ---------------------------
# CALCULATIONS
# ---------------------------

height_m = height / 100
bmi = round(weight / (height_m ** 2), 1)
calories = int(weight * 30)

score = 100

if bmi < 18.5:
    score -= 20
elif bmi > 25:
    score -= 15

if sleep < 6:
    score -= 10

if workout < 20:
    score -= 10

if water < 2:
    score -= 5

score = max(score, 0)

# ---------------------------
# PREDICTION LOGIC
# ---------------------------

goal = "Likely Achieved" if score >= 75 else "Needs Improvement"

risk = "Low"
if score < 80:
    risk = "Moderate"
if score < 60:
    risk = "High"

# ---------------------------
# KPI DASHBOARD
# ---------------------------

st.subheader("📌 Key Performance Indicators")

k1, k2, k3, k4 = st.columns(4)

k1.metric("BMI", bmi)
k2.metric("Calories Need", f"{calories} kcal")
k3.metric("Health Score", f"{score}/100")
k4.metric("Risk Level", risk)

st.markdown("---")

# ---------------------------
# INSIGHTS SECTION
# ---------------------------

st.subheader("🧠 Smart Recommendation Engine")

if score >= 85:
    st.success("Excellent overall health trend detected. Keep maintaining your current routine.")
elif score >= 70:
    st.warning("Moderate performance. Improve consistency in workouts, hydration, and sleep.")
else:
    st.error("Low health score detected. Focus on exercise, sleep recovery, and nutrition immediately.")

st.markdown("---")

# ---------------------------
# WEEKLY WORKOUT TRENDS
# ---------------------------

st.subheader("📈 Weekly Workout Trend Analysis")

trend_df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Workout_Minutes": [20, 35, 25, 40, 30, 50, workout]
})

st.bar_chart(trend_df.set_index("Day"))

st.markdown("---")

# ---------------------------
# SAMPLE DATASET SECTION
# ---------------------------

st.subheader("📊 Fitness Dataset Insights")

df = pd.DataFrame({
    "Age": [21, 24, 30, 28, 35, 26, 32, age],
    "Weight": [55, 72, 80, 60, 90, 58, 85, weight],
    "Workout": [30, 15, 20, 45, 10, 40, 18, workout],
    "Sleep": [7, 6, 5, 8, 5, 7, 6, sleep],
    "Water": [2.5, 2.0, 1.8, 3.0, 1.5, 2.8, 2.1, water],
    "Score": [82, 70, 65, 88, 55, 84, 60, score]
})

st.dataframe(df, use_container_width=True)

st.markdown("---")

# ---------------------------
# CORRELATION HEATMAP
# ---------------------------

st.subheader("🔥 Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(8, 5))
cax = ax.matshow(corr)

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="left")
plt.yticks(range(len(corr.columns)), corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}", va="center", ha="center", fontsize=8)

fig.colorbar(cax)
st.pyplot(fig)

st.markdown("---")

# ---------------------------
# USER SUMMARY
# ---------------------------

st.subheader("📋 Personalized Summary")

summary = pd.DataFrame({
    "Metric": [
        "Age", "Height", "Weight", "Workout Minutes",
        "Sleep Hours", "Water Intake", "BMI",
        "Calories Need", "Health Score", "Goal Prediction"
    ],
    "Value": [
        age, height, weight, workout,
        sleep, water, bmi,
        calories, score, goal
    ]
})

st.table(summary)

st.markdown("---")

# ---------------------------
# ABOUT PROJECT
# ---------------------------

st.subheader("ℹ️ About Project")

st.write("""
FitTrack AI is a final year Data Science project developed to analyze user health data,
visualize lifestyle patterns, and generate predictive fitness insights.

This platform demonstrates:
- Data collection and preprocessing
- Health metric analytics
- Trend visualization
- Correlation analysis
- Rule-based prediction system
""")

st.markdown("---")
st.caption("© FitTrack AI | Final Year Data Science Project")