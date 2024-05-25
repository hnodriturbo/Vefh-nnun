""" 
genre_icons_tv_shows = {
    'Action & Adventure': {'name': 'Action & Adventure', 'icon': 'fa-fist-raised'},
    'Animation': {'name': 'Animation', 'icon': 'fa-film'},
    'Comedy': {'name': 'Comedy', 'icon': 'fa-face-grin-squint'},
    'Crime': {'name': 'Crime', 'icon': 'fa-mask'},
    'Documentary': {'name': 'Documentary', 'icon': 'fa-camera'},
    'Drama': {'name': 'Drama', 'icon': 'fa-theater-masks'},
    'Family': {'name': 'Family', 'icon': 'fa-home'},
    'Kids': {'name': 'Kids', 'icon': 'fa-child'},
    'Mystery': {'name': 'Mystery', 'icon': 'fa-user-secret'},
    'News': {'name': 'News', 'icon': 'fa-newspaper'},
    'Reality': {'name': 'Reality', 'icon': 'fa-glasses'},
    'Sci-Fi & Fantasy': {'name': 'Sci-Fi & Fantasy', 'icon': 'fa-rocket'},
    'Soap': {'name': 'Soap', 'icon': 'fa-soap'},
    'Talk': {'name': 'Talk', 'icon': 'fa-microphone'},
    'War & Politics': {'name': 'War & Politics', 'icon': 'fa-helmet-battle'},
    'Western': {'name': 'Western', 'icon': 'fa-hat-cowboy'}
}
 """

""" 
# Genre icons for font awesome for movies
genre_icons_movies = {
    'Action': 'fa-bolt',
    'Adventure': 'fa-hat-cowboy-side',
    'Animation': 'fa-film',
    'Comedy': 'fa-face-grin-squint',
    'Crime': 'fa-mask',
    'Documentary': 'fa-video',
    'Drama': 'fa-theater-masks',
    'Family': 'fa-home',
    'Fantasy': 'fa-dragon',
    'History': 'fa-landmark',
    'Horror': 'fa-ghost',
    'Music': 'fa-music',
    'Mystery': 'fa-user-secret',
    'Romance': 'fa-heart',
    'Science Fiction': 'fa-rocket',
    'TV Movie': 'fa-tv',
    'Thriller': 'fa-knife',
    'War': 'fa-helmet-battle',
    'Western': 'fa-hat-cowboy'
}
 """





""" 
# nav.py

# Standard navigation links
nav_links = {
    'Home': '/',
    'About': '/about_author',
}

# Movies and TV Shows categories for the collapsing sections
# Suppose dropdown_menus is expanded to include an ID for each section
dropdown_menus = {
    'Movies': {
        'id': 'moviesCollapse',
        'links': {
            'Popular Movies': '/category/popular_movies',
            'Top Movies': '/category/top_movies',
            'Browse Categories': '/browse_categories/movies',
        }
    },
    'TV Shows': {
        'id': 'tvShowsCollapse',
        'links': {
            'Popular TV Shows': '/category/popular_tv_shows',
            'Top TV Shows': '/category/top_tv_shows',
            'Browse Categories': '/browse_categories/tv_shows',
        }
    }
}
accordion_categories = {
    'Movies': [
        {'name': 'Popular Movies', 'endpoint': 'show_listings', 'args': {'listing_type': 'popular_movies'}},
        {'name': 'Top Movies', 'endpoint': 'show_listings', 'args': {'listing_type': 'top_movies'}},
    ],
    'TV Shows': [
        {'name': 'Popular TV Shows', 'endpoint': 'show_listings', 'args': {'listing_type': 'popular_tv_shows'}},
        {'name': 'Top TV Shows', 'endpoint': 'show_listings', 'args': {'listing_type': 'top_tv_shows'}},
    ]
}
 """
# nav.py or equivalent in your Flask app


""" 
# Standard navigation links
nav_links = {
    'Home': '/',
    'About': '/about_author',
}

# Dropdown menus for the unified "Explore" and new "Random" functionality
dropdown_menus = {
    'Explore': {
        'Movies': '/movies',
        'TV Shows': '/tv_shows',
        'Browse Categories': '/browse_categories',
    },
    'Random': '/get_random'
}

# Standard navigation links
nav_links = {
    'Home': '/',
    'About': '/about_author',  # Assuming 'about_author' is the route you have defined for the About page
}

 """


""" 
# Adjusting dropdown_menus to include both Movies and TV Shows under an "Explore" category
# and introducing a "Browse Categories" option
dropdown_menus = {
    'Explore': {
        'Popular Movies': '/category/popular_movies',
        'Top Movies': '/category/top_movies',
        'divider1': 'divider',  # Special key to indicate a divider (handled in template)
        'Popular TV Shows': '/category/popular_tv_shows',
        'Top TV Shows': '/category/top_tv_shows',
        'divider2': 'divider',  # Another divider (handled in template)
        'Browse Categories': '/browse_categories',  # A new route you'll need to implement
    },
    'Random': {
        'Random Movie': '/get_random_movie',
        'Random TV Show': '/get_random_movie'
    }
}
 """

# Adding a direct link for "Get Random Movie/TV Show"
# This could be handled differently based on how you implement this functionality.
# If it doesn't fit well within the existing structures, you might handle it directly in the template or through JavaScript.
""" random_link = {
    'Get Random Movie/TV Show': '/get_random'  # A new route for fetching a random movie or TV show
} """







# Dictionary for menu items
""" 
menu_items = {
    'Home': '/',
    'About Us': '/about.html',
    'Generate Random': '/random.html',
    'Movies': {
        'Popular Movies': '/movies/popular_movies.html',
        'Top Movies': '/movies/top_movies.html',
    },
    'TV Shows': {
        'Popular TV Shows': '/tv_shows/popular_tv_shows.html',
        'Top TV Shows': '/tv_shows/top_tv_shows.html',
    }
}
 """
""" 
# Standard navigation links
nav_links = {
    'About': '/about_author',
    'Home': '/'
}

# Dropdown menus adjusted for dynamic category handling and unified detail view
dropdown_menus = {
    'Movies': {
        'Popular Movies': '/category/popular_movies',
        'Top Movies': '/category/top_movies',
    },
    'TV Shows': {
        'Popular TV Shows': '/category/popular_tv_shows',
        'Top TV Shows': '/category/top_tv_shows',
    }
}
 """
