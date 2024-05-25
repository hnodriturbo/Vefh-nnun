from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from config.config import Config
from login.admin import FirebaseAdmin
from login.login_manager import login_bp, login_manager
from login.admin_login import admin_bp
from utils import get_user_role
from navigation import NavigationManager, CategoryManager, UserManager




# Initialize the app and configuration
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY



# Initialize Firebase Admin
firebase_admin = FirebaseAdmin()



# Initialize managers
navigation_manager = NavigationManager()
user_manager = UserManager(firebase_admin.get_db_reference)
category_manager = CategoryManager(firebase_admin.get_db_reference)

# Initialize Flask-Login
login_manager.init_app(app)
login_manager.login_view = 'login.login'




# Register blueprints
app.register_blueprint(login_bp)
app.register_blueprint(admin_bp)





# Context processors
@app.context_processor
def inject_categories():
    categories = category_manager.add_icon_and_route()
    return dict(categories=categories)

@app.context_processor
def inject_links():
    links = navigation_manager.get_links()
    return dict(links=links)



# User class
class User(UserMixin):
    def __init__(self, uid, email):
        self.id = uid
        self.email = email




# Routes
@app.route('/')
def home():
    return render_template('index.html')




@app.route('/user_info')
def user_info():
    if 'user' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login.login'))
    
    user_id = session['user']['localId']
    user_data = firebase_admin.get_db_reference('users').child(user_id).get().val()
    
    return render_template('user_info.html', user=user_data)

@app.route('/category/<subcategory>')
def view_category(subcategory):
    print(f"Fetching posts for subcategory: {subcategory}")
    id_token = session.get('idToken')
    if not id_token:
        flash('Unauthorized access. Please log in.')
        return redirect(url_for('login.login'))

    posts = firebase_admin.get_db_reference('posts').order_by_child("category").equal_to(subcategory).get(token=id_token).val()
    print(f"Posts fetched: {posts}")

    categories = category_manager.add_icon_and_route()
    
    # Find the parent category and the subcategory details
    parent_category = None
    subcategory_details = None
    for category, details in categories.items():
        if subcategory in details['subcategories']:
            parent_category = details
            subcategory_details = details['subcategories'][subcategory]
            break

    if not subcategory_details:
        flash(f"Subcategory '{subcategory}' not found.")
        return redirect(url_for('home'))

    print(f"Subcategory details: {subcategory_details}")
    print(f"Parent category details: {parent_category}")

    return render_template('view_category.html', 
                           subcategory=subcategory_details,
                           parent_category=parent_category,
                           posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = user_manager.register_user(email, password)
            user_id = user['localId']
            firebase_admin.get_db_reference('users').child(user_id).set({"email": email, "role": "user"})
            return redirect(url_for('login.login'))
        except:
            flash('Signup failed', 'danger')
            return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'user' not in session:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        user = session['user']
        post = {
            "title": title,
            "content": content,
            "author_id": user['localId'],
            "author_email": user['email'],
            "category": category
        }
        firebase_admin.get_db_reference('posts').push(post)
        return redirect(url_for('view_category', subcategory=category))
    
    categories = category_manager.get_categories()
    return render_template('create_post.html', categories=categories)

@app.route('/delete_post/<post_id>', methods=['POST'])
def delete_post(post_id):
    user_role = get_user_role()
    post = firebase_admin.get_db_reference('posts').child(post_id).get().val()
    
    if user_role == 'admin' or (post and post['author_id'] == session['user']['localId']):
        firebase_admin.get_db_reference('posts').child(post_id).remove()
        return redirect(url_for('home'))
    
    flash('You do not have permission to delete this post.', 'danger')
    return redirect(url_for('home'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return "Welcome to the Admin Dashboard"

if __name__ == "__main__":
    app.run(debug=True)
