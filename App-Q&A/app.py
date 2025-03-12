from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load Gemini Pro model and get responses

model=genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# Set page configuration
st.set_page_config(page_title="Q&A Demo")

# App Header
st.header("Gemini LLM Application")

# User input field
user_input = st.text_input("Input:", key="input")

# Submit button
submit = st.button("Ask the question")

#When submit is clicked

if submit:
    response=get_gemini_response(user_input)
    st.subheader("The response is")
    st.write(response)