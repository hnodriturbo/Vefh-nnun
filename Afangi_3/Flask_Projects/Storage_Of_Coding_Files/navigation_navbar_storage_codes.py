      
        
        

# Function for using the classes and their methods to create a functional but yet an awesome
# dict of dicts for usage in this awesome project of mine.

""" 
def create_navigation(movie_categories, tv_categories):
    home = Nav_Entry('Home', 'bi-house', '/')
    about_author = Nav_Entry('About Author', 'bi-person', '/about_author')
    movies = Movies_Nav_Entry('Movies', 'bi-film', '/movies', movie_categories)
    tv_shows = TV_Shows_Nav_Entry('TV Shows', 'bi-tv', '/tv_shows', tv_categories)

    navigation_structure = {
        'navbar': {
            'main_navigation': {
                'Home': home.as_dictionary(),
                'About Author': about_author.as_dictionary()
            },
            'main_navigation_accordion': {
                'Movies': movies.as_dictionary(),
                'TV Shows': tv_shows.as_dictionary()
            }
        }
    }

    return navigation_structure
"""







 ###########################################################
""" ##### ------------- STORAGE CODES ------------- ##### """
 ###########################################################
 
 
""" 
class Genre_Nav_Entry(Nav_Entry):
    def __init__(self, genre_id, title, icon, item_type):
        super().__init__(title, icon, f'/{item_type}/genre/{genre_id}', f'{item_type}/genre/{genre_id}')
        self.genre_id = genre_id
        self.item_type = item_type
        
""" 
    
    
    
    

""" 
# Pretty Printed nav_data
{
  "navbar": {
    "main_navigation": {
        "Home": {
            "title": "Home",
            "icon": "bi-house",
            "route": "/",
            "api_endpoint": null,
            "accordion_buttons": null
        },
        "About Author": {
            "title": "About Author",
            "icon": "bi-person",
            "route": "/about_author",
            "api_endpoint": null,
            "accordion_buttons": null
        }
        },
    "main_navigation_accordion": {
        "Movies": {
            "title": "Movies",
            "icon": "bi-film",
            "route": "/movies",
            "api_endpoint": null,
            "accordion_buttons": [
            {
                "title": "Popular Movies",
                "icon": "bi-star-fill",
                "route": "/movies/popular",
                "api_endpoint": "movie/popular",
                "accordion_buttons": null
            },
            {
                "title": "Top Rated",
                "icon": "bi-star-half",
                "route": "/movies/top_rated",
                "api_endpoint": "movie/top_rated",
                "accordion_buttons": null
            },
            {
                "title": "Categories",
                "icon": "bi-list-nested",
                "route": "/movies/categories",
                "api_endpoint": "genre/movie/list",
                "accordion_buttons": null
            }
            ]
        },
      "TV Shows": {
        "title": "TV Shows",
        "icon": "bi-tv",
        "route": "/tv_shows",
        "api_endpoint": null,
        "accordion_buttons": [
          {
            "title": "Popular TV Shows",
            "icon": "bi-star-fill",
            "route": "/tv/popular",
            "api_endpoint": "tv/popular",
            "accordion_buttons": null
          },
          {
            "title": "Top Rated",
            "icon": "bi-star-half",
            "route": "/tv/top_rated",
            "api_endpoint": "tv/top_rated",
            "accordion_buttons": null
          },
          {
            "title": "Categories",
            "icon": "bi-list-nested",
            "route": "/tv/categories",
            "api_endpoint": "genre/tv/list",
            "accordion_buttons": null
          }
        ]
      }
    }
  }
}
"""

""" 
class NavEntry:
    def __init__(self, title, icon, route, api_endpoint=None):
        self.title = title
        self.icon = icon
        self.route = route
        self.api_endpoint = api_endpoint  # API endpoint for fetching data
        self.accordion_buttons = []

    def add_accordion_button(self, title, icon, route, api_endpoint):
        self.accordion_buttons.append(NavEntry(title, icon, route, api_endpoint))

    def as_dict(self):
        # Convert the navigation entry into a dictionary format for Flask templates
        return {
            'title': self.title,
            'icon': self.icon,
            'route': self.route,
            'api_endpoint': self.api_endpoint,
            'accordion': [accordion.as_dict() for accordion in self.accordion_buttons] if self.accordion_buttons else None
        }



class MoviesNavEntry(NavEntry):
    def __init__(self, title, icon, route):
        super().__init__(title, icon, route)
        self.item_type = 'movie'
        self.initialize_movies_accordion()

    def initialize_movies_accordion(self):
        self.add_accordion_button('Popular Movies', 'bi-star-fill', '/movies/popular', 'movie/popular')
        self.add_accordion_button('Top Rated', 'bi-star-half', '/movies/top_rated', 'movie/top_rated')
        self.add_accordion_button('Categories', 'bi-list-nested', '/movies/categories', 'genre/movie/list')
        
        
class TVShowsNavEntry(NavEntry):
    def __init__(self, title, icon, route):
        super().__init__(title, icon, route)
        self.item_type = 'tv'
        self.initialize_tv_shows_accordion()

    def initialize_tv_shows_accordion(self):
        # Here, add children with titles, icons, routes, and specific API endpoints
        self.add_accordion_button('Popular TV Shows', 'bi-star-fill', '/tv/popular', 'tv/popular')
        self.add_accordion_button('Top Rated', 'bi-star-half', '/tv/top_rated', 'tv/top_rated')
        self.add_accordion_button('Categories', 'bi-list-nested', '/tv/categories', 'genre/tv/list')

"""
