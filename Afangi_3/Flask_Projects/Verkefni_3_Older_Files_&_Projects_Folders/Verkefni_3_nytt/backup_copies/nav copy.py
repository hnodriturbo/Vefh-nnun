# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########


accordion_categories = {
    'Movies': {
        'id': 'movies',
        'links': [
            {'name': 'Popular Movies', 'endpoint': 'show_listings', 'args': {'listing_type': 'popular_movies'}},
            {'name': 'Top Movies', 'endpoint': 'show_listings', 'args': {'listing_type': 'top_movies'}},
            {'name': 'Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'movies'}},
        ]
    },
    'TV Shows': {
        'id': 'tv_shows',
        'links': [
            {'name': 'Popular TV Shows', 'endpoint': 'show_listings', 'args': {'listing_type': 'popular_tv_shows'}},
            {'name': 'Top TV Shows', 'endpoint': 'show_listings', 'args': {'listing_type': 'top_tv_shows'}},
            {'name': 'Categories', 'endpoint': 'show_categories', 'args': {'item_type': 'tv_shows'}},
        ]
    }
}


# Standard navigation links remain unchanged
nav_links = {
    'Home': '/',
    'About': '/about_author',
}



# Genre icons for font awesome for tv shows
genre_icons_tv_shows = {
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


genre_icons_movies = {
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

