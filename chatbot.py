import joblib
import pandas as pd
import numpy as np




def chatbot(input_text,intents):
    jollyjunias = joblib.load('./jollyjunias.model')
    tag = jollyjunias.predict([input_text])[0]
    for intent in intents:
        if intent['tag'] == tag:
            print(tag)
            response = np.random.choice(intent['responses'])
            return response
