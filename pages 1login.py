import streamlit as st

st.title("🔐 Login Page")

st.subheader("User Authentication Portal")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        st.success(f"Welcome {username}!")
    else:
        st.error("Please enter username and password.")

st.markdown("---")
st.caption("Secure Access | FitTrack AI")