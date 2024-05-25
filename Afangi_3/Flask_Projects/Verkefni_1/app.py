# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 1 ########
#    ########    Mars 2024   ########


# Import flask and render_template
from flask import Flask, render_template

# Import events from the data.py file
from data import events, menu_items, employees

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', menu_items=menu_items, events=events)



@app.route('/upcoming_events.html')
def upcoming_events():
    return render_template('upcoming_events.html', menu_items=menu_items, events=events)




@app.route('/our_employees.html')
def my_information():
    return render_template('our_employees.html', menu_items=menu_items, employees=employees)

""" 
@app.errorhandler(404)
def page_not_found():
    return render_template('error_handler.html')

 """
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