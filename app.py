import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Streamlit app
st.title("📝 Text-to-AI Generator")
st.write("Transform your text into AI-generated content!")

# Sidebar for API key input
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    if api_key:
        st.success("API key set!")
    else:
        st.warning("Please enter your OpenAI API key to use the app.")

# Model selection
model = st.selectbox(
    "Select AI model:",
    ["gpt-3.5-turbo", "gpt-4"],
    index=0
)

# Text input
user_input = st.text_area("Enter your prompt:", height=150)

# Generate button
if st.button("Generate AI Content"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not user_input:
        st.error("Please enter some text to generate content.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            with st.spinner("Generating content..."):
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful AI assistant."},
                        {"role": "user", "content": user_input}
                    ]
                )
                
                generated_text = response.choices[0].message.content
                st.subheader("Generated Content:")
                st.write(generated_text)
                
                # Add download button
                st.download_button(
                    label="Download Generated Text",
                    data=generated_text,
                    file_name="generated_content.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
