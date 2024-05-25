

"""
General route to handle listings of movies or TV shows based on category and optionally by genre.
Categories could be 'popular', 'top_rated', or 'genre'.
"""
""" 
@app.route('/listings/<item_type>/<category>', defaults={'genre_id': None})
@app.route('/listings/<item_type>/<category>/<int:genre_id>')
def show_listings(item_type, category, genre_id):

    if category == 'genre' and genre_id is None:
        return render_template('404/404.html'), 404
         
    if category not in ['popular', 'top_rated', 'genre']:
        return render_template('404/404.html'), 404
    
    # Handle the AJAX requests for dynamic loading of content
    is_ajax = 'ajax' in request.path
    page = request.args.get('page', 1, type=int)
    
    # Building the endpoint dynamicly based on the category and item type
    if category == 'genre':
        endpoint = f"discover/{'movie' if item_type == 'movies' else 'tv'}?api_key={api_key}&with_genres={genre_id}"
        genre_name = genre_movies[genre_id]['name'] if item_type == 'movies' else genre_tv_shows[genre_id]['name']
        title = f"{genre_name.replace('_', ' ').title()} {item_type.replace('_', ' ').title()} Listings"
    else:
        endpoint = f"{('movie' if item_type == 'movies' else 'tv')}/{category}?api_key={api_key}"
        title = f"{category.replace('_', ' ').title()} {item_type.replace('_', ' ').title()}"
        
    # Fetch the items from TMDB
    items = fetch_from_tmdb(endpoint, page)
    
    # If ajax, return JSON
    if is_ajax:
        return jsonify(items=items)
    
    # Return the template rendering
    return render_template('listings.html', items=items, title=title, listing_type=item_type, has_more_content=len(items) == 20)

 """


# Route to show listings (movies/TV shows)
@app.route('/listings/<listing_type>')
def show_listings(listing_type):
    """
    Display listings for either popular or top-rated movies or TV shows based on the listing type.
    If the listing type is unknown, show a 404 error page.
    """
    page = request.args.get('page', 1, type=int)

    if listing_type not in listing_endpoints:
        return render_template('404/404.html'), 404
    
    items = fetch_from_tmdb(listing_endpoints[listing_type], page)
    title = listing_type.replace('_', ' ').title()
    return render_template('listings.html', items=items, title=title, listing_type=listing_type, has_more_content=len(items) == 20)

# AJAX route to dynamically load more listings
@app.route('/ajax/listings/<listing_type>')
def ajax_listings(listing_type):
    """Handles AJAX requests for loading more listings."""
    page = request.args.get('page', 1, type=int)
    items = fetch_from_tmdb(listing_endpoints[listing_type], page)
    return jsonify(items=items)



# Route for showing listings by genre
@app.route('/category/listings/<int:genre_id>')
def show_listings_by_genre(genre_id):
    """Shows listings for a specific genre, either for movies or TV shows."""
    listing_type = request.args.get('type', 'movies') # the fallback is to movies if no type is found

    # If else statement in one line
    genre_icons = genre_icons_movies if listing_type == 'movies' else genre_icons_tv_shows

    genre_info = genre_icons.get(genre_id)
    
    # If no genre_info is found return 404
    if not genre_info:
        return render_template('404/404.html')
        
    items = fetch_from_tmdb(f"discover/{listing_type}", params={'with_genres': str(genre_id)})
    
    title = f"{genre_info['name']} {listing_type.title()} Listings"
    
    return render_template('listings.html', items=items, title=title, listing_type=listing_type, has_more_content=len(items) == 20)
"""     
    if item_type == 'movies':
        genre_icons = genre_icons_movies
    else:
        genre_icons = genre_icons_tv_shows
"""   
