import os
import requests
from flask import current_app as app

class TMDB_API_Manager:
    def __init__(self):
        self.api_key = os.getenv('TMDB_API_KEY')
        if not self.api_key:
            app.logger.error("TMDB API key is not set.")
            raise ValueError("Missing API key for TMDB API.")
        self.base_url = "https://api.themoviedb.org/3"
        app.logger.info(f"TMDB API Manager initialized with key: {self.api_key}")

    def fetch_data(self, endpoint, params=None):
        default_params = {'api_key': self.api_key, 'language': 'en-US'}
        if params:
            default_params.update(params)
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=default_params)
        response.raise_for_status()
        return response.json()

    def build_endpoint(self, category, item_type, genre_id=None):
        if category in ['discover', 'popular', 'top_rated', 'categories']:
            if category == 'discover' and genre_id:
                return f"discover/{item_type}?with_genres={genre_id}"
            elif category == 'categories':
                return f"genre/{item_type}/list"
            elif category in ['popular', 'top_rated']:
                return f"{item_type}/{category}"
            else:
                app.logger.error("Invalid category or item type specified")
                raise ValueError("Invalid category or item type specified")
        else:
            app.logger.error("Invalid arguments provided to build endpoint")
            raise ValueError("Invalid arguments provided to build endpoint")

    def get_listings(self, item_type, category, genre_id=None, page=1):
        endpoint = self.build_endpoint(category, item_type, genre_id)
        params = {'page': page}
        if genre_id and category == 'discover':
            params['with_genres'] = genre_id
        return self.fetch_data(endpoint, params)
