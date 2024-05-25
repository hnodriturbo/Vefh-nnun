from flask import Flask, render_template

app = Flask(__name__)

# Dictionary for menu items
menu_items = {
    'Home': '/',
    'My Upcoming Events': '/upcoming_events',
    'My Information': '/my_information'
    
}

upcoming_events_list = ['event1', 'event2', 'event3']

my_information_dict = {
    
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upcoming_events.html')
def upcoming_events():
    return render_template('upcoming_events.html')

@app.route('my_information.html')
def my_information():
    return render_template('my_information.html')

if __name__ == '__main__':
    app.run(debug=True)

