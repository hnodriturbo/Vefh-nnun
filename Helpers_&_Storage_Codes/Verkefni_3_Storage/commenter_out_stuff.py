# commented out stuff from data.py and nav.py and app.py 
# from verkefni 3 in vefhönnun áfangi 3


   
"""  
categories = {
    28: {'name': 'Action', 'icon': 'fa-bolt'},
    12: {'name': 'Adventure', 'icon': 'fa-hat-cowboy-side'},
    16: {'name': 'Animation', 'icon': 'fa-film'},
    35: {'name': 'Comedy', 'icon': 'fa-face-grin-squint'},
    80: {'name': 'Crime', 'icon': 'fa-mask'},
    99: {'name': 'Documentary', 'icon': 'fa-camera'},
    18: {'name': 'Drama', 'icon': 'fa-theater-masks'},
    10751: {'name': 'Family', 'icon': 'fa-home'},
    14: {'name': 'Fantasy', 'icon': 'fa-dragon'},
    36: {'name': 'History', 'icon': 'fa-landmark'},
    27: {'name': 'Horror', 'icon': 'fa-ghost'},
    10402: {'name': 'Music', 'icon': 'fa-music'},
    9648: {'name': 'Mystery', 'icon': 'fa-user-secret'},
    10749: {'name': 'Romance', 'icon': 'fa-heart'},
    878: {'name': 'Science Fiction', 'icon': 'fa-rocket'},
    10770: {'name': 'TV Movie', 'icon': 'fa-tv'},  # Typically only applicable to movies
    53: {'name': 'Thriller', 'icon': 'fa-knife'},
    10752: {'name': 'War', 'icon': 'fa-helmet-battle'},
    37: {'name': 'Western', 'icon': 'fa-hat-cowboy'},
    10765: {'name': 'Sci-Fi & Fantasy', 'icon': 'fa-space-shuttle'},  # Common alternative category for TV
    10759: {'name': 'Action & Adventure', 'icon': 'fa-fist-raised'},  # Common for TV
    10762: {'name': 'Kids', 'icon': 'fa-child'},  # Typically TV
    10763: {'name': 'News', 'icon': 'fa-newspaper'},  # Typically TV
    10764: {'name': 'Reality', 'icon': 'fa-mask'},  # Typically TV
    10766: {'name': 'Soap', 'icon': 'fa-soap'},  # Typically TV
    10767: {'name': 'Talk', 'icon': 'fa-microphone'},  # Typically TV
    10768: {'name': 'Politics', 'icon': 'fa-landmark'}  # Typically TV, sometimes under 'War & Politics'
}
"""
    
    
    
    

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
 
 
 
"""
How to activate the debug mode for my powershell terminal in vscode
1. Activate the virtual environment venv with command ".\venv\Scripts\Activate.ps1"
2. Set the environment variable of FLASK_DEBUG to 1 with ' $env:FLASK_DEBUG = "1" '
3. Use "flask run" to run the server with debug mode on.
"""