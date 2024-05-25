




##### ----- Suggestion of two way working app route from ChatGPT of course ----- #####


@app.route('/listings/<item_type>/<category>', defaults={'genre_id': None})
@app.route('/listings/<item_type>/<category>/<int:genre_id>')
def show_listings(item_type, category, genre_id):
    valid_types = ['movies', 'tv']
    valid_categories = ['popular', 'top_rated', 'genre']

    # Validate item type and category
    if item_type not in valid_types or category not in valid_categories:
        flash('Invalid category or item type specified', 'error')
        return redirect(url_for('home'))  # Ensure this points to the actual home route name

    # Get page number from query parameters, default is 1
    page = request.args.get('page', 1, type=int)
    # Fetch items from the TMDB API
    items = tmdb_manager.get_listings(item_type, category, genre_id, page)

    if items is None or 'results' not in items or not items['results']:
        flash('Failed to fetch items from TMDB API.', 'error')
        return redirect(url_for('home'))  # Redirect to home if fetching fails

    # Construct the title based on the category and genre ID
    title = f"{item_type.capitalize()} {category.replace('_', ' ').capitalize()}" # No need for this anymore because title is now in navigation_navbar.py dictionary file.
    if category == 'genre' and genre_id:
        title += f" - Genre ID: {genre_id}"

    return render_template('listings.html', items=items['results'], title=title, item_type=item_type)
