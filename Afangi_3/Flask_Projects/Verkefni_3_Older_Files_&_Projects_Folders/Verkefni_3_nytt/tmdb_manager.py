# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

# data.py
import requests, os
from nav import *
from flask import flash, render_template
    
# Configuration variables for the TMDB API access
# api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
api_key = os.getenv('TMDB_API_KEY')
base_url = "https://api.themoviedb.org/3"

class TMDB_API_Manager:
    
    # Initialization of the class instance
    def __init__(self) -> None:
        self.api_key = os.getenv('TMDB_API_KEY')
        self.base_url = "https://api.themoviedb.org/3"
        
    
    """Fetch data from TMDB API with specified endpoint and parameters."""
    def fetch_data(self, endpoint, params=None):
        
        # Establish a default parameters, potentially useful accross ALL API calls
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
        response.raise_for_status() # This will raise an error for non-200 responses
        
        # Put the response in json format and into data
        return response.json()
    
    """Get listings for movies or TV shows based on type and category."""
    def get_listings(self, item_type, category, genre_id=None, page=1):
        # If genre_id then use different endpoint and display the items from that category
        if genre_id:
            endpoint = f"dicover/{item_type}?with_genres={genre_id}"
        else:
            endpoint = f"{item_type}/{category}"
            
        params = {'page': page}

        data = self.fetch_data(endpoint, params)
        
        return data
        # return self.fetch_data(endpoint, params)
        
        
    """Fetch categories for movies or TV shows."""
    def list_categories(self, item_type):
        # Endpoint to list tv or movie categories
        endpoint = f"genre/{item_type}/list"
        data = self.fetch_data(endpoint).get('genres', [])
        return data
        # return self.fetch_data(endpoint).get('genres', [])
    
    
    
    """Fetch detailed information about a specific movie or TV show."""
    def get_item_details(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}"
        data = self.fetch_data(endpoint)
        return data
        #return self.fetch_data(endpoint)

    """Fetch the YouTube trailer key for a specific movie or TV show."""
    def get_trailer_key(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}/videos"
        result = self.fetch_data(endpoint)
        videos = result.get('results', [])
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return video['key']
        # If there is no trailer video return None
        return 
    


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
