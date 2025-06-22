import streamlit as st
import google.generativeai as genai
from datetime import date

# Streamlit app configuration
st.set_page_config(
    page_title=" Ai Chat Bot", 
    page_icon='🤖', 
    layout='centered', 
    initial_sidebar_state='collapsed'
)

# Use markdown to render the centered header
st.markdown(
    "<h2 style='text-align: center; color:rgb(0, 0, 0); background-color: black; border-radius: 100px;'>🤖 Ai Chat Bot</h2>", 
    unsafe_allow_html=True
)

# Initialize session state with model start chat message
if 'chat' not in st.session_state:
    api_key = "AIzaSyAm3N9L424MQfgHoDlkwnLDpDAbINFZUoE" 
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.history = []

# Initialize session state with today's date
if 'today_date' not in st.session_state:
    st.session_state.today_date = date.today().strftime("%d %B %Y"
    )

# CSS for chat style and background
st.markdown(f"""
<style>
    /* Set the background image for the entire app */
    .stApp {{
        background-image: url("https://www.outsourcing-pharma.com/resizer/v2/MPATO6FVUFIGNIRSUZSXMXDSGQ.jpg?auth=86bbf44afabc36231f86da4b0d275661227693e9f0eeeca9cf51cef90db28281"); /* Medicine/Pharmacy theme */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    .user-message {{
        border-radius: 12px;
        padding: 12px;
        margin: 8px 0;
        max-width: 75%;
        align-self: flex-end;
        background-color:rgb(238, 184, 47); /* Soft blue for user messages */
        color: white;
        font-family: 'Arial', sans-serif;
    }}
    .bot-message {{
        border-radius: 12px;
        align-self: flex-start;
        padding: 12px;
        margin: 8px 0;
        max-width: 75%;
        background-color:rgb(50, 150, 143);
        color: #000;
        font-family: 'Arial', sans-serif;
        border: 1px solid #ddd;
    }}
    .chat-date {{
        text-align: center;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100px;
        background-color: #e0f2f1;
        margin: -15px auto;
        padding: 5px;
        font-family: 'Arial', sans-serif;
    }}
    .message-container {{
        display: flex;
        flex-direction: column;
    }}
    h2 {{
        font-family: 'Arial', sans-serif;
    }}
</style>
""", unsafe_allow_html=True)

# Display the chat history
st.markdown(
    f'<div class="chat-date">{st.session_state.today_date}</div>', 
    unsafe_allow_html=True
)

for message in st.session_state.history:
    st.markdown(
        f'<div class="message-container"><div class="user-message">{message["user"]}</div></div>', 
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="message-container"><div class="bot-message">{message["bot"]}</div></div>', 
        unsafe_allow_html=True
    )

# Function to add message to history
def add_message(user, bot):
    st.session_state.history.append({"user": user, "bot": 'Dipraj, here is my answer :-\n\n' + bot})

# Function to handle question input and response
def handle_question(question):
    try:
        response = st.session_state.chat.send_message(question)
        add_message(question, response.text)
    except Exception as e:
        st.error(f"Error generating response: {e}")

# Input box for user questions
question = st.chat_input("Ask PharmaBot about medicines: ")
if question:
    handle_question(question)
    st.rerun()  # Use st.rerun() instead of st.experimental_rerun()
