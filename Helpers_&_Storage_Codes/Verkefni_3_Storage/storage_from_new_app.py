


# this chatgpt was trying to solve my problems with some item manager, but this is isnt nearly as dynamic
# as i would want it to be.


""" 
# Home page route which could list genres or other relevant information
@app.route('/')
def home():
    # Example usage of GenreManager to fetch genres for movies, assuming it's still relevant
    genres = item_manager.fetch_genres('movie')  # Assuming fetch_genres method is available in ItemManager
    return render_template('categories.html', genres=genres, item_type='movie')
 """
# Dynamic routes for top rated and popular movies and TV shows
@app.route('/<item_type>/top-rated')
def show_top_rated(item_type):
    """
    Route to display top rated movies or TV shows.
    """
    if item_type not in ['movie', 'tv']:
        return "Invalid item type", 404
    items = item_manager.fetch_top_rated(item_type)
    return render_template('listings.html', items=items.get('results', []), title=f"Top Rated {item_type.title()}")

@app.route('/<item_type>/popular')
def show_popular(item_type):
    """
    Route to display popular movies or TV shows.
    """
    if item_type not in ['movie', 'tv']:
        return "Invalid item type", 404
    items = item_manager.fetch_popular(item_type)
    return render_template('listings.html', items=items.get('results', []), title=f"Popular {item_type.title()}")

# Compile this complete Flask application setup into a single script file.
code = """
from flask import Flask, render_template, url_for



class ItemManager(TMDBManager):
    def fetch_top_rated(self, item_type):
        endpoint = f"/{item_type}/top_rated"
        return self._send_request(endpoint)

    def fetch_popular(self, item_type):
        endpoint = f"/{item_type}/popular"
        return self._send_request(endpoint)

class EndpointManager:
    def get_home_url(self):
        return url_for('home')

app = Flask(__name__)
item_manager = ItemManager()
endpoint_manager = EndpointManager()

@app.route('/')
def home():
    genres = item_manager.fetch_genres('movie')
    return render_template('categories.html', genres=genres, item_type='movie')

@app.route('/<item_type>/top-rated')
def show_top_rated(item_type):
    if item_type not in ['movie', 'tv']:
        return "Invalid item type", 404
    items = item_manager.fetch_top_rated(item_type)
    return render_template('listings.html', items=items.get('results', []), title=f"Top Rated {item_type.title()}")

@app.route('/<item_type>/popular')
def show_popular(item_type):
    if item_type not in ['movie', 'tv']:
        return "Invalid item type", 404
    items = item_manager.fetch_popular(item_type)
    return render_template('listings.html', items=items.get('results', []), title=f"Popular {item_type.title()}")

if __name__ == '__main__':
    app.run(debug=True)
"""