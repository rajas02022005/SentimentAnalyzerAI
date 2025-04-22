import streamlit as st
from textblob import TextBlob

# Set page config
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="💬",
    layout="centered"
)

# Title and UI
st.title("💬 AI-Powered Sentiment Analyzer")
st.markdown("Enter text below to analyze its **sentiment** using Natural Language Processing.")

# Input box
user_input = st.text_area("Enter your text here:")

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity == 0:
        return "Neutral 😐"
    else:
        return "Negative 😞"

# Button to analyze
if st.button("Analyze"):
    if user_input.strip() != "":
        result = analyze_sentiment(user_input)
        st.subheader("Sentiment Result:")
        st.success(result)
    else:
        st.warning("Please enter some text to analyze.")
