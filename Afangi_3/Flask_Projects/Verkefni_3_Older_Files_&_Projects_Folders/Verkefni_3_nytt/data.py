# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

# data.py
import requests
from nav import *
from flask import flash, render_template

# Configuration variables for the TMDB API access
api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
base_url = "https://api.themoviedb.org/3"



# Til Danna:
# ætla að pusha þetta inn en ég er í miðri breytingu á öllu saman og er færa mig yfir í klasa frekar
# en stök functions til að einfalda síðuna mína en mátt alveg skoða alla kóðana hérna.




############################################################################################
def fetch_tmdb_data(endpoint, params=None):
    if params is None:
        params = {'api_key': api_key, 'language': 'en-US', 'page': 1}
    else:
        params.setdefault('api_key', api_key)
        params.setdefault('language', 'en-US')
        params.setdefault('page', 1)

    full_url = f"{base_url}/{endpoint}"
    try:
        response = requests.get(full_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {full_url}: {e}")
        return None

""" 
def fetch_tmdb_data(endpoint, params=None):
"""   
"""
Generic function to fetch data from the TMDB API.
Args:
    endpoint (str): The API endpoint to fetch data from.
    params (dict): Additional parameters for the API request.
Returns:
    dict or None: JSON response from the API or None if an error occurs.
"""
"""     if params is None:
        params = {}
    params.setdefault('api_key', api_key)
    params.setdefault('language', 'en-US')
    params.setdefault('page', 1) # Default to page 1 if not specified

    try:
        response = requests.get(f"{base_url}/{endpoint}", params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}, endpoint: {endpoint}, params: {params}")
        return None # Return None or appropriate error handling
 """
############################################################################################






############################################################################################

def build_endpoint(item_type, category, genre_id=None):
    """
    Build API endpoint for different TMDB requests based on the type of listing.
    """
    if category == 'genre' and genre_id:
        return f"discover/{item_type}?with_genres={genre_id}"
    return f"{item_type}/{category}"
############################################################################################






############################################################################################

def fetch_categories(item_type):
    """
    Fetches genre categories from TMDB API for either movies or TV shows.
    Args:
        item_type (str): Specifies whether 'movies' or 'tv' categories are fetched.
    Returns:
        list: List of genre categories.
    """
    endpoint = 'genre/movie/list' if item_type == 'movies' else 'genre/tv/list'
    return fetch_tmdb_data(endpoint).get('genres', [])

############################################################################################






############################################################################################

def get_details(item_id, item_type='movie'):
    """
    Fetches detailed information for a movie or TV show by ID.
    Args:
        item_id (int): The ID of the movie or TV show.
        item_type (str): Specifies the type, 'movie' or 'tv'.
    Returns:
        dict or None: The detailed information of the item.
    """
    endpoint = f"{item_type}/{item_id}"
    return fetch_tmdb_data(endpoint)

############################################################################################






############################################################################################

def get_trailer_key(item_id, item_type='movie'):
    """
    Fetches the YouTube trailer key for a movie or TV show.
    Args:
        item_id (int): The ID of the movie or TV show.
        item_type (str): Specifies the type, 'movie' or 'tv'.
    Returns:
        str or None: YouTube trailer key if available.
    """
    endpoint = f"{item_type}/{item_id}/videos"
    videos = fetch_tmdb_data(endpoint)
    if videos and 'results' in videos:
        return next((video['key'] for video in videos['results'] if video['type'] == 'Trailer' and video['site'] == 'YouTube'), None)
    return None

############################################################################################




############################################################################################

def build_title(item_type, category, genre_id=None):
    """
    Dynamically build titles for pages based on the item type, category, and possibly genre.
    Handles specific cases for 'popular' and 'top_rated' dynamically for both TV shows and movies.
    """
    # Map readable names to categories for better display
    category_names = {
        'popular': 'Popular',
        'top_rated': 'Top Rated'
    }

    # Default to a general category description if not a special category
    category_description = category_names.get(category, 'Category')

    # Define genre dictionaries based on the item type
    genre_dict = genre_tv_shows if item_type == 'tv' else genre_movies
    
    # Build the title based on genre or general category
    if genre_id and genre_id in genre_dict:
        genre_name = genre_dict[genre_id]['name']
        return f"{genre_name} {item_type.title()} Listings"
    return f"{category_description} {item_type.title()} Listings"

############################################################################################

