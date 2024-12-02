import firebase_admin
from firebase_admin import credentials, db

firebase_credentials = json.loads(os.environ["FIREBASE_CREDENTIALS"])
cred = credentials.Certificate(firebase_credentials)

# cred = credentials.Certificate("https://github.com/MinThant47/Otto/blob/main/otto-8275b-firebase-adminsdk-1zc00-881e8332a3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://otto-8275b-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

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



