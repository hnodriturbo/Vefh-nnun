

import json
from flask import Flask, render_template, redirect, url_for, session
from navigation import CategoryManager, NavigationManager

app = Flask(__name__)
app.secret_key = 'hnodri'  # Required for session management

 
category_manager = CategoryManager(lambda x: x)



navigation_manager = NavigationManager()





@app.context_processor
def inject_categories():
    categories = category_manager.add_icon_and_route()
    print(categories.items()) 
    return dict(categories=categories)

@app.context_processor
def inject_links():
    links = navigation_manager.get_links()
    return dict(links=links)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    # Simulate login process
    session['user'] = {'email': 'user@example.com'}
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
