# -*- coding: utf-8 -*-
"""SignInver3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lVgVy107KVKSWwt0BjIXQoAntTNA9q3z
"""

import streamlit as st
import datetime
import re
from PIL import Image
import base64
import json
import os

# Function to save user data to a JSON file
def save_user_data(user_data):
    # Check if the file exists
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            users = json.load(f)
    else:
        users = []

    users.append(user_data)

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

# Function to validate email format
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# Function to validate phone number
def is_valid_phone(phone):
    pattern = r"^\d{10}$"
    return re.match(pattern, phone) is not None

# Function to validate password (at least 8 characters)
def is_valid_password(password):
    return len(password) >= 8

# Function to check if user exists
def check_user_credentials(email, password):
    if not os.path.exists("users.json"):
        return False

    with open("users.json", "r") as f:
        users = json.load(f)

    for user in users:
        if user["email"] == email and user["password"] == password:
            return True

    return False

# Set page configuration
st.set_page_config(
    page_title="Authentication App",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make it look like the image
st.markdown("""
<style>
    .auth-container {
        background-color: #4A8FE7;
        padding: 30px;
        border-radius: 15px;
        color: white;
    }
    .stButton > button {
        background-color: white;
        color: #4A8FE7;
        font-weight: bold;
        width: 100%;
        padding: 10px;
        border-radius: 25px;
        border: none;
    }
    .social-button {
        background-color: white;
        border-radius: 50%;
        padding: 10px;
        margin: 5px;
    }
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 5px;
    }
    ::placeholder {
        color: rgba(255, 255, 255, 0.7);
    }
    .stCheckbox > div > label {
        color: white;
    }
    .stDateInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 5px;
    }
    .stSelectbox > div > div > div {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Create two tabs for Sign In and Sign Up
tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

# Session 1: Sign In
with tab1:
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Sign In</h1>", unsafe_allow_html=True)

    # Email input
    email_signin = st.text_input("Email", key="email_signin", placeholder="Enter your Email")

    # Password input
    password_signin = st.text_input("Password", key="password_signin", type="password", placeholder="••••••")

    # Forgot Password link
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown("<div style='text-align: right;'><a href='#' style='color: white;'>Forgot Password?</a></div>", unsafe_allow_html=True)

    # Remember me checkbox
    remember_me = st.checkbox("Remember me")

    # Login button
    if st.button("LOGIN", key="login_button"):
        if email_signin and password_signin:
            if check_user_credentials(email_signin, password_signin):
                st.success("Login successful!")
                st.session_state.logged_in = True
                st.session_state.username = email_signin
            else:
                st.error("Invalid email or password")
        else:
            st.warning("Please enter your email and password")

    # OR separator
    st.markdown("<div style='text-align: center; margin: 20px 0;'>- OR -</div>", unsafe_allow_html=True)

    # Social login buttons
    st.markdown("<div style='text-align: center;'>Sign in with</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col2:
        st.markdown("<div class='social-button'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/1024px-Facebook_Logo_%282019%29.png' width='30'></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='social-button'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2048px-Google_%22G%22_Logo.svg.png' width='30'></div>", unsafe_allow_html=True)

    # Sign up link
    st.markdown("<div style='text-align: center; margin-top: 20px;'>Don't have an Account? <a href='#' style='color: white; text-decoration: underline;'>Sign up</a></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Session 2: Sign Up
with tab2:
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Sign Up</h1>", unsafe_allow_html=True)

    # Full name
    full_name = st.text_input("Full Name", placeholder="Enter your Name")

    # Gender
    gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])

    # Birthdate
    birthdate = st.date_input("Birthdate", min_value=datetime.date(1900, 1, 1))

    # Address
    address = st.text_input("Address", placeholder="Enter your address")

    # Zip code
    zip_code = st.text_input("Zip Code", placeholder="Enter your zip code")

    # Phone number
    phone = st.text_input("Phone Number", placeholder="Enter your Phone number")

    # Favorite dish
    fav_dish = st.text_input("Favorite Dish", placeholder="Enter your favorite dish")

    # Unfavorite dish
    unfav_dish = st.text_input("Unfavorite Dish", placeholder="Enter your unfavorite dish")

    # Email
    email = st.text_input("Email", placeholder="Enter your Email")

    # Password
    password = st.text_input("Password", type="password", placeholder="Enter your Password")

    # Confirm Password
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm Password")

    # Register button
    if st.button("REGISTER", key="register_button"):
        # Validate inputs
        if not full_name:
            st.error("Please enter your full name")
        elif not gender:
            st.error("Please select your gender")
        elif not phone:
            st.error("Please enter your phone number")
        elif not is_valid_phone(phone):
            st.error("Please enter a valid 10-digit phone number")
        elif not email:
            st.error("Please enter your email")
        elif not is_valid_email(email):
            st.error("Please enter a valid email address")
        elif not password:
            st.error("Please enter a password")
        elif not is_valid_password(password):
            st.error("Password must be at least 8 characters long")
        elif password != confirm_password:
            st.error("Passwords do not match")
        else:
            # Create user data dictionary
            user_data = {
                "full_name": full_name,
                "gender": gender,
                "birthdate": str(birthdate),
                "address": address,
                "zip_code": zip_code,
                "phone": phone,
                "favorite_dish": fav_dish,
                "unfavorite_dish": unfav_dish,
                "email": email,
                "password": password
            }

            # Save user data
            save_user_data(user_data)

            st.success("Registration successful! You can now sign in.")

    # Sign in link
    st.markdown("<div style='text-align: center; margin-top: 20px;'>Have an Account? <a href='#' style='color: white; text-decoration: underline;'>Sign in</a></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Home page (visible after login)
if 'logged_in' in st.session_state and st.session_state.logged_in:
    st.sidebar.success(f"Welcome {st.session_state.username}!")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))

    st.title("Welcome to the App!")
    st.write("You are now logged in. This is the home page of your application.")