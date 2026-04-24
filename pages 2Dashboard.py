import streamlit as st

st.title("📊 Dashboard")

age = st.slider("Age", 18, 60, 21)
height = st.slider("Height (cm)", 140, 210, 160)
weight = st.slider("Weight (kg)", 35, 150, 55)

height_m = height / 100
bmi = round(weight / (height_m ** 2), 1)
calories = int(weight * 30)

c1, c2 = st.columns(2)

c1.metric("BMI", bmi)
c2.metric("Calories Need", f"{calories} kcal")

if bmi < 18.5:
    st.warning("Underweight")
elif bmi < 25:
    st.success("Normal Weight")
else:
    st.error("Overweight")