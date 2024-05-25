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
$base_url = "../";
/* Include the files to make the page */
include $base_url . "database/database.php";
include $base_url . "sidebar.php";
include $base_url . "topnavbar.php";
include $base_url . "database/encryption_functions.php";
include "order_functions.php";

/* Decrypt the token from the URL */
if(isset($_GET['token'])) {
    $encryptedToken = $_GET['token'];
    /* - MAKE THE ORDER_UNIQUE_ID TO USE FOR FETCHING ORDER INFO - */
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
} 
else { /* if token is not set redirect back to orders.php */
    header("Location: orders.php?message=Token error");
}

/* Set the action and confirm variables and if they are net in the url set them to nothing */
$action = isset($_GET['action']) ? $_GET['action'] : '';
$confirm = isset($_GET['confirm']) ? $_GET['confirm'] : '';



/* --------------- DELETE ORDER ----------------- */
if(isset($_GET['token']) && $action === 'delete' && $confirm === 'confirm') {
    $encryptedToken = $_GET['token'];
    if(deleteOrder($encryptedToken)) {
        header("Location: orders.php?message=Order was successfully deleted");
    } else {
        header("Location: order_info.php?token=$encryptedToken&action=showinfo&message=Deletion was not succesful");
    }
}

/* --------------- UPDATE ORDER INFORMATION ----------------- */
if($_SERVER['REQUEST_METHOD'] == 'POST') {
    if(isset($_GET['token']) && $action == 'updateorderinfo') {
        if(updateOrdersTable($order_unique_id)) {
            header("Location: orders.php?message=Order number $order_id has been updated successfully!");
        } else {
            header("Location: orders.php?message=There was an error updating this order");
        }
    }
}

/* ---------- VIEW ORDER INFORMATION AND ECHO THE EDIT PAGE ------------ */

if(isset($_GET['token']) && $action == 'showinfo') {
    $encryptedToken = $_GET['token'];
    /* - MAKE THE ORDER_UNIQUE_ID TO USE FOR FETCHING ORDER INFO - */
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
    /* Get the order information and put it in an array */
    $order_info = getOrders(null, null, $order_unique_id);
    /* Function sem tekur inn order status og skilar gildi í css */
    $selectedOrderStatus = $order_info[0]['order_status'];
    $order_status_class = getOrderStatusClass($selectedOrderStatus);
    echo '
<div class="col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100 margin-top">
<!-- Container for the first content -->
<div class="container-fluid">
<!-- Nested Row and div to center the content -->
<div class="row">
            <!-- -------- HÉR BYRJAR CARD ---------- -->
<div class="card card-lg-width col-lg-10 col-12 mx-auto">
';    /* Hérna loka ég echo til að keyra message row ef hún er til staðar í urli */  
        if(isset($_GET['message'])) {
            $message = $_GET['message'];
            echo '<div class="row"><div class="col-12"><div class="alert bg-danger-subtle center" style="height: 100px;"><h1>' . $message . '</h1></div></div></div>';
        }
/* Restart the echo statement */
echo '                  
    <!-- --------- HÉR ER CARD HEADER MEÐ TITIL - ORDER ID - CREATED AT ------------ -->
    <div class="card-header d-flex">
        <div class="borderradius kirsty-bold-italic my-card-header d-flex align-items-center">
            <!-- ----- ORDER INFO ----- -->
            <div class="col-3 whitetext nowrap orders-card-header-font-size align-content-start d-flex">&nbsp&nbsp&nbsp&nbsp&nbspOrder Info</div>
            <!-- ----- ORDER ID ----- -->
            <div class="col-4 whitetext nowrap orders-card-header-font-size justify-content-center d-flex justify-content-xl-end xl-align-start">Order: ' . $order_info[0]['order_id'] . ' &nbsp&nbsp&nbsp&nbsp&nbsp</div>
            <!-- ----- CREATED AT ----- -->
            <div class="col-5 whitetext nowrap orders-card-header-font-size d-flex justify-content-end">Created At: ' . $order_info[0]['created_at'] . '&nbsp&nbsp&nbsp&nbsp&nbsp</div>
        </div> <!-- alert bg-body-secondary rounded-pill ... -->
    </div> <!-- card header -->
    <!-- --------- ---------- HÉR BYRJAR CARD BODY OG FORM ---------- ------------ -->
    <div class="card-body orders-card-body-font-size">
        <form action="order_info.php?token=' . $encryptedToken . '&action=updateorderinfo" method="POST" name="update_orders_table">
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <!-- ORDER STATUS ROW -->
            <div class="row p-1 align-items-center"> 
                <div class="col-lg-2 col-5 m-0 p-0"><label class="text-align nowrap whitetext p-2">Order Status:</label></div>
                <div class="col-lg-10 col-7"><span class="form-control-order-status' . $order_status_class . ' center p-2" aria-label="default input example">' . $order_info[0]['order_status'] . '</span></div>
            </div> <!-- ROW -->
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <!-- Order ID - ORDER UNIQUE ID - USER ID -->
            <div class="row p-1 align-items-center">
                <div class="col-lg-2 col-4"><label class="nowrap whitetext">Order ID:</label></div>
                <div class="col-lg-2 col-8"><span class="form-control-span center" aria-label="default input example">' . $order_info[0]['order_id'] . '</span></div>
                <hr class="d-lg-none">
                <div class="col-lg-2 col-4"><label class="nowrap whitetext">Order Unique ID:</label></div>
                <div class="col-lg-2 col-8 d-flex"><span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">' . $order_info[0]['order_unique_id'] . '</span></div>  
                <hr class="d-lg-none">
                <div class="col-lg-2 col-4"><label class="nowrap whitetext">User ID:</label></div>
                <div class="col-lg-2 col-8"><span class="form-control-span center" aria-label="default input example">' . $order_info[0]['user_id'] . '</span></div>
            </div> <!-- row p-1 align-items-center -->
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <!-- FIRSTNAME - LASTNAME - EMAIL -->
            <div class="row p-1 align-items-center">
                <div class="col-lg-1 col-4 m-0 p-0"><label class="nowrap-overflow-hidden whitetext align-items-start d-flex">Firstname:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="firstname" value="' . $order_info[0]['firstname'] . '" aria-label="default input example"></div>
                <hr class="d-lg-none">
                <div class="col-lg-1 col-4 m-0 p-0"><label class="nowrap whitetext">Lastname:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="lastname" value="' . $order_info[0]['lastname'] . '" aria-label="default input example"></div>
                <hr class="d-lg-none">
                <div class="col-lg-1 col-4 m-0 p-0"><label class="nowrap whitetext">E-mail:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="email" value="' . $order_info[0]['email'] . '" aria-label="default input example"></div>
            </div> <!-- row p-1 align-items-center -->
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <!-- ADDRESS - ADDRESS 2 - POSTALCODE -->
            <div class="row p-1 align-items-center"> 
                <div class="col-lg-1 col-4 m-0 p-0"><label class="nowrap whitetext align-items-start d-flex">Address:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="address" value="' . $order_info[0]['address'] . '" aria-label="default input example"></div>
                <hr class="d-lg-none">
                <div class="col-lg-1 col-4 m-0 p-0"><label class="nowrap whitetext">Address 2:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="address2" value="' . $order_info[0]['address2'] . '" aria-label="default input example"></div>
                <hr class="d-lg-none">
                <div class="col-lg-1 col-4 m-0 p-0"><label class="nowrap whitetext">Postalcode:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="postalcode" value="' . $order_info[0]['postalcode'] . '" aria-label="default input example"></div>
            </div> <!-- row p-1 align-items-center -->
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <!-- CITY - STATE - COUNTRY -->
            <div class="row p-1 align-items-center"> 
                <div class="col-lg-1 col-4"><label class="nowrap whitetext">City:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="city" value="' . $order_info[0]['city'] . '" aria-label="default input example"></div>
                <hr class="d-lg-none">
                <div class="col-lg-1 col-4"><label class="nowrap whitetext">State:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="state" value="' . $order_info[0]['state'] . '" aria-label="default input example">
                </div>
                <hr class="d-lg-none">
                <div class="col-lg-1 col-4"><label class="nowrap whitetext">Country:</label></div>
                <div class="col-lg-3 col-8"><input class="form-control bg-dark-subtle" type="text" name="country" value="' . $order_info[0]['country'] . '" aria-label="default input example"></div>
            </div> <!-- row p-1 align-items-center -->
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <!-- FINAL PRICE - CHANGE ORDER STATUS -->
            <div class="row p-1 align-items-center">
                <div class="col-lg-2 col-4"><label class="nowrap whitetext align-items-start d-flex">Final Price:</label></div>
                <div class="col-lg-2 col-8"><span class="form-control-span center" aria-labe="default input example">' . $order_info[0]['final_price'] . ' ISK</span></div>
                <hr class="d-lg-none">
                <!-- CHANGE ORDER STATUS -->
                <div class="col-lg-4 col-4"><label class="nowrap whitetext justify-content-end d-flex">Change Order Status:</label></div>
                <div class="col-lg-4 col-8">
';  /* Run foreach lúppu sem echoar valmöguleikunum í order_status */ 
$options = array('Made', 'Confirmed', 'Processed', 'Delivered', 'Cancelled');
echo '<select class="form-select bg-dark-subtle" name="order_status">';
foreach ($options as $option) { /* condition ? valueIfTrue : ValueIfFalse */
/* $var   =    (if condition == true) Assigns(?) 'selected' otherwise(:) assigns '' */
$selected = ($selectedOrderStatus == $option) ? 'selected' : '';
echo '<option value="' . $option . '" ' . $selected . '>' . $option . '</option>';
} /* If the current option matches the selected order status, we set the $selected variable to the string 'selected'; otherwise, it remains empty.*/
echo '</select>';
echo '
                </div> <!-- col-lg-2 col-8 -->
            </div> <!-- row p-1 align-items-center -->

            <hr class="my-horizontal-line"></hr>    <!-- Línan -->

            <!-- BUTTON ROW -->
            <div class="row p-1 align-items-center">

                <div class="col-3 d-flex justify-content-center">
                    <a class="btn btn-outline-info w-100" href="order_items.php?token=' . $encryptedToken . '&action=showitems">
                        <h4>See Ordered Items</h4>
                    </a>
                </div>

                <div class="col-3 d-flex justify-content-center">
                    <a class="btn btn-outline-warning w-100" href="orders_payment.php">
                        <h4>See Payment Info</h4>
                    </a>
                </div>
            

                <div class="col-1"></div>
                
                <div class="col-5 d-flex justify-content-center">
                    <button class="btn btn-outline-secondary w-100" type="POST" name="update_orders_table">
                        <h4>Confirm changes</h4>
                    </button>
                </div>

            </div> <!-- row p-1 align-items-center -->
        </form> <!-- END OF FORM -->

        <hr class="my-horizontal-line"></hr>    <!-- Línan -->
        <hr class="my-horizontal-line"></hr>    <!-- Línan -->
        <hr class="my-horizontal-line"></hr>    <!-- Línan -->
        <hr class="my-horizontal-line"></hr>    <!-- Línan -->

        
        <!-- ------------ DELETE ORDER ----------- -->
        <div class="row p-1 align-items-center">
            <div class="col-lg-12 d-flex justify-content-center">
                <span class="alert borderradius nowrap delete-text" style="max-width: 100%;">
                    WARNING ! BELOW IS FOR DELETING THE ORDER !!
                </span>
            </div>
            <hr class="my-horizontal-line"></hr>    <!-- Línan -->
            <div class="col-lg-12 d-lg-flex justify-content-center">
                <a class="btn btn-outline-danger w-100" style="height: 50px;" href="order_info.php?token=' . $encryptedToken . '&action=delete">
                    <h2>Delete Order</h2>
                </a>
            </div>
        </div>
    </div> <!-- card-body -->
</div> <!-- card -->
</div> <!-- row -->
</div> <!-- container-fluid -->
</div> <!-- col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100 -->
';
}


/* ---------------- DELETE CONFIRMATION -------------- */
/* code for displaying confirmation of deletion window */
if(isset($_GET['token']) && $action === 'delete') {
    $encryptedToken = $_GET['token'];
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
    $order_info = getOrders($order_unique_id);
    /* echo here the html code of the confirmation question */
    echo '
<div class="col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100">
    <!-- Container for the first content -->
    <div class="container-fluid d-flex justify-content-center align-items-center vh-100">
        <!-- Nested Row and div to center the content -->
        <div class="row">
                        <!-- -------- HÉR BYRJAR CARD ---------- -->
            <div class="card card-lg-width col-lg-10 col-12 mx-auto" style="margin-top: 100px; width: 100%">
                <!-- --------- HÉR ER CARD HEADER MEÐ TITIL - ORDER ID - CREATED AT ------------ -->
                <div class="card-header d-flex w-100">
                    <div class="alert borderradius kirsty-bold-italic delete-text d-flex align-items-center w-100">
                        <!-- ----- ORDER INFO ----- -->
                        <div class="col-3 nowrap orders-card-header-font-size align-content-start d-flex">&nbsp&nbsp&nbsp&nbsp&nbspOrder Info</div>
                        <!-- ----- ORDER ID ----- -->
                        <div class="col-4 nowrap orders-card-header-font-size justify-content-center d-flex justify-content-xl-end xl-align-start">Order: ' . $order_info[0]['order_id'] . ' &nbsp&nbsp&nbsp&nbsp&nbsp</div>
                        <!-- ----- CREATED AT ----- -->
                        <div class="col-5 nowrap orders-card-header-font-size d-flex justify-content-end">Created At: ' . $order_info[0]['created_at'] . '&nbsp&nbsp&nbsp&nbsp&nbsp</div>
                    </div> <!-- alert bg-body-secondary rounded-pill ... -->
                </div> <!-- card header -->
                <hr class="my-horizontal-line"></hr>    <!-- Línan -->
                <!-- --------- ---------- HÉR BYRJAR CARD BODY OG FORM ---------- ------------ -->
                <div class="card-body orders-card-body-font-size" style="margin-top: 10px;">
                    <!-- ------------ DELETE ORDER ----------- -->
                    <div class="row p-1 align-items-center">
                        <div class="col-12 d-flex justify-content-center"><label class="btn btn-danger borderradius"><h1>Warning !! Are you sure want to delete this order ?!</h1></label></div>
                    </div>
                    <hr class="my-horizontal-line"></hr>    <!-- Línan -->
                    <div class="row p-1 align-items-center">
                        <div class="col-8 d-flex justify-content-center"><a class="btn btn-outline-primary custom-btn-outline-danger w-100" style="height: 50px;" href="order_info.php?token=' . $encryptedToken . '&action=showinfo"><h2>Cancel and go back</h2></a></div>
                        <div class="col-4 d-flex justify-content-center"><a class="btn btn-outline-danger custom-btn-outline-danger w-100 nowrap" style="height: 50px;" href="order_info.php?token=' . $encryptedToken . '&action=delete&confirm=confirm"><h2>Delete order</h2></a></div> <!-- col-4 -->
                    </div> <!-- row -->
                </div> <!-- card-body -->
                <div class="card-footer">
                    <div class="row p-1 align-items-center">
                        <div class="col-12 d-flex justify-content-center"><label class="btn btn-outline-secondary borderradius"><h4>Note that this will also delete the ordered items and payment information</h4></label></div>
                    </div>
                </div> <!-- card footer -->
            </div> <!-- card -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div> <!-- col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100 -->
';
}

?>