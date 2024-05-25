              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


<?php

/* Since this file loads when AJAX POST is delivered I get the token, product_id 
and action from the AJAX POST and store it in the variables to use for info fetching */
$encryptedToken = $_POST['token'];
$product_id = $_POST['product_id'];
$action = $_POST['action'];

/* Now starts the normal procedure, decrypt the order_unique_id and retrival of order info  */
$order_unique_id = decrypt_order_unique_id($encryptedToken);
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
<!-- Container for the first content -->
<div class="container-fluid vh-100">
<!-- Nested Row and div to center the content -->
<div class="row vh-100 align-items-center justify-content-center center d-flex">
        <!-- -------- HÉR BYRJAR CARD ---------- -->
<div class="card card-lg-width col-lg-10 col-12 mx-auto" style="margin-top: -100px; height: 450px;">
            
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

           

        <!-- -------- CARD-BODY CONTAINING THE CONFIRMATION QUESTION ---------- -->  
<div class="card-body justify-content-center align-items-center center d-flex" style="margin-top: 0px;">
    <div class="alert alert-danger">
        <h1 class="text-center">
        You want to delete product number ' . $product_info['product_id'] . ' - ' . $product_info['name'] . '?
        </h1>
    </div>
</div><!-- card-body -->

    <!-- -------- CARD-FOOTER CONTAINING THE CONFIRM AND CANCEL DELETION ---------- -->  
<div class="card-footer pb-5 d-flex justify-content-center align-items-center" style="border-top: 0px;">
    


        <!-- -------- COL-2 - CONFIRM DELETION OF ITEM FROM ORDER ---------- -->  
    <div class="col-7">

        <button class="confirm-item-delete btn btn-outline-danger toggle-btn-outline-danger-box-shadow btn-lg w-100 borderradius" 
            href="#"
            data-token="' . $encryptedToken . '"
            data-product_id="' . $product_id . '"
            data-product_name="' . $product_info['name'] . '"
            data-action="confirm-item-delete"
            data-order_id="' . $order_info[0]['order_id'] . '">
            <h2>Delete this item</h2>
        </button>

    </div>



    <div class="col-2"></div>


        <!-- -------- COL-3 - CANCEL DELETION OF ITEM FROM ORDER ---------- -->  
    <div class="col-3">
        <button class="cancel-item-delete btn btn-secondary btn-lg borderradius w-100 toggle-btn-outline-secondary-box-shadow" 
        href="#"
        data-token="' . $encryptedToken . '"
        data-product_id="' . $product_id . '"
        data-action="cancel-item-delete"
        data-order_id="' . $order_info[0]['order_id'] . '" >
        <h2>Cancel</h2>
        
        </button> 
    </div>





</div> <!-- CARD-FOOTER -->
</div> <!-- CARD -->
</div> <!-- ROW -->
</div><!-- container-fluid -->

<script src="../js/extras.js"></script>

    ';
/* } */