import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBySKECQi_vmg2Z36rbic65bf3fK3zl4EM"
genai.configure(api_key=GOOGLE_API_KEY)

# Model Initiate
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get chatbot response
def get_response(user_input):
    # Generate response using Google Generative AI
    response = model.generate_content(user_input)
    return response.text

st.set_page_config(page_title="EMOTIONLESS HUMAN", layout="centered")
st.title("Emotionless Human 🤖")
st.write("Powered by Google Generative AI")

# Add custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f7f9fc;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stTextInput input {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1em;
        transition: border-color 0.3s;
    }
    .stTextInput input:hover {
        border-color: #45a049;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 1.2em;
        border: none;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .chat-container {
        background-color: #fff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .user-message {
        color: #4CAF50;
    }
    .bot-message {
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# User input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type something...", max_chars=2000)
    submit_button = st.form_submit_button("Send")
    
    if submit_button:
        if user_input:
            response = get_response(user_input)
            st.write(f"<div class='chat-container user-message'>You: {user_input}</div>", unsafe_allow_html=True)
            st.write(f"<div class='chat-container bot-message'>Emotionless Human: {response}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a prompt.")
            
st.write("_________________________________________________________________________________________________________________")
st.write("Created by Emotional Human")
