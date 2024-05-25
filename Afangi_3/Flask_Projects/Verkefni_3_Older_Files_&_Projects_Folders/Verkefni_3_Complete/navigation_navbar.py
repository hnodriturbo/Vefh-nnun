



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
        """ Convert the navigation entry into a dictionary format for Flask templates. """
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


