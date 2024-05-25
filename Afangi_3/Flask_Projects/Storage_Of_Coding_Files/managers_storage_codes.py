






class NavigationManager:
    def __init__(self):
        self.main_navigation = {}
        self.accordion = {}
        self.item_type = item_type

    def add_main_nav_entry(self, route, title, icon):
        """Add an entry to the main navigation."""
        self.main_navigation[title] = BaseNavEntry(route, title, icon).as_dict()

    def add_accordion_section(self, item_type, title, icon, route):
        """Add a new section to the accordion navigation."""
        self.accordion[item_type] = {
            'item_type': item_type,
            'title': title,
            'icon': icon,
            'route': route,
            'accordion_buttons': {}
        }

    def add_button_to_accordion(self, item_type, route, title, icon, endpoint, is_listing=False):
        """Add a button to an existing accordion section."""
        button_entry = BaseNavEntry(route, title, icon, endpoint, is_listing)
        self.accordion[item_type]['accordion_buttons'][title] = button_entry.as_dict()

    def configure_default_navigation(self): 
        """Configure default navigation setup for the application."""
        self.add_main_nav_entry('/', 'Home', 'bi-house')
        self.add_main_nav_entry('/about_author', 'About Author', 'bi-person')
        self.add_accordion_section('movie', 'Movies', 'bi-film', 'movies')
        self.add_accordion_section('tv', 'TV Shows', 'bi-tv', 'tv_shows')
        self.add_button_to_accordion('movie', '/movies/popular', 'Popular Movies', 'bi-film', 'movie/popular')
        self.add_button_to_accordion('movie', '/movies/top_rated', 'Top Rated Movies', 'bi-star', 'movie/top_rated')
        self.add_button_to_accordion('movie', '/movies/categories', 'Movie Categories', 'bi-list', 'genre/{self.item_type}/list', True)
        self.add_button_to_accordion('tv', '/tv_shows/popular', 'Popular TV Shows', 'bi-tv', 'movie/popular')
        self.add_button_to_accordion('tv', '/tv_shows/top_rated', 'Top Rated TV Shows', 'bi-star', 'movie/popular')
        self.add_button_to_accordion('tv', '/tv_shows/categories', 'TV Shows Categories', 'bi-list', 'movie/popular', True)

    def get_navigation(self):
        """Return the complete navigation structure."""
        return {
            'main_navigation': self.main_navigation,
            'accordion': self.accordion
        }
















# Example usage with the new method
nav_manager = NavigationManager()
nav_manager.configure_default_navigation()
navigation = nav_manager.get_navigation()






# A Semi-beautiful way to print out the items in the navigation dictionary of dictionaries
# to see all it's contents for using in the program and ease access because the generators
# of dictionary key's and values are not clear enough to see the structure in whole
# with the naked eye. (at least that's my view on the subject)

# Print the navigation structure
for section, content in navigation.items():
    print(f"\n{section.upper()} SECTION:")
    if section == 'main_navigation':
        for name, details in content.items():
            print(f"  {name}:")
            print(f"    Route: {details['route']}")
            print(f"    Title: {details['title']}")
            print(f"    Icon: {details['icon']}")
    elif section == 'accordion':
        for item_type, item_details in content.items():
            print(f"  {item_type.upper()} ACCORDION:")
            print(f"    Title: {item_details['title']}")
            print(f"    Icon: {item_details['icon']}")
            print(f"    Route: {item_details['route']}")
            for button_title, button_details in item_details['accordion_buttons'].items():
                print(f"      Button - {button_title}:")
                print(f"        Route: {button_details['route']}")
                print(f"        Base Route: {button_details['base_route']}")
                print(f"        Endpoint: {button_details['endpoint']}")
                print(f"        Title: {button_details['title']}")
                print(f"        Icon: {button_details['icon']}")
