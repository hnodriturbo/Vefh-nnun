# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun  Áfanginn ########
#   ######### Skilaverkefni 3 #########
#    ########   Apríl  2024   ########

    #################################
##### ----- Application File ----- #####
    #################################
        ######### app.py #########p
        
# In your main Flask application file
from flask import Flask, render_template, current_app
from navigation_navbar import NavEntry, MoviesNavEntry, TVShowsNavEntry
from tmdb_manager import TMDB_API_JSON
app = Flask(__name__)


# In navigation.py or a similar module
def create_navigation():
    home = NavEntry('Home', 'bi-house', '/')
    about_author = NavEntry('About Author', 'bi-person', '/about_author')
    movies = MoviesNavEntry('Movies', 'bi-film', '/movies')
    tv_shows = TVShowsNavEntry('TV Shows', 'bi-tv', '/tv_shows')

    # Assuming the add_accordion_button method properly adds the required sub-navigation entries
    return {
        'main_navigation': {
            'Home': home.as_dict(),
            'About Author': about_author.as_dict()
        },
        'accordion': {
            'Movies': movies.as_dict(),
            'TV Shows': tv_shows.as_dict()
        }
    }
@app.context_processor
def inject_navigation():
    return {'navigation': create_navigation()}

app.route('/')
def home():
    current_app.logger.info("Rendering index.html")
    return render_template('index.html')

if __name__ == "__main__":
    app.logger.setLevel("DEBUG")
    app.run(debug=True)
        
        
        
        
        
        
        
        

