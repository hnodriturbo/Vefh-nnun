# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########




"""
 ----- Sample frá síðunni -----
  
import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer b6bbab9eb73d6f04fc09b9405d888fa2"
}

response = requests.get(url, headers=headers)

print(response.text)

 """
# Import flask and render_template
from flask import Flask, render_template

# Import datetime
from datetime import datetime

# Import events from the data.py file
from data import events, nav_links, dropdown_menus, employees, menu_items

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', nav_links=nav_links, dropdown_menus=dropdown_menus)

@app.route('/popular_movies.html')
def popular_movies():
    popular_movies = get_popular_movies()
    return render_template('popular_movies.html', popular_movies=popular_movies)

@app.route('/popular_tv_shows.html')
def popular_tv_shows():
    popular_tv_shows = get_popular_tv_shows

""" 
@app.route('/upcoming_events.html')
def upcoming_events():
    sorted_events = sorted(events, key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'))
    return render_template('upcoming_events.html', menu_items=menu_items, events=sorted_events)
 """



@app.route('/our_employees.html')
def my_information():
    return render_template('our_employees.html', menu_items=menu_items, employees=employees)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', menu_items=menu_items), 404


if __name__ == '__main__':
    app.debug = True
    app.run()

""" 
if __name__ == '__main__':
    app.run(debug=True)
    
   """  
""" if __name__ == '__main__':
    app.run(use_reloader=True)
 """
 
 
""" 
How to activate the debug mode for my powershell terminal in vscode
1. Activate the virtual environment venv with command ".\venv\Scripts\Activate.ps1"
2. Set the environment variable of FLASK_DEBUG to 1 with ' $env:FLASK_DEBUG = "1" '
3. Use "flask run" to run the server with debug mode on.
"""