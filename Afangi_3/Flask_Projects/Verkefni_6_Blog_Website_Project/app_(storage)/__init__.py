
# Imports of extensions from flask
from flask import Flask, render_template, request, redirect, url_for, flash, session, render_template_string
# Import jsonify for the ajax listings infinite scrolling
from flask import jsonify





# Function that creates the application to run
def create_app():
    
    
    app = Flask(__name__)
    app.secret_key = 'hnodri'
    
    
    
    @app.route('/')
    def home():
        return render_template('../index.html')

    return app
