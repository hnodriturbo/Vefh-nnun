// Function to handle the button click event
function handleButtonClick(event) {
    // Prevent the default behavior of the button (like submitting a form)
    event.preventDefault();
    // Stop the event from bubbling up the DOM tree
    event.stopPropagation();

    // Get the 'data-action' attribute value from the clicked button
    let action = $(this).attr('data-action');
    // Get the 'data-formSubmit' attribute value from the clicked button
    let formSubmitValue = $(this).attr('data-formSubmit');

    // Log the action to the console
    console.log(action + ' button clicked!');
    // Log the formSubmitValue to the console
    console.log('formSubmitValue = ' + formSubmitValue);

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
    } else {
        // Load content based on the action without sending any form data
        loadContent(action);
    }
}











    // Handle form submitted by clicking the "Submit" button or pressing "Enter"
    function handleButtonClick(event) {
        // Prevent normal form submission, which would cause a page reload
        event.preventDefault();

        // Get the closest button element and it's ID
        let clickedButton = $(event.target).closest('button');
        let submitterId = clickedButton.attr('id');
        let action = clickedButton.attr('data-action');

        let form = $(this);
        let formData = {};

        if (submitterId === 'create-order-proceed') {
            $.each(form.serializeArray(), function(_, field) {
                formData[field.name] = field.value;
            });
            console.log("Form data after serialization:", formData); // Debugging output

        } else if (submitterId === 'create-order-go-back') {
            console.log('go back button clicked with action = ' + action)
            // Skip form submission for back button
            loadContent(action);
            return;
        }

        // Execute loadContent function with the action and formData
        loadContent(action, formData);
    }