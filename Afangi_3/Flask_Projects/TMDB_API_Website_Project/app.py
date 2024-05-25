            # ########## Hreiðar Pétursson ##########
            #  ######## Vefhönnun  Áfanginn ########
            #   ######### Skilaverkefni 3 #########
            #    ########   Apríl  2024   ########

                #################################
            ##### ----- Application File ----- #####
                #################################
                    ######### app.py #########


# I use this if i want a printout of the accordion buttons dictionaries

""" 
for key, value in nav_system.accordion_buttons.items():
    print(f"key: {key}, value={value}")
"""

# Imports of extensions from flask
from flask import Flask, render_template, request, redirect, url_for, flash, session, render_template_string
# Imports of classes & functions from my own files
from navigation_system import NavigationSystem
# Import the Content_Manager
from tmdb_manager import Content_Manager # Now using Content_Manager instead of Base_API_Manager
# Import jsonify for the ajax listings infinite scrolling
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'hnodri'

# Create the navigation
nav_system = NavigationSystem()

# print(nav_system.nav_buttons)
# print(nav_system.accordion_buttons)
# print(nav_system.genres)


# Create an instance of the Content_Manager
api_manager = Content_Manager()


###################################################################

def validate_item_type(item_type):
    """
    Validate the item type to ensure it is either 'movie' or 'tv'.
    """
    if item_type not in ['movie', 'tv']:
        flash('Invalid item type specified.', 'error')
        return None
    return 'Movies' if item_type == 'movie' else 'TV Shows'

@app.context_processor
def inject_navigation():
    """Inject the navigation data into the templates."""
    return {'nav_system': nav_system}


###################################################################










###################################################################

# ----- Home route uses this method to populate rows of scrollable items ----- #
@app.route('/')
def home():
    data = api_manager.fetch_popular_and_top_rated_for_index_page()
    return render_template('index.html', data=data)


# ----- Routes that use listings.html as the end result ----- #
@app.route('/<item_type>/<app_route>')
@app.route('/<item_type>/<app_route>/<int:genre_id>')
@app.route('/<item_type>/<app_route>/<int:genre_id>/<int:page>')
def show_section(item_type, app_route, genre_id=None, page=1):
    item_key = validate_item_type(item_type)
    if not item_key:
        flash('Invalid item type specified.', 'error')
        return redirect(url_for('home'))

    category_details = nav_system.genres[item_key].get(genre_id) if genre_id else nav_system.accordion_buttons[item_key]['buttons'].get(app_route)

    if not category_details:
        flash('Category not found', 'error')
        return redirect(url_for('home'))

    endpoint = category_details['api_endpoint']
    items = api_manager.fetch_category_items(endpoint) if genre_id else api_manager.fetch_popular_and_top_rated_from_button(endpoint)

    if items:
        return render_template('listings.html', items=items, title=category_details['title'], item_type=item_type, category_details=category_details)
    else:
        flash('Failed to retrieve data.', 'error')
        return redirect(url_for('home'))


from flask import jsonify, make_response

@app.route('/ajax/listings/<item_type>/<app_route>', defaults={'genre_id': None, 'page': 1})
@app.route('/ajax/listings/<item_type>/<app_route>/<int:genre_id>', defaults={'page': 1})
@app.route('/ajax/listings/<item_type>/<app_route>/<int:genre_id>/<int:page>')
def ajax_listings(item_type, app_route, genre_id, page):
    try:
        item_key = validate_item_type(item_type)
        if not item_key:
            return jsonify({'error': 'Invalid item type specified'}), 400

        if genre_id:
            category_details = nav_system.genres[item_key].get(genre_id)
        else:
            category_details = nav_system.accordion_buttons[item_key]['buttons'].get(app_route)

        if not category_details:
            return jsonify({'error': 'Category not found'}), 404

        items = api_manager.fetch_category_items(category_details['api_endpoint'], {'page': page})
        if items:
            html = ''.join([render_template('card.html', item=item) for item in items])
            return jsonify(html=html)
        else:
            return jsonify(html=''), 404


    except Exception as e:
        # Log the error or print it out to the console
        print(f"Server Error: {str(e)}")
        return make_response(f"Internal Server Error: {str(e)}", 500)



# ----- The route for listing the categories ----- #
@app.route('/<item_type>/categories')
def list_categories(item_type):
    """
    Route to display all categories for a specified item type (Movies or TV Shows).
    """
    item_key = validate_item_type(item_type)
    if not item_key:
        return redirect(url_for('home'))

    categories = nav_system.genres[item_key]
    
    print(categories)
    return render_template('categories.html', genres=categories, item_type=item_type)




# ----- The route for showing the item details no matter where you are on the site ----- #
@app.route('/item/<item_type>/<int:item_id>')
def show_item_details(item_type, item_id):
    # Retrieve or set up the breadcrumbs list
    if 'breadcrumbs' not in session:
        session['breadcrumbs'] = []
        session['breadcrumbs'].append(request.path)
    
    
    item = api_manager.get_item_details(item_type, item_id)
    if not item:
        flash('Item details not found.', 'error')
        return redirect(url_for('home'))

    trailer_key = api_manager.get_trailer_key(item_type, item_id)
    return render_template('item_details.html', item_details=item, item_type=item_type, trailer_key=trailer_key)




# ----- Held ég eigi eftir að klára gera þetta ----- # (ætla skila inn verkefninu samt til að klára þetta verkefni af)
@app.route('/about_author')
def about_author():
    return render_template('about_author.html')





# Run the application !!!!
if __name__ == "__main__":
    app.run(debug=True)




""" 
@app.route('/<item_type>/<app_route>')
@app.route('/<item_type>/<app_route>/<int:genre_id>', defaults={'page': None})
@app.route('/<item_type>/<app_route>/<int:genre_id>/<int:page>')
def show_section(item_type, app_route, genre_id=None, page=None):
    
    
    item_key = validate_item_type(item_type)
    if not item_key:
        flash('Invalid item type specified.', 'error')
        return redirect(url_for('home'))
    if genre_id:
        category_details = nav_system.genres[item_key].get(genre_id)
    # Fetch category details from navigation system based on item type and route
    else:
        category_details = nav_system.accordion_buttons[item_key]['buttons'].get(app_route)
    
    print(f'category_details : {category_details}')
    
    
    if not category_details:
        flash('Category not found', 'error')
        return redirect(url_for('home'))

    # Use the Content_Manager to fetch data
    endpoint = category_details['api_endpoint']

    if genre_id:
        items = api_manager.fetch_category_items(endpoint)
        
    else:
        print(endpoint)
        items = api_manager.fetch_popular_and_top_rated_from_button(endpoint)
        
    if items:
        if request.args.get('ajax', False):
            # For AJAX requests, return JSON data directly
            return jsonify(results=items, has_more=(len(items) > 0))
        # For regular requests, render the full page with data
        return render_template('listings.html', items=items, title=category_details['title'], item_type=item_type, category_details=category_details)
    
    else:
        flash('Failed to retrieve data.', 'error')
        return redirect(url_for('home'))
    
    """



"""
Handle navigation for 'popular', 'top_rated', and specific genre listings.
"""
""" 
@app.route('/<item_type>/<app_route>', defaults={'genre_id': None})
@app.route('/<item_type>/<app_route>/<int:genre_id>')
def show_section(item_type, app_route, genre_id):

    item_key = validate_item_type(item_type)
    if not item_key:
        return redirect(url_for('home'))

    category_details = None
    # Fetch category details from navigation system based on item type and route
    category_details = nav_system.genres[item_key].get(genre_id) if genre_id else nav_system.accordion_buttons[item_key]['buttons'].get(app_route)
    if not category_details:
        flash('Category not found', 'error')
        return redirect(url_for('home'))

    is_ajax = request.args.get('ajax', False)  # Check if it's an AJAX request
    data = api_manager.make_request(category_details['api_endpoint'])
    if data:
        if is_ajax:
            # Return JSON response if it's an AJAX request
            return jsonify(data=data.get('results', []))
        # Render page normally if not an AJAX request
        return render_template('listings.html', items=data.get('results', []), title=category_details['title'], item_type=item_type)
    else:
        flash('Failed to retrieve data.', 'error')
        return redirect(url_for('home'))
    
"""


""" 

@app.route('/<item_type>/<app_route>')
def show_section(item_type, app_route):
    print(f"Requested item_type: {item_type}, app_route: {app_route}")
    
    
    # Initialize button_details to None
    button_details = None
    
    # Validate item_type   
    if item_type == 'movie':
        item_key = 'Movies'
    elif item_type == 'tv':
        item_key = 'TV Shows'
    else:
        print(f"Invalid item_type provided")
        flash(f'Invalid item_type', 'error')
        return redirect(url_for('home'))


    if app_route in ['popular', 'top_rated']:
        # Attempt to retrieve the button details directly using `app_route` as the key
        button_details = nav_system.accordion_buttons[item_key]['buttons'].get(app_route)

        # Make sure and print out some details... :)
        if button_details:
            print(f"Button details found: Title: {button_details['title']}, API Endpoint: {button_details['api_endpoint']}")
    else:
        print(f"did not make it through in making button_details to the details dictionary")
        flash('did not make it through in making button_details to the details dictionary', 'error')
        return redirect(url_for('home'))

    # If we have the dictionary of button_details
    if button_details:
        print(button_details['api_endpoint'])
        # Make the API request
        data = api_manager.make_request(button_details['api_endpoint'])
        
        if data is None:
            print('failed to retrieve data from the API.')
            flash('Failed to retrieve data from the API.', 'error')
            return redirect(url_for('home'))
        
        # Render template with the data
        return render_template('listings.html', items=data.get('results', []), title=button_details['title'], item_type=item_type)
        
    else:  # Redirect if no details were found
        flash('No matching section found.', 'error')
        return redirect(url_for('home'))
 """