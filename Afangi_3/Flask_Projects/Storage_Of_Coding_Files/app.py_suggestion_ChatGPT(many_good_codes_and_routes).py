from flask import Flask, render_template, url_for, redirect, request, jsonify, flash
from navigation_navbar import create_navigation
from tmdb_manager import TMDB_API_Manager
from endpoint_manager import Endpoint_Manager

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Instance of TMDB_API_Manager
tmdb_manager = TMDB_API_Manager()

# Initialize your navigation data
navigation = create_navigation()

@app.route('/')
def home():
    """
    Home page route.
    """
    return render_template('index.html')

@app.route('/<item_type>/<category>')
def show_category_listings(item_type, category):
    """
    General route for displaying listings based on item type and category.
    Category can be 'popular', 'top_rated', or 'categories'.
    """
    if item_type not in ['Movies', 'TV Shows'] or category not in ['popular', 'top_rated', 'categories']:
        flash("Invalid category or item type specified.")
        return redirect(url_for('home'))
    
    # Fetch items based on type and category
    items = tmdb_manager.get_listings(item_type.lower(), category)
    return render_template('listings.html', items=items['results'], title=f"{category.title()} {item_type}")

@app.route('/categories/<item_type>')
def show_categories(item_type):
    """
    Route to display categories for Movies or TV Shows.
    """
    categories = tmdb_manager.list_categories(item_type.lower())
    if not categories:
        flash("Failed to fetch categories.")
        return redirect(url_for('home'))
    return render_template('categories.html', categories=categories, item_type=item_type)

# Error handling for 404 not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
