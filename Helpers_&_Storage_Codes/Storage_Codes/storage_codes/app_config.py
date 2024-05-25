

# app_config.py

""" 
Description:
        This file import's the logging mechanisms and creates a logger handler that
        logs stuff to the file app.log where we implement a coding line for it.


"""

from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Set up the logger
handler = RotatingFileHandler('logging_file.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

def get_logger():
    return app.logger






"""
    -----  
        Sample frá verkefnalýsingunni frá Danna í Vefhönnun... veit ekki með hvort 
        ég noti authentication en held ég sleppi alveg þar 
    -----
"""
"""  
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


