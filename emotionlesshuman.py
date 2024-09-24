import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBySKECQi_vmg2Z36rbic65bf3fK3zl4EM"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize chat history in session state
if 'history' not in st.session_state:
    st.session_state['history'] = []

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

# Add custom CSS for styling with background image
st.markdown("""
<style>
    body {
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfT36KghC2WzoMs2HTYF6kafuQwTwJzVEueQ&s');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        font-family: 'Helvetica Neue', sans-serif;
        color: #ffffff; /* Change text color for better visibility */
    }
    .stTextInput input {
        border: 2px solid #534B62;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1em;
        transition: border-color 0.3s;
    }
    .stTextInput input:hover {
        border-color: #D0BCD5;
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
        background-color: #D3FFE9;
    }
    .chat-container {
        background-color: rgba(9, 9, 9, 0.8); /* Semi-transparent background for better readability */
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .user-message {
        color: #4B5043;
    }
    .bot-message {
        color: #9BC4BC;
    }
</style>
""", unsafe_allow_html=True)

# User input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type something...", max_chars=2000)
    submit_button = st.form_submit_button("Send")
    
    if submit_button and user_input:
        response = get_response(user_input)
        
        # Update chat history
        st.session_state['history'].append({"role": "user", "content": user_input})
        st.session_state['history'].append({"role": "bot", "content": response})

        # Clear the input field
        user_input = ""

# Chat display box
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

# Display the latest message on top
if st.session_state['history']:
    last_message_index = len(st.session_state['history']) - 1
    st.markdown(f"<div class='chat-container bot-message'>Emotionless Human: {st.session_state['history'][last_message_index]['content']}</div>", unsafe_allow_html=True)
    
    # Display the rest of the messages
    for message in st.session_state['history'][:-1]:  # Exclude the last message already displayed
        if message['role'] == 'user':
            st.markdown(f"<div class='chat-container user-message'>You: {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-container bot-message'>Emotionless Human: {message['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.write("_________________________________________________________________________________________________________________")
st.write("Created by Emotional Human")
