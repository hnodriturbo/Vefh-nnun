from flask import Flask, render_template, request, redirect, url_for, flash, session
from navigation import NavigationManager, UserManager, CategoryManager
from login.admin import FirebaseAdmin
from login.login_manager import LoginManagerWrapper
app = Flask(__name__)


firebase = pyrebase.initialize_app(firebase_config)




auth = firebase.auth()
db = firebase.database()




user_manager = UserManager(auth, db)
navigation_manager = NavigationManager()
category_manager = CategoryManager(db)





from flask import Flask
from config import Config

from login.admin_login import AdminLoginManager

app = Flask(__name__)
app.config.from_object(Config)

login_manager_wrapper = LoginManagerWrapper(app)
admin_login_manager = AdminLoginManager(app)




@app.context_processor
def inject_categories():
    categories = category_manager.add_icon_and_route()
    return dict(categories=categories)

@app.context_processor
def inject_links():
    links = navigation_manager.get_links()
    return dict(links=links)





@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return "Welcome to the Admin Dashboard"



class User(UserMixin):
    def __init__(self, uid, email):
        self.id = uid
        self.email = email






@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user_info')
def user_info():
    if 'user' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))
    
    user_id = session['user']['localId']
    user_data = db.child("users").child(user_id).get().val()
    
    return render_template('user_info.html', user=user_data)






@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = user_manager.login_user(email, password)
            session['user'] = user
            session['user_id'] = user['localId']
            session['role'] = user_manager.get_user_role(user['localId'])
            session['idToken'] = user['idToken']  # Store the ID token in the session
            return redirect(url_for('home'))
        except:
            flash('Login Failed. Check your credentials')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('user_id', None)
    session.pop('role', None)
    session.pop('idToken', None)  # Remove the ID token from the session
    user_manager.logout_user()
    return redirect(url_for('home'))









@app.route('/category/<subcategory>')
def view_category(subcategory):
    print(f"Fetching posts for subcategory: {subcategory}")
    id_token = session.get('idToken')
    if not id_token:
        flash('Unauthorized access. Please log in.')
        return redirect(url_for('login'))

    posts = db.child("posts").order_by_child("category").equal_to(subcategory).get(token=id_token).val()
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
            db.child("users").child(user_id).set({"email": email, "role": "user"})
            return redirect(url_for('login'))
        except:
            flash('Signup failed', 'danger')
            return redirect(url_for('signup'))
    return render_template('signup.html')





@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'user' not in session:
        return redirect(url_for('login'))
    
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
        db.child("posts").push(post)
        return redirect(url_for('view_category', subcategory=category))
    
    categories = category_manager.get_categories()
    return render_template('create_post.html', categories=categories)





@app.route('/delete_post/<post_id>', methods=['POST'])
def delete_post(post_id):
    user_role = get_user_role()
    post = db.child("posts").child(post_id).get().val()
    
    if user_role == 'admin' or (post and post['author_id'] == session['user']['localId']):
        db.child("posts").child(post_id).remove()
        return redirect(url_for('home'))
    
    flash('You do not have permission to delete this post.', 'danger')
    return redirect(url_for('home'))




@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return "Welcome to the Admin Dashboard"








if __name__ == "__main__":
    app.run(debug=True)





#  ------------ ############### *************** ############### -------------
############### --------------_**Storage Codes**_-------------- ###############
#  ------------ ############### *************** ############### -------------


""" 
import os

@app.before_request
def auto_login():
    if 'user' not in session and os.getenv('FLASK_ENV') == 'development':
        try:
            user = auth.sign_in_with_email_and_password("admin@admin.com", "123456")
            session['user'] = user
            session['user_id'] = user['localId']
            session['role'] = user_manager.get_user_role(user['localId'])
            session['idToken'] = user['idToken']  # Store the ID token in the session
            print("Logged in as admin user")

            # Pretty print categories for debugging
            category_manager.pretty_print_categories()

        except Exception as e:
            print(f"Auto login failed: {e}")

auto_login()
 """