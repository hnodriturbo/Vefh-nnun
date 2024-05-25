                # ########## Hreiðar Pétursson ##########
                #  ######## Vefhönnun  Áfanginn ########
                #   ######### Skilaverkefni 3 #########
                #    ########   Apríl  2024   ########

def generate_genre_entry(genre_id, title, icon, item_type):
    """Generate a dictionary entry for a genre with a consistent route structure."""
    return {
        'item_type': item_type,
        'title': title,
        'icon': icon,
        'route': f"/{item_type}/genre/{genre_id}"
    }
# This returns a dictionary with exactly this setup as in the return statement. One dictionary for every genre


# Movies Categories Setup
movie_categories = {
    'item_type': 'movie',
    28: generate_genre_entry(28, 'Action', 'bi-bolt', 'movie'),
    12: generate_genre_entry(12, 'Adventure', 'bi-hat-cowboy-side', 'movie'),
    16: generate_genre_entry(16, 'Animation', 'bi-film', 'movie'),
    35: generate_genre_entry(35, 'Comedy', 'bi-face-grin-squint', 'movie'),
    80: generate_genre_entry(80, 'Crime', 'bi-mask', 'movie'),
    99: generate_genre_entry(99, 'Documentary', 'bi-camera', 'movie'),
    18: generate_genre_entry(18, 'Drama', 'bi-theater-masks', 'movie'),
    10751: generate_genre_entry(10751, 'Family', 'bi-house', 'movie'),
    14: generate_genre_entry(14, 'Fantasy', 'bi-dragon', 'movie'),
    36: generate_genre_entry(36, 'History', 'bi-landmark', 'movie'),
    27: generate_genre_entry(27, 'Horror', 'bi-ghost', 'movie'),
    10402: generate_genre_entry(10402, 'Music', 'bi-music', 'movie'),
    9648: generate_genre_entry(9648, 'Mystery', 'bi-user-secret', 'movie'),
    10749: generate_genre_entry(10749, 'Romance', 'bi-heart', 'movie'),
    878: generate_genre_entry(878, 'Science Fiction', 'bi-rocket', 'movie'),
    10770: generate_genre_entry(10770, 'TV Movie', 'bi-tv', 'movie'),
    53: generate_genre_entry(53, 'Thriller', 'bi-knife', 'movie'),
    10752: generate_genre_entry(10752, 'War', 'bi-helmet-battle', 'movie'),
    37: generate_genre_entry(37, 'Western', 'bi-hat-cowboy', 'movie')
}

# TV Shows Categories Setup
tv_categories = {
    'item_type': 'tv',
    10759: generate_genre_entry(10759, 'Action & Adventure', 'bi-fist-raised', 'tv'),
    16: generate_genre_entry(16, 'Animation', 'bi-film', 'tv'),
    35: generate_genre_entry(35, 'Comedy', 'bi-face-grin-squint', 'tv'),
    80: generate_genre_entry(80, 'Crime', 'bi-mask', 'tv'),
    99: generate_genre_entry(99, 'Documentary', 'bi-camera', 'tv'),
    18: generate_genre_entry(18, 'Drama', 'bi-theater-masks', 'tv'),
    10751: generate_genre_entry(10751, 'Family', 'bi-house', 'tv'),
    10762: generate_genre_entry(10762, 'Kids', 'bi-people-fill', 'tv'),
    9648: generate_genre_entry(9648, 'Mystery', 'bi-user-secret', 'tv'),
    10763: generate_genre_entry(10763, 'News', 'bi-newspaper', 'tv'),
    10764: generate_genre_entry(10764, 'Reality', 'bi-glasses', 'tv'),
    10765: generate_genre_entry(10765, 'Sci-Fi & Fantasy', 'bi-stars', 'tv'),
    10766: generate_genre_entry(10766, 'Soap', 'bi-droplet-half', 'tv'),
    10767: generate_genre_entry(10767, 'Talk', 'bi-mic-fill', 'tv'),
    10768: generate_genre_entry(10768, 'War & Politics', 'bi-bank2', 'tv'),
    37: generate_genre_entry(37, 'Western', 'bi-hat-cowboy', 'tv')
}