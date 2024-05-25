# ########## Hreiðar Pétursson ##########
#  ######## Vefhönnun Áfanginn ########
#   ######### Skilaverkefni 3 ########
#    ########   Apríl 2024   ########




# Dictionary for menu items
menu_items = {
    'Home': '/',
    'About Us': '/about.html',
    'Generate Random': '/random.html',
    'Movies': {
        'Popular Movies': '/popular_movies.html',
        'Top Movies': '/top_movies.html',
    },
    'TV Shows': {
        'Popular TV Shows': '/popular_tv_shows.html',
        'Top TV Shows': '/top_tv_shows.html',
    }
}


# Standard navigation links
nav_links = {
    'Home': '/',
    'About Us': '/about.html',
    'Generate Random': '/random.html',
}

# Dropdown menus
dropdown_menus = {
    'Movies': {
        'Popular Movies': '/popular_movies.html',
        'Top Movies': '/top_movies.html',
    },
    'TV Shows': {
        'Popular TV Shows': '/popular_tv_shows.html',
        'Top TV Shows': '/top_tv_shows.html',
    }
}




# These are my fictional events to use on the PARENT site.
events = [
    {
        "name": "Music Fest 2024",
        "description": "A gathering of the best local and international music talents.",
        "image": "img/music_fest.jpg",
        "price": 50000,
        "date": "15-06-2024",
        "location": {
            "place": "Reykjavik Park",
            "latitude": "64.1466",
            "longitude": "-21.9426"
        }
    },
    {
        "name": "Golden Circle Classic Tour",
        "description": "Discover Iceland's most iconic natural attractions in one day.",
        "image": "img/golden_circle.jpg",
        "price": 10000,
        "date": "20-05-2024",
        "location": {
            "place": "Thingvellir National Park",
            "latitude": "64.2558",
            "longitude": "-21.1295"
        }
    },
    {
        "name": "Northern Lights Adventure",
        "description": "Experience the magical Aurora Borealis on this exclusive night tour.",
        "image": "img/northern_lights.jpg",
        "price": 15000,
        "date": "15-09-2024",
        "location": {
            "place": "Vik",
            "latitude": "63.4194",
            "longitude": "-19.0064"
        }
    },
    {
        "name": "Glacier Hiking & Ice Climbing",
        "description": "Explore the stunning glaciers of Iceland with an expert guide.",
        "image": "img/glacier_hiking.jpg",
        "price": 20000,
        "date": "10-07-2024",
        "location": {
            "place": "Skaftafell",
            "latitude": "64.0148",
            "longitude": "-16.9769"
        }
    },
    {
        "name": "Blue Lagoon Spa Day",
        "description": "Relax in the geothermal waters of the Blue Lagoon.",
        "image": "img/blue_lagoon.jpg",
        "price": 25000,
        "date": "05-08-2024",
        "location": {
            "place": "Blue Lagoon",
            "latitude": "63.8804",
            "longitude": "-22.4495"
        }
    },
    {
        "name": "Whale Watching Tour",
        "description": "Get up close with Iceland's marine giants in their natural habitat.",
        "image": "img/whale_watching.jpg",
        "price": 9500,
        "date": "25-06-2024",
        "location": {
            "place": "Husavik",
            "latitude": "66.0449",
            "longitude": "-17.3389"
        }
    },
    {
        "name": "Viking History Tour",
        "description": "Dive into the rich Viking history and culture of Iceland.",
        "image": "img/viking_history.jpg",
        "price": 8500,
        "date": "30-04-2024",
        "location": {
            "place": "Reykjavik",
            "latitude": "64.1283",
            "longitude": "-21.8277"
        }
    },
    {
        "name": "Icelandic Horse Riding",
        "description": "Experience the unique gait of the Icelandic horse through stunning landscapes.",
        "image": "img/horse_riding.jpg",
        "price": 12000,
        "date": "15-05-2024",
        "location": {
            "place": "Akureyri",
            "latitude": "65.6822",
            "longitude": "-18.0902"
        }
    },
    {
        "name": "Reykjavik Food Tour",
        "description": "Savour the tastes of Iceland on this culinary adventure through the capital.",
        "image": "img/food_tour.jpg",
        "price": 11000,
        "date": "20-07-2024",
        "location": {
            "place": "Reykjavik",
            "latitude": "64.1465",
            "longitude": "-21.9426"
        }
    },
    {
        "name": "Lava Tunnel Exploration",
        "description": "Venture into the heart of a lava tunnel for a unique subterranean experience.",
        "image": "img/lava_tunnel.jpg",
        "price": 13500,
        "date": "25-08-2024",
        "location": {
            "place": "Raufarholshellir",
            "latitude": "63.9422",
            "longitude": "-21.3964"
        }
    }
]






# Employee data
employees = [
    {
        "name": "Hreiðar Pétursson",
        "position": "Tour Guide",
        "image": "img/hreidar.jpg",
        "bio": "Hreiðar has been guiding tours through Iceland's stunning landscapes for over 5 years. Her passion for Icelandic history and nature makes her tours unforgettable.",
    },
    {
        "name": "Ólafur Kristjánsson",
        "position": "Operations Manager",
        "image": "img/olafur.jpg",
        "bio": "Ólafur ensures all tours operate smoothly and guests have the best experience. With a background in logistics, he's the backbone of our operations.",
    },
    {
        "name": "Gunnar Jónsson",
        "position": "Customer Support Specialist",
        "image": "img/gunnar.jpg",
        "bio": "Sigríður's love for helping others shines through in her dedication to assisting our guests with any questions or concerns. She's always ready to help with a smile.",
    }
]
