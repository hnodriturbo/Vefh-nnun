







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


    
    
    
    
    
    
######### ----- Interesting Codes From endpoint_manager.py ----- #########

  

    # Not Using
    def search_endpoint(self, query):
        """Build endpoint for searching across multiple types."""
        return f"{self.base_url}/search/multi?query={query}"


""" 
'now_playing' : {
    'endpoint' : {self.base_url}/{item_type}/{category}
}
'upcoming' : {
    'endpoint' : {self.base_url}/{item_type}/{category}
}Q
# This is only for category tv and catego                                                    ry variable would be 'on_the_air' & 'airing_today' .... 
# Maybe put this as a possibility in the TV Shows dropdown button items buttons ?
# First let's make the page work like before !!!!!!!!!!
elif category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"
"""



































"""     
    # Endpoint builder for the genres listings
    def genre_endpoint(self, item_type='movie'):
    
        # Build endpoint for fetching genres, either combined or specific to movies or TV.
        #     endpoint example: https://api.themoviedb.org/3/genre/{item_type}/list
        # ---------------------________self.base_url________-______{item_type}_____
        
        # If we would use all the returns would be overloaded because fetching from both item_type='tv' and item_type='movie' would produce alot of results
        if item_type == 'all':
            return self.base_url + "/genre/movie/list", self.base_url + "/genre/tv/list"
        else:
            return self.base_url + f"/genre/{item_type}/list"
"""
""" 


# Endpoints availability and suggestions of many different possibilities of endpoints for TMDB database:

if category in ['popular', 'top_rated', 'now_playing', 'upcoming'] and item_type in ['movie', 'tv']:
    return f"{self.base_url}/{item_type}/{category}"


elif category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"
   

# Genre listing
elif category == 'categories':
    return f"{self.base_url}/genre/{item_type}/list" 
    
    

# If category selection is discover then the url has discover in it and item_types + genre_id
# therefore opening a category and discover the listings of that selected specified category    

elif category == 'discover' and genre_id:
    return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
    

    
results is that category possibilites are:

if category == 'discover':
    discover_category_items = {
        base_url : www.blablaaa.com/w/3...
        item_type : item_type
        genre_id : genre_id
    }
    
    
    
elif category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"
    
    
categories = {
    'item_type' : 'movie' ? 'tv'
    'popular' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    'top_rated' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    'now_playing' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    'upcoming' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    
}
    

# Common endpoints with direct paths

if category in ['popular', 'top_rated', 'now_playing', 'upcoming'] and item_type in ['movie', 'tv']:
    return f"{self.base_url}/{item_type}/{category}"

------------------------------------------------------------------------

# TV-specific endpoints

if category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"

------------------------------------------------------------------------
------------------------------------------------------------------------

# Discovery with genre filters
elif category == 'discover' and genre_id:
    return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
    
------------------------------------------------------------------------
------------------------------------------------------------------------

# Genre listing
elif category == 'categories':
    return f"{self.base_url}/genre/{item_type}/list"
    
------------------------------------------------------------------------
------------------------------------------------------------------------

# Default handling, fall back to standard category/item_type endpoint
return f"{self.base_url}/{item_type}/{category}"

------------------------------------------------------------------------
------------------------------------------------------------------------

def search_endpoint(self, query):
    return f"{self.base_url}/search/multi?query={query}"
        
     
        
"""





















# endpoint_manager.py suggestion from chatgpt:

import requests, os

class Endpoint_Manager:
    def __init__(self, base_url="https://api.themoviedb.org/3"):
        self.base_url = base_url

    def build_endpoint(self, category, item_type, genre_id=None):
        # Example endpoint logic
        if category == 'discover' and genre_id:
            return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
        if category in ['popular', 'top_rated']:
            return f"{self.base_url}/{item_type}/{category}"
        return f"{self.base_url}/{item_type}/{category}"


# Another ChatGPT suggestion of the TMDB API Manager
class TMDB_API_Manager:
    def __init__(self, endpoint_manager):
        self.api_key = os.getenv('TMDB_API_KEY')
        self.endpoint_manager = endpoint_manager

    def fetch_data(self, category, item_type, genre_id=None, params=None):
        endpoint = self.endpoint_manager.build_endpoint(category, item_type, genre_id)
        params = params or {}
        params.update({'api_key': self.api_key, 'language': 'en-US', 'page': 1})
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def get_listings(self, item_type, category, genre_id=None, page=1):
        return self.fetch_data(category, item_type, genre_id, {'page': page})

    def list_categories(self, item_type):
        return self.fetch_data('categories', item_type)

    def get_item_details(self, item_type, item_id):
        return self.fetch_data(f"{item_type}/{item_id}", item_type)

    def get_trailer_key(self, item_type, item_id):
        data = self.fetch_data(f"{item_type}/{item_id}/videos", item_type)
        for video in data.get('results', []):
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return video['key']
        return None

# Usage
endpoint_manager = Endpoint_Manager()
tmdb_api_manager = TMDB_API_Manager(endpoint_manager)

