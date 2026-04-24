import streamlit as st
import pandas as pd

st.title("📈 Analytics Page")

st.subheader("Weekly Workout Trend")

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Workout Minutes": [20, 35, 25, 40, 30, 50, 45]
})

st.bar_chart(df.set_index("Day"))

st.subheader("Sample Dataset")

st.dataframe(df, use_container_width=True)