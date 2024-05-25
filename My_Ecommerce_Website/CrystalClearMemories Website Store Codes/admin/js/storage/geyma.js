/*            <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->   */   


    // ------- basic way to chech if entry exists and replace it 
        const formDataObject = formToObject(form[0]);

        // Look for an entry with the same action in the formDataArray
        let existingEntry = null;
        for (let i = 0; i < formDataArray.length; i++) {
            if (formDataArray[i].action === formSubmit) {
                existingEntry = formDataArray[i];
                break;
            }
        }
        
        if (existingEntry) {
            // Update the existing entry with the new form data
            existingEntry.data = formDataObject;
        } else {
            // Push a new entry into the formDataArray
            formDataArray.push({ action: formSubmit, data: formDataObject });
        }
        



            /* This is my event listener for the navbar height */
/* if the toggler icon is clicked the fixed height will change so it can expand */
/* document.addEventListener('DOMContentLoaded', function() {
    let navbar = document.querySelector('#topNavbar');
    let navbarContent = document.querySelector('#navbarTogglerDemo01');
    let toggler = document.querySelector('.navbar-toggler');

    toggler.addEventListener('click', function() {
        if (navbarContent.classList.contains('show')) {
            navbar.classList.add('limited-height');
        } else {
            navbar.classList.remove('limited-height');
        }
    });
});
 */



/* document.addEventListener('DOMContentLoaded', function() {
    let navbar = document.querySelector('#topNavbar');
    let navbarContent = document.querySelector('#navbarTogglerDemo01');

    // When the navbar is shown
    navbarContent.addEventListener('shown.bs.collapse', function() {
        navbar.classList.add('expanded');
    });

    // When the navbar is hidden
    navbarContent.addEventListener('hidden.bs.collapse', function() {
        navbar.classList.remove('expanded');
    });
});
 */



document.addEventListener('DOMContentLoaded', function() {
    let navbarToggler = document.querySelector('.navbar-toggler');
    let navbar = document.querySelector('.navbar');

    navbarToggler.addEventListener('click', function() {
        if (navbar.classList.contains('expanded')) {
            navbar.classList.remove('expanded');
        } else {
            navbar.classList.add('expanded');
        }
    });
});




/* bootstraps event */
/* Bootstrap also provides specific collapse events. You can use these events 
to add or remove the expanded class based on whether the navbar is shown or hidden. */

document.addEventListener('DOMContentLoaded', function() {
    let navbar = document.querySelector('.navbar');
    let navbarContent = document.querySelector('#navbarTogglerDemo01');

    // When the navbar is shown
    navbarContent.addEventListener('shown.bs.collapse', function() {
        navbar.classList.add('expanded');
    });

    // When the navbar is hidden
    navbarContent.addEventListener('hidden.bs.collapse', function() {
        navbar.classList.remove('expanded');
    });
});





    
    // Example starter JavaScript for disabling form submissions if there are invalid fields
    (() => {
        'use strict'
      
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        const forms = document.querySelectorAll('.needs-validation')
      
        // Loop over them and prevent submission
        Array.from(forms).forEach(form => {
          form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
              event.preventDefault()
              event.stopPropagation()
            }
      
            form.classList.add('was-validated')
          }, false)
        })
      })()





/* -------------------------------------- */
/* ---------- QUANTITY BUTTONS ---------- */
/* -------------------------------------- */



// extras.js
quantityValue = 1;
// Object to store quantity values for each product

function updateQuantity(productId) {
    const quantityElement = document.getElementById("display-quantity-" + productId);
    const quantityValue = parseInt(quantityElement.dataset.quantity);
    quantityElement.textContent = quantityValue; // Update the displayed quantity
    document.getElementById("quantity-" + productId).value = quantityValue; // Update the hidden input value
  }
  
  function decreaseQuantity(productId) {
    const quantityElement = document.getElementById("display-quantity-" + productId);
    let quantityValue = parseInt(quantityElement.dataset.quantity);
    if (quantityValue > 1) {
      quantityValue--;
      quantityElement.dataset.quantity = quantityValue; // Update the data-quantity attribute
      updateQuantity(productId);
    }
  }
  
  function increaseQuantity(productId) {
    const quantityElement = document.getElementById("display-quantity-" + productId);
    let quantityValue = parseInt(quantityElement.dataset.quantity);
    // You can add a maximum quantity limit if needed
    quantityValue++;
    quantityElement.dataset.quantity = quantityValue; // Update the data-quantity attribute
    updateQuantity(productId);
  }
  
  function enableQuantityManagement(productId, initialQuantity) {
    const quantityElement = document.getElementById("display-quantity-" + productId);
    quantityElement.dataset.quantity = initialQuantity; // Set the initial data-quantity attribute
    updateQuantity(productId); // Update the displayed and hidden input values
  }
  




let quantityValue;
function decreaseQuantity() {
    if (quantityValue > 1) {
        quantityValue--;
        document.getElementById("display-quantity").textContent = quantityValue;
        document.getElementById("quantity").value = quantityValue;
    }
}
function increaseQuantity() {
    quantityValue++;
    document.getElementById("display-quantity").textContent = quantityValue;
    document.getElementById("quantity").value = quantityValue;
}

function enableQuantityManagement(initialQuantity) {
    quantityValue = initialQuantity;
    document.getElementById("display-quantity").textContent = quantityValue;
}

let quantityValue = 1;
function decreaseQuantity() {
    if (quantityValue > 1) {
        quantityValue--;
        document.getElementById("quantity").textContent = quantityValue;
    }
}
function increaseQuantity() {
    quantityValue++;
    document.getElementById("quantity").textContent = quantityValue;
}






  /* --------------------------------------------------------------------- */
 /* ------ FUNCTION TO CONSTANTLY SWITCH CSS CLASSES USING JAVASCRIPT ----- */
/* ------------------------------------------------------------------------- */


// Function to toggle the specified classes on the button element
function toggleFromClassToClass(buttonElement, defaultClass, alternateClass) {
    buttonElement.classList.toggle(defaultClass);
    buttonElement.classList.toggle(alternateClass);
}

// Get references to the button elements by their respective IDs
const buttonDanger = document.getElementById('toggle-btn-danger');
const buttonSecondary = document.getElementById('toggle-btn-secondary');
const buttonWarning = document.getElementById('toggle-btn-warning');
const buttonInfo = document.getElementById('toggle-btn-info');


/* use setInterval to run the function to change classes */
// Toggle the 'btn-danger' and 'btn-outline-danger' classes on 'buttonDanger' every 1000ms (1 second)
/* setInterval(() => toggleFromClassToClass(buttonDanger, 'btn-danger', 'btn-outline-danger'), 1000); */
// Toggle the 'btn-secondary' and 'btn-outline-secondary' classes on 'buttonSecondary' every 500ms (0.5 seconds)
/* setInterval(() => toggleFromClassToClass(buttonSecondary, 'btn-secondary', 'btn-outline-secondary'), 500);*/
// Toggle the 'btn-warning' and 'btn-outline-warning' classes on 'buttonWarning' every 1000ms (1 second)
/* setInterval(() => toggleFromClassToClass(buttonWarning, 'btn-warning', 'btn-outline-warning'), 1000); */
// Toggle the 'btn-info' and 'btn-outline-info' classes on 'buttonInfo' every 500ms (0.5 seconds)
/* setInterval(() => toggleFromClassToClass(buttonInfo, 'btn-info', 'btn-outline-info'), 500); */




/* ------------------------------------------------------------------------- */
/* --------- NOTAÐI ÞETTA FYRST EN ER BÚINN AÐ EINFALDA KÓÐANN ------------- */
/* ------------------------------------------------------------------------- */


function toggleButton(buttonElement, defaultClass, alternateClass) {
    if (buttonElement.classList.contains(defaultClass)) {
        buttonElement.classList.remove(defaultClass);
        buttonElement.classList.add(alternateClass);
    } else {
        buttonElement.classList.remove(alternateClass);
        buttonElement.classList.add(defaultClass);
    }
}

const buttonDanger = document.getElementById('button-danger');
let isDanger = true;

function toggleDangerButton() {
    toggleButton(buttonDanger, 'btn-danger', 'btn-outline-danger');
    isDanger = !isDanger;
}

buttonDanger.addEventListener('click', toggleDangerButton);
setInterval(toggleDangerButton, 500);

const buttonSecondary = document.getElementById('button-secondary');
let isSecondary = true;

function toggleSecondaryButton() {
    toggleButton(buttonSecondary, 'btn-secondary', 'btn-outline-secondary');
    isSecondary = !isSecondary;
}

buttonSecondary.addEventListener('click', toggleSecondaryButton);
setInterval(toggleSecondaryButton, 500);



const button_danger = document.getElementById('toggle-btn-danger');
let isDanger = true;

function toggleButtonClass() {
  if (isDanger) {
    button_danger.classList.remove('btn-danger');
    button_danger.classList.add('btn-outline-danger');
  } else {
    button_danger.classList.remove('btn-outline-danger');
    button_danger.classList.add('btn-danger');
  }
  isDanger = !isDanger;
}

button_danger.addEventListener('click', toggleButtonClass);

setInterval(toggleButtonClass, 1000);



const button_secondary = document.getElementById('toggle-btn-secondary');
let isSecondary = true;

function toggleSecondaryButton() {
    if (isSecondary) {
    button_secondary.classList.remove('btn-secondary');
    button_secondary.classList.add('btn-outline-secondary');
    } else {
    button_secondary.classList.remove('btn-outline-secondary');
    button_secondary.classList.add('btn-secondary');
    }
    isSecondary = !isSecondary;
}
button_secondary.addEventListener('click', toggleSecondaryButton);


setInterval(toggleSecondaryButton, 1000);






function showDeletionConfirmation(productId, token) {
  // Construct the URL with the given parameters and static values
  var url = `orders_items_delete.php?token=${token}&action=delete&product_id=${productId}&confirm=ask`;

  fetch(url)
      .then(response => response.text())
      .then(data => {
          // This is the content echoed by your PHP script
          document.getElementById("resultContainer").innerHTML = data;
      })
      .catch(error => {
          console.error('There was a problem with the fetch operation:', error.message);
      });
  }


var element = document.querySelector('div');
var token = element.getAttribute('data-token');
var productId = element.getAttribute('data-product-id');


echo '<div data-product-id="'.$productId.'" data-token="'.$decryptedToken.'"></div>';

function confirmDelete() {
// Hide the order items container
document.getElementById('orderItems').style.display = 'none';

// Update the URL without reloading the page
history.pushState({}, '', 'orders_items.php?token=yourToken&action=confirmDelete');

// Make an AJAX call to fetch the delete confirmation container
fetchContent('confirmDelete');
}

function performDelete() {
// Here you'd typically make an AJAX call to actually delete the product from the database.

// After deleting, redirect or load another content or show a success message.
alert('Product deleted successfully!');
}

function cancelDelete() {
// You can redirect back to showing items or hide the delete confirmation container
history.pushState({}, '', 'orders_items.php?token=yourToken&action=showitems');
fetchContent('showitems');
}

function fetchContent(action) {
var xhr = new XMLHttpRequest();
xhr.open('GET', 'orders_items.php?token=yourToken&action=' + action, true);

xhr.onload = function() {
  if (xhr.status == 200) {
      // Update main content based on the action
      if (action === 'showitems') {
          document.getElementById('orderItems').innerHTML = xhr.responseText;
      } else if (action === 'confirmDelete') {
          document.getElementById('confirmDeleteContainer').innerHTML = xhr.responseText;
      }
  }
}
xhr.send();
}

document.addEventListener("DOMContentLoaded", function() {
var deleteButtons = document.querySelectorAll(".delete-button");

deleteButtons.forEach(function(button) {
  button.addEventListener("click", function(event) {
      var productId = event.currentTarget.getAttribute("data-product-id");
      var token = event.currentTarget.getAttribute("data-token");
      
      // Now you can use productId and token for any logic you want, e.g. AJAX calls.
      console.log("Deleting product ID:", productId, "with token:", token);
  });
});
});
    // This binds a click event listener to any element with the class 'item-update-quantity-button'.
    // Even if such elements are dynamically added to the page later on, the listener will still work.
    $(document).on('click', '.order-item-update-quantity', function() {
        // Extract data attributes from the clicked button. 
        // This data will be sent to the server.
        var token = $(this).data('token');
        var action = $(this).data('action'); // should be 'updatequantity' or similar
        var product_id = $(this).data('product_id');
        var new_quantity = $(this).siblings('.quantity-input').val(); // Assuming there's an input field for the new quantity near the button

        // Sending the extracted data to the PHP backend via AJAX
        $.ajax({
            type: "POST",
            url: "order_items.php",
            data: {
                token: token,
                action: action,
                product_id: product_id,
                new_quantity: new_quantity
            },
            dataType: 'json', // Expecting JSON data in return from the server
            success: function(response) {
                // Using the returned JSON data, you update the relevant parts of the page.
                // For example, if the server returns the new quantity and total price, you can update those specific elements.
                if(response.success) { // Assuming the server returns a 'success' field in its JSON response
                    $('#item-' + product_id + ' .item-quantity').text(response.quantity); // Update the displayed quantity
                    $('#item-' + product_id + ' .item-total-price').text(response.total_price); // Update the displayed total price (if applicable)
                } else {
                    alert(response.message); // If the server indicates an error, show the message
                }
            },
            error: function() {
                alert("There was an error processing your request. Please try again.");
            }
        });
    });



    


/* ---------------------------------------------------- */
/* --- SCRIPT FOR MAKING THE PAGE STAY ON THE SAME PAGE */
/* ---------------------------------------------------- */

document.addEventListener("DOMContentLoaded", function() {
    // Attach click event to the "Update Quantity" button
    document.getElementById("update_quantity_btn").addEventListener("click", function() {
        // Get form data
        var formData = new FormData(document.getElementById("quantity_form"));

        // Submit form data using Fetch API
        fetch("orders_items.php", {
            method: "POST",
            body: formData,
        })
        .then(response => {
            // Handle the server response if needed
            // For example, you can update the view with the updated data
            // without refreshing the whole page.
            // ...

            // Optionally, reload the view (if needed)
            // window.location.reload();
        })
        .catch(error => {
            // Handle any error that occurs during the Fetch request
            // ...
        });
    });
});


// DOMContentLoaded sér um að allt html sé hlaðið áður en javascript kóðinn keyrir
// Hér er kóði sem er án þess að nota DOMContentLoaded 

// Attach click event to the "Update Quantity" button
document.getElementById("update_quantity_btn").addEventListener("click", function() {
    // Get form data
    var formData = new FormData(document.getElementById("quantity_form"));

    // Submit form data using Fetch API
    fetch("orders_items.php", {
        method: "POST",
        body: formData,
    })
    .then(response => {
        // Handle the server response if needed
        // For example, you can update the view with the updated data
        // without refreshing the whole page.
        // ...

        // Optionally, reload the view (if needed)
        // window.location.reload();
    })
    .catch(error => {
        // Handle any error that occurs during the Fetch request
        // ...
    });
});



let step1Data = [];
let step2Data = [];

$(document).ready(function() {
    // Transition from Step 1 to Step 2
    $("#goToStep2").click(function() {
        $.post("add_action.php", {
            action: 'proceed_to_step2',
            firstname: $(".order-firstname").val(),
            lastname: $(".order-lastname").val(),
            email: $(".order-email").val()
            // ... add other fields as needed
        }, function(data) {
            // Store the received data in the step1Data array
            step1Data.push(data);

            $("#step1").hide();
            $("#step2").show();
        }, "json"); // We expect the server response to be in JSON format
    });

    // Transition back to Step 1 from Step 2
    $("#goToStep1").click(function() {
        $("#step2").hide();
        $("#step1").show();
    });

    // Finalize the order
    $("#finalizeOrder").click(function() {
        // Store Step 2 data (order items) using class selectors
        let itemData = {
            product_id: $(".item-product_id").val(),
            quantity: $(".item-quantity").val(),
            // ... add other fields as needed
        };

        step2Data.push(itemData);
        finalizeOrder();
    });
});


