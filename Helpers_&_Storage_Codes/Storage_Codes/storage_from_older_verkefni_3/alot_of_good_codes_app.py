# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

# Hreiðar Pétursson - Vefhönnun Áfanginn - Skilaverkefni 3 - Apríl 2024

# app.py

from flask import Flask, render_template, request, jsonify, session, flash, redirect, url_for

# Import all the whole files, not just one method or class or function
import pprint # for debugging purposes

# Import * from various files needed for everything to function correctly
from data import *
from navigation_navbar import nav_links, accordion_categories, genre_movies, genre_tv_shows
from managers import TMDB_API_Manager
from endpoint_manager import Endpoint_Manager
from request_formatter import Request_Formatter

""" Define app as the flask __name__, secret key and setup_logging """
app = Flask(__name__)
app.secret_key = 'hnodri'
setup_logging(app)

tmdb_manager = tmdb_manager()



# ----- Automatic injection of nav_links and accordion_categories dicts ---- #
@app.context_processor
def inject_navigation_data():
    """
    Automatically injects navigation links and categories into all templates.
    Returns:
        dict: Contains data to be injected into templates.
    """
    return {'nav_links': nav_links, 'accordion_categories': accordion_categories}



@app.route('/')
def show_home():
    return render_template('index.html')



# The Routes that display listings of either popular, top rated or listings from categories
@app.route('/listings/<item_type>/<category>', defaults={'genre_id': None})
@app.route('/listings/<item_type>/<category>/<int:genre_id>')
def show_listings(item_type, category, genre_id):
    
    if category not in ['popular', 'top_rated', 'genre']:
        flash('Invalid category specified', 'error')
        return redirect(url_for('/'))

    if category == 'genre' and genre_id is None:
        flash('Genre ID must be provided for genre listings', 'error')
        return redirect(url_for('/'))

    # Build endpoint
    endpoint = build_endpoint(item_type, category, genre_id)
    
    # Collect additional params if needed
    params = {'page': request.args.get('page', default=1, type=int)}
    
    # Fetch data
    items = fetch_tmdb_data(endpoint, params)

    if items is None:
        flash('Failed to fetch items from TMDB API.', 'error')
        return redirect(url_for('page_not_found'))

    title = build_title(item_type, category, genre_id)
    
    print(f"Item Type: {item_type}, Category: {category}")
    
    return render_template('listings.html', items=items.get('results', []), title=title, item_type=item_type)

@app.route('/ajax/listings/<item_type>', methods=['GET'])
def ajax_listings(item_type):
    category = request.args.get('category', 'popular') # Default to popular
    page = request.args.get('page', 1, type=int)
    genre_id = request.args.get('genre_id', None) # Optional genre_id
    
    # Build the endpoint dynamicly based on the category and genre
    if category == 'genre' and genre_id:
        endpoint = f"discover/{item_type}?with_genres={genre_id}"
    else:
        endpoint = f"{item_type}/{category}"
        
    # Add the API key and other parameters
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': page
    }
    endpoint = build_endpoint(item_type, category, genre_id)
    # Fetch the items
    data = fetch_tmdb_data(endpoint, params)
    
    if data and 'results' in data:
        return jsonify(data['results'])
    else:
        return jsonify({'error': 'No Data Found'}), 404


@app.route('/categories/<item_type>')
def show_categories(item_type):
    """
    Route to display categories of either movies or TV shows.
    """
    genres = fetch_categories(item_type)
    if genres is None:
        flash('Failed to fetch categories from the TMDB API', 'error')
        return redirect(url_for('page_not_found'))
    genre_type = genre_movies if item_type == 'movies' else genre_tv_shows
    return render_template('categories.html', genres=genres, genre_type=genre_type, item_type=item_type, title=f"{item_type.title()} Categories")







@app.route('/details/<item_type>/<int:item_id>')
def show_details(item_id, item_type):
    """
    Displays detailed information for a specific movie or TV show.
    """
    item_details = get_details(item_id, item_type)
    if item_details is None:
        flash('Failed to fetch item details from the TMDB API', 'error')
        return redirect(url_for('page_not_found'))
    trailer_key = get_trailer_key(item_id, item_type)
    return render_template('item_details.html', item_details=item_details, item_type=item_type, trailer_key=trailer_key)







""" Error handler for handling all error and when on 404 page 10 seconds later you go to index """
@app.errorhandler(404)
def page_not_found(e):
    
    # Get some details about the request that resulted in the error
    path = request.path
    
    method = request.method
    error_message = f"Attempted to access {path} with method {method} but encountered a 404 error."
    
    # Log the error internally as well
    app.logger.error(error_message)
    
    # Pass the error message to the template
    return render_template('404/404.html', error_message=error_message), 404





if __name__ == '__main__':
    app.run(debug=True)
    
    
    



""" 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html'), 404
"""


    
    
    
    
    

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






""" 
@app.route('/')
def homepage():
    carousel_data = []

    for name_of_button, details in accordion_categories.items():
        category_data = {
            'name': name_of_button,  # This seems more appropriate for naming each section
            'items': []
        }

        for link in details['links']:
            if link['endpoint'] == 'show_listings':
                link_item_type = link['args'].get('item_type', 'N/A')
                link_category = link['args'].get('category', 'N/A')
                link_name = link['name']
                endpoint = build_endpoint(link_item_type, category=link_category)
                data = fetch_tmdb_data(endpoint)

                if data:
                    for item in data['results']:  # Assuming 'results' is a list of items
                        # Append each item as a dictionary, directly ensuring 'overview' and other keys exist
                        category_data['items'].append({
                            'title': item.get('title', 'No Title'),
                            'overview': item.get('overview', 'No overview provided.'),
                            'poster_path': item.get('poster_path', ''),
                            'release_date': item.get('release_date', 'No date provided')
                        })

        carousel_data.append(category_data)

    print(carousel_data)  # Use this to inspect the structure
    return render_template('index.html', carousel_data=carousel_data)

"""






""" 
            print(category, item_type)

    
            items = fetch_tmdb_data(build_endpoint(item_type, category))
    
            if items and 'results' in items:
                
                carousel_data.append({
                    'title': link['name'],
                    'items': items['results'][:20],
                    'more_link': url_for(link['endpoint'], **link['args'])
                })
            else:
                flash(f"Failed to fetch items for {link['name']}", category='error')
            all_data[category] = carousel_data
        print(all_data)  # See the structure of all_data before passing to the template

    return render_template('index.html', carousels_data=all_data)

"""