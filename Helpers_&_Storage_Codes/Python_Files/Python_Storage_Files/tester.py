# Assuming the class is defined in a file named tmdb_manager.py and correctly imported
from tmdb_manager import TMBD_API_Manager

# Creating an instance with the correct API key
tmdb_manager = TMBD_API_Manager(base_url="https://api.themoviedb.org/3", api_key='b6bbab9eb73d6f04fc09b9405d888fa2')
print(tmdb_manager.base_url)  # This will print the correct base URL
