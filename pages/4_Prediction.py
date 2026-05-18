import streamlit as st
import joblib
import numpy as np

# Load ML Model
model = joblib.load("models/calories_model.pkl")

# Page Title
st.title("🤖 AI Fitness Prediction System")

st.write(
    "Analyze workout performance and predict calories burned using Machine Learning."
)

# ---------------- USER INPUTS ----------------

st.subheader("🏃 Enter Fitness Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    age = st.slider(
        "Age",
        10, 80, 25
    )

    height = st.slider(
        "Height (cm)",
        120, 220, 170
    )

    weight = st.slider(
        "Weight (kg)",
        30, 150, 70
    )

with col2:

    bmi = st.slider(
        "BMI",
        10.0, 50.0, 22.0
    )

    running_time = st.slider(
        "Running Time (min)",
        1, 180, 30
    )

    running_speed = st.slider(
        "Running Speed (km/h)",
        1.0, 25.0, 8.0
    )

    distance = st.slider(
        "Distance (km)",
        0.5, 50.0, 5.0
    )

# Heart Rate
heart_rate = st.slider(
    "Average Heart Rate",
    60, 200, 100
)

# Convert Gender
gender_value = 0 if gender == "male" else 1

# ---------------- PREDICTION ----------------

if st.button("Predict Fitness Performance"):

    input_data = np.array([[
        gender_value,
        age,
        height,
        weight,
        bmi,
        running_time,
        running_speed,
        distance,
        heart_rate
    ]])

    prediction = model.predict(input_data)

    calories = prediction[0]

    # ---------------- RESULTS ----------------

    st.subheader("📊 Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🔥 Calories Burned",
            f"{calories:.2f}"
        )

    # Fitness Score
    fitness_score = min(100, int(calories / 5))

    with c2:
        st.metric(
            "⭐ Fitness Score",
            f"{fitness_score}/100"
        )

    # Workout Level
    if calories > 350:
        level = "Advanced 💪"

    elif calories > 200:
        level = "Intermediate ⚡"

    else:
        level = "Beginner 🏃"

    with c3:
        st.metric(
            "🏆 Workout Level",
            level
        )

    # ---------------- RECOMMENDATIONS ----------------

    st.subheader("💡 AI Recommendations")

    if calories > 350:

        st.success(
            "Excellent workout performance! Maintain consistency and hydration."
        )

        st.info(
            "Recommended: Strength training + balanced nutrition."
        )

    elif calories > 200:

        st.warning(
            "Good workout performance. Increase intensity slightly for better results."
        )

        st.info(
            "Recommended: Cardio exercises and protein-rich diet."
        )

    else:

        st.error(
            "Low calorie burn detected. Increase workout duration and activity level."
        )

        st.info(
            "Recommended: Daily walking, cardio, and hydration improvement."
        )

    # ---------------- HEALTH INSIGHTS ----------------

    st.subheader("📈 Fitness Insights")

    if bmi < 18.5:
        st.warning("BMI indicates Underweight condition.")

    elif bmi < 25:
        st.success("BMI indicates Normal fitness range.")

    else:
        st.error("BMI indicates Overweight condition.")

    # Progress Bar
    st.subheader("🏅 Fitness Progress")

    st.progress(fitness_score / 100)

# Footer
st.markdown("---")

st.caption("FitTrack AI | Intelligent Fitness Analytics System")