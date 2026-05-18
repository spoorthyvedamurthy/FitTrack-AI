import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

st.page_link("pages/2_Dashboard.py", label="📊 Dashboard")
st.page_link("pages/3_Analytics.py", label="📈 Analytics")
st.page_link("pages/4_Prediction.py", label="🤖 Prediction")

# Page Title
st.title("📈 Fitness Analytics Dashboard")

st.write(
    "Interactive analysis of workout performance and fitness metrics."
)

# ---------------- SAMPLE DATA ----------------

df = pd.DataFrame({

    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],

    "Calories Burned": [220, 340, 280, 410, 390, 520, 470],

    "Workout Time": [30, 45, 40, 60, 55, 75, 70],

    "Water Intake": [2.0, 2.5, 2.2, 3.0, 3.1, 4.0, 3.5]

})

# ---------------- KPI CARDS ----------------

st.subheader("📊 Weekly Performance Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🔥 Total Calories",
        int(df["Calories Burned"].sum())
    )

with c2:
    st.metric(
        "🏃 Total Workout Time",
        int(df["Workout Time"].sum())
    )

with c3:
    st.metric(
        "💧 Avg Water Intake",
        round(df["Water Intake"].mean(), 1)
    )

# ---------------- CALORIES CHART ----------------

st.subheader("🔥 Calories Burn Trend")

fig1 = px.line(
    df,
    x="Day",
    y="Calories Burned",
    markers=True,
    title="Daily Calories Burned"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- WORKOUT TIME ----------------

st.subheader("🏋️ Workout Duration Analysis")

fig2 = px.bar(
    df,
    x="Day",
    y="Workout Time",
    text="Workout Time",
    title="Workout Duration"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- WATER INTAKE ----------------

st.subheader("💧 Hydration Monitoring")

fig3 = px.area(
    df,
    x="Day",
    y="Water Intake",
    title="Daily Water Intake"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- PERFORMANCE INSIGHTS ----------------

st.subheader("💡 Performance Insights")

best_day = df.loc[
    df["Calories Burned"].idxmax(),
    "Day"
]

st.success(
    f"Highest calorie burn achieved on {best_day} 💪"
)

st.info(
    "Consistent exercise and hydration improve overall fitness performance."
)

st.warning(
    "Maintain balanced nutrition and recovery for better endurance."
)

# ---------------- DATA TABLE ----------------

st.subheader("📄 Weekly Fitness Dataset")

st.dataframe(
    df,
    use_container_width=True
)

# Footer
st.markdown("---")

st.caption("FitTrack AI | Interactive Analytics Dashboard")