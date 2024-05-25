


from categories import TV_Shows_Categories, Movies_Categories




def create_navigation():
    
    navigation = {
        
        # 'main_navigation' - the two buttons on the right that says "Home" and "About"
        'main_navigation': {
            
            # Home dict
            'Home': {
                'title': 'Home',
                'icon': 'bi-house' ,
                'route': '/'
            },
            
            # About dict
            'About': {
                'title': 'About Author',
                'icon': 'bi-person-raised-hand',
                'route': '/about_author'
                
            },
            
        }, 
        
##### ------------------------------------------------------------------------------ #####
        
        # Accordion buttons (Movies, TV Shows)
        'accordion': {
            
            
            'Movies': {
                
                # Item type is here to be represented in all of this dictionary 
                # (making it no need for putting this in every dictionary inside this one)
                'item_type': 'movie',
                
                'title': 'Movies',
                'icon': 'bi-film',
                
                # Use the route value to open the correct accordion
                'route': 'accordion_movies',
                
                
                'accordion_buttons': 
                                    {
                                    'popular': {
                                        'title': 'Popular Movies',
                                        'route': '/movies/popular',
                                        'icon': 'bi-film'
                                        },
                                    'top_rated': {
                                        'title': 'Top Rated Movies',
                                        'route': '/movies/top_rated',
                                        'icon': 'bi-star'
                                        },
                                    'categories': {
                                        'title': 'Movie Categories',
                                        'route': '/movies/categories',
                                        'icon': 'bi-list'
                                        }
                                    }
            },
            
            
            
            'TV Shows': {
                
                # Item type is here to be represented in all of this dictionary 
                # (making it no need for putting this in every dictionary inside this one)
                'item_type': 'tv',
                
                'title': 'TV Shows',
                'icon': 'bi-film',
                
                # Use the route value to open the correct accordion
                'route': 'open_accordion_tv_shows',
                
                
                'accordion_buttons': 
                                    {
                                    'popular': {
                                        'title': 'Popular TV Shows',
                                        'icon': 'bi-tv',
                                        'route': '/tv/popular'
                                    },
                                    'top_rated': {
                                        'title': 'Top Rated TV Shows',
                                        'icon': 'bi-star',
                                        'route': '/tv/top_rated'
                                        
                                    },
                                    'categories': {
                                        'title': 'TV Shows Categories',
                                        'icon': 'bi-list',
                                        'route': '/tv/categories'
                                        
                                    }
                            }
            }
        },
        
        # 'categories' dict that uses list comprehension to unpack the items in the below dicts
        'categories': {

                    # I use list comprehension to iterate over the dictionary of categories to create 
                    # these 'Movies' dictionary and 'TV Shows' dictionary that hold all the information needed
                    'Movies': {genre_id: detail for genre_id, detail in Movies_Categories.items()},
                    
                    'TV Shows': {genre_id: detail for genre_id, detail in TV_Shows_Categories.items()}
        } 
        
    } # Navigation

    return navigation




""" 
Description:
            This file contains everything I have commented out in the
            navigation_navbar.py file. I update the file regularly during
            the page building and therefore I update the codes in the file
            but for reverting purposes I want to keep these codes in the
            rare case I would need to go back and use them again.
"""



""" 
# Updated TV Shows Categories with route details
TV_Shows_Categories = {
    10759: {'title': 'Action & Adventure', 'icon': 'bi-fist-raised', 'route': '/tv/genre/10759'},
    16: {'title': 'Animation', 'icon': 'bi-film', 'route': '/tv/genre/16'},
    35: {'title': 'Comedy', 'icon': 'bi-face-grin-squint', 'route': '/tv/genre/35'},
    80: {'title': 'Crime', 'icon': 'bi-mask', 'route': '/tv/genre/80'},
    99: {'title': 'Documentary', 'icon': 'bi-camera', 'route': '/tv/genre/99'},
    18: {'title': 'Drama', 'icon': 'bi-theater-masks', 'route': '/tv/genre/18'},
    10751: {'title': 'Family', 'icon': 'bi-house', 'route': '/tv/genre/10751'},
    10762: {'title': 'Kids', 'icon': 'bi-people-fill', 'route': '/tv/genre/10762'},
    9648: {'title': 'Mystery', 'icon': 'bi-user-secret', 'route': '/tv/genre/9648'},
    10763: {'title': 'News', 'icon': 'bi-newspaper', 'route': '/tv/genre/10763'},
    10764: {'title': 'Reality', 'icon': 'bi-glasses', 'route': '/tv/genre/10764'},
    10765: {'title': 'Sci-Fi & Fantasy', 'icon': 'bi-stars', 'route': '/tv/genre/10765'},
    10766: {'title': 'Soap', 'icon': 'bi-droplet-half', 'route': '/tv/genre/10766'},
    10767: {'title': 'Talk', 'icon': 'bi-mic-fill', 'route': '/tv/genre/10767'},
    10768: {'title': 'War & Politics', 'icon': 'bi-bank2', 'route': '/tv/genre/10768'},
    37: {'title': 'Western', 'icon': 'bi-hat-cowboy', 'route': '/tv/genre/37'}
}

"""


""" 
# Updated Movies Categories with route details
Movies_Categories = {
    28: {
        'title': 'Action', 
        'icon': 'bi-bolt', 
        'route': '/movies/genre/28'
    },
    12: {
        'title': 'Adventure', 
        'icon': 'bi-hat-cowboy-side', 
        'route': '/movies/genre/12'
    },
    16: {'title': 'Animation', 'icon': 'bi-film', 'route': '/movies/genre/16'},
    35: {'title': 'Comedy', 'icon': 'bi-face-grin-squint', 'route': '/movies/genre/35'},
    80: {'title': 'Crime', 'icon': 'bi-mask', 'route': '/movies/genre/80'},
    99: {'title': 'Documentary', 'icon': 'bi-camera', 'route': '/movies/genre/99'},
    18: {'title': 'Drama', 'icon': 'bi-theater-masks', 'route': '/movies/genre/18'},
    10751: {'title': 'Family', 'icon': 'bi-house', 'route': '/movies/genre/10751'},
    14: {'title': 'Fantasy', 'icon': 'bi-dragon', 'route': '/movies/genre/14'},
    36: {'title': 'History', 'icon': 'bi-landmark', 'route': '/movies/genre/36'},
    27: {'title': 'Horror', 'icon': 'bi-ghost', 'route': '/movies/genre/27'},
    10402: {'title': 'Music', 'icon': 'bi-music', 'route': '/movies/genre/10402'},
    9648: {'title': 'Mystery', 'icon': 'bi-user-secret', 'route': '/movies/genre/9648'},
    10749: {'title': 'Romance', 'icon': 'bi-heart', 'route': '/movies/genre/10749'},
    878: {'title': 'Science Fiction', 'icon': 'bi-rocket', 'route': '/movies/genre/878'},
    10770: {'title': 'TV Movie', 'icon': 'bi-tv', 'route': '/movies/genre/10770'},
    53: {'title': 'Thriller', 'icon': 'bi-knife', 'route': '/movies/genre/53'},
    10752: {'title': 'War', 'icon': 'bi-helmet-battle', 'route': '/movies/genre/10752'},
    37: {'title': 'Western', 'icon': 'bi-hat-cowboy', 'route': '/movies/genre/37'}
}

"""


""" 
# The Movies Categories titles and icons
Movies_Categories = {
    28: {'title': 'Action', 'icon': 'bi-bolt'},
    12: {'title': 'Adventure', 'icon': 'bi-hat-cowboy-side'},
    16: {'title': 'Animation', 'icon': 'bi-film'},
    35: {'title': 'Comedy', 'icon': 'bi-face-grin-squint'},
    80: {'title': 'Crime', 'icon': 'bi-mask'},
    99: {'title': 'Documentary', 'icon': 'bi-camera'},
    18: {'title': 'Drama', 'icon': 'bi-theater-masks'},
    10751: {'title': 'Family', 'icon': 'bi-house'},
    14: {'title': 'Fantasy', 'icon': 'bi-dragon'},
    36: {'title': 'History', 'icon': 'bi-landmark'},
    27: {'title': 'Horror', 'icon': 'bi-ghost'},
    10402: {'title': 'Music', 'icon': 'bi-music'},
    9648: {'title': 'Mystery', 'icon': 'bi-user-secret'},
    10749: {'title': 'Romance', 'icon': 'bi-heart'},
    878: {'title': 'Science Fiction', 'icon': 'bi-rocket'},
    10770: {'title': 'TV Movie', 'icon': 'bi-tv'},
    53: {'title': 'Thriller', 'icon': 'bi-knife'},
    10752: {'title': 'War', 'icon': 'bi-helmet-battle'},
    37: {'title': 'Western', 'icon': 'bi-hat-cowboy'}
}

# The TV Shows Categories titles and icons
TV_Shows_Categories = {
    10759: {'title': 'Action & Adventure', 'icon': 'bi-fist-raised'},
    16: {'title': 'Animation', 'icon': 'bi-film'},
    35: {'title': 'Comedy', 'icon': 'bi-face-grin-squint'},
    80: {'title': 'Crime', 'icon': 'bi-mask'},
    99: {'title': 'Documentary', 'icon': 'bi-camera'},
    18: {'title': 'Drama', 'icon': 'bi-theater-masks'},
    10751: {'title': 'Family', 'icon': 'bi-house'},
    10762: {'title': 'Kids', 'icon': 'bi-people-fill'},
    9648: {'title': 'Mystery', 'icon': 'bi-user-secret'},
    10763: {'title': 'News', 'icon': 'bi-newspaper'},
    10764: {'title': 'Reality', 'icon': 'bi-glasses'},
    10765: {'title': 'Sci-Fi & Fantasy', 'icon': 'bi-stars'},
    10766: {'title': 'Soap', 'icon': 'bi-droplet-half'},
    10767: {'title': 'Talk', 'icon': 'bi-mic-fill'},
    10768: {'title': 'War & Politics', 'icon': 'bi-bank2'},
    37: {'title': 'Western', 'icon': 'bi-hat-cowboy'}
}


"""
      
"""         
        # Categories dictionaries we loop through in categories.html to retrive every genre name and put an icon to it
        'categories': {
            
            # Listings of Movies Categories
            'Movies': {
                # Loop through the Movies_Categories to create this specific dictionary to make this work
                genre_id: {'title': 'Genre Name', 'icon': 'fa-icon-name'}
                for genre_id in Movies_Categories
            }, # Movies
            
            
            
            # Listings of TV Shows Categories
            'TV Shows': {
                # Loop through the TV_Shows_Categories to create this specific dictionary to make this work
                genre_id: {'title': 'Genre Name', 'icon': 'fa-icon-name'}
                for genre_id in TV_Shows_Categories
            }, # TV Shows
"""

""" 
Movies_Categories = {
    'Movies': {
            
            28: {'title': 'Action', 'icon': 'fa-bolt'},
            12: {'title': 'Adventure', 'icon': 'fa-hat-cowboy-side'},
            16: {'title': 'Animation', 'icon': 'fa-film'},
            35: {'title': 'Comedy', 'icon': 'fa-face-grin-squint'},
            80: {'title': 'Crime', 'icon': 'fa-mask'},
            99: {'title': 'Documentary', 'icon': 'fa-camera'},
            18: {'title': 'Drama', 'icon': 'fa-theater-masks'},
            10751: {'title': 'Family', 'icon': 'fa-home'},
            14: {'title': 'Fantasy', 'icon': 'fa-dragon'},
            36: {'title': 'History', 'icon': 'fa-landmark'},
            27: {'title': 'Horror', 'icon': 'fa-ghost'},
            10402: {'title': 'Music', 'icon': 'fa-music'},
            9648: {'title': 'Mystery', 'icon': 'fa-user-secret'},
            10749: {'title': 'Romance', 'icon': 'fa-heart'},
            878: {'title': 'Science Fiction', 'icon': 'fa-rocket'},
            10770: {'title': 'TV Movie', 'icon': 'fa-tv'},
            53: {'title': 'Thriller', 'icon': 'fa-knife'},
            10752: {'title': 'War', 'icon': 'fa-helmet-battle'},
            37: {'title': 'Western', 'icon': 'fa-hat-cowboy'}
        }
}
TV_Shows_Categories = {
        'TV Shows': {
        'page_title': 'TV Show Genres',
        10759: {'title': 'Action & Adventure', 'icon': 'fa-fist-raised'},
        16: {'title': 'Animation', 'icon': 'fa-film'},
        35: {'title': 'Comedy', 'icon': 'fa-face-grin-squint'},
        80: {'title': 'Crime', 'icon': 'fa-mask'},
        99: {'title': 'Documentary', 'icon': 'fa-camera'},
        18: {'title': 'Drama', 'icon': 'fa-theater-masks'},
        10751: {'title': 'Family', 'icon': 'fa-home'},
        10762: {'title': 'Kids', 'icon': 'fa-child'},
        9648: {'title': 'Mystery', 'icon': 'fa-user-secret'},
        10763: {'title': 'News', 'icon': 'fa-newspaper'},
        10764: {'title': 'Reality', 'icon': 'fa-glasses'},
        10765: {'title': 'Sci-Fi & Fantasy', 'icon': 'fa-rocket'},
        10766: {'title': 'Soap', 'icon': 'fa-soap'},
        10767: {'title': 'Talk', 'icon': 'fa-microphone'},
        10768: {'title': 'War & Politics', 'icon': 'fa-helmet-battle'},
        37: {'title': 'Western', 'icon': 'fa-hat-cowboy'}
    }
}
"""

"""             
# Categories dict Button
'Categories': {
'title': 'Explore Categories',
'route': '/categories',
'icon': None  # Optional: Add icon if necessary
}
"""