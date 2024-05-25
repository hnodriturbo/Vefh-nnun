            # ########## Hreiðar Pétursson ##########
            #  ######## Vefhönnun Áfanginn ########
            #   ######### Skilaverkefni 3 ########
            #    ########   Apríl 2024   ########


#---- ##### ----- ########################### ----- ##### ----#
##### ----- ##### ----- tmdb_managar.py ----- ##### ----- #####
#---- ##### ----- ########################### ----- ##### ----#

""" For clarity here is my TMDB_API_KEY: """
""" 36dfeb735a6d3633c2364db52ed2075c """

import requests
from flask import flash

class API_Manager:
    def __init__(self, base_url='https://api.themoviedb.org/3', api_key='36dfeb735a6d3633c2364db52ed2075c'):
        self.base_url = base_url
        self.api_key = api_key
        print(f"API Manager initialized with base URL {self.base_url} and API Key {self.api_key}")

    def make_request(self, api_endpoint, params=None):
        """ Send a request to the TMDB API with given endpoint and parameters """
        
        default_params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'page': 1
        }
        
        # Merging provided parameters with defaults
        params = {**default_params, **(params or {})}
        print(f"Making request to {api_endpoint} with params {params}")
        
        try:
            full_url = f"{self.base_url}/{api_endpoint}"
            print(f"Full URL: {full_url}")  # Display the full URL being accessed
            response = requests.get(full_url, params=params)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            print("Request successful, processing response...")
            return response.json()
        
        except requests.RequestException as e:
            error_msg = f'Error accessing API: {e}'
            print(error_msg)  # Log error to console
            flash(error_msg, 'error')
            return None
        
        
    def get_movies_and_tv_shows_by_genre(self, item_type, genre_id):
        endpoint = f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
        data = self.make_request(endpoint)
        return data
            
    def list_categories(self, item_type):
        """ Fetch categories for movies or TV shows. """
        endpoint = f"genre/{item_type}/list"
        data = self.make_request(endpoint).get('genres', [])
        return data

    def get_item_details(self, item_type, item_id):
        """ Fetch detailed information about a specific movie or TV show. """
        endpoint = f"{item_type}/{item_id}"
        data = self.make_request(endpoint)
        return data

    def get_trailer_key(self, item_type, item_id):
        """ Fetch the YouTube trailer key for a specific movie or TV show. """
        endpoint = f"{item_type}/{item_id}/videos"
        result = self.make_request(endpoint)
        videos = result.get('results', [])
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return video['key']
        return None  # Return None if no trailer video is found
    
    
    
    
    
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################






""" ----- BaseNavEntry Initialization description ----- """ 
"""
Initialize a navigation entry with the route, title, icon, and whether it represents a listing page.

:param route: The URL route for this entry.
:param title: The display title for this entry.
:param icon: The icon class for this entry, typically for frontend display.
:param is_listing: A boolean indicating if this route is a listing page, affecting URL generation.
"""

""" ----- as_dict description ----- """ 
"""
Convert the navigation entry into a dictionary format that can be easily used in Flask templates.

:return: A dictionary representing this navigation entry with enhanced URL handling.
"""


""" 
class BaseNavEntry:
    def __init__(self, route, title, icon, endpoint, is_listing=False):
        self.route = route
        self.title = title
        self.icon = icon
        self.endpoint = endpoint
        self.is_listing = is_listing

    def as_dict(self):
        # Remove leading slash to simplify concatenation and usage in templates.
        endpoint = self.route.strip('/')
        # Determine the endpoint URL based on whether this is a 'listing' type page.
        endpoint = f"genre/{item_type}/list" if self.is_listing else self.endpoint
        return {
            'route': self.route,
            'title': self.title,
            'icon': self.icon,
            'endpoint': endpoint,
        }
"""



""" 
    def generate_nav_entry(route, title, icon, is_listing=False):
        endpoint = route.strip('/')
        if is_listing:
            endpoint = f"genre/{endpoint}/list"
        return {'route': route, 
                'title': title, 
                'icon': icon, 
                'endpoint': endpoint}
"""



