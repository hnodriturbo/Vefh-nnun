                # ########## Hreiðar Pétursson ##########
                #  ######## Vefhönnun  Áfanginn ########
                #   ######### Skilaverkefni 3 #########
                #    ########   Apríl  2024   ########







""" 

This is a way to make my index page work because it will require carousels for each part of the child sites

@app.route('/')
def home():
    popular_movies = tmdb_api_manager.get_listings('movie', 'popular')
    top_rated_movies = tmdb_api_manager.get_listings('movie', 'top_rated')
    categories = tmdb_api_manager.list_categories('movie')  # Assuming this returns all categories
    return render_template('index.html', popular_movies=popular_movies, top_rated_movies=top_rated_movies, categories=categories)


"""


            ##################################################################
##### ---------------- App Route Suggestion Code Im Interested In ---------------- #####
            ##################################################################
            
# This is a app route I am VERY interested in to integrate into my project.

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
    title = f"{item_type.capitalize()} {category.replace('_', ' ').capitalize()}"
    if category == 'genre' and genre_id:
        title += f" - Genre ID: {genre_id}"

    return render_template('listings.html', items=items['results'], title=title, item_type=item_type)


    
    
    
    
    
    
    
    
    
    
            ##################################################################
##### ---------------- This code below is from tmdb_manager.py file ---------------- #####
            ##################################################################
                   
"""     
    def fetch_data(self, endpoint, params=None):
        default_params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'page': 1
        }

        # If params provided, update default_params with these so custom params can override defaults
        if params:
            default_params.update(params)

        # Construct the full URL for the API request
        url = f"{self.base_url}/{endpoint}"

        # Get the data into response with requests.get or raise for status error
        response = requests.get(url, params=params)
        # This will raise an error for non-200 responses (error response)
        response.raise_for_status()

        # Put the response in json format and into data
        return response.json()
"""
    
    
    
    
"""Fetch data from TMDB API with specified endpoint and additional parameters."""
"""         
# Initialize default parameters or use the provided dictionary
if params is None:
    params = {}
    
# Ensure the API key is included in the parameters
params['api_key'] = self.api_key

# construct the full url for the endpoint        
url = f"{self.base_url}/{endpoint}"

# Make the GET request with the parameters
response = requests.get(url, params=params)
response.raise_for_status() # This will rais an exception for HTTP (for example 401 errors)

"""
    
    
    
    
    
    
    
"""         
default_params = {
    'api_key': self.api_key,
    'language': 'en-US',
    'page': 1
}

# If params provided, update default_params with these so custom params can override defaults
if params:
    default_params.update(params)

# Construct the full URL for the API request
url = f"{self.base_url}/{endpoint}"

# Get the data into response with requests.get or raise for status error
response = requests.get(url, params=params)
# This will raise an error for non-200 responses (error response)
response.raise_for_status()

# Put the response in json format and into data
return response.json()
"""

""" 
Another version of this tmdb manager
"""
""" 
class TMDBManager:
    import os
    import requests

    API_KEY = os.getenv("TMDB_API_KEY")
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self):
        if not self.API_KEY:
            raise ValueError("TMDB API key not found in environment variables.")

    def _send_request(self, endpoint, params={}):
        params['api_key'] = self.API_KEY
        full_url = f"{self.BASE_URL}{endpoint}"
        response = self.requests.get(full_url, params=params)
        response.raise_for_status()
        return response.json()

"""


