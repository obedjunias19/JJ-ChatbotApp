import streamlit as st
import pandas as pd
import time
from chatbot import *

counter = 0

df = pd.read_json('./chatbot-intents.json')
intents = df.intents.values

def main():
    global counter
    assistant_response = ""
    
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
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        assistant_response = chatbot(prompt,intents)
        print(assistant_response)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        if assistant_response.lower() in ['goodbye', 'bye']:
            assistant_response = "Thank you for chatting with me. Have a great day!"
        
        # # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
   
    # st.sidebar.image("hhttps://cdn.pixabay.com/photo/2023/02/05/20/01/ai-generated-7770474_960_720.png", use_container_width=True)
    # st.write("Don't Wait!!! Just start typing to start the conversation.")

    # counter += 1
    # user_input = st.text_input("You:", key=f"user_input_{counter}")

    # if user_input:
    #     response = chatbot(user_input,intents)
    #     st.text_area("JJ:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

    #     if response.lower() in ['goodbye', 'bye']:
    #         st.write("Thank you for chatting with me. Have a great day!")
    #         st.stop()

if __name__ == '__main__':
    main()
