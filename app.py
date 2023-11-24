import streamlit as st
import pandas as pd
import time
from chatbot import *

counter = 0

df = pd.read_json('./chatbot-intents.json')
intents = df.intents.values

def main():
    
    st.set_page_config(
        page_title="Jolly Junias - Feel Good Chatbot",
        page_icon="J❤️J",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    st.title("Jolly Junias - Feel Good Chatbot 😊")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = chatbot(prompt,intents)
            
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    

if __name__ == '__main__':
    main()
