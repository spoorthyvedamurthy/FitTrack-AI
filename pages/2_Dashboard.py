import streamlit as st

# Page Title
st.title("📊 FitTrack AI Dashboard")

st.write(
    "Monitor fitness metrics, workout performance, and health analytics."
)

# ---------------- USER SUMMARY ----------------

st.subheader("👤 User Health Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🔥 Calories Burned",
        "420"
    )

with c2:
    st.metric(
        "⚖️ BMI",
        "22.4"
    )

with c3:
    st.metric(
        "❤️ Heart Rate",
        "98 BPM"
    )

with c4:
    st.metric(
        "🏃 Workout Time",
        "60 min"
    )

# ---------------- FITNESS SCORE ----------------

st.subheader("⭐ Fitness Score")

fitness_score = 82

st.progress(fitness_score / 100)

st.success(
    f"Overall Fitness Score: {fitness_score}/100"
)

# ---------------- HEALTH STATUS ----------------

st.subheader("📈 Health Status")

col1, col2 = st.columns(2)

with col1:

    st.info(
        "✅ BMI is within healthy range."
    )

    st.success(
        "💪 Workout consistency is excellent."
    )

with col2:

    st.warning(
        "💧 Increase daily hydration slightly."
    )

    st.info(
        "🏃 Cardio performance is improving."
    )

# ---------------- DAILY GOALS ----------------

st.subheader("🎯 Daily Goals")

goal1 = st.checkbox(
    "30 Minutes Workout",
    value=True
)

goal2 = st.checkbox(
    "Drink 3L Water",
    value=False
)

goal3 = st.checkbox(
    "Burn 400 Calories",
    value=True
)

goal4 = st.checkbox(
    "Sleep 8 Hours",
    value=False
)

# ---------------- AI RECOMMENDATIONS ----------------

st.subheader("🤖 AI Recommendations")

st.success(
    "Maintain current workout consistency for improved endurance."
)

st.info(
    "Recommended: Increase hydration and include stretching exercises."
)

st.warning(
    "Monitor sleep schedule for better recovery performance."
)

# ---------------- QUICK INSIGHTS ----------------

st.subheader("📌 Quick Insights")

st.write("""
- Consistent workouts improve cardiovascular performance.
- Balanced nutrition supports better calorie management.
- Hydration plays an important role in workout recovery.
- Regular exercise improves overall fitness score.
""")

# Footer
st.markdown("---")

st.caption("FitTrack AI | Intelligent Fitness Dashboard")