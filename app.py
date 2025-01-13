import streamlit as st
import pandas as pd
import pickle
import string

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    return text

# Load the trained model and vectorizer
try:
    model = pickle.load(open("Spam.pkl", "rb"))
    vectorizer = pickle.load(open("msg.pkl", "rb"))
except Exception as e:
    st.error("Error loading model or vectorizer. Ensure 'Spam.pkl' and 'msg.pkl' are in the same directory.")
    st.stop()

# Streamlit App Layout
st.set_page_config(
    page_title="SMS Spam Detection System Using NLP",
    page_icon="📧",
    layout="wide",
)

# Sidebar
with st.sidebar:
    st.title("📧 Spam Email Classifier")
    st.markdown(
        """
        This app classifies email text as:
        - **SPAM**: Unwanted or junk email.
        - **HAM**: Legitimate or not spam.
        
        Powered by Natural Language Processing(NLP) is a machine learning technique.
        """
    )
    st.markdown("---")
    st.info("Developer: **Varalaxmi Sadula**")

# Main Section
st.title("SMS Spam Detection System Using NLP")
st.markdown("### Enter the email text below to classify it as Spam or Ham.")

# Input section
email_input = st.text_area("Email Text", height=200, placeholder="Type or paste the email text here...")

# Predict Button
if st.button("🔍 Classify Email"):
    if email_input.strip() == "":
        st.warning("Please enter some text to classify.")
    else:
        # Preprocess the input
        processed_email = preprocess_text(email_input)
        
        # Transform the input using the vectorizer
        transformed_email = vectorizer.transform([processed_email])
        
        # Predict using the model
        prediction = model.predict(transformed_email)[0]
        
        # Display the result
        if prediction == 1:
            st.error("🚨 This email is classified as **SPAM**.")
        else:
            st.success("✅ This email is classified as **HAM** (not spam).")

# Footer with subtle branding
st.markdown(
    """
    <style>
        footer {visibility: hidden;}
        .stApp {background-color: #f9f9f9;}
    </style>
    """,
    unsafe_allow_html=True,
)


