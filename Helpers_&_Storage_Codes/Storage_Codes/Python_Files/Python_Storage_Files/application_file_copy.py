# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun  Áfanginn ########
#   ######### Skilaverkefni 3 #########
#    ########   Apríl  2024   ########

    #################################
##### ----- Application File ----- #####
    #################################
        ######### app.py #########
        
        
from flask import Flask, render_template, request
from managers import Dynamic_API_Manager
from navigation_navbar import create_navigation    




app = Flask(__name__)




api_manager = Dynamic_API_Manager()
navigation = create_navigation()


navigation = create_navigation()

@app.context_processor
def inject_navigation(navigation):
    return dict(navigation=navigation)

    
@app.route('/')
def home():
    return render_template('index.html')
 
 
# Route to handle listing pages
@app.route('/listings/<item_type>/<category>')
def show_listings(item_type, category):
    endpoint = navigation['accordion']['accordion_buttons'][category]['endpoint']
    title = navigation['accordion']['accordion_buttons'][category]['title']
    items = api_manager.make_request(endpoint)
    return render_template('listings.html', items=items, item_type=item_type, title=title, endpoint=endpoint)
 
 
 
 
 
 
 
 
 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html'), 404













if __name__ == '__main__':
    app.run(debug=True)











#############################################################
#############################################################
#############################################################
# --------------- ##### STORAGE CODES ##### --------------- #
# --------------- ##### STORAGE CODES ##### --------------- #
#############################################################
#############################################################
#############################################################







    


