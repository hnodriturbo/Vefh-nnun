from flask import Flask
from blueprints.navigation import navigation_bp
from blueprints.post import post_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hnodriturbo'

    # Register blueprints
    app.register_blueprint(navigation_bp, url_prefix='/navigation')
    app.register_blueprint(post_bp, url_prefix='/post')

    return app
