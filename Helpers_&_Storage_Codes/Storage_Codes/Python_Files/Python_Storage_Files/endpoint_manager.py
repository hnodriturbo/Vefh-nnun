# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########

    #################################
##### --- Endpoint Manager File --- #####
    #################################
    
# from flask import flash, render_template

# import requests
# import request_formatter

# I have this import for the future in case i need to use this here
# from navigation_navbar import create_navigation

# from tmdb_manager import TMDB_API_Manager
# from request_formatter import RequestFormatter
 
import requests, os


# Endpoint Manager Class
class Endpoint_Manager:
    """ 
    Description:
        This endpoint manager is used for creating the urls for the api to retrive the
        items from. After the TMDB API Manager gets the urls, it uses the API to retrive
        the results from TMDB. Then we display the results by injecting them into html.
    """
    # Initialization of the Endpoint_Manager
    def __init__(self, base_url="https://api.themoviedb.org/3"):
        self.base_url = base_url
        # Set more things if needed 
        # ( maybe the categories list or list or all available api urls )
           
     
    # Build endpoint URLs dynamically based on the category and item type.
    def build_endpoint(self, category, item_type, genre_id=None):
        """ Categories I use in this application are:
            categories (list tv or movie ALL categories)
            popular (list popular items)
            top Rated (list top rated items)
            discover (list items from specific category)
        """
    
        if category in ['discover', 'popular', 'top_rated', 'categories'] and item_type in ['movie', 'tv']:
            
            # List all items with that genre_id to discover the items from that genre
            if category == 'discover':
                if genre_id:
                    return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
                else:
                    """ Do something here for fails """
                   
                    
            # Category listings of items for either movies or tv shows
            elif category == 'categories':
                if item_type:
                    return f"{self.base_url}/genre/{item_type}/list"
            
            
            # Popular and top rated categories endpoints
            elif category == 'popular' or 'top_rated':
                    return f"{self.base_url}/{item_type}/{category}"
            else:
                """ Do something here for fails, this instance, return to 404 with message that item_type wasnt either movie or tv and it must be either one ... ? """    
        else:
            """ Do something here for fails. Here we need a message to the 404 saying it didnt get the right arguments to make any feasible endpoint to build on... ? """
        
        # Default endpoint url
        return f"{self.base_url}/{item_type}/{category}"
    

    # Not Using
    def search_endpoint(self, query):
        """Build endpoint for searching across multiple types."""
        return f"{self.base_url}/search/multi?query={query}"


""" 


'now_playing' : {
    'endpoint' : {self.base_url}/{item_type}/{category}
}
'upcoming' : {
    'endpoint' : {self.base_url}/{item_type}/{category}
}

# This is only for category tv and category variable would be 'on_the_air' & 'airing_today' .... 

# Maybe put this as a possibility in the TV Shows dropdown button items buttons ?

# First let's make the page work like before !!!!!!!!!!

# Example endpoint for "on_the_air" and "airing_today" (item_type == "tv" and category == ['on_the_air', 'airing_today'])
elif category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"
"""



































"""     
    # Endpoint builder for the genres listings
    def genre_endpoint(self, item_type='movie'):
    
        # Build endpoint for fetching genres, either combined or specific to movies or TV.
        #     endpoint example: https://api.themoviedb.org/3/genre/{item_type}/list
        # ---------------------________self.base_url________-______{item_type}_____
        
        # If we would use all the returns would be overloaded because fetching from both item_type='tv' and item_type='movie' would produce alot of results
        if item_type == 'all':
            return self.base_url + "/genre/movie/list", self.base_url + "/genre/tv/list"
        else:
            return self.base_url + f"/genre/{item_type}/list"
"""
""" 
Categories_List (Ég bjó þennan til, til þess að átta mig á að popular og top rated eru líka categories)

if category in ['popular', 'top_rated', 'now_playing', 'upcoming'] and item_type in ['movie', 'tv']:
    return f"{self.base_url}/{item_type}/{category}"

elif category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"
    
# Genre listing
elif category == 'categories':
    return f"{self.base_url}/genre/{item_type}/list" 
    
# If category selection is discover then the url has discover in it and item_types + genre_id
# therefore opening a category and discover the listings of that selected specified category    
elif category == 'discover' and genre_id:
    return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
    
results is that category possibilites are:
if category == 'discover':
    discover_category_items = {
        base_url : www.blablaaa.com/w/3...
        item_type : item_type
        genre_id : genre_id
    }
elif category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"
categories = {
    'item_type' : 'movie' ? 'tv'
    'popular' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    'top_rated' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    'now_playing' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    'upcoming' : {
        'endpoint' : {self.base_url}/{item_type}/{category}
    }
    
}
    
    
    
"""

""" 

# Common endpoints with direct paths

if category in ['popular', 'top_rated', 'now_playing', 'upcoming'] and item_type in ['movie', 'tv']:
    return f"{self.base_url}/{item_type}/{category}"

------------------------------------------------------------------------

# TV-specific endpoints

if category in ['on_the_air', 'airing_today'] and item_type == 'tv':
    return f"{self.base_url}/tv/{category}"

------------------------------------------------------------------------

# Discovery with genre filters
elif category == 'discover' and genre_id:
    return f"{self.base_url}/discover/{item_type}?with_genres={genre_id}"
------------------------------------------------------------------------
# Genre listing
elif category == 'categories':
    return f"{self.base_url}/genre/{item_type}/list"
------------------------------------------------------------------------
# Default handling, fall back to standard category/item_type endpoint
return f"{self.base_url}/{item_type}/{category}"
------------------------------------------------------------------------
    def search_endpoint(self, query):
        return f"{self.base_url}/search/multi?query={query}"
"""