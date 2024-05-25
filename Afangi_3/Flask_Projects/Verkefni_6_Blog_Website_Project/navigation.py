from flask import Flask, render_template
import pyrebase
from Cryptodome.PublicKey import RSA
from Cryptodome.Util.asn1 import DerSequence, DerInteger, DerBitString
from Cryptodome.Util.number import long_to_bytes, bytes_to_long

class NavigationManager:
    def __init__(self):
        self.links = [
            {"name": "Home", "url": "/"},
            {"name": "Blog", "url": "/blog"},
            {"name": "Admin", "url": "/admin"},
            # More links can be added here
        ]

    def get_links(self):
        return self.links

class UserManager:
    def __init__(self, firebase_auth):
        self.auth = firebase_auth

    def register_user(self, email, password):
        return self.auth.create_user_with_email_and_password(email, password)

    def login_user(self, email, password):
        return self.auth.sign_in_with_email_and_password(email, password)

    def logout_user(self):
        self.auth.current_user = None

class CategoryManager:
    def __init__(self, firebase_db):
        self.db = firebase_db

    def create_category(self, head_category, subcategories):
        category = {"subcategories": subcategories}
        self.db.child("categories").child(head_category).set(category)
        
    def get_categories(self):
        return self.db.child("categories").get().val()
    
    def initialize_categories(self):
        categories = {
            "Technology": ["Programming", "AI", "Cybersecurity", "Gadgets", "Software Development"],
            "Emerging Technologies": ["Blockchain", "Quantum Computing", "IoT", "5G", "AR/VR"],
            "Tech Industry Trends": ["Startups", "Tech Giants", "Investment", "Mergers & Acquisitions", "Market Analysis"]
        }
        for head_category, subcategories in categories.items():
            self.create_category(head_category, subcategories)
