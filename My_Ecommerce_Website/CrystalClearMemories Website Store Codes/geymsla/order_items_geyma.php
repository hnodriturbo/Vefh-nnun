<?php




 /* - MAKE THE ORDER_UNIQUE_ID TO USE FOR FETCHING ORDER INFO - */
/* 
if(isset($_GET['token'])) {
    $encryptedToken = $_GET['token'];
    
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
} else {
    header("Location: orders.php?message=Token error");
}
$action = $_GET['action'] ?? "";
if(isset($_GET['product_id'])) {
    $product_id = $_GET['product_id'];
    foreach($products_data as $product_data) {
        $productid = $product_data['product_id'];
        if($productid == $product_id) {
            $product_info = $product_data;
        }
    }
}
 */



    
    /* If product_id is in the url set the $product_id and fetch the product info  */
/* 
    if(isset($_GET['product_id'])) {
        $product_id = $_GET['product_id'];
        foreach($products_data as $product_data) {
            $productid = $product_data['product_id'];
            if($productid == $product_id) {
                $product_info = $product_data;
            }
        }
    }
 */

/* 
    if (isset($_POST['token']) && $action == 'item-delete' && isset($_POST['product_id'])) {
        include 'order_items_delete.php';
        exit;
    }
    if (isset($_POST['token']) && $action == 'confirm-item-delete' && isset($_POST['product_id'])) {
        if(deleteOrderItemFromOrder($order_unique_id, $product_id)) {
            $message = "Product id: " . $product_id . " from order: " . $order_id . " has been successfully deleted";
        } else {

            $message = "Failed to delete product: " . $product_id . " from order: " . $order_id;
        }
        include "order_showitems.php";
    }  
    if(isset($_POST['token']) && $action == 'cancel-item-delete' && isset($_POST['product_id'])) {
        $message = "You cancelled deletion of product: " . $product_id . " from order: " . $order_id;
        include "order_showitems.php";
    }
     */





/* 
if($encryptedToken) {
    $order_unique_id = decrypt_order_unique_id($order_unique_id);
    if(!$order_unique_id) {
        die("Error decrypting the token.");
    }
 */




     /* Fetch the order_info using getOrders and order_unique_id */
         /* Fetch all rows in order_items and put it in an associative array */
   /* use $product_id in order_items_data to fetch the products related to it */

/* if($encryptedToken != null) {
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
    $order_info = getOrders(null, null, $order_unique_id);
    $order_items_data = getOrderItems($order_unique_id);
    $products_data = getAllProductsFromOrderItemsData($order_items_data);
} */









/* 
error_reporting(E_ALL);
ini_set('display_errors', 1);

ob_start();

session_start();

if(!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}

if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}

else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
$base_url = "../";

include "$base_url" . "database/database.php";
include "$base_url" . "sidebar.php";
include "$base_url" . "topnavbar.php";
include "$base_url" . "database/encryption_functions.php";
include "orders_functions.php";


if(isset($_GET['token'])) {
    $encryptedToken = $_GET['token'];

    $order_unique_id = decrypt_order_unique_id($encryptedToken);
} 
else { 
    header("Location: orders.php?message=Token error");
}

$action = isset($_GET['action']) ? $_GET['action'] : '';
$confirm = isset($_GET['confirm']) ? $_GET['confirm'] : '';
 */




if (isset($_GET['token']) && $action == 'delete' && isset($_GET['product_id']) && $confirm == 'ask') {
    

    /* Start by getting the token and decrypt it into order_unique_id */
    $encryptedToken = $_GET['token'];
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
    $product_id = $_GET['product_id'];

    /* Fetch the order_info using getOrders and order_unique_id */
    $order_info = getOrders(null, null, $order_unique_id);

    /* Fetch all rows in order_items and put it in an associative array */
    $order_items_data = getOrderItems($order_unique_id);
    


    /* use $product_id in order_items_data to fetch the products related to it */
    $products_data = getAllProductsFromOrderItemsData($order_items_data);
    foreach ($products_data as $product_data) {
        $products_data_product_id = $product_data['product_id'];
        if ($products_data_product_id == $product_id) {
            $product_info = $product_data;
        }
    }
    echo '
<div class="col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100" id="resultContainer">
<!-- Container for the first content -->
<div class="container-fluid">
<!-- Nested Row and div to center the content -->
<div class="row">
            <!-- -------- HÉR BYRJAR CARD ---------- -->
<div class="card card-lg-width col-lg-10 col-12 mx-auto" style="margin-top: 100px;">
                
<!-- --------- HÉR ER CARD HEADER MEÐ TITIL - ORDER ID - CREATED AT ------------ -->
<div class="card-header d-flex">
    <div class="alert borderradius kirsty-bold-italic my-card-header d-flex align-items-center">
        <!-- ----- ORDER INFO ----- -->
        <div class="col-3 whitetext nowrap orders-card-header-font-size align-content-start d-flex">&nbsp&nbsp&nbsp&nbsp&nbspOrder Info</div>
        <!-- ----- ORDER ID ----- -->
        <div class="col-4 whitetext nowrap orders-card-header-font-size justify-content-center d-flex justify-content-xl-end xl-align-start">Order: ' . $order_info[0]['order_id'] . ' &nbsp&nbsp&nbsp&nbsp&nbsp</div>
        <!-- ----- CREATED AT ----- -->
        <div class="col-5 whitetext nowrap orders-card-header-font-size d-flex justify-content-end">Created At: ' . $order_info[0]['created_at'] . '&nbsp&nbsp&nbsp&nbsp&nbsp</div>
    </div> <!-- alert bg-body-secondary rounded-pill ... -->

        </div> <!-- card header -->
            <br><br><br><br>
        <div class="card-body">
        <div class="card-title text-center text-white">
        <h2 class="card-title text-center">Are you sure you want to delete this product number ' . $product_info['product_id'] . ' - ' . $product_info['name'] . '?</h2>
    </div>
        </div><!-- card-body -->

        <div class="card-footer pb-5 d-flex justify-content-center align-items-center" style="border-top: 0px;">
            <div class="col-2">
                <a class="btn btn-danger btn-lg borderradius w-100" href="#">
                    Delete
                </a>
            </div>
            <div class="col-2"></div>

            <div class="col-3">
                <a class="btn btn-secondary btn-lg borderradius w-100" href="#">
                Cancel
                </a> 
            </div>
        </div>

    </div> <!-- card -->
</div> <!-- col-12 admin users table -->
</div><!-- row -->
</div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->

    ';
}