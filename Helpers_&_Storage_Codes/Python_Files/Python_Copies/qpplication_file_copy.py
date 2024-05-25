# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun  Áfanginn ########
#   ######### Skilaverkefni 3 #########
#    ########   Apríl  2024   ########

    #################################
##### ----- Application File ----- #####
    #################################
        ######### app.py #########
        
        
        
from flask import Flask, render_template, url_for, redirect, request


# Import the managers from tmdb_manager.py and endpoint_manager.py
from tmdb_manager import Dynamic_API_Manager


# creates all endpoints and uses navigation_navbar dict of dicts for it.
from endpoint_manager import Endpoint_Manager


# Import the logger
from app_config import get_logger


# Import the create_navigation function to create the super dict I have created for the structure layout of the website
from navigation_navbar import create_navigation


# Let's start the flask app in the name of app ( very awesome idea of describing the app with the var app ... hehe )
app = Flask(__name__)


# My Secret key and I have no idea why i need it to be here.... haha! :)
app.secret_key = 'hnodri'


# We want to log for helping in creating this awesome website
logger = get_logger()


# Create navigation super dict ( see structure layout in the top part of the file )
navigation = create_navigation()


# Create instances of the managers so they can be used and their methods
tmdb_manager = Dynamic_API_Manager()







""" 
    What this @app.context_processor does:
        Automatically injects navigation links and categories into all templates.
"""
@app.context_processor
def inject_navigation():
    application_ctx = create_navigation()
    return dict(navigation=application_ctx)
""" 
@app.route('/init-tmdb')
def init_tmdb():
    manager = TMDB_API_Manager()
    manager.log_initialization()
    return 'TMDB API Manager Initialized ! ! !'
 """

""" items = tmdb_api_manager.get_listings('movie', 'popular')  """ 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<item_type>/<category>')
def show_listings(item_type, category):
    endpoint = tmdb_manager.get_data(category, item_type, language='en-US')
    items = tmdb_manager.make_request(endpoint)
    return render_template('listings.html', items=items)




""" Movies Endpoint app routes """
""" 

@app.route('/movies/<category>')
def show_movies(category):
    endpoint = endpoint_manager.build_endpoint(category, 'movie')
    movies = tmdb_api_manager.fetch_data(endpoint)
    return render_template('listings.html', items=movies['results'], title=f"{category.title()} Movies", item_type='movie')
 """
""" TV Shows Endpoint app routes """
""" 
@app.route('/tv/<category>')
def show_tv(category):
    endpoint = endpoint_manager.build_endpoint(category, 'tv')
    tv_shows = tmdb_api_manager.fetch_data(endpoint)
    return render_template('listings.html', items=tv_shows['results'], title=f"{category.title()} TV Shows", item_type='tv')

@app.route('/item/<item_type>/<int:item_id>')
def item_details(item_type, item_id):
    item = tmdb_api_manager.get_item_details(item_type, item_id)
    trailer_key = tmdb_api_manager.get_trailer_key(item_type, item_id)
    return render_template('item_details.html', item_details=item, item_type=item_type, trailer_key=trailer_key)

@app.route('/categories/<item_type>')
def show_categories(item_type):
    genres = tmdb_api_manager.list_categories(item_type)
    return render_template('categories.html', genres=genres, item_type=item_type, title=f"{item_type.title()} Categories")
 """
if __name__ == '__main__':
    app.run(debug=True)






""" 
I am in no need for a error page if the errors get displayed in base.html 
file at the top row, but below the navbar

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html'), 404
"""







#############################################################
#############################################################
#############################################################
# --------------- ##### STORAGE CODES ##### --------------- #
# --------------- ##### STORAGE CODES ##### --------------- #
#############################################################
#############################################################
#############################################################


""" 
@app.context_processor
def inject_navigation():
    from navigation_navbar import navigation  # Ensure you import your navigation structure
    return dict(navigation=navigation)
"""




    


