# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########
# request_formatter.py
import logging
from logging.handlers import RotatingFileHandler
from flask import has_request_context, request

class RequestFormatter(logging.Formatter):
    """Custom request formatter for logging."""
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)

def setup_logging(app):
    """Sets up the logging configuration."""
    formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )
    
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    handler.setFormatter(formatter)
    
    # Get the Flask app's logger from the Flask imported here, not globally
    from flask import current_app as app
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
