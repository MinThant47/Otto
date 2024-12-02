import streamlit as st
from groq import Groq

groq_api_key = st.secrets["GROQ_API_KEY"]

# # Request a response from the model
# response = client.chat.completions.create(model="groq:llama-3.2-3b-preview", messages=messages)

def ask_question(message, sys_message="You are a helpful agent.",
         model="groq:llama-3.2-3b-preview"):

         client = Groq(
             api_key=groq_api_key,
         )
         
         chat_completion = client.chat.completions.create(
                messages = [
                          {"role": "system", "content": sys_message},
                          {"role": "user", "content": "Please give a one line answer to this question:" + message }
                      ],
             model=model,
         )
         response = chat_completion.choices[0].message.content

    # Return the content of the model's response
    return response

