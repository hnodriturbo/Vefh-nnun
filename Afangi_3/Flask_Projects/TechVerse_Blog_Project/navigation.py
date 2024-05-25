# navigation.py
from flask import Flask, render_template, session, url_for
import pyrebase
import json
from firebase_admin import auth






class NavigationManager:
    def __init__(self):
        self.links = [
            {"name": "Home", "url": "/", "icon": "fa-home"},
            {"name": "Blog", "url": "/blog", "icon": "fa-blog"},
        ]

    def get_links(self):
        if 'user' in session and session.get('role') == 'admin':
            self.links.append({"name": "Admin", "url": "/admin", "icon": "fa-user-shield"})
        return self.links





class CategoryManager:
    def __init__(self, db_reference_function):
        self.db = db_reference_function('')

    def get_categories(self):
        with open('storage/categories_and_more.json', 'r') as file:
            data = json.load(file)
        categories = data.get('categories', {})
        return categories if categories else {}

    def add_icon_and_route(self):
        categories = self.get_categories()
        updated_categories = {}
        for key, value in categories.items():
            updated_categories[key] = {
                'title': value['title'],
                'icon': value['icon'],
                'route': value['route'],
                'subcategories': value['subcategories']
            }
        return updated_categories






class UserManager:
    def __init__(self, db_reference_function):
        self.db = db_reference_function('')
        self.auth = auth

    def register_user(self, email, password, role='user'):
        user = self.auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']
        self.db.child("users").child(user_id).set({
            "email": email,
            "role": role
        })
        return user

    def login_user(self, email, password):
        return self.auth.sign_in_with_email_and_password(email, password)

    def get_user_role(self, user_id):
        user = self.db.child("users").child(user_id).get().val()
        return user.get("role", "user") if user else "user"

    def logout_user(self):
        self.auth.current_user = None

