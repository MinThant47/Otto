# import streamlit as st
import aisuite as ai

provider_configs = {
            "groq": {
                "api_key": "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",
            }
        }
client = ai.Client(provider_configs=provider_configs)

# groq_api_key = st.secrets["GROQ_API_KEY"]

# # Request a response from the model
# response = client.chat.completions.create(model="groq:llama-3.2-3b-preview", messages=messages)
def ask_question(message, sys_message="You are a helpful agent.",
         model="groq:llama-3.2-3b-preview"):
    # Initialize the AI client for accessing the language model
    client = ai.Client(provider_configs)
    # Construct the messages list for the chat
    messages = [
        {"role": "system", "content": sys_message},
        {"role": "user", "content": "Please give a one line answer to this question:" + message }
    ]

    # Send the messages to the model and get the response
    response = client.chat.completions.create(model=model, messages=messages)

    # Return the content of the model's response
    return response.choices[0].message.content

# def ask_question(message, sys_message="You are a helpful agent.",
#          model="groq:llama-3.2-3b-preview"):

#          client = Groq(
#              api_key=groq_api_key,
#          )
         
#          chat_completion = client.chat.completions.create(
#                 messages = [
#                           {"role": "system", "content": sys_message},
#                           {"role": "user", "content": "Please give a one line answer to this question:" + message }
#                       ],
#              model=model,
#          )
#          response = chat_completion.choices[0].message.content

#     # Return the content of the model's response
#     return response

