import requests
import json

# The requests.get(url, params=params) constructs the url and this url looks really like this:
# https://api.themoviedb.org/3/movie/popular?api_key=36dfeb735a6d3633c2364db52ed2075c&language=en-US&page=1
# It takes the url variable and adds to it and begins with "?" and the the params one by one with "&" in between the params

url = "https://api.themoviedb.org/3/configuration"
params = {
    "api_key": "36dfeb735a6d3633c2364db52ed2075c",
    "language": "en-US",
}

# Use requests to get the response
response = requests.get(url, params=params)

# Parsing the response into raw json data
json_data = response.json()
"""
Description:
    The `json.dumps()` method converts a Python object (like a dictionary, list, tuple, etc.) into a JSON-formatted string. 
    This method is particularly useful for serializing Python data structures into JSON format, which can then be easily 
    stored, transmitted over a network, or used in other contexts where JSON is required.

    - `argument`: This is the primary data that you want to serialize into JSON. It must be a Python object like a dictionary or list.
    - `indent`: This optional parameter specifies the number of spaces to use for indentation to format the JSON output. 
      If unspecified or None, the JSON data will be printed in a single line. If an integer (commonly 4 or 2) is provided, 
      it will format the output with that number of spaces for indentation, making it more human-readable.

Example:
    To pretty print JSON data, use:
        pretty_printed_json_data = json.dumps(json_data, indent=4)
    This command will serialize `json_data` and format it with an indentation of 4 spaces.

    To compact the JSON data into a single line string, use:
        json_string = json.dumps(json_data)
    This command will serialize `json_data` without any extra spaces or new lines.

Key Methods of the json Module:
    - `json.dumps()`: Serializes Python objects into a JSON formatted string.
    - `json.loads()`: Deserializes a JSON formatted string into a Python object.
    - `json.dump()`: Serializes Python objects as JSON formatted data to a file-like object (e.g., a file opened in write mode).
    - `json.load()`: Deserializes JSON formatted data from a file-like object into a Python object.
"""

# Example usage of json.dumps() with indentation
pretty_printed_json_data = json.dumps(json_data, indent=4)
print(pretty_printed_json_data)

# Example usage of json.dumps() without indentation (compact)
json_string = json.dumps(json_data)
print(json_string)
