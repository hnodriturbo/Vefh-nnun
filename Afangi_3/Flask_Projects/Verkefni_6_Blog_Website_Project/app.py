from flask import Flask, render_template, request, redirect, url_for, flash, session
from navigation import NavigationManager, UserManager, CategoryManager
import pyrebase


navigation = NavigationManager()

links = navigation.get_links()
print(links)


app = Flask(__name__)
app.secret_key = 'hnodri'



firebase_config = {
    "apiKey": "AIzaSyACKLkhphco7AcrxbdhcE12K6Fsz1StmFw",
    "authDomain": "cyberpulse-project.firebaseapp.com",
    "databaseURL": "https://cyberpulse-project-default-rtdb.firebaseio.com/",
    "projectId": "cyberpulse-project",
    "storageBucket": "cyberpulse-project.appspot.com",
    "messagingSenderId": "1019060348990",
    "appId": "1:1019060348990:web:1274ad1163098a44a2496f"
}


firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

navigation = NavigationManager()
user_manager = UserManager(auth)
category_manager = CategoryManager(db)




# Function to get user role
def get_user_role():
    if 'user' in session:
        user_id = session['user']['localId']
        user_data = db.child("users").child(user_id).get().val()
        return user_data.get('role', 'user')
    return 'guest'





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = user_manager.login_user(email, password)
            session['user'] = user
            return redirect(url_for('home'))
        except:
            flash('Authentication failed', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')





@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))






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





@app.route('/')
def home():
    links = navigation.get_links()
    return render_template('index.html', links=links)






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
        return redirect(url_for('view_category', category=category))
    
    categories = category_manager.get_categories()
    return render_template('create_post.html', categories=categories)





@app.route('/category/<category>')
def view_category(category):
    posts = db.child("posts").order_by_child("category").equal_to(category).get().val()
    return render_template('view_category.html', category=category, posts=posts)




@app.route('/delete_post/<post_id>', methods=['POST'])
def delete_post(post_id):
    user_role = get_user_role()
    post = db.child("posts").child(post_id).get().val()
    
    if user_role == 'admin' or (post and post['author_id'] == session['user']['localId']):
        db.child("posts").child(post_id).remove()
        return redirect(url_for('home'))
    
    flash('You do not have permission to delete this post.', 'danger')
    return redirect(url_for('home'))







if __name__ == "__main__":
    app.run(debug=True)
