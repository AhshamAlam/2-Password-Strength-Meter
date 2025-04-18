# imports
import re
import streamlit as st

# Set page config
st.set_page_config(page_title="Password Strength Checker", page_icon="⚡", layout="centered")

# Custom styling for center alignment and black background
st.markdown("""
    <style>
        .centered-title {
            text-align: center;
            color: white;
            font-size: 2.5em;
            font-weight: bold;
        }
        .centered-subtitle {
            text-align: center;
            color: #AAAAAA;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .centered-subheading {
            text-align: center;
            color: white;
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 30px;
        }
        body {
            background-color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown("<div class='centered-title'>🔐 Password Strength Checker</div>", unsafe_allow_html=True)
st.markdown("<div class='centered-subtitle'>🛡️ Check the strength of your password</div>", unsafe_allow_html=True)
st.markdown("<div class='centered-subheading'>🧠 This is a simple password strength checker by Ahsham Alam!</div>", unsafe_allow_html=True)

# Password checking logic
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")
  
    if re.search(r'[A-Z]', password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Include both uppercase and lowercase letters.")
    
    if re.search(r'[\d]', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one number.")
    
    if re.search(r'[!@#$%^&*()_+{}|:"<>?~-]', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one special character.")

    if score == 4:
        st.success("✅ Your password is strong!")
    elif score == 3:
        st.warning("⚠️ Your password is medium.")
    else:
        st.error("❌ Your password is weak.")

    if feedback:
        with st.expander("💡 How to improve your password"):
            for item in feedback:
                st.write(item)

# Input field
password = st.text_input("🔑 Enter your password", type="password", help="Minimum 8 characters, with uppercase, lowercase, number, and special character.")

# Button and result
if st.button("🚀 Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("⚠️ Please enter a password.")

