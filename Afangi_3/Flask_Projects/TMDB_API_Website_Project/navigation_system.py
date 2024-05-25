            # ########## Hreiðar Pétursson ##########
            #  ######## Vefhönnun  Áfanginn ########
            #   ######### Skilaverkefni 3 #########
            #    ########   Apríl  2024   ########
            
            
            
class NavigationSystem:
    def __init__(self):
        self.nav_buttons = {}
        self.accordion_buttons = {}
        self.genres = {'Movies': {}, 'TV Shows': {}}
        self.initialize_nav_buttons()
        self.initialize_accordion_buttons()
        self.initialize_genres()
        
        
    def initialize_nav_buttons(self):
        """Initialize the standard navigation buttons."""
        self.nav_buttons['Home'] = {
            'app_route': '/',
            'icon': 'bi-house'
            }
        self.nav_buttons['About Author'] = {
            'app_route': '/about_author',
            'icon': 'bi-person'
            }
        print(f"Initialized nav_buttons")

    def initialize_accordion_buttons(self):
        """Initialize the accordion buttons for Movies and TV Shows."""
        self.accordion_buttons['Movies'] = {
            'item_type': 'movie',
            'icon': 'bi-film',
            'accordion': 'movie_accordion',
            'buttons': self.get_movie_buttons()
        }
        self.accordion_buttons['TV Shows'] = {
            'item_type': 'tv',
            'icon': 'bi-tv',
            'accordion': 'tv_accordion',
            'buttons': self.get_tv_show_buttons()
        }
        print(f"Initialized accordion_buttons")
        
        
    def get_movie_buttons(self):
        """Generate buttons for the Movies section."""
        return {
            'popular': {'title': 'Popular Movies', 'icon': 'bi-star-fill', 'app_route': 'popular', 'api_endpoint': 'movie/popular'},
            'top_rated': {'title': 'Top Rated Movies', 'icon': 'bi-star-half', 'app_route': 'top_rated', 'api_endpoint': 'movie/top_rated'},
            'categories': {'title': 'Movie Categories', 'icon': 'bi-list-nested', 'app_route': 'list_categories', 'api_endpoint': 'genre/movie/list'}
        }

    def get_tv_show_buttons(self):
        """Generate buttons for the TV Shows section."""
        return {
            'popular': {'title': 'Popular TV Shows', 'icon': 'bi-star-fill', 'app_route': 'popular', 'api_endpoint': 'tv/popular'},
            'top_rated': {'title': 'Top Rated TV Shows', 'icon': 'bi-star-half', 'app_route': 'top_rated', 'api_endpoint': 'tv/top_rated'},
            'categories': {'title': 'TV Show Categories', 'icon': 'bi-list-nested', 'app_route': 'list_categories', 'api_endpoint': 'genre/tv/list'}
        }
        
    def initialize_genres(self):
        """Initialize specific dictionaries for movie and TV show genres."""
        # Setup for Movie genres
        movie_genre_data = {
            28: {'title': 'Action', 'icon': 'bi-bolt', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=28'},
            12: {'title': 'Adventure', 'icon': 'bi-compass', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=12'},
            16: {'title': 'Animation', 'icon': 'bi-film', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=16'},
            35: {'title': 'Comedy', 'icon': 'bi-emoji-smile', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=35'},
            80: {'title': 'Crime', 'icon': 'bi-shield-shaded', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=80'},
            99: {'title': 'Documentary', 'icon': 'bi-camera-reels', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=99'},
            18: {'title': 'Drama', 'icon': 'bi-mask', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=18'},
            10751: {'title': 'Family', 'icon': 'bi-people', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=10751'},
            14: {'title': 'Fantasy', 'icon': 'bi-stars', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=14'},
            36: {'title': 'History', 'icon': 'bi-book-half', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=36'},
            27: {'title': 'Horror', 'icon': 'bi-droplet-half', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=27'},
            10402: {'title': 'Music', 'icon': 'bi-music-note-beamed', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=10402'},
            9648: {'title': 'Mystery', 'icon': 'bi-eye', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=9648'},
            10749: {'title': 'Romance', 'icon': 'bi-heart-half', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=10749'},
            878: {'title': 'Science Fiction', 'icon': 'bi-gear-wide-connected', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=878'},
            10770: {'title': 'TV Movie', 'icon': 'bi-tv', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=10770'},
            53: {'title': 'Thriller', 'icon': 'bi-speedometer2', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=53'},
            10752: {'title': 'War', 'icon': 'bi-shield-fill-plus', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=10752'},
            37: {'title': 'Western', 'icon': 'bi-person', 'app_route': 'categories', 'api_endpoint': 'discover/movie?with_genres=37'}
        }


        # Setup for TV show genres
        tv_genre_data = {
            10759: {'title': 'Action & Adventure', 'icon': 'bi-hurricane', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10759'},
            16: {'title': 'Animation', 'icon': 'bi-film', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=16'},
            35: {'title': 'Comedy', 'icon': 'bi-emoji-laughing', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=35'},
            80: {'title': 'Crime', 'icon': 'bi-shield-lock', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=80'},
            99: {'title': 'Documentary', 'icon': 'bi-camera-reels', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=99'},
            18: {'title': 'Drama', 'icon': 'bi-mask', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=18'},
            10751: {'title': 'Family', 'icon': 'bi-people-fill', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10751'},
            10762: {'title': 'Kids', 'icon': 'bi-balloon-heart-fill', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10762'},
            9648: {'title': 'Mystery', 'icon': 'bi-eye', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=9648'},
            10763: {'title': 'News', 'icon': 'bi-newspaper', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10763'},
            10764: {'title': 'Reality', 'icon': 'bi-eyeglasses', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10764'},
            10765: {'title': 'Sci-Fi & Fantasy', 'icon': 'bi-stars', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10765'},
            10766: {'title': 'Soap', 'icon': 'bi-bubbles', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10766'},
            10767: {'title': 'Talk', 'icon': 'bi-mic-mute-fill', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10767'},
            10768: {'title': 'War & Politics', 'icon': 'bi-shield-fill-plus', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=10768'},
            37: {'title': 'Western', 'icon': 'bi-hat-cowboy', 'app_route': 'categories', 'api_endpoint': 'discover/tv?with_genres=37'}
        }

        # Add the genre list details into dictionaries "Movies" & "TV Shows"
        self.genres['Movies'] = movie_genre_data
        self.genres['TV Shows'] = tv_genre_data
        
        print(f"Initialized Genres for Movies and TV Shows")
        # print(self.genres['Movies'])
        # print(self.genres['TV Shows'])
    
"""
         
#navigation = {
    'Home': {
        'app_route': '/',
        'icon': 'bi-house'
    },
    'About Author': {
        'app_route': '/about_author',
        'icon': 'bi-person'
    },
    'Movies': {
        'item_type': 'movie',
        'icon': 'bi-film',
        'accordion': 'movie_accordion',
        
        'buttons': {
            
            'popular': {
                'title': 'Popular Movies',
                'icon': 'bi-star-fill',
                'app_route': 'popular',
                'api_endpoint': 'movie/popular'
            },
            
            'top_rated': {
                'title': 'Top Rated Movies',
                'icon': 'bi-star-half',
                'app_route': 'top_rated',
                'api_endpoint': 'movie/top_rated'
            },
            
            'categories': {
                'title': 'Movie Categories',
                'icon': 'bi-list-nested',
                'app_route': 'list_categories',
                'api_endpoint': 'genre/movie/list'
            }
            
        }
        
    },
    
    
    
    'TV Shows': {
        
        'item_type': 'tv',
        'icon': 'bi-tv',
        'accordion': 'tv_accordion',
        
        'buttons': {
            
            'popular': {
                'title': 'Popular TV Shows',
                'icon': 'bi-star-fill',
                'app_route': 'popular',
                'api_endpoint': 'tv/popular'
            },
            
            'top_rated': {
                'title': 'Top Rated TV Shows',
                'icon': 'bi-star-half',
                'app_route': 'top_rated',
                'api_endpoint': 'tv/top_rated'
            },
            
            'categories': {
                'title': 'TV Show Categories',
                'icon': 'bi-list-nested',
                'app_route': 'list_categories',
                'api_endpoint': 'genre/tv/list'
            }
            
        }
        
    }
"""        
        
        
        

        
        
        
# Example usage
#nav_system = NavigationSystem()
#print(nav_system.nav_buttons)
#print(nav_system.accordion_buttons)
#print(nav_system)

#for dict in nav_system.nav_buttons, nav_system.accordion_buttons:
#    print(dict)


# Pretty printing the navigation structure using Python's pprint
#import pprint
#pprint.pprint(nav_system.accordion_buttons)

""" 
    Description: Navigational Dictionaries
    
        - Pretty printed navigational dictionaries:
        
        {
            "nav_buttons": {
                "Home": "/",
                "About Author": "/about_author"
            },
            
            
            
            
            
            "accordion_buttons": {
                
                "Movies": {
                    "item_type": "movie",
                    "icon": "bi-film",
                    "accordion": "movie_accordion",
                    
                    "buttons": {
                        
                        "popular": {
                            "title": "Popular Movies",
                            "icon": "bi-star-fill",
                            "app_route": "/movies/popular",
                            "section": "popular",
                            "api_endpoint": "movie/popular"
                        },
                        
                        "top_rated": {
                            "title": "Top Rated Movies",
                            "icon": "bi-star-half",
                            "app_route": "/movies/top_rated",
                            "section": "top_rated",
                            "api_endpoint": "movie/top_rated"
                        },
                        
                        "categories": {
                            "title": "Movie Categories",
                            "icon": "bi-list-nested",
                            "app_route": "/movies/categories",
                            "section": "list",
                            "api_endpoint": "genre/movie/list"
                        }
                        
                    }
                },
                
                
                
                
                "TV Shows": {
                    
                    "item_type": "tv",
                    "icon": "bi-tv",
                    "accordion": "tv_accordion",
                    
                    "buttons": {
                        "popular": {
                        "title": "Popular TV Shows",
                        "icon": "bi-star-fill",
                        "app_route": "/tv/popular",
                        "section": "popular",
                        "api_endpoint": "tv/popular"
                        },
                        
                        "top_rated": {
                        "title": "Top Rated TV Shows",
                        "icon": "bi-star-half",
                        "app_route": "/tv/top_rated",
                        "section": "top_rated",
                        "api_endpoint": "tv/top_rated"
                        },
                        
                        "categories": {
                        "title": "TV Show Categories",
                        "icon": "bi-list-nested",
                        "app_route": "/tv/categories",
                        "section": "list",
                        "api_endpoint": "genre/tv/list"
                        }
                        
                    }
                }
            }
        }


"""


























      
        
"""         
    def get_movie_buttons(self):
        return {
            
            'popular': {
                'title': 'Popular Movies',
                'icon': 'bi-star-fill',
                'app_route': 'popular',
                'api_endpoint': 'movie/popular'
            },
            
            'top_rated': {
                'title': 'Top Rated Movies',
                'icon': 'bi-star-half',
                'app_route': 'top_rated',
                'api_endpoint': 'movie/top_rated'
            },
            
            'categories': {
                'title': 'Movie Categories',
                'icon': 'bi-list-nested',
                'app_route': 'categories',
                'api_endpoint': 'genre/movie/list'
            }
            
        }

    def get_tv_show_buttons(self):
        return {
            'popular': {
                'title': 'Popular TV Shows',
                'icon': 'bi-star-fill',
                'app_route': 'popular',
                'api_endpoint': 'tv/popular'
            },
            'top_rated': {
                'title': 'Top Rated TV Shows',
                'icon': 'bi-star-half',
                'app_route': 'top_rated',
                'api_endpoint': 'tv/top_rated'
            },
            'categories': {
                'title': 'TV Show Categories',
                'icon': 'bi-list-nested',
                'app_route': 'categories',
                'api_endpoint': 'genre/tv/list'
            }
        }
"""