            # ########## Hreiðar Pétursson ##########
            #  ######## Vefhönnun Áfanginn ########
            #   ######### Skilaverkefni 3 ########
            #    ########   Apríl 2024   ########


#---- ##### ----- ########################### ----- ##### ----#
##### ----- ##### ----- tmdb_managar copy.py ----- ##### ----- #####
#---- ##### ----- ########################### ----- ##### ----#

""" For clarity here is my TMDB_API_KEY: """
""" b6bbab9eb73d6f04fc09b9405d888fa2 """
""" For clarity here is my TMDB_API_KEY_2: """
""" 36dfeb735a6d3633c2364db52ed2075c """



import os
import requests
from flask import flash


# " ----- ########################################################## ----- "
#        " -- #### --- __ TMDB_API_JSON - The Parent __ --- ####  -- "
# " ----- ########################################################## ----- "

class TMDB_API_JSON:
    def __init__(self, api_key='36dfeb735a6d3633c2364db52ed2075c', base_url='https://api.themoviedb.org/3'):
        # Use my #1 API Key as the API Key but have the second one for default backup
        self.api_key = api_key or os.getenv('tmdb_api_key', '36dfeb735a6d3633c2364db52ed2075c')
        self.base_url = base_url


        
    def make_request(self, endpoint, params=None):
        """ Send a request to the specified API endpoint with parameters. """
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


# " ----- ##########################################################  ----- "
#    " -- ### --- __ Dynamic API Data Manager - The Child __ --- ###  -- "
# " ----- ##########################################################  ----- "

class Dynamic_API_Data_Manager(TMDB_API_JSON):
    def __init__(self, base_url='https://api.themoviedb.org/3', api_key='36dfeb735a6d3633c2364db52ed2075c', language='en-US', page=1):
        super().__init__(api_key, base_url)
        
        self.language = 'en-US'
        self.page = 1


    # Method for getting the data making the request with all information needed
    def get_data(self, item_type, category, additional_params=None):
        
        """
        Fetch data dynamically based on the endpoint category and item type.
        Adjust 'language' and 'page' as needed for specific calls.
        Endpoint for listing categories is specifically built within a function
        in navigation_navbar.py
        """
        
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
    
    
        
    """Fetch detailed information about a specific movie or TV show."""
    def get_item_details(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}"
        return super().make_request(endpoint)

    
    
    
    
    
    
    
    """ 
    Here below are good and very logical code samples i may use:
    
        def fetch_media(self, media_type, category, params=None):


        ##### Generic method to fetch movies or TV shows based on type and category. #####

        # A very simple construct of the endpoint (but is more needed then this if we define 
        # the cateogry to be more possibilitys like is_category=True... if false then list 
        # all categories, if true then list that category.. easy to add this kind of logic 
        # into this method
        
        endpoint = f'{media_type}/{category}'
        
        return self.make_request(endpoint, params=params)

    
    
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """Fetch categories for movies or TV shows."""
    def list_categories(self, item_type):
        # Endpoint to list tv or movie categories
        endpoint = f"genre/{item_type}/list"
        data = self.make_request(endpoint).get('genres', [])
        return data
        # return self.fetch_data(endpoint).get('genres', [])

    """Fetch the YouTube trailer key for a specific movie or TV show."""
    def get_trailer_key(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}/videos"
        result = self.make_request(endpoint)
        videos = result.get('results', [])
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return video['key']
        # If there is no trailer video return None
        return 
    
        # Not Using
    def search_endpoint(self, query):
        """Build endpoint for searching across multiple types."""
        return f"{self.base_url}/search/multi?query={query}"

    
    """ Tester of the class """
    def print(self):
        print(f"api key: {self.api_key}")
        print(f"base url: {self.base_url}")


    
    
    
    
    
    

""" ----- ##########################################  ----- """


""" For clarity here is my TMDB_API_KEY: """
""" b6bbab9eb73d6f04fc09b9405d888fa2 """


# Configuration variables for the TMDB API access
# api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
# api_key_2 = "36dfeb735a6d3633c2364db52ed2075c"
# api_key = os.getenv('TMDB_API_KEY')
# base_url = "https://api.themoviedb.org/3"


