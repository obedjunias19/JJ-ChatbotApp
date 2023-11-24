import joblib
import pandas as pd




def chatbot(input_text,intents):
    jollyjunias = joblib.load('./jollyjunias.model')
    tag = jollyjunias.predict([input_text])[0]
    for intent in intents:
        if intent['tag'] == tag:
            print(tag)
            response = random.choice(intent['responses'])
            return response