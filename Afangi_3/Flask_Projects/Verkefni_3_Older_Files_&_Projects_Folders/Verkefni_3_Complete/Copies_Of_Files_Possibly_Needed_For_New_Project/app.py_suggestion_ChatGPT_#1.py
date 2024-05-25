# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun  Áfanginn ########
#   ######### Skilaverkefni 3 #########
#    ########   Apríl  2024   ########

    #################################
##### ----- Application File ----- #####
    #################################
        ######### app.py #########


from flask import Flask, render_template, request, abort


from managers import Dynamic_API_Data_Manager

from navigation_navbar import create_navigation    


app = Flask(__name__)
app.secret_key = 'hnodriturbo'





api_manager = Dynamic_API_Data_Manager()


navigation = create_navigation()

@app.context_processor
def inject_navigation():
    return dict(navigation=create_navigation())
 
 
@app.route('/')
def home():
    return render_template('index.html')
 


@app.route('/listings/<item_type>/<category>')
def show_listings(item_type, category, title):
    data = api_manager.get_data(item_type, category)
    if data and 'results' in data:
        items = data['results']
        title = f"{category.title()} {item_type.title()}" # Þarf að gera eitthvern betri titil en þetta og ná í hann úr navigation_navbar dict en ekki svona
        
        return render_template('listings.html', items=items, title=title, item_type=item_type)
    else:
        abort(404)
        
        
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html'), 404





if __name__ == 'main':
    app.run(debug=True)


from flask import Flask, render_template, url_for, redirect, request, jsonify, flash
from navigation_navbar import create_navigation
from managers import Dynamic_API_Data_Manager


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Instance of TMDB_API_Manager
tmdb_manager = Dynamic_API_Data_Manager()

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
    
    
    
    
    

