# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ////////////////        Author: Hreiðar Pétursson        \\\\\\\\\\\\\\\\
# //////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
# /////////////              -- Skilaverkefni 3 --            \\\\\\\\\\\\\
# ////      Description: Manages dictonaries for other files to        \\\\
# //   retrive from. These dictionaries represent everything that is     \\
# /             in the navbar, endpoints, args like item_type             \
# ////////                  to be movie or tv show                 \\\\\\\\
# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



"""
create_navigation() creates a navigational dict with links for the website's navbar.

This dictionary includes:

    - `main_navigation`: Contains primary links such as "Home" and "About the Author", 
    
    - `accordion`:  Houses two main categories, "Movies" and "TV Shows", each with 
                    accordion for specific sub-categories like "Popular" and "Top Rated", 
                    along with a special route for categories.
                    
    - `categories`: Maps genres under "Movies" and "TV Shows" with specific titles and 
                    icons, enabling dynamic endpoint generation crucial for API interactions.

This setup allows for a dynamic, functional navbar that serves the site navigation.
"""
# navigation_navbar.py python codes file for the navbar and accordion buttons and details

# Function that generates a nav entry and takes base_route, title, icon & is_category boolean
def generate_nav_entry(route, title, icon, item_type, is_listing=False):
    """ Generate navigation entry with automatic endpoint and route setup. """
    
    # Make the endpoint the same as base_route but take out the slash (no need for double coding)
    endpoint = route.strip("/")
    
    # If is_category boolean is True then make the endpoint to be this
    if is_listing:
        endpoint = f"genre/{item_type}/list"
    else:
        endpoint = f"{item_type}/{route}"
      
        
    # Return dictionary with the Title, icon, route & endpoint
    return {
        'route': route,
        'title': title,
        'icon' : icon,
        'endpoint': endpoint 
    }
        # endpoint changes to genre/{endpoint}/list if 
        # is_listin is True, which is the case when the 
        # button List Cateories is pressed
        

def generate_nav_entry(route, title, icon, is_listing=False):
    endpoint = route.strip('/')
    if is_listing:
        endpoint = f"genre/{endpoint}/list"
    return {'route': route, 'title': title, 'icon': icon, 'endpoint': endpoint}

from categories import tv_categories, movie_categories


def create_navigation():
    """Create a complete navigation dictionary for the application."""
    navigation = {
        'main_navigation': {
            'Home': generate_nav_entry('/', 'Home', 'bi-house'),
            'About': generate_nav_entry('/about_author', 'About Author', 'bi-person'),
        },
        'accordion': {
            'movie': {
                'item_type': 'movie',
                'title': 'Movies',
                'icon': 'bi-film',
                'route': '/movies',
                'accordion_buttons': {
                    'popular': generate_nav_entry('/movies/popular', 'Popular Movies', 'bi-film'),
                    'top_rated': generate_nav_entry('/movies/top_rated', 'Top Rated Movies', 'bi-star'),
                    'categories': generate_nav_entry('/movies/categories', 'Movie Categories', 'bi-list', is_listing=True)
                }
            },
            'tv': {
                'item_type': 'tv',
                'title': 'TV Shows',
                'icon': 'bi-tv',
                'route': '/tv_shows',
                'accordion_buttons': {
                    'popular': generate_nav_entry('/tv_shows/popular', 'popular', 'Popular TV Shows', 'bi-tv'),
                    'top_rated': generate_nav_entry('/tv_shows/top_rated', 'top_rated', 'Top Rated TV Shows', 'bi-star'),
                    'categories': generate_nav_entry('/tv_shows/categories', 'list' , 'TV Shows Categories', 'bi-list', is_listing=True)
                }
            }
        },
        'categories': {
            'Movies': {genre_id: {'title': detail['title'], 'icon': f"bi-{detail['icon']}"}
                       for genre_id, detail in movie_categories.items()},
            'TV Shows': {genre_id: {'title': detail['title'], 'icon': f"bi-{detail['icon']}"}
                         for genre_id, detail in tv_categories.items()}
        }    
    }
    return navigation

