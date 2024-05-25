//    /* ------------------------------------------------- *\    //
//   /* -----------      Hreiðar Pétursson      ----------- *\   //
//  /* ------------- -- ------------------- -- ------------- *\  //
// /* -------      Verkefni Vefhönnun Haust 2023      ------- *\ // 

  // -------------------------------------------------------- \\
 // ------------------------ extras.js ----------------------- \\
// ------------------------------------------------------------ \\


// DOM loaded function (runs when the document is fully loaded)
$(document).ready(function() {
    
    // Function to position the collapsible content
    function positionContent($btn) {
        var $content = $($btn.data('bs-target')); // $ to clarify a jquery object
        var offset = $btn.offset();

        $content.css({
            top: offset.top + $btn.outerHeight(), // Position below the button
            left: offset.left, // Align with the left edge of the button
            position: 'fixed' // Ensure positioning is fixed to the viewport
        });
    }

    // Hover event listener for navbar buttons
    $('.navbar-button').mouseenter(function () { 
        var $content = $($(this).data('bs-target'));
        positionContent($(this));
        $content.collapse('show');
    });

    // Close the content when the mouse leaves the button or collapsed content
    $('.navbar-button').mouseleave(function () { 
        var $content = $($(this).data('bs-target'));
        setTimeout(function () {
            if (!$content.is(':hover')) {
                $content.collapse('hide');
            }

        }, 1000); // Adjust delay as needed
    });


    /* If mouse is over the collapsed content and leaves the are then hide the content */
    $('.collapse-content').mouseleave(function () {
        $(this).collapse('hide');
    })


// Function to initialize event listeners for navbar buttons
function initNavbarButtonEvents() {
    // Setup hover listeners for navbar buttons
    $('.navbar-button').off('mouseenter').on('mouseenter', function() {
        // Logic for showing collapsible content
        var $content = $($(this).data('bs-target'));
        positionContent($(this));
        $content.collapse('show');

    }).on('mouseleave', function() {
        // Logic for hiding collapsible content
        var $content = $($(this).data('bs-target'));
        setTimeout(function () {
            if (!$content.is(':hover')) {
                $content.collapse('hide');
            } // End of if statement
        }, 100); // Adjust delay as needed
    });

    // Setup listener for collapsing content
    $('.collapse-content').off('mouseleave').on('mouseleave', function() {
        $(this).collapse('hide');
    });
}

});

/* 
    $('.navbar-button').click(function() {
        var $btn = $(this); 
        var $content = $($(this).data('bs-target'));

       
        var offset = $btn.offset();
        $content.css({
            top: offset.top + $btn.outerHeight(),
            left: offset.left,
            position: 'fixed'
        });
    });

 */


/*     
$(".dropdown").on("hide.bs.collapse",function() {

    $(this).find(".dropdown-menu").first().addClass("sliding" )
  
  });
  
  $(".dropdown").on("hidden.bs.collapse",function() {
  
    $(this).find(".dropdown-menu").first().removeClass("sliding" )
  
  });
  
  $(document).click(function() {
  
    $(".dropdown-menu.collapse.show").collapse("hide");
      
  });
 */

/*   $('.collapse').collapse(); */




// Function to initialize event listeners for navbar buttons
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
