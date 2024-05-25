# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ////////////////        Author: Hreiðar Pétursson        \\\\\\\\\\\\\\\\
# //////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
# /////////////              -- Skilaverkefni 3 --            \\\\\\\\\\\\\
# ////      Description: Manages dictonaries for other files to        \\\\
# //   retrive from. These dictionaries represent everything that is     \\
# /             in the navbar, endpoints, args like item_type             \
# ////////                  to be movie or tv show                 \\\\\\\\
# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
                        ##### ----- nav.py ----- #####


# Standard navigation links remain unchanged
nav_links = {
    'Home': '/',
    'About': '/about_author' if '/about_author' else '/footer'
}


# Updated accordion_categories to match new route structure
accordion_categories = {
    'Movies': {
        'item_type': 'movie',
        'links': [
            {'name': 'Popular Movies', 'app_route': 'show_listings', 'args': {'item_type': 'movie', 'category': 'popular'}},
            {'name': 'Top Mwovies', 'endpoint': 'show_listings', 'args': {'item_type': 'movie', 'category': 'top_rated'}},
            {'name': 'Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'movie'}}
        ]
    },
    
    
    'TV Shows': {
        'item_type': 'tv',
        'buttons': [
            
                # Button to display popular TV Show listings
                {
                'title': 'Popular TV Shows', 
                'app_route': 'show_listings', 
                'category': 'popular'
                },
                
                # Button for displaying the top rated tv shows from tmdb
                {
                'title': 'Top TV Shows', 
                'app_route': 'show_listings', 
                'category': 'top_rated'
                },
                
                # Button for showing and listing all categories for TV Shows
                {
                'title': 'Categories', 
                'app_route': 'show_categories',
                'category': 'list'
                }
        ]
    }
}


# Define accordion categories with links that are dynamically generated
accordion_categories = {
    'Movies': {
        'id': 'movies_accordion',
        'links': [
            {'name': 'Popular Movies', 'endpoint': 'show_listings', 'args': {'item_type': 'movie', 'category': 'popular'}},
            {'name': 'Top Rated Movies', 'endpoint': 'show_listings', 'args': {'item_type': 'movie', 'category': 'top_rated'}},
            {'name': 'Movie Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'movie'}}
        ]
    },
    'TV Shows': {
        'id': 'tv_shows_accordion',
        'links': [
            {'name': 'Popular TV Shows', 'endpoint': 'show_listings', 'args': {'item_type': 'tv', 'category': 'popular'}},
            {'name': 'Top Rated TV Shows', 'endpoint': 'show_listings', 'args': {'item_type': 'tv', 'category': 'top_rated'}},
            {'name': 'TV Show Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'tv'}}
        ]
    }
}




genre_movies = {
    28: {'name': 'Action', 'icon': 'fa-bolt'},
    12: {'name': 'Adventure', 'icon': 'fa-hat-cowboy-side'},
    16: {'name': 'Animation', 'icon': 'fa-film'},
    35: {'name': 'Comedy', 'icon': 'fa-face-grin-squint'},
    80: {'name': 'Crime', 'icon': 'fa-mask'},
    99: {'name': 'Documentary', 'icon': 'fa-camera'},
    18: {'name': 'Drama', 'icon': 'fa-theater-masks'},
    10751: {'name': 'Family', 'icon': 'fa-home'},
    14: {'name': 'Fantasy', 'icon': 'fa-dragon'},
    36: {'name': 'History', 'icon': 'fa-landmark'},
    27: {'name': 'Horror', 'icon': 'fa-ghost'},
    10402: {'name': 'Music', 'icon': 'fa-music'},
    9648: {'name': 'Mystery', 'icon': 'fa-user-secret'},
    10749: {'name': 'Romance', 'icon': 'fa-heart'},
    878: {'name': 'Science Fiction', 'icon': 'fa-rocket'},
    10770: {'name': 'TV Movie', 'icon': 'fa-tv'},
    53: {'name': 'Thriller', 'icon': 'fa-knife'},
    10752: {'name': 'War', 'icon': 'fa-helmet-battle'},
    37: {'name': 'Western', 'icon': 'fa-hat-cowboy'}
}


# Genre icons for font awesome for tv shows
genre_tv_shows = {
    10759: {'name': 'Action & Adventure', 'icon': 'fa-fist-raised'},
    16: {'name': 'Animation', 'icon': 'fa-film'},
    35: {'name': 'Comedy', 'icon': 'fa-face-grin-squint'},
    80: {'name': 'Crime', 'icon': 'fa-mask'},
    99: {'name': 'Documentary', 'icon': 'fa-camera'},
    18: {'name': 'Drama', 'icon': 'fa-theater-masks'},
    10751: {'name': 'Family', 'icon': 'fa-home'},
    10762: {'name': 'Kids', 'icon': 'fa-child'},
    9648: {'name': 'Mystery', 'icon': 'fa-user-secret'},
    10763: {'name': 'News', 'icon': 'fa-newspaper'},
    10764: {'name': 'Reality', 'icon': 'fa-glasses'},
    10765: {'name': 'Sci-Fi & Fantasy', 'icon': 'fa-rocket'},
    10766: {'name': 'Soap', 'icon': 'fa-soap'},
    10767: {'name': 'Talk', 'icon': 'fa-microphone'},
    10768: {'name': 'War & Politics', 'icon': 'fa-helmet-battle'},
    37: {'name': 'Western', 'icon': 'fa-hat-cowboy'}
}

