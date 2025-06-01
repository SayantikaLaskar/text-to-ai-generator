import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up the Streamlit app
st.title("🚀 Text-to-AI Generator (Gemini Flash)")
st.write("Powered by Google's Gemini 1.5 Flash API")

# Sidebar for API key input
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your Google AI API key:", type="password")
    if api_key:
        st.success("API key set!")
    else:
        st.warning("Please enter your Google AI API key.")

# Model selection (Gemini Flash is the default)
model_name = st.selectbox(
    "Select model:",
    ["gemini-1.5-flash", "gemini-1.5-pro"],
    index=0
)

# Text input
user_input = st.text_area("Enter your prompt:", height=150)

# Generate button
if st.button("Generate AI Content"):
    if not api_key:
        st.error("Please enter your Google AI API key in the sidebar.")
    elif not user_input:
        st.error("Please enter some text to generate content.")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            
            with st.spinner("Generating content..."):
                response = model.generate_content(user_input)
                
                generated_text = response.text
                st.subheader("Generated Content:")
                st.write(generated_text)
                
                # Add download button
                st.download_button(
                    label="Download Generated Text",
                    data=generated_text,
                    file_name="gemini_generated_content.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
