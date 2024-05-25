# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########


from flask import Flask, render_template, session, request, redirect, url_for
import requests
import json

api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"
base_url = "https://api.themoviedb.org/3"


# Dynamic fetching of data in pages from the TMDB API
def fetch_from_tmdb(endpoint, page=1, params=None):
    """
    Fetch data from TMDB API for a given endpoint, page number, and additional parameters.
    """
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






def fetch_categories(item_type):
    
    endpoint = 'genre/movie/list' if item_type == 'movies' else 'genre/tv/list'
    
    url = f"{base_url}/{endpoint}?api_key={api_key}&language=en-US"
    
    response = requests.get(url)

    return response.json().get('genres', []) if response.status_code == 200 else []
"""     
    if response.status_code == 200:
        data = response.json()
        return data.get('genres', [])
    else:
        print(f"Failed to get genres data from TMDB API. Status code: {response.status_code}")
        return []
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

        # I used this to see the API fetched json info
        # print(json.dumps(details, indent=4, sort_keys=True))
        
        return details
    else:
        return None




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


