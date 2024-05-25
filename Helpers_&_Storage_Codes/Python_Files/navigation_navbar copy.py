# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ////////////////        Author: Hreiðar Pétursson        \\\\\\\\\\\\\\\\
# //////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
# /////////////              -- Skilaverkefni 3 --            \\\\\\\\\\\\\
# ////      Description: Manages dictonaries for other files to        \\\\
# //   retrive from. These dictionaries represent everything that is     \\
# /             in the navbar, endpoints, args like item_type             \
# ////////                  to be movie or tv show                 \\\\\\\\
# ////////////////////////////////////--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
                        ##### ----- nav.py ----- #####
 site_navigation = {
    'navigation': {
        'title': 'Main Site Navigation Links',
        'buttons': {
            'Home': {
                'title': 'Home',
                'item_type': 'main',
                'app_route': '/'
            },
            'About': {
                'title': 'About the Author of this Web-Project to make the best use of APIs',
                'item_type': 'info',
                'app_route': '/about_author'
            },
            'Categories': {
                'title': 'Explore Categories',
                'item_type': 'category',
                'app_route': '/categories'
            }
        }
    },
    'accordion_buttons': {
        'Movies': {
            'title': 'Movies',
            'item_type': 'movie',
            'buttons': {
                'popular_movies': {
                    'title': 'Popular Movies',
                    'app_route': '/show_listings',
                    'category': 'popular'
                },
                'top_movies': {
                    'title': 'Top Movies',
                    'app_route': '/show_listings',
                    'category': 'top_rated'
                },
                'categories': {
                    'title': 'Movie Categories',
                    'app_route': '/show_categories',
                    'category': 'list'
                }
            }
        },
        'TV Shows': {
            'title': 'TV Shows',
            'item_type': 'tv',
            'buttons': {
                'popular_tv_shows': {
                    'title': 'Popular TV Shows',
                    'app_route': '/show_listings',
                    'category': 'popular'
                },
                'top_tv_shows': {
                    'title': 'Top TV Shows',
                    'app_route': '/show_listings',
                    'category': 'top_rated'
                },
                'categories': {
                    'title': 'TV Show Categories',
                    'app_route': '/show_categories',
                    'category': 'list'
                }
            }
        }
    },
    'categories_list': {
        'title': 'Media Genre Categories with Icons',
        'buttons': {
            'list_categories': {
                'title': 'Listings Of Categories - Please Select',
                'app_route': '/show_categories',
                'category': 'list',
                'icon': 'fa-layer-group'
            }
        },
        'details': {
            'title': 'Choose To List Genres From Either Movies or TV Shows',
            'intro': 'Select from the following options to explore genres:',
            'categories': {
                    'title': 'Movie Categories',
                    'app_route': '/show_categories',
                    'category': 'list'
                },
            'buttons': {
                'Movies': {
                    'title': 'Movie Genres',
                    'icon': 'fa-film',
                    'app_route': '/categories/movies'
                },
                'TV Shows': {
                    'title': 'TV Show Genres',
                    'icon': 'fa-tv',
                    'app_route': '/categories/tv_shows'
                }
            }
        }
    }
}
                      
                        
site_navigastion = {
    'right_button': {
            'title': 'Main Site Navigation Links',
            'links': {
                'Home': {
                    'title': 'Home',
                    'item_type': 'main',  # Suggesting 'main' for primary navigation links
                    'app_route': '/'
                },
                'About': {
                    'title': 'About the Author of this Web-Project to make the best use of APIs',
                    'item_type': 'info',  # Using 'info' to denote informational content
                    'app_route': '/about_author'
                }
            }
    },
    
    
    'accordion_buttons': {
        # Movies library for the accordion buttons, title, app_route and category
        'Movies': {
            'title': 'Movies',
            'item_type': 'movie',
            
            'buttons': {
                'popular_movies': {
                    'title': 'Popular Movies',
                    'app_route': 'show_listings',
                    'category': 'popular'
                },
                'top_movies': {
                    'title': 'Top Movies',
                    'app_route': 'show_listings',
                    'category': 'top_rated'
                },
                'categories': {
                    'title': 'Categories',
                    'app_route': 'show_categories',
                    'category': 'list'
                }
                
            } # 'buttons': 
            
        }, # 'Movies'
        
        # TV Shows library for the accordion buttons, title, app_route and category
        'TV Shows': {
            'item_type': 'tv',
            'buttons': {
                'popular_tv_shows': {
                    'title': 'Popular TV Shows',
                    'app_route': 'show_listings',
                    'category': 'popular'
                },
                'top_tv_shows': {
                    'title': 'Top TV Shows',
                    'app_route': 'show_listings',
                    'category': 'top_rated'
                },
                'categories': {
                    'title': 'Categories',
                    'app_route': 'show_categories',
                    'category': 'list'
                }
            }
        }
    }
}



Movies_Categpriesa = {
'Movies': {
        'page_title': 'Movie Genres',
        28: {'title': 'Action', 'icon': 'fa-bolt'},
        12: {'title': 'Adventure', 'icon': 'fa-hat-cowboy-side'},
        16: {'title': 'Animation', 'icon': 'fa-film'},
        35: {'title': 'Comedy', 'icon': 'fa-face-grin-squint'},
        80: {'title': 'Crime', 'icon': 'fa-mask'},
        99: {'title': 'Documentary', 'icon': 'fa-camera'},
        18: {'title': 'Drama', 'icon': 'fa-theater-masks'},
        10751: {'title': 'Family', 'icon': 'fa-home'},
        14: {'title': 'Fantasy', 'icon': 'fa-dragon'},
        36: {'title': 'History', 'icon': 'fa-landmark'},
        27: {'title': 'Horror', 'icon': 'fa-ghost'},
        10402: {'title': 'Music', 'icon': 'fa-music'},
        9648: {'title': 'Mystery', 'icon': 'fa-user-secret'},
        10749: {'title': 'Romance', 'icon': 'fa-heart'},
        878: {'title': 'Science Fiction', 'icon': 'fa-rocket'},
        10770: {'title': 'TV Movie', 'icon': 'fa-tv'},
        53: {'title': 'Thriller', 'icon': 'fa-knife'},
        10752: {'title': 'War', 'icon': 'fa-helmet-battle'},
        37: {'title': 'Western', 'icon': 'fa-hat-cowboy'}
    }
}
TV_Shows_Categories = {
        'TV Shows': {
        'page_title': 'TV Show Genres',
        10759: {'title': 'Action & Adventure', 'icon': 'fa-fist-raised'},
        16: {'title': 'Animation', 'icon': 'fa-film'},
        35: {'title': 'Comedy', 'icon': 'fa-face-grin-squint'},
        80: {'title': 'Crime', 'icon': 'fa-mask'},
        99: {'title': 'Documentary', 'icon': 'fa-camera'},
        18: {'title': 'Drama', 'icon': 'fa-theater-masks'},
        10751: {'title': 'Family', 'icon': 'fa-home'},
        10762: {'title': 'Kids', 'icon': 'fa-child'},
        9648: {'title': 'Mystery', 'icon': 'fa-user-secret'},
        10763: {'title': 'News', 'icon': 'fa-newspaper'},
        10764: {'title': 'Reality', 'icon': 'fa-glasses'},
        10765: {'title': 'Sci-Fi & Fantasy', 'icon': 'fa-rocket'},
        10766: {'title': 'Soap', 'icon': 'fa-soap'},
        10767: {'title': 'Talk', 'icon': 'fa-microphone'},
        10768: {'title': 'War & Politics', 'icon': 'fa-helmet-battle'},
        37: {'title': 'Western', 'icon': 'fa-hat-cowboy'}
    }
}
