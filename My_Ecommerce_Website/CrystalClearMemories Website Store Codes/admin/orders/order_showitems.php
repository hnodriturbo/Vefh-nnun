              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


<?php 


/* <div class="col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100" id="ordersItemsContainer"> */
echo '
<!-- Container for the first content -->
<div class="container-fluid">
<!-- Nested Row and div to center the content -->
<div class="row">

            <!-- -------- HÉR BYRJAR CARD ---------- -->
<div class="card card-lg-width col-lg-10 col-12 mx-auto">
';
echo '<div id="message-container">';
/*------------ MESSAGE DISPLAY ROW ------------- */

if(!empty($message)) {
    echo '<div class="row">
            <div class="col-12">
                <div class="alert alert-success center order-items-message-font-size">' . $message . '</div>
            </div>
        </div>
    ';
} 
echo '</div>';

echo'             
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

<!-- --------- ---------- HÉR BYRJAR CARD BODY ---------- ------------ -->
<div class="card-body my-white-text-with-shadow">

    <!-- Order ID - ORDER UNIQUE ID - USER ID -->
    <div class="row p-1 align-items-center">

    <hr class="my-horizontal-line p-1"></hr>    <!-- Línan -->

        <div class="col-lg-2 col-4 text-align-end">
            <label class="nowrap whitetext">Order ID:</label>
        </div>
        <div class="col-lg-2 col-8">
            <span class="form-control-span center" aria-label="default input example">
                ' . $order_info[0]['order_id'] . '
            </span>
        </div>
        <div class="col-lg-2 col-4 text-align-end">
            <label class="nowrap whitetext">Order Unique ID:</label>
        </div>
        <div class="col-lg-2 col-8 align-items-center justify-content-center center d-flex">
            <span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">
                ' . $order_info[0]['order_unique_id'] . '
            </span>
        </div>  
        <div class="col-lg-2 col-4 text-align-end">
            <label class="nowrap whitetext">User ID:</label>
        </div>
        <div class="col-lg-2 col-8">
            <span class="form-control-span center" aria-label="default input example">
                ' . $order_info[0]['user_id'] . '
            </span>
        </div>
    </div> <!-- row p-1 align-items-center -->

    <hr class="my-horizontal-line"></hr>    <!-- Línan -->
    <hr class="my-horizontal-line"></hr>    <!-- Línan -->
    ';



/* -------------------------------------------------------------- */
/* ----- HERE STARTS THE DISPLAY OF THE ORDER_ITEM PRODUCTS ----- */
/* -------------------------------------------------------------- */

foreach($products_data as $product_data) {
    /* For each product looped through i set the $product_id */
    $product_id = $product_data['product_id'];
    /* And use it and the order_items_data to get related row from order_items */
    $order_item_data = getOrderItemData($order_items_data, $order_unique_id, $product_id);
    /* Get the category name */
    $category_id = $product_data['category_id'];
    $category_name = getCategoryName($category_id);
    /* Set the image variable to use the image url */
    $image = $product_data['image'];
    /* Set quantity variable */
    $quantity = intval($order_item_data['quantity']);
    /* Echo the information in order_item_data and product_data */
    echo '
<div class="container-fluid">
<div class="row">
    <div class="col-5">
        <div class="row p-1 align-items-center">
            <div class="col-4">
                <label class="nowrap my-white-text-with-shadow">Name:</label>
            </div>
            <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">
                    ' . $product_data['name'] . '
                </span>
            </div>
        </div>
        <div class="row p-1 align-items-center">
            <div class="col-4">
                <label class="nowrap my-white-text-with-shadow">Descr:</label>
            </div>
            <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">
                    ' . $product_data['description'] . '
                </span>
            </div>
        </div>
        <div class="row p-1 align-items-center">
            <div class="col-4">
                <label class="nowrap my-white-text-with-shadow">Cat ID:</label>
            </div>
            <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">
                    ' . $product_data['category_id'] . '
                </span>
            </div>
        </div>
        <div class="row p-1 align-items-center">
            <div class="col-4">
                <label class="nowrap my-white-text-with-shadow">C Name:</label>
            </div>
            <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">
                    ' . $category_name . '
                </span>
            </div>
        </div>

        <!-- 
        BUTTON ROW - DELETE THIS ITEM FROM ORDER BUTTON 
        er að geyma þetta aðeins
        <a href="#" onclick="showDeletionConfirmation(' . $product_id . ', \'$encryptedToken\')" 
        class="btn btn-outline-danger toggle-btn-outline-danger-box-shadow w-100">Delete this item from order</a> 
        -->

        <div class="row p-1 align-items-center">
            <div class="col-12">

                <button class="item-delete-button btn btn-outline-danger toggle-btn-outline-danger-box-shadow w-100" 
                  data-token="' . $encryptedToken . '" 
                  data-product_id="' . $product_data['product_id'] . '" 
                  data-action="item-delete">
                  Delete this item from order
                </button>
                </form>
            </div>
        </div>
    </div>

    <!-- COL-5 SEM GEYMIR PRODUCT_ID - QUANTITY - PRICE - TOTAL_PRICE -->
    <div class="col-5">

        <div class="row p-1 align-items-center">
            <div class="col-4">
                <label class="nowrap my-white-text-with-shadow">Pr. ID:</label>
            </div>
            <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden" aria-label="default input example">
                    ' . $order_item_data['product_id'] . '
                </span>
            </div>
        </div>

        <div id="item-' . $order_item_data['product_id'] . '" class="item-row">
            <div class="row p-1 align-items-center">
                <div class="col-4">
                    <label class="nowrap my-white-text-with-shadow">Qty:</label>
                </div>
                <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden display-quantity" id="display-quantity-' . $order_item_data['product_id'] . '">
                ' . $order_item_data['quantity'] . '
                    </span>
                </div>
            </div>
        
            <div class="row p-1 align-items-center">
                <div class="col-4">
                    <label class="nowrap my-white-text-with-shadow">Price:</label>
                </div>
                <div class="col-8">
                    <span class="form-control-span center nowrap-overflow-hidden">
                        ' . $order_item_data['price'] . '
                    </span>
                </div>
            </div>
        
            <div class="row p-1 align-items-center">
                <div class="col-4">
                    <label class="nowrap my-white-text-with-shadow">T. Price:</label>
                </div>
                <div class="col-8">
                <span class="form-control-span center nowrap-overflow-hidden item-total-price"
                id="total-price-product-' . $order_item_data['product_id'] . '">
                ' . $order_item_data['total_price'] . '
                    </span>
                </div>
            </div>
        </div>
';



echo '<!-- CHANGE QUANTITY BUTTON AND INCREASE DEACREASE -->
    <div class="row p-1">

        <!-- COLUMN 1 - THE CHANGE QUANTITY BUTTON -->
        <div class="col-lg-6 col-6 d-flex justify-content-end p-0">
            <button class="finalize-quantity btn btn-outline-secondary toggle-btn-outline-secondary-box-shadow w-100" 
            href="#"
            data-token="' . $encryptedToken . '" 
            data-action="updatequantity" 
            data-product_id="' . $order_item_data['product_id'] . '">
                Change quantity
            </button>
        </div>

        <!-- COLUMN 2 - DECREASE QUANTITY - QUANTITY VALUE - INCREASE QUANTITY -->
        <div class="col-lg-6 col-6 d-flex justify-content-end">
            <!-- Decrease quantity button -->
            <button class="btn btn-secondary w-25 decrease" type="button" data-product_id="' . $order_item_data['product_id'] . '" type="button">
                -
            </button>
            <!-- Live quantity display -->
            <span class="whitetext center d-flex change-quantity" id="change-quantity-' . $order_item_data['product_id'] . '" style="padding-left: 20px; padding-right: 20px;">
                ' . $order_item_data['quantity'] . '
            </span>
            <!-- Increase quantity button -->
            <button class="btn btn-secondary w-25 increase" type="button" data-product_id="' . $order_item_data['product_id'] . '" type="button">
                +
            </button>
        </div>

    </div> <!-- row -->

            </div>
            <!-- ----------- HÉRNA ER MYNDIN AF VÖRUNNI ------------ -->
            <div class="col-2">
                <img src="' . $base_url . 'img/products/' . $image . '" alt="Product Image" class="mythumbnail">
            </div>
        </div> <!-- row -->
    </div> <!-- container-fluid -->

    <!-- end each product that displays by displaying these two lines -->
    <hr class="my-horizontal-line"></hr>    <!-- Línan -->
    <hr class="my-horizontal-line"></hr>    <!-- Línan -->

    
    '; /* End of echo statement */
} /* End of foreach($products_data as $product_data) */
/* -------------------------------------------------------------- */
    /* ----- HERE ENDS THE DISPLAY OF THE ORDER_ITEM PRODUCTS ----- */
/* -------------------------------------------------------------- */

    /* ----- ECHO REST OF THE PAGE ----- */
echo '
</div> <!-- card-body -->
</div> <!-- card -->
</div> <!-- row -->
</div> <!-- container-fluid -->
</div> <!-- col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100 -->


-->

'; /* End the echo statement */

?>


<!-- NEED TO FIX - LOADS MULTIPLE TIMES WHEN THE PAGE RELOADS -->
<script src="<?php echo $base_url; ?>js/order_showitems.js"></script>




