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
""" 
class CategoryManager:
    def __init__(self, db_reference_function):
        self.db = db_reference_function('')

    def get_categories(self):
        categories = self.db.child("categories").get().val()
        return categories if categories else {}

    def add_icon_and_route(self):
        categories = self.get_categories()
        updated_categories = {}

        for category, details in categories.items():
            updated_subcategories = {
                subcategory: {
                    "title": subdetails["title"],
                    "icon": subdetails["icon"],
                    "route": subdetails["route"]
                }
                for subcategory, subdetails in details.get("subcategories", {}).items()
            }

            updated_categories[category] = {
                "title": details["title"],
                "icon": details["icon"],
                "route": details["route"],
                "subcategories": updated_subcategories
            }

        return updated_categories
 """

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


""" 
class CategoryManager:
    def __init__(self, db):
        self.db = db

    def create_category(self, head_category, details):
        self.db.child("categories").child(head_category).set(details)

    def get_categories(self):
        categories = self.db.child("categories").get().val()
        return categories if categories else {}

    def initialize_categories(self):
        
        categories = {
            
            "Technology": {
                "title": "Technology",
                "icon": "fa-microchip",
                "route": "/technology",
                
                "subcategories": {
                    
                    "Programming": {
                        "title": "Programming",
                        "icon": "fa-code",
                        "route": "/technology/programming"
                    },
                    
                    "AI": {
                        "title": "Artificial Intelligence",
                        "icon": "fa-robot",
                        "route": "/technology/ai"
                    },
                    
                    "Cybersecurity": {
                        "title": "Cybersecurity",
                        "icon": "fa-shield-alt",
                        "route": "/technology/cybersecurity"
                    },
                    
                    "Gadgets": {
                        "title": "Gadgets",
                        "icon": "fa-mobile-alt",
                        "route": "/technology/gadgets"
                    },
                    
                    "Software Development": {
                        "title": "Software Development",
                        "icon": "fa-laptop-code",
                        "route": "/technology/software-development"
                    }
                    
                }
                
            },
            
            
            "Emerging Technologies": {
                "title": "Emerging Technologies",
                "icon": "fa-rocket",
                "route": "/emerging-technologies",
                
                "subcategories": {
                    
                    "Blockchain": {
                        "title": "Blockchain",
                        "icon": "fa-link",
                        "route": "/emerging-technologies/blockchain"
                    },
                    
                    "Quantum Computing": {
                        "title": "Quantum Computing",
                        "icon": "fa-atom",
                        "route": "/emerging-technologies/quantum-computing"
                    },
                    
                    "IoT": {
                        "title": "Internet of Things",
                        "icon": "fa-wifi",
                        "route": "/emerging-technologies/iot"
                    },
                    
                    "5G": {
                        "title": "5G Technology",
                        "icon": "fa-signal",
                        "route": "/emerging-technologies/5g"
                    },
                    
                    "AR/VR": {
                        "title": "AR/VR",
                        "icon": "fa-vr-cardboard",
                        "route": "/emerging-technologies/ar-vr"
                    }
                    
                }
                
            },
            
            "Tech Industry Trends": {
                "title": "Tech Industry Trends",
                "icon": "fa-chart-line",
                "route": "/tech-industry-trends",
                
                "subcategories": {
                    
                    "Startups": {
                        "title": "Startups",
                        "icon": "fa-lightbulb",
                        "route": "/tech-industry-trends/startups"
                    },
                    
                    "Tech Giants": {
                        "title": "Tech Giants",
                        "icon": "fa-building",
                        "route": "/tech-industry-trends/tech-giants"
                    },
                    
                    "Investment": {
                        "title": "Investment",
                        "icon": "fa-chart-bar",
                        "route": "/tech-industry-trends/investment"
                    },
                    
                    "Mergers & Acquisitions": {
                        "title": "Mergers & Acquisitions",
                        "icon": "fa-handshake",
                        "route": "/tech-industry-trends/mergers-acquisitions"
                    },
                    
                    "Market Analysis": {
                        "title": "Market Analysis",
                        "icon": "fa-search-dollar",
                        "route": "/tech-industry-trends/market-analysis"
                    }
                    
                }
                
            }
            
        }
        
        for head_category, details in categories.items():
            self.create_category(head_category, details)
 """
""" 
class CategoryManager:
    def __init__(self, db):
        self.db = db

    def create_category(self, head_category, subcategories, icon):
        category = {"subcategories": subcategories, "icon": icon}
        self.db.child("categories").child(head_category).set(category)

    def get_categories(self):
        categories = self.db.child("categories").get().val()
        return categories if categories else {}
        
    def initialize_categories(self):
        categories = {
            "Technology": {"subcategories": ["Programming", "AI", "Cybersecurity", "Gadgets", "Software Development"], "icon": "fa-microchip"},
            "Emerging Technologies": {"subcategories": ["Blockchain", "Quantum Computing", "IoT", "5G", "AR/VR"], "icon": "fa-rocket"},
            "Tech Industry Trends": {"subcategories": ["Startups", "Tech Giants", "Investment", "Mergers & Acquisitions", "Market Analysis"], "icon": "fa-chart-line"}
        }
        for head_category, details in categories.items():
            self.create_category(head_category, details["subcategories"], details["icon"])

 """
""" 
class CategoryManager:
    def __init__(self, db, auth):
        self.db = db
        self.auth = auth

    def create_category(self, head_category, subcategories):
        category = {"subcategories": subcategories}
        user = self.auth.current_user
        if user:
            self.db.child("categories").child(head_category).set(category, user['idToken'])
        else:
            raise Exception("User not authenticated")

    def get_categories(self):
        user = self.auth.current_user
        if user:
            categories = self.db.child("categories").get(user['idToken']).val()
            return categories if categories else {}
        else:
            raise Exception("User not authenticated")
        
        
    def initialize_categories(self):
        categories = {
            "Technology": ["Programming", "AI", "Cybersecurity", "Gadgets", "Software Development"],
            "Emerging Technologies": ["Blockchain", "Quantum Computing", "IoT", "5G", "AR/VR"],
            "Tech Industry Trends": ["Startups", "Tech Giants", "Investment", "Mergers & Acquisitions", "Market Analysis"]
        }
        for head_category, subcategories in categories.items():
            self.create_category(head_category, subcategories)

    def initialize_sample_posts(self):
        sample_posts = [
            {"title": "Introduction to AI", "content": "Content about AI...", "author_id": "sampleUser", "author_email": "user@example.com", "category": "Technology"},
            {"title": "Blockchain Basics", "content": "Content about Blockchain...", "author_id": "sampleUser", "author_email": "user@example.com", "category": "Emerging Technologies"}
        ]
        user = self.auth.current_user
        if user:
            for post in sample_posts:
                self.db.child("posts").push(post, user['idToken'])
        else:
            raise Exception("User not authenticated")

 """




""" 
class CategoryManager:
    def __init__(self, db):
        self.db = db

    def create_category(self, head_category, subcategories):
        category = {"subcategories": subcategories}
        self.db.child("categories").child(head_category).set(category)
        
    def get_categories(self):
        categories = self.db.child("categories").get().val()
        return categories if categories else {}

    def initialize_categories(self):
        categories = {
            "Technology": ["Programming", "AI", "Cybersecurity", "Gadgets", "Software Development"],
            "Emerging Technologies": ["Blockchain", "Quantum Computing", "IoT", "5G", "AR/VR"],
            "Tech Industry Trends": ["Startups", "Tech Giants", "Investment", "Mergers & Acquisitions", "Market Analysis"]
        }
        for head_category, subcategories in categories.items():
            self.create_category(head_category, subcategories)
    
    def initialize_sample_posts(self):
        sample_posts = [
            {"title": "Introduction to AI", "content": "Content about AI...", "author_id": "sampleUser", "author_email": "user@example.com", "category": "Technology"},
            {"title": "Blockchain Basics", "content": "Content about Blockchain...", "author_id": "sampleUser", "author_email": "user@example.com", "category": "Emerging Technologies"}
        ]
        for post in sample_posts:
            self.db.child("posts").push(post)

"""




""" 
#from Cryptodome.PublicKey import RSA
#from Cryptodome.Util.asn1 import DerSequence, DerInteger, DerBitString
#from Cryptodome.Util.number import long_to_bytes, bytes_to_long

"""

""" 
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
"""
