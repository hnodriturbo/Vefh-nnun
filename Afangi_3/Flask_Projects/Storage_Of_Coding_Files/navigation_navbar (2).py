            # ########## Hreiðar Pétursson ##########
            #  ######## Vefhönnun  Áfanginn ########
            #   ######### Skilaverkefni 3 #########
            #    ########   Apríl  2024   ########





class NavEntry:
    def __init__(self, title, icon, route, api_endpoint=None):
        self.title = title
        self.icon = icon
        self.route = route
        self.api_endpoint = api_endpoint
        self.sections = {}

    def add_section(self, key, title, icon, route, api_endpoint):
        self.sections[key] = NavEntry(title, icon, route, api_endpoint)

    def as_dictionary(self):
        """ Converts the navigation entry into a dictionary format. """
        return {
            'sections': {k: v.as_dictionary() for k, v in self.sections.items()}
        } if self.sections else {
            'title': self.title,
            'icon': self.icon,
            'route': self.route,
            'api_endpoint': self.api_endpoint
        }

class MoviesNavEntry(NavEntry):
    def __init__(self, title, icon, route):
        super().__init__(title, icon, route)
        self.initialize_movies_sections()

    def initialize_movies_sections(self):
        self.add_section('popular', 'Popular Movies', 'bi-star-fill', '/movies/popular', 'movie/popular')
        self.add_section('top_rated', 'Top Rated', 'bi-star-half', '/movies/top_rated', 'movie/top_rated')
        self.add_section('categories', 'Categories', 'bi-list-nested', '/movies/categories', 'genre/movie/list')

class TVShowsNavEntry(NavEntry):
    def __init__(self, title, icon, route):
        super().__init__(title, icon, route)
        self.initialize_tv_shows_sections()

    def initialize_tv_shows_sections(self):
        self.add_section('popular', 'Popular TV Shows', 'bi-star-fill', '/tv/popular', 'tv/popular')
        self.add_section('top_rated', 'Top Rated', 'bi-star-half', '/tv/top_rated', 'tv/top_rated')
        self.add_section('categories', 'Categories', 'bi-list-nested', '/tv/categories', 'genre/tv/list')

def create_navigation():
    nav_root = NavEntry('root', None, None)  # Root does not contribute to the output
    nav_root.add_section('Home', 'Home', 'bi-house', '/', None)
    nav_root.add_section('About Author', 'About Author', 'bi-person', '/about_author', None)

    movies = MoviesNavEntry('Movies', 'bi-film', '/movies')
    tv_shows = TVShowsNavEntry('TV Shows', 'bi-tv', '/tv_shows')

    nav_root.sections['Movies'] = movies
    nav_root.sections['TV Shows'] = tv_shows

    return {k: v.as_dictionary() for k, v in nav_root.sections.items()}

""" 
class Navigation_Manager:
    def __init__(self):
        self.entries = []

    def add_entry(self, title, icon, route, api_endpoint=None):
        entry = Nav_Entry(title, icon, route, api_endpoint)
        self.entries.append(entry)
        return entry

    def get_navigation_data(self):
        return {entry.title: entry.as_dictionary() for entry in self.entries}


"""
""" 
def create_navigation():
    nav_manager = Nav_Entry('root', None, None)  # Root entry
    nav_manager.add_section('Home', 'Home', 'bi-house', '/', None)
    nav_manager.add_section('About Author', 'About Author', 'bi-person', '/about_author', None)

    movies = Movies_Nav_Entry('Movies', 'bi-film', '/movies')
    tv_shows = TV_Shows_Nav_Entry('TV Shows', 'bi-tv', '/tv_shows')

    nav_manager.sections['Movies'] = movies
    nav_manager.sections['TV Shows'] = tv_shows

    return nav_manager.as_dictionary()
"""
""" 
   - Pretty Printed Dictionary:
   
        {
            
            
            'Home': {
                'title': 'Home',
                'icon': 'bi-house',
                'route': '/',
                'api_endpoint': None,
                'accordion_buttons': None
            },
            
            
            'About Author': {
                'title': 'About Author',
                'icon': 'bi-person',
                'route': '/about_author',
                'api_endpoint': None,
                'accordion_buttons': None
            },
            
            
            'Movies': {
                'title': 'Movies',
                'icon': 'bi-film',
                'route': '/movies',
                'api_endpoint': None,
                'accordion_buttons': [
                    {
                        'title': 'Popular Movies',
                        'icon': 'bi-star-fill',
                        'route': '/movies/popular',
                        'api_endpoint': 'movie/popular',
                        'accordion_buttons': None
                    },
                    {
                        'title': 'Top Rated',
                        'icon': 'bi-star-half',
                        'route': '/movies/top_rated',
                        'api_endpoint': 'movie/top_rated',
                        'accordion_buttons': None
                    },
                    {
                        'title': 'Categories',
                        'icon': 'bi-list-nested',
                        'route': '/movies/categories',
                        'api_endpoint': 'genre/movie/list',
                        'accordion_buttons': None
                    }
                ] # End of accordion buttons list of dicts for the Movies accordion button
            }, # End of Movies menu dropdown button of accordion buttons
            
            
            'TV Shows': {
                'title': 'TV Shows',
                'icon': 'bi-tv',
                'route': '/tv_shows',
                'api_endpoint': None,
                'accordion_buttons': [
                    {
                        'title': 'Popular TV Shows',
                        'icon': 'bi-star-fill',
                        'route': '/tv/popular',
                        'api_endpoint': 'tv/popular',
                        'accordion_buttons': None
                    },
                    {
                        'title': 'Top Rated',
                        'icon': 'bi-star-half',
                        'route': '/tv/top_rated',
                        'api_endpoint': 'tv/top_rated',
                        'accordion_buttons': None
                    },
                    {
                        'title': 'Categories',
                        'icon': 'bi-list-nested',
                        'route': '/tv/categories',
                        'api_endpoint': 'genre/tv/list',
                        'accordion_buttons': None
                    }
                ] # End of accordion buttons list of dicts for the TV Shows accordion button
            } # End of TV Shows menu dropdown button of accordion buttons
        } # End of the dict


"""
    
    
    
    


    
    
    
    
    
"""           
def create_genre_listings(movie_categories, tv_categories):
    genres = {
        'movies': {},
        'tv_shows': {}
    }
    for genre_id, details in movie_categories.items():
        genres['movies'][genre_id] = Genre_Nav_Entry(genre_id, details['title'], details['icon'], 'movie').as_dictionary()
    for genre_id, details in tv_categories.items():
        genres['tv_shows'][genre_id] = Genre_Nav_Entry(genre_id, details['title'], details['icon'], 'tv').as_dictionary()
    return genres
"""
   
""" 
# A special Nav_Entry that is tailored to handle genre listings separately
class Genre_Nav_Entry(Nav_Entry):
    def __init__(self, genre_id, title, icon, item_type):
        route = f'/{item_type}/genre/{genre_id}'
        api_endpoint = route
        super().__init__(title, icon, route, api_endpoint)
        self.genre_id = genre_id
        self.item_type = item_type

"""

 



""" Use this print statements to print out the dictionary """
# Print the structured navigation to see the full setup
nav_data = create_navigation()
# print(nav_data)


# Pretty printing the navigation structure using Python's pprint
import pprint
pprint.pprint(nav_data)


