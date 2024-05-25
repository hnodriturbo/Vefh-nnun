########################################################
########################################################

from firebase_admin import auth, credentials, initialize_app
from firebase_admin.exceptions import FirebaseError
import pyrebase
from pprint import pprint

########################################################
########################################################


##### ----- Category Manager Class ----- #####

class CategoryManager:
    def __init__(self, db):
        self.db = db

    def get_categories(self):
        try:
            categories = self.db.child("categories").get().val()
            return categories
        except Exception as e:
            print(f"Error fetching categories: {e}")
            return None

    def get_category_posts(self, category, subcategory):
        try:
            posts = self.db.child("categories").child(category).child("subcategories").child(subcategory).child("posts").get().val()
            return posts
        except Exception as e:
            print(f"Error fetching category posts: {e}")
            return None

""" 
class CategoryManager:
    def __init__(self, db):
        # Initialize the CM with the DB and fetching of the categories
        self.db = db
        self.categories = self.fetch_categories()
        print("Debug: CategoryManager initialized with categories")
        
        # Pretty print the categories for debugging purposes
        # self.pretty_print_categories()

    # Mehtod for fetching the categories
    def fetch_categories(self):
        categories = self.db.child("categories").get().val()
        print("Debug: Fetched categories from Firebase")
        # pprint(categories)  # Initial pretty print during fetching for debugging
        return categories

    # Method for pretty printing the categories in the shell
    #def pretty_print_categories(self):
        #print("Debug: Pretty print of categories:")
        # pprint(self.categories)

 """

########################################################
########################################################




##### ----- Navigation Manager Class ----- #####
class NavigationMenuManager:
    def __init__(self):
        self.menu_items = self.fetch_menu_items()
        # print("Debug: NavigationMenuManager initialized with menu items:")
        # pprint(self.menu_items)

    def fetch_menu_items(self):
        # This method should be implemented to fetch the menu items from a database or configuration
        # For now, we'll use a static example
        menu_items = [
            {"title": "Home", "icon": "fa-home", "route": "/"},
            {"title": "About", "icon": "fa-info", "route": "about"},
            {"title": "Contact", "icon": "fa-envelope", "route": "contact"},
        ]
        return menu_items




########################################################
########################################################


##### ----- User Manager Class ----- #####
class UserManager:
    def __init__(self, auth, db):
        self.auth = auth
        self.db = db

    def create_user(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            self.db.child("users").child(user_id).set({"email": email, "role": "user"})
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    def login_user(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except Exception as e:
            print(f"Error logging in user: {e}")
            return None

    def get_user_role(self, user_id):
        try:
            user_role = self.db.child("users").child(user_id).child("role").get().val()
            return user_role
        except Exception as e:
            print(f"Error fetching user role: {e}")
            return None

##### ----- Function for initializing the firebase db and auth ----- #####

def initialize_firebase():
    firebase_config = {
        "apiKey": "AIzaSyB0Oq8M_klVmgg4RN2qMEXtQ7klGwjrsO0",
        "authDomain": "techverse-project.firebaseapp.com",
        "databaseURL": "https://techverse-project-default-rtdb.firebaseio.com",
        "projectId": "techverse-project",
        "storageBucket": "techverse-project.appspot.com",
        "messagingSenderId": "350091993628",
        "appId": "1:350091993628:web:4f170c4e98bf55ba2475d9"
    }
    
    firebase = pyrebase.initialize_app(firebase_config)
    
    db = firebase.database()
    auth = firebase.auth()
    print("Debug: Firebase initialized")
    
    # We return the db and auth here for the db and authentication configurations
    return db, auth
