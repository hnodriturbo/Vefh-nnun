/*        <-- -------------------- ADMIN SÍÐAN --------------------- -->
        <-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
      <-- -------------------------------------------------------------- -->
    <-- --------------------------- MADE 2023 ---------------------------- -->   */

// Table of contents:

// 2. The loadContent function - my main function
    // hérna ætla ég skrifa smá lýsingu hvað hún gerir

// 3. Update buttons function
    // smá lýsing

// 4. Button click function
    // smá lýsing

// 5. Refresh, back, forward buttons (popstate) event
    // smá lýsing

// 6. Session Storage - Form To Object, Store, Get, Remove, Print functions
    // smá lýsing

 

/* ----------------------------------------------------------------------------- */
/* ------------------------- Document ready function --------------------------- */

/* When document is ready this function executes */
$(function() {


    function handleProductAddition(productId, quantity) {
        console.log("Sending AJAX request for product:", productId); // Add this line
        $.ajax({
            url: 'create_fetch_products.php',
            type: 'POST',
            data: { product_id: productId },
            dataType: 'json',
            success: function(product) {
                console.log("Fetched product:", product); // Modify this line
                let addedProducts = JSON.parse(sessionStorage.getItem('addedProducts')) || [];
                product.quantity = quantity; // Add quantity to product object
                addedProducts.push(product);
                sessionStorage.setItem('addedProducts', JSON.stringify(addedProducts));
                displayAddedProducts(); // Moved inside success callback
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error:", error); // Add this line
            }
        });
    }
    
    
    


// Function to display added products
function displayAddedProducts() {
    const addedProducts = JSON.parse(sessionStorage.getItem('addedProducts')) || [];
    let addedProductsHtml = '';

    addedProducts.forEach(product => {
        // For each added product, create HTML markup.
        addedProductsHtml += `
            <div class="added-product row">
            <div class="col-2">
                <img src="../img/products/${product.image}" alt="${product.name}" class="img-fluid">
            </div>
            <div class="col-8">
                <h4>${product.name}</h4>
                <p>${product.product_id}</p>
                <p>${product.price} ISK</p>
            </div>
            <div class="col-2">
                <div class="row">
                <button class="btn btn-danger remove-product-btn" data-product-id="${product.product_id}">Remove</button>
                </div>
            </div>
        </div>
        `;
    });

    // Update the container with the new HTML
    // First hide the container, then update HTML, and finally apply fade in effect
    $('#added-products-window-container').fadeOut(300, function() {
        $(this).html(addedProductsHtml).fadeIn(300);
    });
}

// Use event delegation for remove buttons
$('#added-products-window-container').on('click', '.remove-product-btn', function() {
    const productIdToRemove = $(this).data('product-id');
    console.log("Product ID to remove:", productIdToRemove); // Log for debugging
    removeProduct(productIdToRemove);
    displayAddedProducts(); // Refresh display after removal
});


// Function to remove a product from the 'addedProducts' array in session storage
// Function to remove a product
function removeProduct(product_id) {
    let addedProducts = JSON.parse(sessionStorage.getItem('addedProducts')) || [];
    console.log("Before removal:", addedProducts);
    addedProducts = addedProducts.filter(product => product.product_id !== product_id);
    console.log("After removal:", addedProducts);
    sessionStorage.setItem('addedProducts', JSON.stringify(addedProducts));
    displayAddedProducts(); // Refresh display after removal
}






    // This retrives the product id and quantity and console logs it - WORKING
    $(document).on('click', '.add-to-order-btn', function() {
        const productId = $(this).data('product-id');
        const quantityInput = $(this).closest('.product-container').find('input[name="quantity"]').val();
        let quantity = parseInt(quantityInput) || 0; // Corrected line

        if (quantity > 0) {
            handleProductAddition(productId, quantity);
            console.log("Product ID:", productId, "Quantity:", quantity);
        }
        // Add logic to handle adding the product to order
        // For example, you might want to store the product ID and quantity in session storage or perform another action

    });














    $('#category-dropdown').on('change', function() {
        console.log("Dropdown changed"); // Add this line

        const categoryId = $(this).val();

        $.ajax({
            url: 'create_fetch_products.php',
            type: 'POST',
            data: { category_id: categoryId },
            dataType: 'json',
            success: function(products) {
                let productHtml = '';
                products.forEach(product => {
                    productHtml += `
                        <div class="product-container row">
                            <div class="col-2">
                                <img src="../img/products/${product.image}" alt="${product.name}" class="img-fluid">
                            </div>
                            <div class="col-8">
                                <h4>${product.name}</h4>
                                <p>${product.description}</p>
                                <p>${product.price} ISK</p>
                            </div>
                            <div class="col-2">
                                <div class="row">
                                Quantity :<input class="form-control bg-dark-subtle" type="number" name="quantity" min="1" aria-label="default input example">
                                </div>
                                <br>
                                <div class="row">
                                    <button data-product-id="${product.product_id}" class="btn btn-secondary add-to-order-btn">Add to Order</button>
                                </div>
                            </div>
                        </div>
                    `;
                });

                $('#product-window-container').fadeOut(300, function() {
                    $(this).html(productHtml).fadeIn(300);
                })
                // $('#product-window-container').html(productHtml);
            }
        });
    });


    
/* ----------------------------------------------------------------------------- */
/* -------- 1. Function for loading the content and submitting the form -------- */
let currentIndex = 0
// Function for loading the main content and use ajax to POST to my PHP script
function loadContent(action, repopulate = false,  fromPopstate = false) {
    // Debug statement
    console.log("loadContent called with action: " + action + ":: fromPopstate : " + fromPopstate);

    /* storeActiveStepInSession(action); */
    const currentStepNumber = parseInt(sessionStorage.getItem("Active-Step-Number"))
    console.log("loadContent stepnumber from session: ", sessionStorage.getItem("Active-Step-Number"))

    // Start the ajax script and POST the action, formSubmit and formData
    $.ajax({ 
        url: 'create_index.php',
        method: 'POST',
        data: { action: action },
        // On success execute this code
        success: function(response) {
            if(!fromPopstate) { // If not popstate event then push the new action to the url
                // Every time a page loads i set the active step number that was loaded in sessionStorage
                storeActiveStepInSession(action);
                window.history.pushState({ action: action }, '', `create_index.php?action=${action}`);
            } 
            // Fade out main content container
            $('#main-content-container').fadeOut(300, function() {
                // and fade in the servers response
                $(this).html(response).fadeIn(300);
                // Console log session data for learning
                printSessionData();

                // If action is from popstate(back, forward) 
                if(repopulate) {
                    // Repopulate the fields with the existing data from array
                    repopulateFields(action);
                }
                // Envoke clear button functionality
                clearButtonFunction();
                // Update the buttons attributes and text
                updateButtons(action);
                // On focus actively validate the inputs
                activeInputFieldsValidation();
                // If there are any products in the session display them
                displayAddedProducts();
            });

        }
    });
}

/* --  --- 1. FUNCTION FOR LOADING THE MAIN CONTENT AND SUBMIT THE FORM ------ */
/* ----------------------------------------------------------------------------- */


/* ----------------------------------------------------------------------------- */


/* ----------------------------------------------------------------------------- */
  /* --------------- ----- 2. The updateButtons function ----- --------------- */

// Update buttons based on the current action
function updateButtons(action) {
    switch (action) {
        // If action is create-order-step-1 update buttons values
        case 'create-order-step-1':
            // Proceed button
            $('#create-order-proceed span').text('Proceed to step 2');
            $('#create-order-proceed').attr('data-action', 'create-order-step-2');
            $('#create-order-proceed').attr('data-formSubmit', 'create-order-step-1');
            // Go back button
            $('#create-order-go-back span').text('Go back to index');
            $('#create-order-go-back').attr('data-action', 'go-to-index');
            break;
        // If action is create-order-step-2 update buttons values
        case 'create-order-step-2':                
            // Create order proceed button text and attributes
            $('#create-order-proceed span').text('Proceed to step 3');
            $('#create-order-proceed').attr('data-action', 'create-order-step-3');
            $('#create-order-proceed').attr('data-formSubmit', 'create-order-step-2');
            // Create order go back button text and attributes
            $('#create-order-go-back span').text('Go back to step 1')
            $('#create-order-go-back').attr('data-action', 'create-order-step-1');
            break;
        // If action is create-order-step-3 update buttons values
        case 'create-order-step-3':
            // Proceed button
            $('#create-order-proceed span').text('Proceed to step 4');
            $('#create-order-proceed').attr('data-action', 'create-order-step-4');
            $('#create-order-proceed').attr('data-formSubmit', 'create-order-step-3');
            // Go back button
            $('#create-order-go-back span').text('Go back to step 2');
            $('#create-order-go-back').attr('data-action', 'create-order-step-2');
            break;

    }
}
  /* --------------- ----- 2. The updateButtons function ----- --------------- */
/* ----------------------------------------------------------------------------- */


   /* ----------------------------------------------------------------------- */


/* ---------------------------------------------------------------------------- */
/* ---------- ----- 3. Function that handles the button click ----- ----------- */

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

    // On proceed button click get the closest form and if it has data check validity
    if (buttonID === 'create-order-proceed') {
        removeFormDataFromSession(action); // Remove the openings step session data
        let form = clickedButton.closest('form'); // get the closest form using jQuery
        if (form.length) { // if form has some values and length
            if (form[0].checkValidity()) { // if form is valid
                // Convert the form into an object and store in session
                const formDataObject = formToObject(form[0]); 
                storeFormDataInSession(formSubmit, formDataObject);
                // Execute loadContent with action after storing the data in session
                loadContent(action, false, false);
            } else {
                // If form is not valid, add 'was-validated' class to show validation feedback
                form.addClass('was-validated');
            }
        } else { // If there is no form (like from index start) loadContent with the action
            loadContent(action, false, false)
        }
    // if go back button click execute the loadContent only with the action
    } else if (buttonID === 'create-order-go-back') {
        // By putting popstate as true it repopulates the fields in loadContent
        loadContent(action, true, false); 
        
    }
}

// On Proceed or Go Back button click execute the handleButtonClick function
$(document).off('click', '#create-order-proceed, #create-order-go-back').on('click', '#create-order-proceed, #create-order-go-back', handleButtonClick);


 /* --------- ---- 3. Function that handles the button click ---- ---------- */
/* -------------------------------------------------------------------------- */


  /* ---------------------------------------------------------------------- */


/* -------------------------------------------------------------------------- */
  /* ----- --- 4. Refresh, back, forward buttons (popstate) event --- ----- */

/* This is the back and forward buttons */
// Executes the loadContent based on the action in previous or forward steps
window.addEventListener('popstate', function(event) {
    // Check if 'state' property exists in the event object
    if (event.state) {
        // Get 'action' value from 'state' property
        let action = event.state && event.state.action;

        /* --------------------------- */
        if (action && action.startsWith("create-order-step-")) {
            const attemptedStepNumber = parseInt(action.replace("create-order-step-", ""));
            const currentStepNumber = parseInt(sessionStorage.getItem("Active-Step-Number"));

            console.log("attempting to open step number: ", attemptedStepNumber);
            console.log("popstate currentStepNumber from session: ", currentStepNumber);

            // If user tries to open a step number higher then open with forward button (popstate)
            if (attemptedStepNumber > currentStepNumber) {
                // NÆS ÞETTA VIRKAR ! STOPPAR VIÐKOMANDI Í AÐ FARA ÁFRAM
                // GERA VALIDATION Á FORMINU HÉRNA OG VIRKJA ÖLL FUNCTIONIN
                event.preventDefault(); // Prevent the forward navigation
                alert('Please complete the current step before proceeding.');
                history.back()
                return false;
            } else {
                storeActiveStepInSession(action);
                // Handle the normal behaviour for the popstate event
                // Load content based on the 'action' value and indicate popstate event
                loadContent(action, true, true);
            }
        
        }

        /* --------------------------- */

    } else {
        // No 'state' property, load default or index content
        loadContent('go-to-index', false, true);
    }
});
function storeActiveStepInSession(action) {
    if (action.startsWith("create-order-step-")) {
        actionStepNumberForSessionStorage = parseInt(action.replace("create-order-step-", ""));
        sessionStorage.setItem("Active-Step-Number", actionStepNumberForSessionStorage);
    }
}

// On new page load (Refresh) get the action from the url 
// To repopulate them with the existing data
window.addEventListener('load', function() {
    const action = new URL(window.location).searchParams.get("action");
    if (action) {
        storeActiveStepInSession(action);

        // Execute the necessary functions after a page refresh 
        updateButtons(action)
        repopulateFields(action);
        activeInputFieldsValidation();
        clearButtonFunction();
        displayAddedProducts();
        printSessionData();
        console.log("Page loaded from refresh with action:", action);
        /* loadContent(action, true, true) */

        
    } else {
        console.log("No action specified in the URL.");
        // Handle cases where there is no action parameter in the URL if needed
    }
});
/* 
        repopulateFields(action);
        activeInputFieldsValidation();
        clearButtonFunction();
         */
  /* ----- --- 4. Refresh, back, forward buttons (popstate) event --- ----- */
/* -------------------------------------------------------------------------- */


// ------------------------------------------------------------------ //
// ------------------------------------------------------------------ //



/* --------------------------------------------------------------------------- */
 /* ----- 5. Session Storage - Form To Object, Store, Get, Remove, Print ---- */

// Function converting the form data to object for storage in session
function formToObject(formElement) {
    const formDataObject = {};
    const formElements = formElement.elements;
    for (let i = 0; i < formElements.length; i++) {
        const element = formElements[i];
        if(element.name) {
            formDataObject[element.name] = element.value;
        }
    }
    // Added products
    const addedProducts = JSON.parse(sessionStorage.getItem('addedProducts')) || [];
    formDataObject['addedProducts'] = addedProducts

    return formDataObject;
}

// Function for storing the form data in the sessionStorage
function storeFormDataInSession(formSubmit, formDataObject) {
    const formDataString = JSON.stringify(formDataObject);
    sessionStorage.setItem(formSubmit, formDataString);
}

// Function for getting the form data from sessionStorage
function getFormDataFromSession(action) {
    const formDataString = sessionStorage.getItem(action);
    if (formDataString) {
        return JSON.parse(formDataString);
    }
    return null
}

// Function to remove the form data from sessionStorage
function removeFormDataFromSession(action) {
    sessionStorage.removeItem(action);
}

// Handle product addition function
/* function handleProductAddition(productId, quantity) {
    let addedProducts = JSON.parse(sessionStorage.getItem('addedProducts')) || []
    
    let existingProduct = addedProducts.find(p => p.productId === productId);
    if(existingProduct) {
        existingProduct.quantity += quantity;
    } else {
        addedProducts.push({ productId, quantity });
    }

    sessionStorage.setItem('addedProducts', JSON.stringify(addedProducts));
} */


// Function to print and console log the session data for learning purposes
function printSessionData() {
    // Get the total number of items in sessionStorage
    const sessionLength = sessionStorage.length;
    // If there's no data in sessionStorage
    if (sessionLength === 0) {
        console.log("No data in sessionStorage.");
        return;
    }
    // Loop through each key in sessionStorage
    for (let i = 0; i < sessionLength; i++) {
        const key = sessionStorage.key(i);
        const value = sessionStorage.getItem(key);
        console.log(`Java session storage : Key: ${key}, Value: ${value}`);
    }
}

 /* ----- 5. Session Storage - Form To Object, Store, Get, Remove, Print ---- */
/* --------------------------------------------------------------------------- */


// ---------------------------------------------------------------------------- //

/* --------------------------------------------------------------------------- */
  /* ----- ----- -------- 6. Ýmis nauðsynleg functions --------- ----- ----- */

// 1. Form to Object for storage in session



/* Function that retrives the stored data and repopulates the input fields */
function repopulateFields(action) {
    let retrivedFormDataObject = null;
    // First try to get data from session storage
    const storedSessionData = sessionStorage.getItem(action);
    if(storedSessionData) {
        retrivedFormDataObject = JSON.parse(storedSessionData);
    }
    // If data is found use it to repopulate the input fields
    if (retrivedFormDataObject) {
        Object.keys(retrivedFormDataObject).forEach(fieldName => {
            const fieldValue = retrivedFormDataObject[fieldName];
            const fieldElement = document.querySelector(`[name="${fieldName}"]`);
            if (fieldElement) {
                fieldElement.value = fieldValue
            }
        });
    }
}

// This handles the CLEAR button click
function clearButtonFunction() {
    $('.clear-form-button-js').click(function() {
        let form = $(this).closest('form');
        if(form.length) {
            form[0].reset();
        }
    });
}


// Validate function that takes inputField as parameter
function validateInput(inputField) {
    // Gets the DOM element of the input field using inputField.get(0) and checks its validity.
    let validity = inputField.get(0).checkValidity();
    // Removes the is-invalid and is-valid classes from the input field, so we can reset its state.
    // Adds the is-valid class if the input field is valid, and the is-invalid class if it's not.
    inputField.removeClass('is-invalid is-valid').addClass(validity ? 'is-valid' : 'is-invalid');
}

// Active input fields validation on focus (click)
function activeInputFieldsValidation() {
    $('.needs-validation .form-control').off('focus').on('focus', function() {
        let inputField = $(this);
        validateInput(inputField);
        inputField.on('input', function() {
            validateInput(inputField);
        }).on('blur', function() {
            inputField.off('input');
        });
    });
}

  /* ----- ----- -------- 6. Ýmis nauðsynleg functions --------- ----- ----- */
/* --------------------------------------------------------------------------- */



}); // document ready function

