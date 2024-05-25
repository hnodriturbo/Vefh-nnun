# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

# Hreiðar Pétursson - Vefhönnun Áfanginn - Skilaverkefni 3 - Apríl 2024

from flask import Flask, render_template, request, jsonify, session, flash
from data import *
from nav import *



app = Flask(__name__)
app.secret_key = 'hnodri'

api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
base_url = "https://api.themoviedb.org/3"



# Context processor to inject navigation data into all templates
@app.context_processor
def inject_navigation_data():
    """Injects navigation links and accordion categories into all templates."""
    return {'nav_links': nav_links, 'accordion_categories': accordion_categories}




# Home page route
@app.route('/')
def home():
    """Render the home page with necessary data."""
    return render_template('index.html')





# The Routes that display listings of either popular, top rated or listings from categories
@app.route('/listings/<item_type>/<category>', defaults={'genre_id': None})
@app.route('/listings/<item_type>/<category>/<int:genre_id>')
def show_listings(item_type, category, genre_id):
    if category not in ['popular', 'top_rated', 'genre']:
        flash('Invalid category specified', 'error')
        return render_template('404.html'), 404

    if category == 'genre' and genre_id is None:
        flash('Genre ID must be provided for genre listings', 'error')
        return render_template('404.html'), 404

    endpoint = build_endpoint(item_type, category, genre_id)
    items = fetch_from_tmdb(endpoint, request.args.get('page', 1, type=int))
    title = build_title(item_type, category, genre_id)

    return render_template('listings.html', items=items, title=title, listing_type=item_type, has_more_content=len(items) == 20)








# Route to show categories of movies or TV shows
@app.route('/categories/<item_type>')
def show_categories(item_type):
    """Displays categories of either movies or TV shows."""
    genres = fetch_categories(item_type)
    genre_type = genre_movies if item_type == 'movies' else genre_tv_shows
    return render_template('categories.html', genres=genres, genre_type=genre_type, item_type=item_type, title=f"{item_type.title()} Categories")





# Route for showing detailed item information
@app.route('/details/<item_type>/<int:item_id>')
def show_details(item_id, item_type):

    item_details = get_details(item_id, item_type)
    trailer_key = get_trailer_key(item_id, item_type)  # Fetch the trailer key

    if not item_details:
        return render_template('404/404.html'), 404
    
    return render_template('item_details.html', item_details=item_details, item_type=item_type, trailer_key=trailer_key)






# Error handler for 404 not found
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page not found handler."""
    return render_template('404/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

 
"""
 ----- Sample frá síðunni -----
  
import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer b6bbab9eb73d6f04fc09b9405d888fa2"
}

response = requests.get(url, headers=headers)

print(response.text)

 """
 
 
 
"""
How to activate the debug mode for my powershell terminal in vscode
1. Activate the virtual environment venv with command ".\venv\Scripts\Activate.ps1"
2. Set the environment variable of FLASK_DEBUG to 1 with ' $env:FLASK_DEBUG = "1" '
3. Use "flask run" to run the server with debug mode on.
"""