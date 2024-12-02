import aisuite as ai
import streamlit as st
# import os
# from dotenv import load_dotenv
# load_dotenv()
# os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

# client = ai.Client()

# messages = [
#     {"role": "system", "content": "You are a helpful agent, who answers with brevity."},
#     {"role": "user", "content": 'Hi'},
# ]

# # Request a response from the model
# response = client.chat.completions.create(model="groq:llama-3.2-3b-preview", messages=messages)

def ask_question(message, sys_message="You are a helpful agent.",
         model="groq:llama-3.2-3b-preview"):
                  
    groq_api_key = st.secrets["GROQ_API_KEY"]
    provider_configs = {
            "groq": {
                "api_key": groq_api_key,
            }
        }              

    client = ai.Client()
    client.configure(provider_configs)
    
    messages = [
        {"role": "system", "content": sys_message},
        {"role": "user", "content": "Please give a one line answer to this question:" + message }
    ]

    # Send the messages to the model and get the response
    response = client.chat.completions.create(model=model, messages=messages)

    # Return the content of the model's response
    return response.choices[0].message.content

