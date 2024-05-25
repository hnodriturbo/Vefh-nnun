

class Nav_Entry:
    def __init__(self, item_type, api_manager, route=None, title=None, icon=None):
        self.item_type = item_type
        self.api_manager = api_manager
        self.route = route
        self.title = title
        self.icon = icon
        
        
    def generate_entry(self):
        
        """ Generate navigation entry """
        
        endpoint_route = self.route[1:] if self.route.startswith('/') else self.route
        endpoint = f"{self.item_type}/{endpoint_route}"
        return {
            'route': self.route,
            'title': self.title,
            'icon': self.icon,
            'endpoint': endpoint
        } # Return this awesome dictionary



class Nav_System:
    """System to manage navigation entries for different item types and utility links."""
    def __init__(self, api_manager):
        self.api_manager = api_manager
        self.entries = {
            'movie': Nav_Entry('movie', self.api_manager),
            'tv': Nav_Entry('tv', self.api_manager)
        }
        
        print(self.entries)
        self.right_buttons = {
            'home': Nav_Entry('home', self.api_manager, route='/', title='Home', icon='bi-house'),
            'about_author': Nav_Entry('about_author', self.api_manager, route='/about_author', title='About Author', icon='bi-person')
        }

    def generate_entries(self):
        """Generate navigation entries for all categories and right-aligned links."""
        navigation = {
            'categories': {},
            'right_aligned': {}
        }
        for item_type, nav_entry in self.entries.items():
            navigation['categories'][item_type] = {
                'title': 'Movies' if item_type == 'movie' else 'TV Shows',
                'icon': 'bi-film' if item_type == 'movie' else 'bi-tv',
                'buttons': {
                    'popular': nav_entry.generate_entry('popular', 'Popular Movies', 'bi-star'),
                    'top_rated': nav_entry.generate_entry('top_rated', 'Top Rated Movies', 'bi-star'),
                    'categories': nav_entry.generate_entry('categories', 'Movies Categories', 'bi-list')
                }
            }
        for key, nav_entry in self.right_buttons.items():
            navigation['right_aligned'][key] = nav_entry.generate_entry()

        return navigation




"""         
params['api_key'] = self.api_key
params['language'] = self.language
params['page'] = self.page


    
def make_request(self, endpoint, params={}):
    

    full_url = f"{self.base_url}/{endpoint}"
    
    response = requests.get(full_url, params=params) 
    response.raise_for_status()
    return response.json()


"""














""" 
class Endpoint_Manager(TMDB_API_Manager):
def __init_subclass__(cls) -> None:
    return super().__init_subclass__()


def get_data(self, item_type, category, additional_params=None):
    params = {'language': 'en-US', 'page': 1}

    if additional_params:
        params.update(additional_params)
        
    endpoint = f"{item_type}/{category}"
    
    return self.api_manager.make_request(endpoint, params)


 """
""" # " ----- ########################################################## ----- "
#        " -- #### --- __ TMDB_API_JSON - The Parent __ --- ####  -- "
# " ----- ########################################################## ----- "

class TMDB_API_JSON:
    def __init__(self, api_key='36dfeb735a6d3633c2364db52ed2075c', base_url='https://api.themoviedb.org/3'):
        # Use my #1 API Key as the API Key but have the second one for default backup
        self.api_key = api_key or os.getenv('tmdb_api_key', '36dfeb735a6d3633c2364db52ed2075c')
        self.base_url = base_url


        
    def make_request(self, endpoint, params=None):

        # Default Parameters
        params = params or {}
        params.update({
            'api_key': self.api_key,
            'language': self.language,
            'page': self.page
        })
        
        # Construct the full url - Endpoint should come from get_data argument endpoint = f"{item_type}/{category}"
        full_url = f"{self.base_url}/{endpoint}" 
        
        # Use requests.get() method with the full url and parameter args
        response = requests.get(full_url, params=params)
        
        # Sample: {self.base_url} + / + {endpoint} + / + {params}
        
        # If there is a error then we use raise_for_status()
        response.raise_for_status()
  
        # Put the response of the json() method into data
        data = response.json()
        
        # Return the data
        return data
 """

# " ----- ##########################################################  ----- "
#    " -- ### --- __ Dynamic API Data Manager - The Child __ --- ###  -- "
# " ----- ##########################################################  ----- "
        
"""
Fetch data dynamically based on the endpoint category and item type.
Adjust 'language' and 'page' as needed for specific calls.
Endpoint for listing categories is specifically built within a function
in navigation_navbar.py
"""

"""        
class Dynamic_API_Data_Manager(TMDB_API_JSON):
    def __init__(self, base_url='https://api.themoviedb.org/3', api_key='36dfeb735a6d3633c2364db52ed2075c', language='en-US', page=1):
        super().__init__(api_key, base_url)
        
        self.language = 'en-US'
        self.page = 1


    # Method for getting the data making the request with all information needed
    def get_data(self, item_type, category, additional_params=None):

        endpoint = f"{item_type}/{category}"  # Construct endpoint with item_type and category
        params = {
            'api_key': self.api_key,
            'language': self.language,
            'page': self.page
        }
        
        if additional_params:
            params.update(additional_params)
        print("Item type:", item_type)  # Should print "movie"
        print("Category:", category)   # Should print "popular"
        endpoint = f"{item_type}/{category}"
        print("Constructed Endpoint:", endpoint)  # Should print "movie/popular"

        return super().make_request(endpoint, params)
    
    
        

    def get_item_details(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}"
        return super().make_request(endpoint)

"""    
    
    
    
"""
Fetch categories for movies or TV shows.
"""
"""     
def list_categories(self, item_type):
    # Endpoint to list tv or movie categories
    endpoint = f"genre/{item_type}/list"
    data = self.make_request(endpoint).get('genres', [])
    return data
    # return self.fetch_data(endpoint).get('genres', [])
 """


"""
Fetch the YouTube trailer key for a specific movie or TV show.
"""
"""     
def get_trailer_key(self, item_type, item_id):
    endpoint = f"{item_type}/{item_id}/videos"
    result = self.make_request(endpoint)
    videos = result.get('results', [])
    for video in videos:
        if video['site'] == 'YouTube' and video['type'] == 'Trailer':
            return video['key']
    # If there is no trailer video return None
    return 
 """    
    
    
"""Build endpoint for searching across multiple types."""
"""     
    def search_endpoint(self, query):
        return f"{self.base_url}/search/multi?query={query}"
"""
    
""" Tester of the class """
"""     
    def print(self):
        print(f"api key: {self.api_key}")
        print(f"base url: {self.base_url}")

"""
    
        
    
""" 
    Storage Code Method(s) :
    
    ##### Generic method to fetch movies or TV shows based on type and category. #####

    # A very simple construct of the endpoint (but is more needed then this if we define 
    # the cateogry to be more possibilitys like is_category=True... if false then list 
    # all categories, if true then list that category.. easy to add this kind of logic 
    # into this method
    
    # Fetch media based on media_type('tv' or 'movie') and category('popular', 'top_rated', 'genre/{genre_id}/list')
    def fetch_media(self, media_type, category, params=None):
        endpoint = f'{media_type}/{category}'
        return self.make_request(endpoint, params=params)

"""



    

    
    
    
    

""" ----- ##########################################  ----- """


# Configuration variables for the TMDB API access
# api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
# api_key_2 = "36dfeb735a6d3633c2364db52ed2075c"
# api_key = os.getenv('TMDB_API_KEY')
# base_url = "https://api.themoviedb.org/3"


