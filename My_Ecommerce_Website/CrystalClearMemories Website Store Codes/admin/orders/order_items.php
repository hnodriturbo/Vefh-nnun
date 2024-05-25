              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
/* Using header(Location...) virkar ekki nema hafa ob_start(); */
ob_start();
/* Start the session */
session_start();

/* Store the current URL in a session variable */
/* in case admin is not logged in he will be directed to this page after the login */
if(!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}

/* Check if admin_uid and login_date is in the SESSION variable */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
/* Check the cookie also for admin_uid and if time is acceptable */
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}

/* Check if the script is running from an AJAX request and put either true or false in the variable $is_ajax */
$is_ajax = (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest');

/* Set the base url to set the folder working in */
$base_url = "../";

// If it's NOT an AJAX request, include the sidebar
if (!$is_ajax) {
    include_once "$base_url" . "sidebar.php";
    include_once "$base_url" . "topnavbar.php";
}

/* Include the files to make the page */
require_once "$base_url" . "database/database.php";
require_once "$base_url" . "database/encryption_functions.php";
require_once "order_functions.php";

/* Set value from GET, elseif set value from POST, else set value to null */
$encryptedToken = $_GET['token'] ?? $_POST['token'] ?? null;
$action = $_GET['action'] ?? $_POST['action'] ?? "";
$product_id = $_GET['product_id'] ?? $_POST['product_id'] ?? null;



// If the token exists, fetch order details
if ($encryptedToken) {
    $order_details = fetchOrderDetails($encryptedToken);
    
    $order_unique_id = $order_details['order_unique_id'];
    $order_info = $order_details['order_info'];
    $order_items_data = $order_details['order_items_data'];
    $products_data = $order_details['products_data'];
}


/* IF SERVER REQUEST METHOD IS POST I FETCH THE INFO AND RETRIVE ALL THE ORDER INFO */
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    /* Store info from the AJAX POST and store it in variables to use */
    $encryptedToken = $_POST['token'] ?? null;
    $product_id = $_POST['product_id'] ?? null;
    $action = $_POST['action'] ?? null;
    $order_id = $_POST['order_id'] ?? null;
    $product_name = $_POST['product_name'] ?? null;

    if($encryptedToken) {
        $order_details = fetchOrderDetails($encryptedToken);
        $order_unique_id = $order_details['order_unique_id'];
        $order_info = $order_details['order_info'];
        $order_items_data = $order_details['order_items_data'];
        $products_data = $order_details['products_data'];
    }

    switch ($action) {
        /* If change quantity button is pressed the ajax script send here the new quantity and */
        /* I change the quantity in the database and fetch the new total price and echo it through */
        /* json to the ajax and then AJAX changes the values of quantity and total price fields */
        case 'updatequantity':
            $new_quantity = $_POST['new_quantity'];
            $result = changeQuantityOrderItems($new_quantity, $order_unique_id, $product_id);
            if ($result) {
                $new_total_price = getNewTotalPrice($product_id, $order_unique_id);
                echo json_encode([
                    'success' => true,
                    'message' => "Quantity for product: " . $product_id . " has been changed to: " . $new_quantity,
                    'new_total_price' => $new_total_price
                ]);
            } else {
                echo json_encode([
                    'success' => false,
                    'message' => "There was a failure updating the quantity of product: " . $product_id
                ]);
            }
            exit;

        /* item-delete - include page that displays and asks for confirmation */
        case 'item-delete':
            include 'order_items_delete.php';
            break;

        /* Confirm item deletion - use delete logic and set $message */
        case 'confirm-item-delete':
            if(deleteOrderItemFromOrder($order_unique_id, $product_id)) {
                $message = "Product: " . $product_id . " - " . $product_name . " from order: " . $order_id . " has been successfully deleted";
            } else {
                $message = "Failed to delete product: " . $product_id . " from order: " . $order_id;
            }
            include "order_showitems.php";
            break;

        /* If pressed Cancel deletion button - Set $message and go back to order_showitems */
        case 'cancel-item-delete':
            $message = "You cancelled deletion of product: " . $product_id . " from order: " . $order_id;
            include "order_showitems.php";
            break;
 
        /* Defaulta að senda þá tilbaka í order info */
        default:
            header("Location: order_info.php?token=$encryptedToken");
    }

} 

/* BÚA TIL SÍÐUNA EF EKKI POST BEIÐNI */
else {
    echo '<div class="col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100 margin-top" id="ordersItemsContainer">';
    if($encryptedToken && $action === 'showitems') {
        include "order_showitems.php";
    }
    echo '</div>';
}








?>

