from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image  # Missing import

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image):
    response = model.generate_content([input_text, image])  # Pass both input text and image
    return response.text

# Set page configuration
st.set_page_config(page_title="Gemini Image Demo")

# App Header
st.header("Gemini Application")

# User input field
user_input = st.text_input("Input:", key="input")

# Image uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

image = None
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image.", use_column_width=True)  # Fixed typo

# Submit button
submit = st.button("Tell me about the image")

if submit:
    if uploaded_image is not None:
        response = get_gemini_response(user_input, image)
        st.write("Response:", response)
    else:
        st.warning("Please upload an image before submitting.")
