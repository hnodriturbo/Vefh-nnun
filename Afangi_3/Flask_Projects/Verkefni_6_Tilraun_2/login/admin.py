# login/admin.py
import firebase_admin
from firebase_admin import credentials, auth, db
from config.config import Config

class FirebaseAdmin:
    def __init__(self):
        self.service_account_path = Config.FIREBASE_ADMIN_SERVICE_ACCOUNT_PATH
        self.database_url = Config.FIREBASE_DATABASE_URL
        self._initialize_app()
        self.auth = auth
        self.db = db
        
        
    def _initialize_app(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(self.service_account_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': self.database_url
            })

    def verify_id_token(self, id_token):
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except Exception as e:
            print(f"Error verifying ID token: {e}")
            return None

    def get_user(self, uid):
        try:
            user = auth.get_user(uid)
            return user
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def create_custom_token(self, uid):
        try:
            custom_token = auth.create_custom_token(uid)
            return custom_token
        except Exception as e:
            print(f"Error creating custom token: {e}")
            return None

    def authenticate_user(self, email, password):
        try:
            user = auth.get_user_by_email(email)
            return user
        except Exception as e:
            print(f'Error authenticating user: {e}')
            return None

    def get_db_reference(self, path):
        return db.reference(path)
