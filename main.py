import streamlit as st
import PyPDF2
import openai
import re
import os
from api import OPENAI_API_KEY

# OpenAI API
# configure in a new script "api.py" in the same folder
# just create an empty file .py and filled like this (with your API KEY):
#
# OPENAI_API_KEY = "your_api_key"
#
#

openai.api_key = OPENAI_API_KEY  # setting the API key

if not OPENAI_API_KEY:
    st.error("⚠️ OpenAI API Key is missing! Set it as an environment variable.")
else:
    openai.api_key = OPENAI_API_KEY

# Title of the app
st.title("📚 AI-Powered Flashcard Generator from PDFs")

# File uploader
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Drag and drop a PDF file", type=["pdf"])

# User input for number of flashcards
num_flashcards = st.sidebar.number_input("Number of Flashcards", min_value=1, max_value=20, value=5)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text[:3000]  # Limit text to 3000 characters to prevent model overload

# Function to generate flashcards using OpenAI
def generate_flashcards(text, num_flashcards):
    prompt = f"""
    Extract {num_flashcards} key concepts from the following text and generate educational flashcards. 
    Format each flashcard as:
    Q: (question); A: (answer);; 

    Text:
    {text}

    (it is important to respect the ";" format between question and answer and ";;" between flashcards)

    Generate exactly {num_flashcards} flashcards:
    """

    # ✅ Correct OpenAI API call (no need for `openai.OpenAI()`)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI that generates educational flashcards."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]  # ✅ Correctly extracting the response


# Process the PDF and generate flashcards
if uploaded_file:
    with st.spinner("Processing PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
    
    if pdf_text:
        with st.spinner("Generating Flashcards..."):
            flashcards = generate_flashcards(pdf_text, num_flashcards)
        
        st.subheader("📌 Generated Flashcards:")
        st.text_area("Flashcards", flashcards, height=300)
