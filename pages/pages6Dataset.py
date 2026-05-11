import streamlit as st
import pandas as pd

# Page Title
st.title("📂 Dataset Explorer")

st.write("Explore and analyze project datasets.")

# Dataset Selection
dataset_option = st.selectbox(
    "Select Dataset",
    ["Calories", "Heart", "Exercise"]
)

# Load Dataset
if dataset_option == "Calories":
    df = pd.read_csv("dataset/caloriesburned.csv")

elif dataset_option == "Heart":
    df = pd.read_csv("dataset/heart.csv")

else:
    df = pd.read_csv("dataset/exercise.csv")

# Dataset Preview
st.subheader("📄 Dataset Preview")
st.dataframe(df, use_container_width=True)

# Shape
st.subheader("📏 Dataset Shape")
rows, cols = df.shape

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", rows)

with col2:
    st.metric("Columns", cols)

# Columns
st.subheader("🧾 Column Names")
st.write(df.columns.tolist())

# Missing Values
st.subheader("❗ Missing Values")
st.dataframe(df.isnull().sum().reset_index().rename(
    columns={"index": "Column", 0: "Missing Values"}
))

# Statistical Summary
st.subheader("📊 Statistical Summary")
st.dataframe(df.describe(), use_container_width=True)

# Dataset Information
st.subheader("ℹ️ Dataset Information")

buffer = []

df.info(buf=buffer)

info_text = "\n".join(buffer)

st.text(info_text)

# Sample Charts
st.subheader("📈 Quick Visualization")

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_cols) > 0:

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    st.bar_chart(df[selected_col].head(20))

else:
    st.warning("No numeric columns available.")

# Footer
st.success("Dataset loaded successfully ✅")