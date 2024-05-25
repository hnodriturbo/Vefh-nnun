//    /* ------------------------------------------------- *\    //
//   /* -----------      Hreiðar Pétursson      ----------- *\   //
//  /* ------------- -- ------------------- -- ------------- *\  //
// /* -------      Verkefni Vefhönnun Haust 2023      ------- *\ // 

  // -------------------------------------------------------- \\
 // ------------------------- spa.js ------------------------- \\
// ------------------------------------------------------------ \\

/**

 * spa.js - Single Page Application Script
 * This script manages the dynamic content loading and navigation for a Single Page Application.
 * It handles the loading of different components like navbar, carousel, and main content based on URL parameters.
 * It also manages browser history for seamless navigation within the application.

 */

/**
 * SPA (Single Page Application) Script
 * 
 * This script facilitates the dynamic loading of content for the website,
 * handling different components such as the navbar, carousel, and main content.
 * It also manages browser history for seamless navigation within the SPA.
 */



/** --- Description of the navbar functionality --- 
 * Function to load the navbar content html file
 * Dynamically load the "navbar.html" into the designated placeholder
 * Initialize navbar button events after loading the navbar
 * Setup hover listeners for navbar buttons
 * Setup listener for collapsing content
 * Position the collapsible content in the navbar
 */ 
 



/**
 * Load Navbar
 * This function loads the navigation bar of the website. It dynamically
 * adds the menu items and ensures they are displayed correctly.
 */
function loadNavbar() {
    // Dynamically load the "navbar.html" into the designated placeholder
    $('#navbar-placeholder').load('navbar.html', function() {
        // Initialize navbar button events after loading the navbar
        initNavbarButtonEvents();
    });
}

/**
 * Initialize Navbar Button Events
 * Sets up click events for the navbar buttons. This allows users to
 * interact with the navbar, ensuring the correct content is loaded when
 * a menu item is clicked.
 */
function initNavbarButtonEvents() {
    // Setup hover listeners for navbar buttons
    $('.navbar-button').off('mouseenter mouseleave')
        .on('mouseenter', function() {
            // Close any open collapsible contents before opening a new one
            $('.collapse-content').collapse('hide');

            // Find the collapsible content related to the hovered button
            var $content = $($(this).data('bs-target'));

            // Position the content correctly and show it
            positionContent($(this));
            $content.collapse('show');
        })
        .on('mouseleave', function() {
            // Logic for hiding collapsible content after a delay
            var $content = $($(this).data('bs-target'));
            setTimeout(function () {
                // Check if the mouse is no longer hovering over the button or its content
                if (!$content.is(':hover')) {
                    // If not, hide the collapsible content
                    $content.collapse('hide');
                } // End of if statement
            }, 100); // Adjust delay as needed
        });

    // Setup listener for collapsing content
    $('.collapse-content').off('mouseleave').on('mouseleave', function() {
        // Hide the content when the mouse leaves the collapsible area
        $(this).collapse('hide');
    });
}


/**
 * Position Content in Navbar
 * Adjusts the position of collapsible content within the navbar. This
 * function is important for ensuring that the collapsible elements open
 * and close correctly in the navbar.
 */
function positionContent($btn) {
    var $content = $($btn.data('bs-target')); // $ to clarify a jquery object
    var offset = $btn.offset();

    $content.css({
        top: offset.top + $btn.outerHeight() - $(window).scrollTop(), // Position below the button
        left: offset.left, // Align with the left edge of the button
        position: 'fixed' // Ensure positioning is fixed to the viewport
    });
}


// Function for showing the content
function showContent($btn) {
    $('.collapse-content').collapse('hide');
    var $content = $($btn.data('bs-target'));
    positionContent($(this));
    $content.collapse('show');
}


// Function for hiding the content
function hideContent($content) {
    setTimeout(function () {
        if (!$content.is(':hover')) {
            $content.collapse('hide');
        }
    }, 1000); // Adjust delay as needed
}    


















/**
 * Load Carousel
 * This function handles the loading of the image carousel on the website.
 * It dynamically adds images and controls to the carousel for interactive
 * image display.
 */
function loadCarousel() {
    // Dynamically load the "carousel.html" into the designated placeholder
    $('#carousel-placeholder').load('carousel.html');
}

/**
 * Load About Section
 * Loads the 'About' section of the website. This function dynamically
 * fetches and displays information about the event or organization.
 */
function loadAboutEvent() {
    // Dynamically load the "about.html" into the designated placeholder
    $('#about-placeholder').load('about.html');
}






















/**
 * Load Main Content
 * Dynamically loads the main content of the website based on URL
 * parameters. This function is key to the SPA's ability to show
 * different content without reloading the page.
 */
function loadContent() {

    // Retrieve the 'action' parameter from the URL
    var action = new URLSearchParams(window.location.search).get('action');
    
    // Determine the content URL, defaulting to 'main-site.html' if no action specified
    var contentUrl = action ? action : 'main-site.html';

    // Make an AJAX request to load the specified content
    $.ajax({
        url: contentUrl,
        type: 'GET',
        dataType: 'html',
        success: function(response) {
            // Replace the main content with the response, using fade transitions
            $('.main-content').fadeOut('fast', function() {
                $(this).html(response).fadeIn('slow');

            });
            // Reinitialize navbar button events every time new content is loaded
            initNavbarButtonEvents();
        },

        // Display an error message if content loading fails
        error: function() {
            $('.main-content').html('<h1>Error loading content.</h1>').fadeIn('slow');
        }
    }); // End of AJAX request
} // End of loadContent() function
























/**
 * Dynamic Content Loading Handler
 * This event handler manages the loading of content when different parts
 * of the website are clicked. It ensures that the right content is loaded
 * dynamically as the user navigates the site.
 */
$(document).off('click', '.load-content').on('click', '.load-content', function(e) {
    // Prevent the default anchor tag behavior
    e.preventDefault();

    // Construct the new URL using the href attribute of the clicked element
    var url = $(this).attr('href');
    var newUrl = 'index.html?action=' + url;

    // Update the browser's address bar and history without reloading the page
    window.history.pushState({ path: newUrl }, '', newUrl);

    // Load the new content
    loadContent();

}); // End of load-content event handler

















/**
 * Browser Navigation Event Handler
 * Handles browser navigation events like the back and forward buttons.
 * This ensures that the SPA responds correctly to browser history
 * navigation actions.
 */
window.onpopstate = function(event) {
    // Load the appropriate content if the history state exists
    if (event.state && event.state.path) {
        loadContent();
    }
};




















/**
 * Close Splash Screen
 * Closes the splash screen used for promotions or announcements on the
 * website. This function is triggered either manually by the user or
 * automatically after a set time.
 */
function closeSplashScreen() {
    document.querySelector('.splash-screen').style.display = 'none';
  }

/**
 * Subscribe Image Click Event
 * Adds functionality to the subscription image in the splash screen,
 * allowing users to subscribe to the newsletter when they click on the
 * image.
 */
document.querySelector('.subscribe-image').addEventListener('click', function() {
    
    // Scroll to the subscription form container
    document.getElementById('subscription-form-container').scrollIntoView({ behavior: 'smooth' });

    // Optionally, close the splash screen
    closeSplashScreen();
});

/**
 * Auto Close Splash Screen
 * Automatically closes the splash screen after a set time delay. This
 * ensures that the splash screen does not stay on the user's screen
 * indefinitely.
 */
setTimeout(closeSplashScreen, 10000); // 10 seconds delay















/**
 * Document Ready Initialization
 * Executes certain functions when the webpage is fully loaded. This is
 * important for initializing various components of the SPA after the
 * entire document is ready.
 */
$(document).ready(function() {


    // Load the navbar and carousel, and then the main content
    loadCarousel();
    loadContent();
    loadNavbar();
    


    // navbar button hover event listener
    $('.navbar-button').mouseenter(function () {
        showContent($(this));
    }).mouseleave(function () {
        hideContent($($(this).data('bs-target')));
    });


    // collapse-content hover event listener
    $('.collapse-content').mouseleave(function () {
        $(this).collapse('hide');
    }) 


    // Position the collapsible content in the navbar when scrolling
    $(window).scroll(function() {
        if ($('.collapse-content.show').length) {
            positionContent($('.navbar-button:hover'));
        }
    });

}); // End of document ready function


