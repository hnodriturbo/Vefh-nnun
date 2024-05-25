                # ########## Hreiðar Pétursson ##########
                #  ######## Vefhönnun Áfanginn ########
                #   ######### Skilaverkefni 3 ########
                #    ########   Apríl 2024   ########

      #---- ##### ----- ########################### ----- ##### ----#
          ## ----- ##### ----- tmdb_manager.py ----- ##### ----- ## 
      #---- ##### ----- ########################### ----- ##### ----#

#              """ For clarity here is my TMDB_API_KEY: """
#                """ 36dfeb735a6d3633c2364db52ed2075c """

import requests
from flask import flash

######## -------------------------------------------------------------- ########
   # ---- ###       ########################################       ### ---- #
######## -------------------------------------------------------------- ######## 

""" 
        Description:
            This is the Base_API_Manager. It handles the initialization and 
            communication with The Movie Database (TMDB) API.
"""
class Base_API_Manager:
    def __init__(self, base_url='https://api.themoviedb.org/3', api_key='36dfeb735a6d3633c2364db52ed2075c'):
        self.base_url = base_url
        self.api_key = api_key
        print(f"API Manager initialized with base URL {self.base_url} and API Key {self.api_key}")


    """  
        Description:
            Sends a request to the TMDB API using the specified endpoint 
            and parameters, handling any potential errors.
    """
    def make_request(self, api_endpoint, params=None):
        
        default_params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'page': 1
        }
        print(params) 
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

##### ----- Here ends the Base_API_Manager and Content_Manager begins ----- #####




""" 
        Description:
            Content_Manager extends Base_API_Manager to specifically handle
            fetching content data based on genre for movies and TV shows.
"""

class Content_Manager(Base_API_Manager):
    """
        Description:
            Process the API response, extracting the specified key if provided,
            and handling any missing or error data gracefully.
            param key: Optional key to extract data from the response.
    """
    def process_response(self, response, key=None):
        if response is None:
            flash("Failed to fetch data from TMDB API.", 'error')
            return [] if key else {}

        # Extract data by key if specified, with a fallback default
        if key:
            return response.get(key, [])
        return response



    """ 
        Description:
            Makes a request to the parent class with specific endpoint
            asssociated with the accordion buttons from the navbar.
            Uses listings.html
    """
    def fetch_popular_and_top_rated_from_button(self, endpoint, params=None):
        response = self.make_request(endpoint, params)
        return self.process_response(response, key='results')
        
    """ 
        Description:
            Fetches items form a specific category.
            Uses listings.html
    """
    def fetch_category_items(self, endpoint, params=None):
        response = self.make_request(endpoint, params)
        return self.process_response(response, key='results')

    """ 
        Description:
            Lists all genres available for either 'movie' or 'tv'
            (movies or TV shows).
    """
    def list_categories(self, item_type):
        endpoint = f"genre/{item_type}/list"
        response = self.make_request(endpoint)
        return self.process_response(response, key='genres')


    ####### ---- ###       ##########################       ### ---- #######


    """ 
        Description:
            Retrieves detailed information about a specific movie or 
            TV show using its ID.
            Uses item_details.html
    """
    def get_item_details(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}"
        response = self.make_request(endpoint)
        return self.process_response(response)


    ####### ---- ###       ##########################       ### ---- #######


    """ 
        Description:
            Fetches the YouTube trailer key for a movie or TV show 
            if available.
            Inside item_details.html
    """
    def get_trailer_key(self, item_type, item_id):
        endpoint = f"{item_type}/{item_id}/videos"
        response = self.make_request(endpoint)
        videos = self.process_response(response, key='results')
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return video['key']
        return None  # Return None if no trailer video is found


    ####### ---- ###       ##########################       ### ---- #######


    """ 
        Description:
            Aggregates popular and top-rated movies and TV shows into a 
            single dictionary for use in index.html to populate that file 
            with scrollable rows of the cards for items.
            Uses index.html
    """
    def fetch_popular_and_top_rated_for_index_page(self):
        categories = {
            'tv': ['popular', 'top_rated'],
            'movie': ['popular', 'top_rated']
        }
        
        results = {}
        
        for content_type, category_list in categories.items():
            
            results[content_type] = {}
            
            for category in category_list:
                endpoint = f"{content_type}/{category}"
                data = self.make_request(endpoint)
                
                results[content_type][category] = self.process_response(data, key='results')
        
        return results


    ####### ---- ###       ##########################       ### ---- #######

######## -------------------------------------------------------------------- ########
   # ---- ###       ##############################################       ### ---- #
######## -------------------------------------------------------------------- ######## 



        
   


"""     
    def get_movies_and_tv_shows_by_genre(self, item_type, genre_id):
        
        endpoint = f"discover/{item_type}"
        
        params = {'with_genres': genre_id}
        
        response = self.make_request(endpoint, params=params)
        
        return self.process_response(response, key='results')
"""



"""     
    def fetch_category_items(self, item_type, genre_id):
        response = self.make_request(url)
        return response.json().get('genres', []) if response.status_code == 200 else []
"""



"""     
    def fetch_category_items(self, endpoint, page=1):
        endpoint = f'discover/movie/with_genres={genre_id}' if item_type == 'movies' else f'discover/tv/with_genres={genre_id}'
        url = f"{self.base_url}/{endpoint}"
        # endpoint = f"{item_type}/{category}"
        params = {
            'page': page
        }
        response = self.make_request(endpoint, params)
        return self.process_response(response)
"""
    