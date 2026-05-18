import streamlit as st

# Page Title
st.title("🔐 FitTrack AI Login")

st.write(
    "Welcome to the Intelligent Fitness Analytics Platform"
)

# ---------------- LOGIN BOX ----------------

with st.container():

    st.subheader("Login to Continue")

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    remember = st.checkbox("Remember Me")

    # Login Button
    if st.button("Login"):

        if username != "" and password != "":

            st.success(
                f"Welcome {username} 🎉"
            )

            st.balloons()

        else:

            st.error(
                "Please enter username and password"
            )

# ---------------- REGISTER SECTION ----------------

st.markdown("---")

st.subheader("📝 New User Registration")

new_user = st.text_input(
    "Create Username"
)

new_password = st.text_input(
    "Create Password",
    type="password"
)

if st.button("Register"):

    if new_user != "" and new_password != "":

        st.success(
            "Registration Successful ✅"
        )

        st.info(
            "Now login using your credentials."
        )

    else:

        st.warning(
            "Please fill all registration fields."
        )

# Footer
st.markdown("---")

st.caption("FitTrack AI | Secure User Access")