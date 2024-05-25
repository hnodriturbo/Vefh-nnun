$(document).ready(function() {
    // Load the navbar
    $("#navbar-placeholder").load("navbar.html");

    // Load the initial main content from parent.html
    $(".main-content").load("parent.html", function() {
        $(this).fadeIn('slow');
    });

    // Setup click event handlers after navbar is loaded
    $(document).on('click', 'nav a', function(e) {
        e.preventDefault();
        var href = $(this).attr('href');

        // Fade out the current content, load new content, and fade it in
        $('.main-content').fadeOut('fast', function() {
            $(this).load(href, function() {
                $(this).fadeIn('slow');
                // Call any necessary scripts specific to the loaded content here
            });
        });
    });
});
