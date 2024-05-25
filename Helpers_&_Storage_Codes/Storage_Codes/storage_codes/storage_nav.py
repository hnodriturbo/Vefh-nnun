




site_navigation = {
    'navigation': {
        'title': 'Main Site Navigation Links',
        'buttons': {
            'Home': '/',
            'About': '/about_author',
            'Categories': '/categories'  # Adding a general categories link
        }
    },
    'categories_list': {
        'title': 'Media Genre Categories with Icons',
        'buttons': {
            'list_categories': {
                'title': 'Listings Of Categories - Please Select',
                'app_route': 'show_categories',
                'category': 'list',
                'icon': 'fa-layer-group'  # Suggested icon for the Categories button
            }
        },
        'details': {
            'title': 'Choose To List Genres From Either Movies or TV Show',
            'intro': 'Select from the following options to explore genres:',
            'Media': {
                'Movies': {
                    'title': 'Movie Genres',
                    'icon': 'fa-film',  # Icon for the Movies card
                    'app_route': '/categories/movies'  # Route to the Movies categories page
                },
                'TV Shows': {
                    'title': 'TV Show Genres',
                    'icon': 'fa-tv',  # Icon for the TV Shows card
                    'app_route': '/categories/tv_shows'  # Route to the TV Shows categories page
                }
            }
        }
    }
}
    