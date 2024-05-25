from flask_frozen import Freezer
from app import app  # Ensure 'app' is your Flask app instance

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
