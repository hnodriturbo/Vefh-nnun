/*        <-- -------------------- ADMIN SÍÐAN -------------------- -->
        <-- ------------------- HREIÐAR PÉTURSSON ------------------- -->
      <-- ------------------------------------------------------------- -->
    <-- --------------------------- MADE 2023 --------------------------- -->   */
    
/*  <-- ---------------------- CREATE_SPA_GEYMA.JS ---------------------- --> */
    
    
    
    /* THIS IS THE GO BACK TO CODE JUST IN CASE - THIS ONE WORKED */
    
    $(document).on('click', '#add-order-step-1', function() {
        console.log('add-order-step-1 button clicked');
        let actionInfo = $(this).data('action');
        $.post("add_action.php", {
            action: actionInfo
        }, function(data) {
            $("#main-content-container").html(data);
        });
    });

    $(document).on('click', '#add-order-step-2', function() {
        console.log('add-order-step-2 button clicked');
        let actionInfo = $(this).data('action');
        $.post("add_action.php", {
            action: actionInfo
        }, function(data) {
            $("#main-content-container").html(data);
        });
    });

    // Function to handle the button click event
function handleButtonClick(event) {
    // Prevent the default behavior of the button (like submitting a form)
    event.preventDefault();
    // Stop the event from bubbling up the DOM tree
    event.stopPropagation();
    // Get the 'data-action' attribute value from the clicked button
    let action = $(this).attr('data-action');
    // Log the action to the console
    console.log(action + ' button clicked!');
    // Load content based on the action
    loadContent(action);
    // Check if the clicked button is inside a form
    if ($(this).closest('form').length) {
        // Get the closest form to the clicked button
        let form = $(this).closest('form');
        // Create an empty object to store the form data
        let formData = {};
        // Serialize the form data into an array and populate the formData object
        $.each(form.serializeArray(), function(_, field) {
            formData[field.name] = field.value;
        });
        // Load content based on the action and send the form data
        loadContent(action, formData);
    } 
    else {
        // Load content based on the action without sending any form data
        loadContent(action);
    } 
}
 
    // If enter button is pressed in the form trigger create-order-proceed button click
    $('form').on('keypress', function(event) {  
        if (event.which == 13) { // 13 is the key code for "Enter"
            event.preventDefault();
            $('#create-order-proceed').click();
        }
    })

    // Function for button click event - retrives the action 
    // & executes loadContent with action as parameter
    function handleButtonClick(event) {
        event.preventDefault();
        event.stopPropagation();
        let action = $(this).attr('data-action');
        console.log(action + ' button clicked !');
        loadContent(action);
    }





            // This foreach loop is only to use console log to iterate
            // over each key and value submitted to check form submit
            formDataArray.forEach((item) => {
                console.log(`Key: action, Value: ${item.action}`);
                for (const [key, value] of Object.entries(item.data)) {
                    console.log(`Key: ${key}, Value: ${value}`);
                } 
            });



    

    function loadContent(action) {
        $.ajax({
            url: 'create_index.php',
            method: 'POST',
            data: { action: action },
            success: function(response) {
                $('#spinner').hide();
                $('#main-content-container').fadeOut(300, function() {
                    $(this).html(response).fadeIn(300);

                    // Update buttons based on the current action
                    switch (action) {
                        case 'create-order-step-1':
                            $('#create-order-go-back').attr('data-action', 'go-to-index');
                            $('#create-order-go-back span').text('Go Back To Index');
                            $('#create-order-proceed').attr('data-action', 'create-order-step-2');
                            $('#create-order-proceed span').text('Proceed to Step 2');
                            break;
                        case 'create-order-step-2':
                            $('#create-order-go-back').attr('data-action', 'create-order-step-1');
                            $('#create-order-go-back span').text('Go Back To Step 1')
                            $('#create-order-proceed').attr('data-action', 'create-order-step-3');
                            $('#create-order-proceed span').text('Proceed to Step 3');
                            break;
                        // Add additional cases for other steps as needed
                    }
                }) 
                // Push a new entry onto the history stack
                window.history.pushState({ action: action }, '', `create_index.php?action=${action}`);
            },
            error: function(xhr, status, error) {
                $("#spinner").hide();
                alert('An error occurred: ' + error);
            }
        });
    }


    // Click event handler for Go Back Button
    $(document).off('click', '#create-order-go-back').on('click', '#create-order-go-back', function(event) {
        event.preventDefault();
        event.stopPropagation();
        let action = $(this).attr('data-action');
        console.log(action + ' button clicked !');
        loadContent(action);

    });
    // Click event handler for Proceed Button
    $(document).off('click', '#create-order-proceed').on('click', '#create-order-proceed', function(event) {
        event.preventDefault();
        event.stopPropagation();
        let action = $(this).attr('data-action');
        console.log(action + ' button clicked !');
        loadContent(action);
    });
    
    // Browsers back and forward buttons
    window.addEventListener('popstate', function(event) {
        if(event.state) {
            let action = event.state.action;
            loadContent(action, false);
        } else {
            loadContent('go-to-index', false);
        }
    })


    // Go Back button click
    $(document).on('click', '#create-order-go-back', function(event) {
        event.stopPropagation();
        let action = $(this).attr('data-action');
        console.log(action + ' button clicked !')
        loadContent(action);
    })
    // Proceed button on click
    $(document).on('click', '#create-order-proceed', function(event) {
        event.stopPropagation();
        let action = $(this).attr('data-action');
        console.log(action + ' button clicked !');
        loadContent(action);

    }) 
     
    $(document).off('click.myNamespace').on('click.myNamespace', '#create-order-go-back', function(event) {
        let action = $(this).attr('data-action');
        console.log(action + ' button clicked !');
        loadContent(action); 
    });
    
    // Go back button
    $('#go-back').off('click').on('click', function(event) {
        event.stopPropagation();
        let action = $(this).attr('data-action');
        console.log('go back to index button clicked')
        loadContent(action);
    })


    // Create order step 1 button
    $('#create-order-step-1').off('click').on('click', function(event) {
        event.stopPropagation();
        console.log('create order step 1 button clicked')
        loadContent('create-order-step-1');
    });


    $('#create-order-step-2').off('click').on('click', function(event) {
        event.stopPropagation();
        console.log('create order step 2 button clicked')
        loadContent('create-order-step-2');
    });




    function getParameterByName(name, url = window.location.href) {
        name = name.replace(/[\[\]]/g, '\\$&');
        var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }

    // Get the action from the URL
    var action = getParameterByName('action');
    if (action) {
        // Load the appropriate content based on the action
        loadContent(action);
    }


    
    // Handle back button in browser
    window.addEventListener("popstate", function(event) {
        if(event.state) {
            const action = event.state.action;
            switch(action) {
                case 'create-order-step-1':
                    loadContent('create-order-step-1', false);
                    break;
                case 'create-order-step-2':
                    loadContent('create-order-step-2', false);
                    break;
                case 'initial':
                default:
                    loadContent('go-to-index', false);
                    break;
            }
        } else {
            loadContent('go-to-index', false);
        }
    });





/*     ÉG BREYTTI AÐEINS OG ER GEYMA ÞETTA */
    // Load content function
    function loadContent(action, pushState = true) {
        console.log('loadContent called with action:', action);
        let url = 'add_action.php';
        $.ajax({
            url: url,
            method: 'GET',
            data: { action: action },
            success: function(response) {
                $('#main-content-container').html(response);
                // Update buttons based on the current action
                switch (action) {
                    case 'create-order-step-1':
                        $('#go-back').attr('data-action', 'go-to-index');
                        $('#go-back').text('Go Back To Index')
                        $('#add-order-step-2').attr('data-action', 'create-order-step-2');
                        $('#add-order-step-2 span').text('Proceed to Step 2');
                        break;
                    case 'create-order-step-2':
                        $('#go-back').attr('data-action', 'create-order-step-1');
                        $('#add-order-step-2').attr('data-action', 'create-order-step-3');
                        $('#add-order-step-2 span').text('Proceed to Step 3');
                        break;
                    // Add additional cases for other steps as needed
                }
                if (pushState) {
                    window.history.pushState({ action: action }, '', '?action=' + action);
                }
            },
            error: function(xhr, status, error) {
                console.error('Error fetching content:', status, error);
            }
        });
    }



    
