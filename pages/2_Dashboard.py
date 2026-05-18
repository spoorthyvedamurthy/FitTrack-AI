import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="FitTrack AI Dashboard",
    page_icon="🏋️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

div[data-testid="metric-container"] {
    background-color: #111827;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🏋️ FitTrack AI Dashboard")

st.write(
    "Monitor fitness metrics, workout performance, and health analytics."
)

# ---------------- USER INPUTS ----------------

st.subheader("📝 Enter Health Details")

col1, col2 = st.columns(2)

with col1:

    calories = st.number_input(
        "🔥 Calories Burned",
        min_value=0,
        value=420
    )

    bmi = st.number_input(
        "⚖️ BMI",
        min_value=10.0,
        max_value=50.0,
        value=22.4
    )

with col2:

    heart_rate = st.number_input(
        "❤️ Heart Rate",
        min_value=40,
        max_value=200,
        value=98
    )

    workout_time = st.number_input(
        "🏃 Workout Time (min)",
        min_value=0,
        value=60
    )

# ---------------- HEALTH SUMMARY ----------------

st.subheader("👤 User Health Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🔥 Calories Burned",
        calories
    )

with c2:
    st.metric(
        "⚖️ BMI",
        bmi
    )

with c3:
    st.metric(
        "❤️ Heart Rate",
        f"{heart_rate} BPM"
    )

with c4:
    st.metric(
        "🏃 Workout Time",
        f"{workout_time} min"
    )

# ---------------- FITNESS SCORE ----------------

st.subheader("⭐ Fitness Score")

fitness_score = min(100, int((calories / 10) + (workout_time / 2)))

st.progress(fitness_score / 100)

st.success(
    f"Overall Fitness Score: {fitness_score}/100"
)

# ---------------- HEALTH STATUS ----------------

st.subheader("📈 Health Status")

col3, col4 = st.columns(2)

with col3:

    if bmi < 18.5:
        st.warning("⚠️ Underweight BMI detected.")

    elif bmi < 25:
        st.success("✅ BMI is within healthy range.")

    else:
        st.error("⚠️ Overweight BMI detected.")

    if workout_time >= 60:
        st.success("💪 Workout consistency is excellent.")

    else:
        st.info("🏃 Increase workout duration for better results.")

with col4:

    if heart_rate > 120:
        st.warning("❤️ High heart rate detected.")

    else:
        st.success("❤️ Heart rate is within normal range.")

    if calories > 500:
        st.success("🔥 Excellent calorie burn achieved.")

    else:
        st.info("🔥 Increase workout intensity slightly.")

# ---------------- DAILY GOALS ----------------

st.subheader("🎯 Daily Goals")

goal1 = st.checkbox(
    "30 Minutes Workout",
    value=workout_time >= 30
)

goal2 = st.checkbox(
    "Burn 400 Calories",
    value=calories >= 400
)

goal3 = st.checkbox(
    "Maintain Healthy BMI",
    value=(18.5 <= bmi <= 24.9)
)

goal4 = st.checkbox(
    "Maintain Heart Rate",
    value=(60 <= heart_rate <= 120)
)

# ---------------- AI RECOMMENDATIONS ----------------

st.subheader("🤖 AI Recommendations")

if calories > 500:

    st.success(
        "Excellent workout performance! Maintain hydration and recovery."
    )

elif calories > 300:

    st.info(
        "Good performance. Increase workout consistency for better endurance."
    )

else:

    st.warning(
        "Increase workout intensity and cardio activity."
    )

if bmi > 25:

    st.warning(
        "Recommended: Weight management and balanced nutrition."
    )

elif bmi < 18.5:

    st.info(
        "Recommended: Nutrient-rich diet and strength training."
    )

else:

    st.success(
        "BMI is balanced. Maintain current fitness routine."
    )

# ---------------- QUICK INSIGHTS ----------------

st.subheader("📌 Quick Insights")

st.write("""
- Regular workouts improve cardiovascular performance.
- Balanced nutrition supports better calorie management.
- Proper hydration improves workout recovery.
- Consistent exercise increases fitness score.
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption("FitTrack AI | Intelligent Fitness Analytics System")