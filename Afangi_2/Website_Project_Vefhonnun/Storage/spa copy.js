// Function to load the navbar
function loadNavbar() {
    $('#navbar-placeholder').load('navbar.html');
}

// Function to load the carousel
function loadCarousel() {
    $('#carousel-placeholder').load('carousel.html');
}

// Function to dynamically load content
function loadContent(url, pushState) {
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'html',
        success: function(response) {
            $('.main-content').fadeOut('fast', function() {
                $(this).html(response);
                $('main-content').fadeIn('slow');

                if (pushState) {
                    history.pushState({ url: url }, null, url);
                }
            });
        },
        error: function() {
            $('.main-content').fadeOut(300, function() {
                $(this).html('<p>Error loading content.</p>').fadeIn(300);
            });
        }
    });
}
        // Fade out the current content, load new content, and fade it in
/*         $('.main-content').fadeOut('fast', function() {
            $(this).load(href, function() {
                $(this).fadeIn('slow');

            });
        });

 */
// Function to determine which content to load based on the current URL
function determineContentToLoad() {
    var params = new URLSearchParams(window.location.search);
    var action = params.get('action');
    var contentUrl = 'index.html?action=main-site.html'; // Default content

    if (action) {
        // Check if the action value is a valid file name
        if (action.endsWith('.html')) {
            contentUrl = action;
        }
    }

    return contentUrl;
}


// Function to handle page initialization and refresh
function initializeOrRefreshPage() {
    var params = new URLSearchParams(window.location.search);
    var action = params.get('action');

    if (!action) {
        // If no action is specified, redirect to ?action=parent.html
        window.location.href = window.location.origin + window.location.pathname + '?action=main-site.html';
    } else {
        // If there is an action, load the Navbar, Carousel, and the content
        loadNavbar();
        loadCarousel();

        var contentToLoad = determineContentToLoad();
        loadContent(contentToLoad, false);
    }
}

// Set up the SPA's initial state when the document is ready
$(document).ready(function() {
    initializeOrRefreshPage();

    // Setup click event handler for dynamic content loading
    $(document).on('click', '.load-content', function(e) {
        e.preventDefault();
        var url = $(this).attr('href');
        loadContent(url, true);
    });

    // Handle browser navigation events (back and forward buttons)
    window.onpopstate = function(event) {
        if (event.state) {
            loadContent(event.state.url, false);
        } else {
            loadContent('index.html', false);
        }
    };
});
