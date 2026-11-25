import streamlit as st

from Log_In import Authentication
from utils import load_css, show_image

st.set_page_config(page_title="Tarhal", layout="wide")

load_css("login.css")


# One Authentication object per browser session
if "auth" not in st.session_state:
    st.session_state.auth = Authentication()

# Control the current view (Login / Register)
if "page" not in st.session_state:
    st.session_state.page = "Login"

# Message shown after a successful registration
if "flash" not in st.session_state:
    st.session_state.flash = None

auth = st.session_state.auth

col1, col2 = st.columns([1, 0.60])


# =========================
# LEFT SIDE
# =========================

with col1:
    # put your own photo in images/login.jpg; AlUla is used if it's missing
    if not show_image("login.jpg"):
        show_image("alula.jpg")

    st.markdown(
        """
        <div class="left-content">
            <p class="small-text">MADE FOR SAUDI ADVENTURES</p>
            <h1>Every journey<br>begins with <i>wonder.</i></h1>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# RIGHT SIDE
# =========================

with col2:

    if st.session_state.page == "Login":
        st.markdown(
            """
            <div class="welcome-text">
                <p class="welcome-small">WELCOME TO TARHAL</p>
                <h2>Welcome back</h2>
                <p>Sign in to continue planning your next Saudi adventure.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="welcome-text">
                <p class="welcome-small">WELCOME TO TARHAL</p>
                <h2>Create your account</h2>
                <p>Join Tarhal and start planning memorable trips across the Kingdom.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =========================
    # LOGIN
    # =========================

    if st.session_state.page == "Login":

        if st.session_state.flash:
            st.success(st.session_state.flash)
            st.session_state.flash = None

        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login →"):
            if auth.validate_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username.strip()
                st.switch_page("pages/Explore.py")
            else:
                st.error("Invalid username or password")

        st.markdown('<p class="account-text">New to Tarhal?</p>', unsafe_allow_html=True)

        with st.container(key="create-account"):
            if st.button("Create an account"):
                st.session_state.page = "Register"
                st.rerun()

    # =========================
    # REGISTER
    # =========================

    else:

        email = st.text_input("Email address", key="register_email")
        username = st.text_input("Username", key="register_username")
        password = st.text_input("Password", type="password", key="register_password")

        if st.button("Create account →"):
            ok, message = auth.sign_up(email, username, password)
            if ok:
                st.session_state.flash = message + " Please log in."
                st.session_state.page = "Login"
                st.rerun()
            else:
                st.warning(message)

        st.markdown('<p class="account-text">Already have an account?</p>', unsafe_allow_html=True)

        with st.container(key="login-account"):
            if st.button("Login"):
                st.session_state.page = "Login"
                st.rerun()
