import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="FitTrack AI", layout="wide")

st.title("🏋️ FitTrack AI")
st.subheader("Health Analytics & Goal Prediction Platform")

# Sidebar Inputs
st.sidebar.header("User Inputs")

age = st.sidebar.slider("Age", 18, 60, 21)
height = st.sidebar.slider("Height (cm)", 140, 210, 160)
weight = st.sidebar.slider("Weight (kg)", 35, 150, 55)
workout = st.sidebar.slider("Workout Minutes", 0, 120, 30)
sleep = st.sidebar.slider("Sleep Hours", 0, 10, 7)
water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 2.5)

# Calculations
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

score = max(score, 0)

# Prediction Logic
goal = "Likely Achieved" if score >= 75 else "Needs Improvement"

# Metrics
c1, c2, c3, c4 = st.columns(4)

c1.metric("BMI", bmi)
c2.metric("Calories", f"{calories} kcal")
c3.metric("Health Score", f"{score}/100")
c4.metric("Goal Prediction", goal)

# Recommendation
st.subheader("🧠 Smart Insights")

if score >= 85:
    st.success("Excellent trend. Keep maintaining your routine.")
elif score >= 70:
    st.warning("Moderate progress. Increase workouts and consistency.")
else:
    st.error("Low fitness score detected. Improve exercise, sleep, hydration.")

# Weekly Workout Chart
st.subheader("📊 Weekly Workout Progress")

chart_data = pd.DataFrame({
    "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Minutes": [20,35,25,40,30,50,workout]
})

st.bar_chart(chart_data.set_index("Day"))

# Correlation Dataset
st.subheader("📈 Sample Fitness Dataset Analysis")

df = pd.DataFrame({
    "Age":[21,24,30,28,35,26,32],
    "Weight":[55,72,80,60,90,58,85],
    "Workout":[30,15,20,45,10,40,18],
    "Sleep":[7,6,5,8,5,7,6],
    "Score":[score,70,65,88,55,82,60]
})

st.dataframe(df)

# Correlation Heatmap
st.subheader("🔥 Correlation Heatmap")

corr = df.corr()

fig, ax = plt.subplots()
cax = ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
fig.colorbar(cax)

st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Final Year Data Science Internship Project | FitTrack AI")