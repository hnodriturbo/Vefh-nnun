import requests

# The requests.get(url, params=params) constructs the url and this url looks really like this:
# https://api.themoviedb.org/3/movie/top_rated?api_key=36dfeb735a6d3633c2364db52ed2075c&language=en-US&page=1
# It takes the url variable and adds to it and begins with "?" and the the params one by one with "&" in between the params

url = "https://api.themoviedb.org/3/movie/top_rated"
params = {
    "api_key": "36dfeb735a6d3633c2364db52ed2075c",
    "language": "en-US",
    "page": 1
}

response = requests.get(url, params=params)
json_data = response.json()
print(json_data)

