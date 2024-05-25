              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->
 






<!-- Container for the first content -->
<div class="container-fluid" id="index">
<!-- Nested Row and div to center the content -->
<div class="row">
<!-- -------- HÉR BYRJAR CARD ---------- -->
<div class="card card-lg-width col-lg-10 col-12 mx-auto">

<!-- If message comes through the url it will be displayed here -->
<?php 
if(!empty($message)) {
echo '
<div id="message-container">
    <div class="row">
        <div class="col-12">
            <div class="alert alert-success center order-items-message-font-size">' . $message . '</div>
        </div>
    </div>
    </div>
';
}
?>
    <div class="my-card-header d-flex borderradius kirsty-bold-italic justify-content-center center my-white-text-with-shadow">
        <h1>Welcome to the Creation! <br> Where new things come alive !</h1>
    </div> <!-- my-card-header -->
        
    
    <!-- --------- ---------- HÉR BYRJAR CARD BODY ---------- ------------ -->
    <div class="card-body my-white-text-with-shadow" style="margin-top: 0px;">
    <br><br><br>
        <!-- -------- BUTTON FOR CREATING NEW ORDER ---------- -->
        <button 
            id="create-order-proceed" 
            class="btn btn-outline-info w-100" 
            style="height: 75px;" 
            href="#"
            data-action="create-order-step-1"
            data-formSubmit="">
            <h1>Create New Order</h1>
        </button>

    <br><br><br>

        <!-- --------- BUTTON FOR CREATING NEW USER ---------- -->
        <button 
            id="create-product"
            class="btn btn-outline-success w-100" 
            style="height: 75px;"
            href="#"
            data-action="create-product-info"
        >
            <h1>Create New Product</h1>
        </button>

    <br><br><br>

        <!-- -------- BUTTON FOR CREATING NEW PRODUCT -------- -->
        <button 
            id="create-user"
            class="btn btn-outline-light w-100" 
            style="height: 75px;"
            href="#"
            data-action="create-user-info"
        >
            <h1>Create New User</h1>
        </button>

    
        </div> <!-- card-body -->
</div> <!-- card -->

</div> <!-- row -->

</div> <!-- container-fluid -->




<!-- <script src="../js/add_order.js"></script> -->