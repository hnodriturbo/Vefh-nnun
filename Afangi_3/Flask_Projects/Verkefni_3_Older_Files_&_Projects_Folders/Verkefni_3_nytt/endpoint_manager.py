# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

    #################################
##### --- Endpoint Manager File --- #####
    #################################
    
from flask import flash, render_template
import requests, request_formatter, nav, data, tmdb_manager

# Endpoint Manager Class
class Endpoint_Manager:
    def __init__(self) -> None:
        self.base_url = "https://api.themoviedb.org/3"
        
    # Build endpoint URLs dynamically based on the category and item type.
    def build_endpoint(self, category, item_type=None, genre_id=None):
        """ Categories I use in this application are:
            discover (list tv or movie ALL categories)
            popular (list popular items)
            top Rated (list top rated items)
            discover (list items from specific category)
        """
        # List all items with that genre_id to discover the items from that genre
        if category == 'discover' and genre_id:
            return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
        
        # Category listings of items for either movies or tv shows
        if category == 'categories':
            return f"{self.base_url}/genre/{item_type}/list"
        
        # Popular and top rated categories endpoints
        if category in ['popular', 'top_rated']:
            if item_type in ['movie', 'tv']:
                return f"{self.base_url}/{item_type}/{category}"
        
        # Default endpoint url for other cases if needed
        return f"{self.base_url}/{item_type}/{category}"
    
    
    
    
    
    
    
    # Not Using
    def search_endpoint(self, query):
        """Build endpoint for searching across multiple types."""
        return f"{self.base_url}/search/multi?query={query}"
    
    # Not Using
    def genre_endpoint(self, item_type='all'):
        """Build endpoint for fetching genres, either combined or specific to movies or TV."""
        if item_type == 'all':
            return self.base_url + "/genre/movie/list", self.base_url + "/genre/tv/list"
        else:
            return self.base_url + f"/genre/{item_type}/list"