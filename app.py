import streamlit as st
import pandas as pd
from chatbot import *

counter = 0

df = pd.read_json('./chatbot-intents.json')
intents = df.intents.values

def main():
    global counter
    st.set_page_config(
        page_title="Jolly Junias - Feel Good Chatbot",
        page_icon="J❤️J",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Jolly Junias - Feel Good Chatbot 😊")
    st.sidebar.image("hhttps://cdn.pixabay.com/photo/2023/02/05/20/01/ai-generated-7770474_960_720.png", use_container_width=True)
    st.write("Don't Wait!!! Just start typing to start the conversation.")

    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if user_input:
        response = chatbot(user_input,intents)
        st.text_area("JJ:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == '__main__':
    main()
