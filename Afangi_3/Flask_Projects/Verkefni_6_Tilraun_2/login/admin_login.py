# login/admin_login.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, UserMixin, LoginManager
from login.admin import FirebaseAdmin
from config.config import Config
import pyrebase

firebase_admin = FirebaseAdmin()

firebase = pyrebase.initialize_app(Config.FIREBASE_CONFIG)
firebase_auth = firebase.auth()

admin_bp = Blueprint('admin', __name__)
login_manager = LoginManager()

class User(UserMixin):
    def __init__(self, uid, email):
        self.id = uid
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    try:
        user_record = firebase_admin.get_user(user_id)
        return User(user_record.uid, user_record.email)
    except:
        return None

@admin_bp.route('/admin/login', methods=['GET', 'POST'])
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
            return redirect(url_for('admin_dashboard'))
        except:
            flash('Invalid email or password.', 'error')

    return render_template('login/admin_login.html')

@admin_bp.route('/admin/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('admin.login'))