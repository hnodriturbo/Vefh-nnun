

""" 


Name                            Value                                   In Use (boolean)
----                            -----                                   ----------------
1 --- "tmdb_api_key_old" ---    "b6bbab9eb73d6f04fc09b9405d888fa2"      False  ( Older key, moved to old variable )
2 --- "tmdb_api_key" ---        "36dfeb735a6d3633c2364db52ed2075c"      True   ( New key, using same variable but with lower caps )



"""




import requests
import json

# The requests.get(url, params=params) constructs the url and this url looks really like this:
# https://api.themoviedb.org/3/movie/popular?api_key=36dfeb735a6d3633c2364db52ed2075c&language=en-US&page=1
# It takes the url variable and adds to it and begins with "?" and the the params one by one with "&" in between the params

url = "https://api.themoviedb.org/3/movie/popular"
params = {
    "api_key": "36dfeb735a6d3633c2364db52ed2075c",
    "language": "en-US",
    "page": 3
}

# Use requests to get the response
response = requests.get(url, params=params)

# Parsing the response into raw json data
json_data = response.json()