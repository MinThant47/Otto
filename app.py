import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
from chatbot import ask_question
from firebase_func import save_data_to_firebase

st.title("Speech-to-Text Testing")
response = ""

# Record audio
st.header("Record Your Voice")
audio_record = audio_recorder()

audio_file_path = "audio_input.wav"

if audio_record:
    st.success("Recording complete!")
    with open(audio_file_path, "wb") as f:
        f.write(audio_record)
    st.audio("audio_input.wav", format="audio/wav")

recognizer = sr.Recognizer()

if audio_record:
    with sr.AudioFile("audio_input.wav") as source:
        audio_data = recognizer.record(source)

        try:
            # Recognize the speech
            text = recognizer.recognize_google(audio_data)
            st.write("Recognized speech: ", text)
            response = ask_question(text)
            save_data_to_firebase(
                {'response': {
                    'res': response,
                    'emotion': "Sad"
                }})
            st.write("Response from the bot: ", response)
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")
