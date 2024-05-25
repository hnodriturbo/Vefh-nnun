# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ////////////////        Author: Hreiðar Pétursson        \\\\\\\\\\\\\\\\
# //////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
# /////////////              -- Skilaverkefni 3 --            \\\\\\\\\\\\\
# ////      Description: Manages dictonaries for other files to        \\\\
# //   retrive from. These dictionaries represent everything that is     \\
# /             in the navbar, endpoints, args like item_type             \
# ////////                  to be movie or tv show                 \\\\\\\\
# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# navigation_navbar.py

def make_nav_route_endpoint(base_route, is_genre=False):
    """ Simple function to derive route and endpoint from a base route. """
    route = f'/{base_route}' if base_route else '/'
    endpoint = base_route.replace("/", "") if not is_genre else f"genre/{base_route.replace('/', '')}/list"
    return route, endpoint

# Apply this function to simplify your navigation setup:
def create_navigation():
    nav_items = {
        'Home': ('', 'Home', 'bi-house'),
        'About': ('about_author', 'About Author', 'bi-person-raised-hand'),
        'Movies': [
            ('movies/popular', 'Popular Movies', 'bi-film'),
            ('movies/top_rated', 'Top Rated Movies', 'bi-star'),
            ('movies/categories', 'Movie Categories', 'bi-list', True)  # True indicates category
        ],
        'TV Shows': [
            ('tv/popular', 'Popular TV Shows', 'bi-tv'),
            ('tv/top_rated', 'Top Rated TV Shows', 'bi-star'),
            ('tv/categories', 'TV Shows Categories', 'bi-list', True)
        ]
    }
    
    navigation = {'main_navigation': {}, 'accordion': {'Movies': {}, 'TV Shows': {}}}
    
    for key, val in nav_items.items():
        if key in ['Home', 'About']:
            route, endpoint = make_nav_route_endpoint(val[0])
            navigation['main_navigation'][key] = {'title': val[1], 'icon': val[2], 'route': route, 'endpoint': endpoint}
        else:
            for item in val:
                route, endpoint = make_nav_route_endpoint(item[0], is_genre=item[3] if len(item) > 3 else False)
                navigation['accordion'][key][item[1]] = {'title': item[1], 'icon': item[2], 'route': route, 'endpoint': endpoint}

    return navigation


""" 
Description:
            When executing this function it will create the "navigation" dict of dicts.
            Layout and the structure has been mapped and created and put here at the
            top of this file.
            
            There are two main parts of the "navigation" dictionary. That is the
            "main_navigation" and then there is the "accordion" which is split into
            two different main dictionaries because the accordion is the dictionary
            for the two dropdown buttons that instead of dropping down normal dropdown
            menu it opens an accordion in the row below the navbar.
            
            "accordion" dictionary is split into two main sections (buttons) that represent
            "Movies" button and "TV Shows" button. Then inside each of them is basic
            information, like "title", "icon" and "route"
            
            These "accordion" buttons both have one extra key:value pair that's called 
            "item_type". This item type info is crucial in the endpoint building for the API.
            
            Then each button has extra dictionaries for the "accordion_buttons". 
            
            The accordion buttons are the buttons that are in the dropped
            down accordion. I use bootstrap for the accordion movements and displaying.
            Each accordion has three buttons and each of them has the basic info as the other
            parts of the dictionary, "title", "icon" and of course the "route".
            
            With this information it's possible to create a very functional navbar which is
            the most importand part of the website, since this is the whole navigation around
            all the aspects of this webpage.
"""

# navigation_navbar.py

from categories import TV_Shows_Categories, Movies_Categories

def create_navigation():
    navigation = {
        'main_navigation': {
            'Home': {
                'title': 'Home',
                'icon': 'bi-house',
                'route': '/',
                'endpoint': None  # No API call needed for home
            },
            'About': {
                'title': 'About Author',
                'icon': 'bi-person-raised-hand',
                'route': '/about_author',
                'endpoint': None  # No API call needed for about
            },
        },
        'accordion': {
            'Movies': {
                'item_type': 'movie',
                'title': 'Movies',
                'icon': 'bi-film',
                'route': 'accordion_movies',
                'accordion_buttons': {
                    'popular': {
                        'title': 'Popular Movies',
                        'route': '/movies/popular',
                        'icon': 'bi-film',
                        'endpoint': 'movie/popular'
                    },
                    'top_rated': {
                        'title': 'Top Rated Movies',
                        'route': '/movies/top_rated',
                        'icon': 'bi-star',
                        'endpoint': 'movie/top_rated'
                    },
                    'categories': {
                        'title': 'Movie Categories',
                        'route': '/movies/categories',
                        'icon': 'bi-list',
                        'endpoint': 'genre/movie/list'
                    }
                }
            },
            'TV Shows': {
                'item_type': 'tv',
                'title': 'TV Shows',
                'icon': 'bi-film',
                'route': 'open_accordion_tv_shows',
                'accordion_buttons': {
                    'popular': {
                        'title': 'Popular TV Shows',
                        'icon': 'bi-tv',
                        'route': '/tv/popular',
                        'endpoint': 'tv/popular'
                    },
                    'top_rated': {
                        'title': 'Top Rated TV Shows',
                        'icon': 'bi-star',
                        'route': '/tv/top_rated',
                        'endpoint': 'tv/top_rated'
                    },
                    'categories': {
                        'title': 'TV Shows Categories',
                        'icon': 'bi-list',
                        'route': '/tv/categories',
                        'endpoint': 'genre/tv/list'
                    }
                }
            }
        },
        'categories': {
            'Movies': {genre_id: detail for genre_id, detail in Movies_Categories.items()},
            'TV Shows': {genre_id: detail for genre_id, detail in TV_Shows_Categories.items()}
        }
    }
    return navigation



