# -*- coding: utf-8 -*-
"""Signupver2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c4SzRn4uXmKr9bBgDU5vytannKFEGrdN
"""

import streamlit as st
from datetime import datetime
import re
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(
    page_title="Authentication System",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state variables if they don't exist
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# CSS to style the app similar to the image
st.markdown("""
<style>
    .main {
        background-color: #4B8BDF;
        background: linear-gradient(135deg, #4B8BDF 0%, #2D6ECF 100%);
    }
    .stButton > button {
        width: 100%;
        background-color: white;
        color: #4B8BDF;
        font-weight: bold;
        border-radius: 20px;
        padding: 10px 0;
        border: none;
    }
    .stTextInput, .stDateInput, .stSelectbox {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 15px;
    }
    .sign-link {
        text-align: center;
        color: white;
    }
    .app-header {
        text-align: center;
        color: white;
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .divider {
        text-align: center;
        color: white;
        margin: 20px 0;
    }
    .social-buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .input-label {
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def validate_email(email):
    """Validate email format"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number (digits only)"""
    pattern = r"^\d+$"
    return re.match(pattern, phone) is not None

def sign_in():
    """Sign in screen"""
    st.markdown('<div class="app-header">Sign In</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown('<p class="input-label">Username</p>', unsafe_allow_html=True)
        username = st.text_input("", placeholder="Enter your Username", key="username_signin")

        st.markdown('<p class="input-label">Password</p>', unsafe_allow_html=True)
        password = st.text_input("", placeholder="Enter your Password", type="password", key="password_signin")

        remember_me = st.checkbox("Remember me")

        login_button = st.button("LOGIN")

        if login_button:
            if username in st.session_state.users and st.session_state.users[username]['password'] == password:
                st.session_state.is_authenticated = True
                st.session_state.current_user = username
                st.success(f"Welcome back, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.markdown('<div class="divider">- OR -</div>', unsafe_allow_html=True)

        st.markdown('<p class="sign-link">Sign in with</p>', unsafe_allow_html=True)

        # Social login buttons (for UI only)
        cols = st.columns([3, 1, 1, 3])
        with cols[1]:
            st.button("f")
        with cols[2]:
            st.button("G")

        st.markdown(f'<p class="sign-link">Don\'t have an Account? <a href="#" onclick="document.getElementById(\'sign_up\').click()">Sign up</a></p>', unsafe_allow_html=True)

def sign_up():
    """Sign up screen"""
    st.markdown('<div class="app-header">Sign Up</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown('<p class="input-label">Full Name</p>', unsafe_allow_html=True)
        full_name = st.text_input("", placeholder="Enter your Name", key="fullname_signup")

        st.markdown('<p class="input-label">Gender</p>', unsafe_allow_html=True)
        gender = st.selectbox("", options=["Male", "Female", "Other"], key="gender_signup")

        st.markdown('<p class="input-label">Birthdate</p>', unsafe_allow_html=True)
        birthdate = st.date_input("", key="birthdate_signup")

        st.markdown('<p class="input-label">Address</p>', unsafe_allow_html=True)
        address = st.text_input("", placeholder="Enter your Address", key="address_signup")

        st.markdown('<p class="input-label">Zip Code</p>', unsafe_allow_html=True)
        zipcode = st.text_input("", placeholder="Enter your Zip Code", key="zipcode_signup")

        st.markdown('<p class="input-label">Phone Number</p>', unsafe_allow_html=True)
        phone = st.text_input("", placeholder="Enter your Phone Number", key="phone_signup")

        st.markdown('<p class="input-label">Favorite Dish</p>', unsafe_allow_html=True)
        favorite_dish = st.selectbox("", options=["Italian", "Chinese", "Mexican", "Indian", "Japanese", "Other"], key="favorite_dish")

        st.markdown('<p class="input-label">Unfavorite Dish</p>', unsafe_allow_html=True)
        unfavorite_dish = st.selectbox("", options=["Italian", "Chinese", "Mexican", "Indian", "Japanese", "Other"], key="unfavorite_dish")

        st.markdown('<p class="input-label">Email</p>', unsafe_allow_html=True)
        email = st.text_input("", placeholder="Enter your Email", key="email_signup")

        st.markdown('<p class="input-label">Password</p>', unsafe_allow_html=True)
        password = st.text_input("", placeholder="Enter your Password", type="password", key="password_signup")

        st.markdown('<p class="input-label">Confirm Password</p>', unsafe_allow_html=True)
        confirm_password = st.text_input("", placeholder="Confirm Password", type="password", key="confirm_password_signup")

        register_button = st.button("REGISTER")

        if register_button:
            # Validate inputs
            errors = []

            if not full_name:
                errors.append("Full name is required")

            if not validate_phone(phone):
                errors.append("Phone number must contain only digits")

            if not validate_email(email):
                errors.append("Invalid email format")

            if password != confirm_password:
                errors.append("Passwords do not match")

            if len(password) < 6:
                errors.append("Password must be at least 6 characters long")

            # Username will be derived from email for simplicity
            username = email.split('@')[0] if email else ""

            if username in st.session_state.users:
                errors.append("User with this email already exists")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Store user data
                st.session_state.users[username] = {
                    'full_name': full_name,
                    'gender': gender,
                    'birthdate': birthdate.strftime('%Y-%m-%d'),
                    'address': address,
                    'zipcode': zipcode,
                    'phone': phone,
                    'favorite_dish': favorite_dish,
                    'unfavorite_dish': unfavorite_dish,
                    'email': email,
                    'password': password,
                    'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }

                st.success(f"Account created successfully! Your username is: {username}")
                # Switch to sign in page
                st.session_state.current_page = "sign_in"
                st.rerun()

        st.markdown(f'<p class="sign-link">Have an Account? <a href="#" onclick="document.getElementById(\'sign_in\').click()">Sign in</a></p>', unsafe_allow_html=True)

def main_app():
    """Main application after authentication"""
    st.title(f"Welcome, {st.session_state.current_user}!")
    st.write("You are successfully logged in.")

    # Display user information if available
    if st.session_state.current_user in st.session_state.users:
        user_data = st.session_state.users[st.session_state.current_user]
        st.subheader("Your Profile Information:")
        for key, value in user_data.items():
            if key != 'password':
                st.write(f"**{key.replace('_', ' ').title()}:** {value}")

    if st.button("Sign Out"):
        st.session_state.is_authenticated = False
        st.session_state.current_user = None
        st.rerun()

# Main app logic
if st.session_state.is_authenticated:
    main_app()
else:
    # Initialize current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "sign_in"

    # Hidden buttons for navigation (activated by links)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("sign_in", key="sign_in", type="hidden"):
            st.session_state.current_page = "sign_in"
            st.rerun()
    with col2:
        if st.button("sign_up", key="sign_up", type="hidden"):
            st.session_state.current_page = "sign_up"
            st.rerun()

    # Display the appropriate page
    if st.session_state.current_page == "sign_in":
        sign_in()
    else:
        sign_up()