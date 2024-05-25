""" -- ## -- _____ My TMDB API Manager _____ -- ## -- """

class TMDB_API_Manager:
    """
    A class to manage interactions with The Movie Database (TMDB) API.
    """
        
# Configuration variables for the TMDB API access
# api_key = "b6bbab9eb73d6f04fc09b9405d888fa2"


api_key = os.getenv('TMDB_API_KEY')
base_url = "https://api.themoviedb.org/3"

# My Awesome TMDB API Class Manager for handling the fetching of data from TMDB
class TMDB_API_Manager:
    
    def __init__(self):
        """
        Initializes the TMDB API Manager instance, setting up the API key and base URL.
        """
        self.api_key = os.getenv('TMDB_API_KEY')
        if not self.api_key:
            app.logger.error('TMDB API key is not set.')
            raise ValueError('Missing API key for TMDB API Class')
        
        self.base_url = "https://api.themoviedb.org/3"
        
        
    def log_initialization(self):
        """Logs the initialization message, ensuring it's called within an app context."""
        app.logger.info(f"TMDB Manager initialized with key: {self.api_key}")
    
    
    
    def fetch_data(self, endpoint, params=None):
        """
        Fetches data from TMDB API given an endpoint and optional parameters.

        Args:
            endpoint (str): The API endpoint to hit.
            params (dict, optional): Additional query parameters for the API request.

        Returns:
            dict: The JSON response from the API.
        """
        # Default parameters for the API request
        default_params = {'api_key': self.api_key, 'language': 'en-US'}
        if params:
            default_params.update(params)
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=default_params)
        response.raise_for_status()
        return response.json()

    def get_listings(self, item_type, category, genre_id=None, page=1):
        """
        Retrieves listings for movies or TV shows based on type, category, and optional genre.

        Args:
            item_type (str): 'movie' or 'tv' indicating the type of items.
            category (str): Category of listings like 'popular', 'top_rated'.
            genre_id (str, optional): Genre ID to filter listings.
            page (int): Page number for pagination.

        Returns:
            dict: JSON data containing the listings.
        """
        

    
    
    
    
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
    
    