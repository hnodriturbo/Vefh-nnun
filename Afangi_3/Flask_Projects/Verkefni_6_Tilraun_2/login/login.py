# login/login.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, UserMixin, LoginManager
import pyrebase
from firebase_admin import auth, credentials, initialize_app
from config.config import Config

# Initialize Pyrebase
firebase = pyrebase.initialize_app(Config.FIREBASE_CONFIG)
firebase_auth = firebase.auth()

# Initialize Firebase Admin SDK
cred = credentials.Certificate(Config.FIREBASE_ADMIN_SERVICE_ACCOUNT_PATH)
initialize_app(cred)

login_bp = Blueprint('login', __name__)
login_manager = LoginManager()

class User(UserMixin):
    def __init__(self, uid, email):
        self.id = uid
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    try:
        user_record = auth.get_user(user_id)
        return User(user_record.uid, user_record.email)
    except:
        return None

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = firebase_auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']
            user_email = user['email']
            login_user(User(user_id, user_email))
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.home'))
        except:
            flash('Invalid email or password.', 'error')

    return render_template('login/login.html')

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('main.home'))
