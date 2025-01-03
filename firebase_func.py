import firebase_admin
from firebase_admin import credentials, db
import streamlit as st
import json

json_data = st.secrets["FIREBASE_CRED"]

firebase_credentials = json.loads(json_data)
cred = credentials.Certificate(firebase_credentials)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://otto-8275b-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
# cred = credentials.Certificate("https://github.com/MinThant47/Otto/blob/main/otto-8275b-firebase-adminsdk-1zc00-881e8332a3.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://otto-8275b-default-rtdb.asia-southeast1.firebasedatabase.app/'
# })

# Reference to the database
ref = db.reference('/')

# Data to be saved
data = {
    'response': {
        'res': "Are you Ok?",
        'emotion': "Sad"
    }
}

# Save data to Firebase Realtime Database
def save_data_to_firebase(data):
    ref.set(data)
    print("Data saved successfully!")



