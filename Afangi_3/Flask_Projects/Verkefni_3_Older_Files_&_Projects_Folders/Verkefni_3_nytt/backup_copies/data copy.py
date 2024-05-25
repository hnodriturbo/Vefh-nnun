# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########


# Data fetching configurations and functions for TMDB API


import requests
import json

from nav import *

api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
base_url = "https://api.themoviedb.org/3"


"""Generic function to fetch data from the TMDB API."""
""" 
def fetch_tmdb_data(endpoint, params=None):
    
    params = params or {}
    params['api_key'] = api_key
    params['language'] = 'en-US'

    response = requests.get(f"{base_url}/{endpoint}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from TMDB. Status code: {response.status_code}")
        return None

 """
def fetch_tmdb_data(endpoint, params=None):
    """Generic function to fetch data from the TMDB API."""
    params = params or {}
    params['api_key'] = api_key
    params['language'] = 'en-US'

    response = requests.get(f"{base_url}/{endpoint}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from TMDB. Status code: {response.status_code}")
        return None


############################################################################################

"""Fetch data from TMDB API for a given endpoint and parameters."""

def fetch_from_tmdb(endpoint, page=1, params=None):

    query_params = {
        'api_key': api_key, 
        'language': 'en-US', 
        'page': page
    }
    if params:
        query_params.update(params)  # Merge additional parameters
    
    response = requests.get(f"{base_url}/{endpoint}", params=query_params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Failed to fetch data from TMDB API. Status code: {response.status_code}")
        return []
    
############################################################################################






############################################################################################

# This is for building end points for listings.html (popular, top rated and listings of categories)
def build_endpoint(item_type, category='genre', genre_id=None):
    """
    Constructs an endpoint URL for fetching movies or TV shows based on the specified criteria.
    
    Args:
        item_type (str): Either 'movie' or 'tv'.
        category (str): Type of endpoint to construct ('genre', 'popular', 'top_rated').
        genre_id (int, optional): The genre ID, required if category is 'genre'.
    
    Returns:
        str: The full endpoint URL for the TMDB API.
    """
    if item_type not in ['movie', 'tv']:
        raise ValueError("Invalid item type specified. Must be 'movie' or 'tv'.")
    
    if category == 'popular':
        return f"{item_type}/popular?api_key={api_key}"
    elif category == 'top_rated':
        return f"{item_type}/top_rated?api_key={api_key}"
    elif category == 'genre':
        if genre_id is None:
            raise ValueError("Genre ID must be provided for genre-specific listings.")
        return f"discover/{item_type}?api_key={api_key}&with_genres={genre_id}"
    else:
        raise ValueError("Invalid category specified. Must be 'genre', 'popular', or 'top_rated'.")

############################################################################################











############################################################################################

# Function to fetch categories of movies or TV shows
def fetch_categories(item_type):
    """Fetch genre categories from TMDB API for either movies or TV shows."""
    endpoint = 'genre/movie/list' if item_type == 'movies' else 'genre/tv/list'
    response = requests.get(f"{base_url}/{endpoint}", params={'api_key': api_key, 'language': 'en-US'})
    if response.status_code == 200:
        return response.json().get('genres', [])
    else:
        return []

############################################################################################








############################################################################################

# This function handles the dynamic fetching of details of either a movie or a tv show
def get_details(item_id, item_type='movie'):
    """
    Fetch details for a movie or TV show by ID.

    Args:
        item_id (int): The ID of the movie or TV show.
        item_type (str): The type of the item, either 'movie' or 'tv'.

    Returns:
        dict: The details of the movie or TV show.
    """
    if item_type == 'movie':
        url = f"{base_url}/movie/{item_id}?api_key={api_key}&language=en-US"
    elif item_type == 'tv':
        url = f"{base_url}/tv/{item_id}?api_key={api_key}&language=en-US"
    else:
        raise ValueError("Invalid item type specified. Must be 'movie' or 'tv'.")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        details = response.json()
        return details
    else:
        return None

############################################################################################






############################################################################################

def build_title(item_type, category, genre_id=None, genre_name=None):
    """
    Build a dynamic title for different listing pages.

    Args:
        item_type (str): Type of the item ('movie' or 'tv').
        category (str): Category type ('popular', 'top_rated', or 'genre').
        genre_id (int, optional): ID of the genre, if category is 'genre'.
        genre_name (str, optional): Name of the genre, to avoid additional lookups if already available.

    Returns:
        str: A formatted title string starting with "Showing".
    """
    # Capitalize the item type for display (e.g., 'movies' -> 'Movies')
    item_type_formatted = item_type.title()  # 'movie' -> 'Movie', 'tv' -> 'Tv'
    if item_type == 'tv':
        item_type_formatted = 'TV Shows'  # Special case for TV shows
    elif item_type == 'movie':
        item_type_formatted = 'Movies'

    # Determine the category description
    if category == 'popular':
        category_description = 'Popular'
    elif category == 'top_rated':
        category_description = 'Top Rated'
    else:
        category_description = 'Category'  # Default if not genre but fallback

    # Handle genre-specific title
    if category == 'genre' and genre_id is not None:
        if genre_name is None:
            # Assuming a function get_genre_name_by_id exists that fetches the genre name based on its ID
            genre_name = get_genre_name_by_id(genre_id, item_type)
        return f"Showing {genre_name} {item_type_formatted}"

    # Return the formatted title
    return f"Showing {category_description} {item_type_formatted}"












############################################################################################

def get_genre_name_by_id(genre_id, item_type):
    """
    Fetch genre name by its ID. Assume you have a predefined mapping or a function that can query this.

    Args:
        genre_id (int): ID of the genre.
        item_type (str): 'movie' or 'tv' to distinguish the source of the genre.

    Returns:
        str: Genre name.
    """
    genre_dict = genre_movies if item_type == 'movie' else genre_tv_shows

    return genre_dict.get(genre_id, {'name':  'Unknown Genre'})['name']  # Default to 'Unknown Genre' if not found

############################################################################################








############################################################################################

def get_trailer_key(item_id, item_type='movie'):
    if item_type == 'movie':
        url = f"{base_url}/movie/{item_id}/videos?api_key={api_key}&language=en-US"
    else:
        # Adjust the URL for TV shows if needed
        url = f"{base_url}/tv/{item_id}/videos?api_key={api_key}&language=en-US"
    
    response = requests.get(url)
    videos = response.json()['results']
    trailer_key = next((video['key'] for video in videos if video['type'] == 'Trailer' and video['site'] == 'YouTube'), None)
    return trailer_key


############################################################################################















    
"""Fetch data from TMDB API for a given endpoint and parameters."""
""" 
# Function to fetch data from TMDB API
def fetch_from_tmdb(endpoint, page=1, params=None):

    query_params = {
        'api_key': api_key, 
        'language': 'en-US', 
        'page': page
        }
    if params:
        query_params.update(params)
    response = requests.get(f"{base_url}/{endpoint}", params=query_params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Failed to fetch data from TMDB API. Status code: {response.status_code}")
        return []
"""









""" 



# Dynamic fetching of data in pages from the TMDB API
def fetch_from_tmdb(endpoint, page=1, params=None):

    url = f"{base_url}/{endpoint}?api_key={api_key}&language=en-US&page={page}"
    if params:
        for key, value in params.items():
            url += f"&{key}={value}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Failed to fetch data from TMDB API. Status code: {response.status_code}")
        return []

    import requests

def fetch_from_tmdb(endpoint, page=1, params=None):

    # Initialize the parameters dictionary with API key, language, and page.
    query_params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': page
    }

    # If there are additional parameters, merge them into the base dictionary.
    if params:
        query_params.update(params)

    # Construct the request with dynamic parameters.
    response = requests.get(f"{base_url}/{endpoint}", params=query_params)

    # Check the response status and return the appropriate result.
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Failed to fetch data from TMDB API. Status code: {response.status_code}")
        return []

 """



""" 
def fetch_categories(item_type):
    
    endpoint = 'genre/movie/list' if item_type == 'movies' else 'genre/tv/list'
    
    url = f"{base_url}/{endpoint}?api_key={api_key}&language=en-US"
    
    response = requests.get(url)

    return response.json().get('genres', []) if response.status_code == 200 else []
 """


"""     
    if response.status_code == 200:
        data = response.json()
        return data.get('genres', [])
    else:
        print(f"Failed to get genres data from TMDB API. Status code: {response.status_code}")
        return []
"""





""" 
def update_breadcrumbs(url, title):
    if 'breadcrumbs' not in session:
        session['breadcrumbs'] = []
    else:
        # Prevent duplication of the last entry
        if session['breadcrumbs'] and session['breadcrumbs'][-1]['url'] == url:
            return

    # Add the new entry without limiting the length of the breadcrumb trail
    session['breadcrumbs'].append({'url': url, 'title': title})
    session.modified = True

 """