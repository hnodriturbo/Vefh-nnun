            # ########## Hreiðar Pétursson ##########
            #  ######## Vefhönnun Áfanginn ########
            #   ######### Skilaverkefni 3 ########
            #    ########   Apríl 2024   ########


#---- ##### ----- ########################### ----- ##### ----#
##### ----- ##### ----- tmdb_managar.py ----- ##### ----- #####
#---- ##### ----- ########################### ----- ##### ----#

""" For clarity here is my TMDB_API_KEY: """
""" 36dfeb735a6d3633c2364db52ed2075c """



import os
import requests
from flask import current_app, flash

class API_Manager:
    def __init__(self, base_url='https://api.themoviedb.org/3', api_key='36dfeb735a6d3633c2364db52ed2075c'):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()  # Using session object to improve performance
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def make_request(self, endpoint, params=None):
        """ Send a request to the TMDB API with given endpoint and parameters """
        
        default_params = {
            'language': 'en-US',
            'page': 1
        }
        
        params = {**default_params, **(params or {})}  # Merge default and provided parameters
        
        try:
            response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            return response.json()
        
        # Log error and maybe return a default value or re-raise a custom exception
        except requests.RequestException as e:
            current_app.logger.error(f"API request failed: {e}")
            flash('Error accessing API', 'error')
            return None



###################################################################
###################################################################
###################################################################
###################################################################
###################################################################







class BaseNavEntry:
    def __init__(self, route, title, icon, endpoint, is_listing=False):
        """
        Initialize a navigation entry with the route, title, icon, and whether it represents a listing page.

        :param route: The URL route for this entry.
        :param title: The display title for this entry.
        :param icon: The icon class for this entry, typically for frontend display.
        :param is_listing: A boolean indicating if this route is a listing page, affecting URL generation.
        """
        self.route = route
        self.title = title
        self.icon = icon
        self.endpoint = endpoint
        self.is_listing = is_listing


    def as_dict(self):
        """
        Convert the navigation entry into a dictionary format that can be easily used in Flask templates.

        :return: A dictionary representing this navigation entry with enhanced URL handling.
        """
        # Remove leading slash to simplify concatenation and usage in templates.
        endpoint = self.route.strip('/')
        # Determine the endpoint URL based on whether this is a 'listing' type page.
        endpoint = f"genre/{item_type}/list" if self.is_listing else self.endpoint
        return {
            'route': self.route,
            'title': self.title,
            'icon': self.icon,
            'endpoint': endpoint,
        }



""" 
    def generate_nav_entry(route, title, icon, is_listing=False):
        endpoint = route.strip('/')
        if is_listing:
            endpoint = f"genre/{endpoint}/list"
        return {'route': route, 
                'title': title, 
                'icon': icon, 
                'endpoint': endpoint}
"""










class NavigationManager:
    def __init__(self):
        self.main_navigation = {}
        self.accordion = {}
        self.item_type = item_type

    def add_main_nav_entry(self, route, title, icon):
        """Add an entry to the main navigation."""
        self.main_navigation[title] = BaseNavEntry(route, title, icon).as_dict()

    def add_accordion_section(self, item_type, title, icon, route):
        """Add a new section to the accordion navigation."""
        self.accordion[item_type] = {
            'item_type': item_type,
            'title': title,
            'icon': icon,
            'route': route,
            'accordion_buttons': {}
        }

    def add_button_to_accordion(self, item_type, route, title, icon, endpoint, is_listing=False):
        """Add a button to an existing accordion section."""
        button_entry = BaseNavEntry(route, title, icon, endpoint, is_listing)
        self.accordion[item_type]['accordion_buttons'][title] = button_entry.as_dict()

    def configure_default_navigation(self): 
        """Configure default navigation setup for the application."""
        self.add_main_nav_entry('/', 'Home', 'bi-house')
        self.add_main_nav_entry('/about_author', 'About Author', 'bi-person')
        self.add_accordion_section('movie', 'Movies', 'bi-film', 'movies')
        self.add_accordion_section('tv', 'TV Shows', 'bi-tv', 'tv_shows')
        self.add_button_to_accordion('movie', '/movies/popular', 'Popular Movies', 'bi-film', 'movie/popular')
        self.add_button_to_accordion('movie', '/movies/top_rated', 'Top Rated Movies', 'bi-star', 'movie/top_rated')
        self.add_button_to_accordion('movie', '/movies/categories', 'Movie Categories', 'bi-list', 'genre/{self.item_type}/list', True)
        self.add_button_to_accordion('tv', '/tv_shows/popular', 'Popular TV Shows', 'bi-tv', 'movie/popular')
        self.add_button_to_accordion('tv', '/tv_shows/top_rated', 'Top Rated TV Shows', 'bi-star', 'movie/popular')
        self.add_button_to_accordion('tv', '/tv_shows/categories', 'TV Shows Categories', 'bi-list', 'movie/popular', True)

    def get_navigation(self):
        """Return the complete navigation structure."""
        return {
            'main_navigation': self.main_navigation,
            'accordion': self.accordion
        }
















# Example usage with the new method
nav_manager = NavigationManager()
nav_manager.configure_default_navigation()
navigation = nav_manager.get_navigation()






# A Semi-beautiful way to print out the items in the navigation dictionary of dictionaries
# to see all it's contents for using in the program and ease access because the generators
# of dictionary key's and values are not clear enough to see the structure in whole
# with the naked eye. (at least that's my view on the subject)

# Print the navigation structure
for section, content in navigation.items():
    print(f"\n{section.upper()} SECTION:")
    if section == 'main_navigation':
        for name, details in content.items():
            print(f"  {name}:")
            print(f"    Route: {details['route']}")
            print(f"    Title: {details['title']}")
            print(f"    Icon: {details['icon']}")
    elif section == 'accordion':
        for item_type, item_details in content.items():
            print(f"  {item_type.upper()} ACCORDION:")
            print(f"    Title: {item_details['title']}")
            print(f"    Icon: {item_details['icon']}")
            print(f"    Route: {item_details['route']}")
            for button_title, button_details in item_details['accordion_buttons'].items():
                print(f"      Button - {button_title}:")
                print(f"        Route: {button_details['route']}")
                print(f"        Base Route: {button_details['base_route']}")
                print(f"        Endpoint: {button_details['endpoint']}")
                print(f"        Title: {button_details['title']}")
                print(f"        Icon: {button_details['icon']}")
