        
        
        
        
        
        
        
        
        
        
        
      
""" 
@app.route('/<item_type>/<category>')
def show_category(item_type, category):
# Fetch the data according to the item_type and category (e.g., 'movies' and 'popular')
    items = api_manager.get_data(item_type, category)
    title = f"{category.title()} {item_type.title()}" # Constructs title like 'Popular Movies'
    return render_template('category.html', items=items, title=title)  

"""

""" 
@app.route('/<item_type>/<category>')
def show_category(item_type, category_endpoine):
    # Fetch data and render template
    
    items = api_manager.make_request(endpoint)
    title = f"{category.title()} {item_type.title()}"
    return render_template('listings.html', items=items, title=title)
 """
""" 
@app.route('/<item_type>/<category>')
def show_category(item_type, category):
# Fetch the data according to the item_type and category (e.g., 'movies' and 'popular')
    items = api_manager.get_data(item_type, category)
    title = f"{category.title()} {item_type.title()}" # Constructs title like 'Popular Movies'
    return render_template('category.html', items=items, title=title)  

 """

 
        
        
        
        
        
        
        
        
        
        
        
""" 
import os
from flask import Flask, render_template, request, abort, flash, redirect, url_for


from tmdb_manager import Dynamic_API_Data_Manager

from navigation_navbar import create_navigation    


app = Flask(__name__)



secret_key = 'hnodriturbo'



 
 
app = Flask(__name__)

app.secret_key = os.environ.get('flask_secret_key', 'hnodriturbo')

api_manager = Dynamic_API_Data_Manager()
navigation = create_navigation()



@app.route('/')
def home():
    return render_template('index.html', navigation=navigation)

@app.route('/<item_type>/<category>')
def show_listings(item_type, category):
    title = request.args.get('title', 'Default Title')
    category = request.args.get('route', '/default-route')
    # Fetch data from TMDB API based on item_type and category
    items = api_manager.get_data(item_type, category)
    print(items)
    return render_template('listings.html', items=items['results'], title=title, item_type=item_type, category=category, navigation=navigation)


@app.route('/item/<item_type>/<int:item_id>')
def show_item_details(item_type, item_id):
    item = api_manager.get_item_details(item_type, item_id)
    print(item)
    trailer_key = api_manager.get_trailer_key(item_type, item_id)
    return render_template('item_details.html', item_details=item, item_type=item_type, trailer_key=trailer_key)


 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html', navigation=navigation), 404

 """

""" 
@app.route('/<item_type>/<category>')
def show_listings(item_type, category):
    # Accessing titles from the navigation structure
    category_title = navigation['accordion'][item_type]['accordion_buttons'][category]['title']
    if category == 'categories':
        genres = api_manager.get_data(category, item_type)
        return render_template('categories.html', genres=genres, title=f"{category_title}", item_type=item_type, navigation=navigation)
    else:
        items = api_manager.get_data(category, item_type)
        return render_template('listings.html', items=items['results'], title=f"{category_title}", item_type=item_type, navigation=navigation)

"""  







""" 
@app.context_processor
def inject_navigation():
    return dict(navigation=create_navigation())
"""



""" 
api_manager = Dynamic_API_Data_Manager()
navigation = create_navigation()

@app.context_processor
def inject_navigation():
    return dict(navigation=create_navigation())
 
@app.route('/')
def home():
    return render_template('index.html')
    
"""

""" 
if __name__ == 'main':
    app.run(debug=True)


from flask import Flask, render_template, url_for, redirect, request, jsonify, flash
from navigation_navbar import create_navigation
from tmdb_manager import Dynamic_API_Data_Manager


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Instance of TMDB_API_Manager
tmdb_manager = Dynamic_API_Data_Manager()

# Initialize your navigation data
navigation = create_navigation()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<item_type>/<category>')
def show_category_listings(item_type, category):

    # Set if and or contitions before going over ti fetching the items in case of some ridicilous error
    if item_type not in ['Movies', 'TV Shows'] or category not in ['popular', 'top_rated', 'categories']:
        flash("Invalid category or item type specified.")
        return redirect(url_for('home'))
    
    
    # Fetch items based on type and category
    items = tmdb_manager.get_listings(item_type.lower(), category)
    return render_template('listings.html', items=items['results'], title=f"{category.title()} {item_type}")

@app.route('/categories/<item_type>')
def show_categories(item_type):

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
    
"""
    

""" 
@app.route('/listings/<item_type>/<category>')
def show_listings(item_type, category, title):
    data = api_manager.get_data(item_type, category)
    if data and 'results' in data:
        items = data['results']
        title = f"{category.title()} {item_type.title()}" # Þarf að gera eitthvern betri titil en þetta og ná í hann úr navigation_navbar dict en ekki svona
        
        return render_template('listings.html', items=items, title=title, item_type=item_type)
    else:
        abort(404)
""" 
