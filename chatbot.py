from groq import Groq
import os

GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
client = Groq()

def ask_question(message):
    chat_completion = client.chat.completions.create(

        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please give a one line answer to this question:" + message,
            }
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )

    # Print the completion returned by the LLM.
    return chat_completion.choices[0].message.content
