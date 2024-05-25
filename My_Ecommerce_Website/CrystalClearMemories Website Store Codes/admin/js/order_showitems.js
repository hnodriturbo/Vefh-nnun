/* ------------------------------------------------------- */
 /* ---------------- HREIÐAR PÉTURSSON ------------------ */
  /* --------------------------------------------------- */
   /* ----- DELETE ITEM FROM AN ORDER AJAX SCRIPT ----- */


/* 
    That said, in modern jQuery development, it's generally considered 
    good practice to wrap your scripts in $(document).ready(...); to avoid 
    any unforeseen issues, especially when your scripts grow and evolve. 
    It's a safeguard to ensure all DOM elements are accessible when your 
    scripts run.

    For consistency and as a good habit, you can put all your jQuery code 
    inside the $(document).ready(...); function, but for the specific case 
    of using .on() with event delegation, it's not strictly necessary. 
*/



/* DOCUMNET READY MAKES SURE THE DOCUMENT(PHP PAGE) LOADS FIRST */
$(document).ready(function() {

    /* ------------------------------------------------------------ */
    /* -------------- ASK FOR DELETE CONFIRMATION --------------- */
    /* ------------------------------------------------------------ */
    $(document).on('click', '.item-delete-button', function() {
        /* Extracting data attributes from the clicked button */
        var token = $(this).data('token');
        var action = $(this).data('action'); 
        var product_id = $(this).data('product_id');
        /* Sending the extracted data to the PHP backend via AJAX */
        $.ajax({
            type: "POST",
            url: "order_items.php",
            data: {
                token: token,
                action: action, /* item-delete */
                product_id: product_id
            },
            success: function(response) {
                /* This is the container that disappears  */
                $('#ordersItemsContainer').html(response); 
            },
            error: function() {
                alert("There was an error processing your request. Please try again.");
            }
        });
    });

    /* ------------------------------------------------------------ */
    /* ------------- CONFIRM DELETE OF ITEM BUTTON ------------ */
    /* ------------------------------------------------------------ */
    $(document).on('click', '.confirm-item-delete', function() {
        var token = $(this).data('token');
        var action = $(this).data('action');
        var product_id = $(this).data('product_id');
        var order_id = $(this).data('order_id');
        var product_name = $(this).data('product_name');

        $.ajax({
            type: "POST",
            url: "order_items.php",
            data: {
                token: token,
                action: action, /* confirm-item-delete */
                product_id: product_id,
                order_id: order_id,
                product_name: product_name
            },
            success: function(response) {
                $('#ordersItemsContainer').html(response);
            },
            error: function() {
                alert("There was an error processing your request. Please try again.");
            }
        });
    });


    /* ------------------------------------------------------------ */
    /* -------------- CANCEL DELETE OF ITEM BUTTON -------------- */
    /* ------------------------------------------------------------ */
    $(document).on('click', '.cancel-item-delete', function() {

        var token = $(this).data('token');
        var action = $(this).data('action');
        var product_id = $(this).data('product_id');
        var order_id = $(this).data('order_id');

        $.ajax({
            type: "POST",
            url: "order_items.php",
            data: {
                token: token,
                action: action, /* cancel-item-delete */
                product_id: product_id,
                order_id: order_id
            },
            success: function(response) {
                $('#ordersItemsContainer').html(response);
            },
            error: function() {
                // Handle error
            }
        });
    });

    /* -------------------------------------------------------------------- */
      /* ---------------- UPDATE QUANTITY AJAX JSON --------------------- */
    /* -------------------------------------------------------------------- */

    // Handle increasing the quantity
    $(document).on('click', '.increase', function() {
        console.log('increas-button-clicked');
        const productId = $(this).data('product_id');
        const quantityElement = $("#change-quantity-" + productId);
        let currentQuantity = parseInt(quantityElement.text(), 10);
        quantityElement.text(currentQuantity + 1);
    });

    // Handle decreasing the quantity
    $(document).on('click', '.decrease', function() {
        const productId = $(this).data('product_id');
        const quantityElement = $("#change-quantity-" + productId);
        let currentQuantity = parseInt(quantityElement.text(), 10);
        if (currentQuantity > 1) {
            quantityElement.text(currentQuantity - 1);
        }
    });



    
        /* Use AJAX to send the new quantity to the server(order_items) and the server updates  */
            /* the database. If json response is success then display the new quantity */
    $(document).on('click', '.finalize-quantity', function() {
        const token = $(this).data('token');
        const action = $(this).data('action');
        const productId = $(this).data('product_id');
        const finalQuantity = $("#change-quantity-" + productId).text();


        /* Ajax uses POST and sends the data retrived from "finalize quantity" button to 
        order_items.php and then uses json on success to update the "display-quantity" field */
        $.ajax({
            type: "POST",
            url: "order_items.php",
            data: {
                token: token,
                action: action,
                product_id: productId,
                new_quantity: finalQuantity
            },
            dataType: 'json',
            success: function(response) {
                if(response.success) {
                    /* On successful update, adjust the displayed quantity */
                    $("#display-quantity-" + productId).text(finalQuantity);
                    $("#total-price-product-" + productId).text(response.new_total_price);
                    $('#message-container').html(`
                    <div class="row">
                    <div class="col-12">
                    <div class="alert alert-success center order-items-message-font-size">
                    ${response.message}
                    </div>
                    </div>
                    </div>
                    `);
                } else {
                    alert("Error updating the quantity. Try again.");
                }
            },
            error: function() {
                alert("There was an error processing your request. Please try again.");
            }
        });
    });

    
}); /* End of document ready */

