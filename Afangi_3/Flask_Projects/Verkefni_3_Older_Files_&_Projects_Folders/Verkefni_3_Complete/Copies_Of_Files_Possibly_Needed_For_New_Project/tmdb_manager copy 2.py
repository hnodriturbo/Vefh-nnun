import requests
import json
from flask import render_template, url_for




###########################################################################################
##### ----- 3 Suggestions of the TMDB Manager Classes From ChatGPT Conversation ----- ##### 
##### ----- 3 Suggestions of the TMDB Manager Classes From ChatGPT Conversation ----- ##### 
##### ----- 3 Suggestions of the TMDB Manager Classes From ChatGPT Conversation ----- ##### 
###########################################################################################


############### --------------- Suggestion Number 1 --------------- ###############


""" 

Option 1: Basic Inheritance :

    BaseAPIManager handles all network communications, while TMDBAPIManager 
    adds specifics like endpoints and parameters.

"""


# Base API Manager
class BaseAPIManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

# TMDB API Manager
class TMDBAPIManager(BaseAPIManager):
    def __init__(self, api_key):
        super().__init__("https://api.themoviedb.org/3")
        self.api_key = api_key

    def get_movie_details(self, movie_id):
        return self.make_request(f"movie/{movie_id}", params={'api_key': self.api_key})

    def get_tv_details(self, tv_id):
        return self.make_request(f"tv/{tv_id}", params={'api_key': self.api_key})




############### --------------- Suggestion Number 2 --------------- ###############

""" 
                NOTICE: I LIKE THIS ONE QUITE A BIT !!!!
                ONLY NEED TO GET CHATGPT TO MERGE ALL THESE
                DIFFERENT METHODS INTO ONE THAT CAN MAKE USE OF 
                ALL OF THE ENDPOINTS AND BUILD THEM WITH ALL THIS 
                INFORMATION I HAVE NOW FROM THE JSON RESPONSES
                            
Option 2: Split Responsibility:

    Here, BaseAPIManager only manages the requests, while TMDBAPIManager 
    manages endpoints, and TMDBContentManager could manage content-specific 
    tasks, like fetching and formatting movie details. 

"""

# Base API Manager
class BaseAPIManager:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def make_request(self, endpoint, params=None):
        params = {'api_key': self.api_key, **(params or {})}
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

# TMDB API Manager
class TMDBAPIManager(BaseAPIManager):
    
    def __init__(self, api_key, base_url, language='en-US', page=1):
        
        super().__init__("https://api.themoviedb.org/3", api_key, base_url)
        
        self.language = language
        self.page = page



api_manager = TMDBAPIManager()

      
      #     ----------------------------     #
####### ----- # extra that i didnt notice # ----- #######
      #     ----------------------------     #



      #     ----------------------------     #
####### ----- # TMDB Content Manager # ----- #######
      #     ----------------------------     #
class TMDBContentManager(api_manager):


    def get_movie_details(self, movie_id):
        """Fetch detailed information about a specific movie."""
        endpoint = f"movie/{movie_id}"
        return api_manager.make_request(endpoint)

    def get_tv_details(self, tv_id):
        """Fetch detailed information about a specific TV show."""
        endpoint = f"tv/{tv_id}"
        return api_manager.make_request(endpoint)

    def list_movie_genres(self):
        """Fetch a list of all movie genres."""
        endpoint = "genre/movie/list"
        return api_manager.make_request(endpoint)

    def list_tv_genres(self):
        """Fetch a list of all TV show genres."""
        endpoint = "genre/tv/list"
        return api_manager.make_request(endpoint)

    def get_movies_by_genre(self, genre_id, page=1):
        """Fetch movies by genre."""
        endpoint = f"discover/movie"
        params = {'with_genres': genre_id, 'page': page}
        return api_manager.make_request(endpoint, params=params)

    def get_tv_by_genre(self, genre_id, page=1):
        """Fetch TV shows by genre."""
        endpoint = f"discover/tv"
        params = {'with_genres': genre_id, 'page': page}
        return api_manager.make_request(endpoint, params=params)






############### --------------- Suggestion Number 3 --------------- ###############

""" 

Option 3: Feature-Specific Managers :

    Create separate classes for movies and TV shows that extend from a 
    common TMDB manager.

"""

# TMDB API Manager
class TMDBAPIManager:
    base_url = "https://api.themoviedb.org/3"

    def __init__(self, api_key):
        self.api_key = api_key

    def make_request(self, endpoint, params=None):
        params = {'api_key': self.api_key, **(params or {})}
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

# Movies Manager
class MoviesManager(TMDBAPIManager):
    def get_details(self, movie_id):
        return self.make_request(f"movie/{movie_id}")

# TV Shows Manager
class TVShowsManager(TMDBAPIManager):
    def get_details(self, tv_id):
        return self.make_request(f"tv/{tv_id}")
