# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

import requests
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from data import * 
from nav import *

app = Flask(__name__)
app.secret_key = 'hnodri'


@app.context_processor
def inject_accordion_categories():
    accordion_categories = {
        'Movies': {
            'id': 'movies',
            'links': [
                {'name': 'Popular Movies', 'endpoint': 'show_listings', 'args': {'listing_type': 'popular_movies'}},
                {'name': 'Top Movies', 'endpoint': 'show_listings', 'args': {'listing_type': 'top_movies'}},
                {'name': 'Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'movies'}},
            ]
        },
        'TV Shows': {
            'id': 'tv_shows',
            'links': [
                {'name': 'Popular TV Shows', 'endpoint': 'show_listings', 'args': {'listing_type': 'popular_tv_shows'}},
                {'name': 'Top TV Shows', 'endpoint': 'show_listings', 'args': {'listing_type': 'top_tv_shows'}},
                {'name': 'Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'tv_shows'}},
            ]
        }
    }
    return dict(accordion_categories=accordion_categories)



@app.route('/')
def home():
    # Update breadcrumbs
    update_breadcrumbs(url_for('home'), 'Home')
    return render_template('index.html', nav_links=nav_links, accordion_categories=accordion_categories)











@app.route('/listings/<listing_type>')
def show_listings(listing_type):
    """
    Display listings for either popular or top-rated movies or TV shows.
    """
    page = request.args.get('page', 1, type=int)
    
    listing_endpoints = {
        'popular_movies': 'movie/popular',
        'top_movies': 'movie/top_rated',
        'popular_tv_shows': 'tv/popular',
        'top_tv_shows': 'tv/top_rated'
    }
    
    if listing_type not in listing_endpoints:
        # If listing is unknown show 404
        return render_template('404/404.html'), 404
    
    endpoint = listing_endpoints[listing_type]
    items = fetch_from_tmdb(endpoint, page=page)
    title = listing_type.replace('_', ' ').title()
    
    # Update breadcrumbs 
    update_breadcrumbs(url_for('show_listings', listing_type=listing_type), title)
    
    # Determine if there is more content
    has_more_content = len(items) == 20

    return render_template('listings.html', items=items, title=title, nav_links=nav_links, accordion_categories=accordion_categories, listing_type=listing_type, has_more_content=has_more_content)

@app.route('/ajax/listings/<listing_type>')
def ajax_listings(listing_type):
    """
    Serve AJAX requests for more listings of a specific type.
    """
    page = request.args.get('page', default=1, type=int)
    
    listing_endpoints = {
        'popular_movies': 'movie/popular',
        'top_movies': 'movie/top_rated',
        'popular_tv_shows': 'tv/popular',
        'top_tv_shows': 'tv/top_rated'
    }

    if listing_type not in listing_endpoints:
        return jsonify({'error': 'Listing type not found'}), 404
    
    endpoint = listing_endpoints[listing_type]
    items = fetch_from_tmdb(endpoint, page=page)
    
    # Here, instead of rendering a template, we return the items as JSON.
    return jsonify(items=items)





@app.route('/categories/<item_type>')
def show_categories(item_type):
    # Capitalize and format the title dynamically based on the item_type
    title = f"{item_type.replace('_', ' ').title()} Categories"

    genres = fetch_categories(item_type)
    
    # Choose dictionary of icons for categories in nav.py 
    if item_type == 'movies':
        genre_icons = genre_icons_movies
    else:
        genre_icons = genre_icons_tv_shows
    # Possible to do the same in one line.... 
    # genre_icons = genre_icons_movies if item_type == 'movies' else genre_icons_tv_shows

    print(json.dumps(genres, indent=4)) 
    if not genres:  # If no genres were found, you might want to handle it appropriately
        return render_template('404/404.html'), 404

    return render_template('categories.html', genres=genres, genre_icons=genre_icons, title=title, nav_links=nav_links, accordion_categories=accordion_categories)


@app.route('/category/listings/<int:genre_id>')
def show_listings_by_genre(genre_id):
    item_type = request.args.get('type', 'movies')  # Gets the item type from query parameter, default is 'movies'
    
    endpoint = f"discover/{item_type}"
    params = {
        'with_genres': genre_id,
        'page': request.args.get('page', 1, type=int)
    }
    
    items = fetch_from_tmdb(endpoint, params=params)
    genre_name = next((info['name'] for id, info in (genre_icons_movies if item_type == 'movies' else genre_icons_tv_shows).items() if id == genre_id), "Genre")
    title = f"{genre_name} {item_type.title()} Listings"

    return render_template('listings.html', items=items, title=title, nav_links=nav_links, accordion_categories=accordion_categories, has_more_content=len(items) == 20)





# The Route for opening details of any item
@app.route('/details/<item_type>/<int:item_id>')
def show_details(item_id, item_type):
    """
    Fetch and display details for a movie or TV show.
    """
    details = get_details(item_id, item_type)
    if not details:
        return render_template('404/404.html', nav_links=nav_links, accordion_categories=accordion_categories), 404
    
    title = details.get('title', details.get('name', 'Details'))
    # Update breadcrumbs
    update_breadcrumbs(request.path, title)
    return render_template('item_details.html', details=details, item_type=item_type, nav_links=nav_links, accordion_categories=accordion_categories)










@app.route('/random')
def show_random():
    """
    Placeholder for showing a random movie or TV show.
    """
    # Placeholder implementation
    # This will be implemented in the future
    pass











@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html', nav_links=nav_links, accordion_categories=accordion_categories), 404













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