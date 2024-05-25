# utils.py
from flask import session
import pyrebase
from config.config import Config

# Initialize Pyrebase
firebase = pyrebase.initialize_app(Config.FIREBASE_CONFIG)
db = firebase.database()

def get_user_role():
    if 'user' in session:
        user_id = session['user']['localId']
        user_data = db.child("users").child(user_id).get().val()
        print(f"Found user in session. user_id={user_id} & stored the user data")
        return user_data.get('role', 'user')
    else:
        print("No user found. Returning 'guest'")
        return 'guest'
