from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from managers import CategoryManager, UserManager, NavigationMenuManager, initialize_firebase
from blueprints.navigation import navigation_bp
from blueprints.post import post_bp
import firebase_admin
from firebase_admin import credentials

app = Flask(__name__)
app.secret_key = 'hnodriturbo'


cred = credentials.Certificate("firebase-admin-sdk.json")
firebase_admin.initialize_app(cred)

# Initialize Firebase and managers
db, auth = initialize_firebase()
category_manager = CategoryManager(db)
user_manager = UserManager(auth, db)
navigation_menu_manager = NavigationMenuManager()

# Register blueprints
app.register_blueprint(navigation_bp, url_prefix='/navigation')
app.register_blueprint(post_bp, url_prefix='/post')


def get_user_role():
    if 'user' in session:
        user_id = session['user']['localId']
        try:
            user_data = db.child("users").child(user_id).get().val()
            if user_data:
                return user_data.get('role', 'user')
            else:
                return 'user'
        except Exception as e:
            print(f"Error fetching user role: {e}")
            return 'guest'
    else:
        return 'guest'
    
    
    
    
@app.before_request
def before_request():
    g.request_context = {}
    g.request_context['categories'] = category_manager.get_categories()
    g.request_context['menu_items'] = navigation_menu_manager.menu_items

    g.user = None
    g.user_role = 'guest'
    
    if 'user' in session:
        user_id = session['user']['localId']
        user_email = session['user']['email']
        user_role = get_user_role()

        g.user = {
            'user_id': user_id,
            'user_email': user_email,
            'user_role': user_role,
            'is_admin': user_role == 'admin'
        }



@app.context_processor
def inject_context():
    return dict(categories=category_manager.get_categories(), menu_items=navigation_menu_manager.menu_items, user_role=g.get('user_role'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Signup failed. Please try again.', 'danger')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Debug: Attempting to log in user with email: {email}")
        user = user_manager.login_user(email, password)
        if user:
            session['user'] = user
            session['user_role'] = get_user_role()
            session['user_id'] = user['localId']
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    user_manager.logout_user(session)
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))

@app.route('/')
def home():
    posts_by_category = {}

    for category, details in g.request_context['categories'].items():
        subcategories = details.get('subcategories', {})
        for subcategory, subdetails in subcategories.items():
            posts_snapshot = db.child("posts").order_by_child("category").equal_to(subdetails['title']).limit_to_first(2).get()
            posts = posts_snapshot.val() if posts_snapshot.val() else {}
            posts_by_category[subdetails['title']] = posts

    return render_template('index.html', posts_by_category=posts_by_category)


if __name__ == '__main__':
    app.run(debug=True)
