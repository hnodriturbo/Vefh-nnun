tmdb_endpoints = {
    "configuration": {
        "url": "https://api.themoviedb.org/3/configuration",
        "params": {"api_key": "your_api_key"},
        "description": "Get the system-wide configuration information."
    },
    "movie_details": {
        "url": "https://api.themoviedb.org/3/movie/{movie_id}",
        "params": {"api_key": "your_api_key", "language": "en-US"},
        "description": "Get the primary information about a movie."
    },
    "search_movie": {
        "url": "https://api.themoviedb.org/3/search/movie",
        "params": {"api_key": "your_api_key", "query": "movie_name", "language": "en-US", "page": 1},
        "description": "Search for movies."
    },
    "trending": {
        "url": "https://api.themoviedb.org/3/trending/{media_type}/{time_window}",
        "params": {"api_key": "your_api_key"},
        "description": "Get the trending media for the day or week."
    },
    "movie_genres": {
        "url": "https://api.themoviedb.org/3/genre/movie/list",
        "params": {"api_key": "your_api_key", "language": "en-US"},
        "description": "Get the list of official genres for movies."
    },
    "tv_details": {
        "url": "https://api.themoviedb.org/3/tv/{tv_id}",
        "params": {"api_key": "your_api_key", "language": "en-US"},
        "description": "Get the primary information about a TV series."
    },
    "person_details": {
        "url": "https://api.themoviedb.org/3/person/{person_id}",
        "params": {"api_key": "your_api_key", "language": "en-US"},
        "description": "Get the primary information about a person."
    }
}
