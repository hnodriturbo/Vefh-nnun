/*        <-- -------------------- ADMIN SÍÐAN --------------------- -->
        <-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
      <-- -------------------------------------------------------------- -->
    <-- --------------------------- MADE 2023 ---------------------------- -->   */


// Info about setting, getting, removing and clearing sessionStorage 
// For me to store the current step user is on after a refresh

// Set Data: You can use the sessionStorage.setItem method to store data. 
/* sessionStorage.setItem("currentStep", "2"); */

// Get Data: You can use the sessionStorage.getItem method to get data. 
/* var currentStep = sessionStorage.getItem("currentStep"); */

// Remove Data: You can use the sessionStorage.removeItem method to remove data
/* sessionStorage.removeItem("currentStep"); */

// Clear Data: You can use the sessionStorage.clear method to clear all data:
/* sessionStorage.clear(); */



// Table of contents - Functions:

// 1. The form validation
    // Smá útskýring

// 2. The loadContent function - my main function
    // hérna ætla ég skrifa smá lýsingu hvað hún gerir

// 3. Update buttons function
    // smá lýsing

// 4. Button click function
    // smá lýsing

// 5. Refresh, back, forward buttons (popstate) event
    // smá lýsing

 

/* ----------------------------------------------------------------------------- */
/* ------------------------- Document ready function --------------------------- */

/* When document is ready this function executes */
$(function() {





/* ----------------------------------------------------------------------------- */
/* ------------ ---- 1. Function for actively validating input ---- ------------ */

// Validate function that takes inputField as parameter
function validateInput(inputField) {
    // Gets the DOM element of the input field using inputField.get(0) and checks its validity.
    let validity = inputField.get(0).checkValidity();
    // Removes the is-invalid and is-valid classes from the input field, so we can reset its state.
    // Adds the is-valid class if the input field is valid, and the is-invalid class if it's not.
    inputField.removeClass('is-invalid is-valid').addClass(validity ? 'is-valid' : 'is-invalid');
}

// Adds a focus event listener to all the input fields inside a form with the needs-validation class.
// When an input field is focused (clicked on), the function inside the event listener is executed.
$('.needs-validation .form-control').on('focus', function() {
    // The input field that triggered the focus event is stored in the inputField variable.
    let inputField = $(this);
    // function executed with the input field as a parameter to immediately validate when focused.
    validateInput(inputField); // Validate immediately on focus
    // Function is called with the input field as a parameter to validate it as the user types.
    inputField.on('input', function() {
        validateInput(inputField); // Validate on further input
    // When user clicks outside the input field, function in the event listener is executed.
    }).on('blur', function() {
        // Stops the input field from being actively validated once the user is done.
        inputField.off('input');
    });
});



/* ------- ---- 1. My form validation code for validating the forms ---- ------- */
/* ----------------------------------------------------------------------------- */


/* ----------------------------------------------------------------------------- */


/* ----------------------------------------------------------------------------- */
/* -------- 2. Function for loading the content and submitting the form -------- */

// Create empty array to keep the form data
let formDataArray = [];

// Function for loading the main content and use ajax to POST to my PHP script
function loadContent(action, formSubmit, formData, fromPopstate = false) {
    // Debug statement
    console.log("loadContent called with action: " + action + " :: formsubmit value: " + formSubmit + " :: fromPopstate : " + fromPopstate);
    
    // First check if the execution is using popstate (back,forward,refresh buttons)
    if(fromPopstate) { // if so, set the formData to null (prevent double formData)
        formData = null;
    }
    if (formData) {
        // Check if a form is submitted by using console log
        console.log("Form submitted!");
        // Push the form data into the array
        formDataArray.push({action: action, data: formData});
    }
    // Set the current action (step) into the sessionStorage
    /* sessionStorage.setItem('currentAction', action); */
    // Start the ajax script and POST the action, formSubmit and formData
    $.ajax({ 
        url: 'create_index.php',
        method: 'POST',
        data: { action: action, formSubmit: formSubmit, formData: formData },
        // On success execute this code
        success: function(response) {
            // Fade out main content container
            $('#main-content-container').fadeOut(300, function() {
                // and fade in the servers response
                $(this).html(response).fadeIn(300); 
                // Execute the updatebuttons with action as parameter
                updateButtons(action);
            });

            if(!fromPopstate) { // If not popstate event then pushState new window history
                window.history.pushState({ action: action }, '', `create_index.php?action=${action}`);
            } 
        },
        // Handle the errors
        error: function(xhr, status, error) {
            console.log('An error occurred: ' + error)
        }
    });
}
/* ------- 2. FUNCTION FOR LOADING THE MAIN CONTENT AND SUBMIT THE FORM -------- */
/* ----------------------------------------------------------------------------- */


/* ----------------------------------------------------------------------------- */


/* ----------------------------------------------------------------------------- */
/* ----------------- ----- 2. The updateButtons function ----- ----------------- */

// Update buttons based on the current action
function updateButtons(action) {
    switch (action) {
        // If action is create-order-step-1 update buttons values
        case 'create-order-step-1':
            // Proceed button
            $('#create-order-proceed span').text('Proceed to Step 2');
            $('#create-order-proceed').attr('data-action', 'create-order-step-2');
            $('#create-order-proceed').attr('data-formSubmit', 'step-1-form-data');
            // Go back button
            $('#create-order-go-back span').text('Go Back To Index');
            $('#create-order-go-back').attr('data-action', 'go-to-index');
            break;
        // If action is create-order-step-2 update buttons values
        case 'create-order-step-2':                
            // Create order proceed button text and attributes
            $('#create-order-proceed span').text('Proceed to Step 3');
            $('#create-order-proceed').attr('data-action', 'create-order-step-3');
            $('#create-order-proceed').attr('data-formSubmit', 'step-2-form-data');
            // Create order go back button text and attributes
            $('#create-order-go-back span').text('Go Back To Step 1')
            $('#create-order-go-back').attr('data-action', 'create-order-step-1');
            break;
    }
}
/* --------------- ----- 2. The updateButtons function ----- --------------- */
/* ------------------------------------------------------------------------- */


/* ------------------------------------------------------------------------- */


/* ------------------------------------------------------------------------- */
/* --------- ----- 3. Function that handles the button click ----- --------- */
// Handle form submitted by clicking the "Submit" button or pressing "Enter"
function handleButtonClick(event) {
    console.log("handleButtonClick called"); // add this line for debug purposes

    // Prevent normal form submission, which would cause a page reload
    event.preventDefault();

    // Get the closest button element and its attributes
    let clickedButton = $(event.target).closest('button');
    let buttonID = clickedButton.attr('id');
    let action = clickedButton.attr('data-action');
    let formSubmit = clickedButton.attr('data-formSubmit');

    // if proceed button click retrieve the formData and execute loadContent with it
    if (buttonID === 'create-order-proceed') {
        let form = clickedButton.closest('form'); // get the closest form using jQuery
        if (form.length) { // if form has some values and length
            // Check form validity
            if (form[0].checkValidity()) { // if form is valid
                let formData = form.serialize(); // serialize the form data
                console.log("Serialized form data:", formData);
                // Execute loadContent with action & formSubmit & formData
                loadContent(action, formSubmit, formData, false);
            } else {
                // If form is not valid, add 'was-validated' class to show validation feedback
                form.addClass('was-validated');
            }
        } else { // in case the proceed button isn't inside a form
            loadContent(action);
        }
    // if go back button click execute the loadContent only with the action
    } else if (buttonID === 'create-order-go-back') {
        loadContent(action, null, null, false);
    }
}



// On Proceed or Go Back button click execute the handleButtonClick function
$(document).off('click', '#create-order-proceed, #create-order-go-back').on('click', '#create-order-proceed, #create-order-go-back', handleButtonClick);


/* --------- ----- 3. Function that handles the button click ----- ---------- */
/* -------------------------------------------------------------------------- */


/* -------------------------------------------------------------------------- */


/* -------------------------------------------------------------------------- */
/* ----- ----- 4. Refresh, back, forward buttons (popstate) event ----- ----- */

/* This is the back and forward buttons */
window.addEventListener('popstate', function(event) {
    // Check if 'state' property exists in the event object
    if (event.state) {
        // Get 'action' value from 'state' property
        let action = event.state.action;
        // Load content based on the retrieved 'action' value and indicate that it's from the popstate event
        loadContent(action, null, null, true);
    } else {
        // No 'state' property, load default or index content
        loadContent('go-to-index', null, null, true);
    }
});


/* ----- ----- 4. Refresh, back, forward buttons (popstate) event ----- ----- */
/* -------------------------------------------------------------------------- */


window.onbeforeunload = function() {
    // Set a URL parameter to indicate that the page was closed
    window.location.href = window.location.href + "?closed=true";
}
/* 
function repopulateFields(storedData) {
    for (const [name, value] of Object.entries(storedData)) {
        const field = $(`[name="${name}"]`);

        if (field.is(':radio, :checkbox')) {
            field.prop('checked', value === 'on');
        } else {
            field.val(value);
        }
    }
}
 */










/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */


}); // document ready function


/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */













/* -------- GEYMA ÞETTA AÐEINS --------- */
/* // Function for handling the popstate refresh button
function handlePopstate(event) {
    // Check if event was triggered by a page refresh
    if(!event.originalEvent || event.originalEvent.type !== 'popstate') {
        // This was triggered by a page refresh
        var action = sessionStorage.getItem('currentAction');
        if(action) {
            loadContent(action, null, null, true);
        } else {
            loadContent('go-to-index', null, null, true);
        }
        return;
    } 
}
// Attach the popstate event handler
$(window).off('popstate', handlePopstate).on('popstate', handlePopstate); */










/* 
// Keep for later use
function finishProcess() {
    // Here will be the finishing process
    // Retrive the users previous steps and show them for overview
    sessionStorage.clear();
}
 */
/* 
        // This was inside the loadContent function - keep for later use
// Repopulate the fields if data exists for the current action
repopulateFields(action, $(this).find('form'));

function repopulateFields(action, form) {
    // Find the matching entry in formDataArray
    let matchingData = formDataArray.find(item => item.action === action);
    if (matchingData) {
        // Loop through the stored data and set the form field values
        for (let key in matchingData.data) {
            form.find(`[name="${key}"]`).val(matchingData.data[key]);
        }
    }
}
  */  





// This is only to see if the array's populated with the data
/* 
formDataArray.forEach((item) => {
    console.log('Action: ', item.action);
    console.log('Form Data: ', item.data);
});
  */           
