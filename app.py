# app.py
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analyzer AI", page_icon="💬")
st.title("💬 AI-Powered Sentiment Analyzer")
st.write("Enter a sentence below and let the AI tell you the sentiment!")

# Load model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

analyzer = load_model()

# Input from user
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            result = analyzer(user_input)[0]
            st.success(f"**Sentiment:** {result['label']}")
            st.info(f"**Confidence:** {round(result['score'] * 100, 2)}%")
