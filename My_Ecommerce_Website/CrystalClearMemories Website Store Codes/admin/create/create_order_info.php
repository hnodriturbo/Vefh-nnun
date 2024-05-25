              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->        
<?php 

$add_order_header = '

<!-- ----- Use container-fluid and row for main content ----- -->
<div class="container-fluid">
    <div class="row">
    <!-- ---------- Here start the card ---------- -->
    <div class="card card-lg-width col-xl-10 col-12 mx-auto">
        <br>
';


$button_row = 
'<br>
        <!-- BUTTON ROW -->
<div class="row align-items-center justify-content-center d-flex p-1">






<!-- ----- PROCEED TO NEXT STEP BUTTON ----- -->
<div class="col-sm-4 col-12 d-flex justify-content-xl-end justify-content-center m-sm-0 m-2 order-0 order-sm-2">
    <button id="create-order-proceed" 
            type="submit"
            class="nowrap btn btn-lg btn-outline-success toggle-btn-outline-secondary-box-shadow create-order-button d-flex align-items-center create-order-sm-size-buttons"
            data-action=""
            data-formSubmit=""
    >

        <span></span> 
        <i class="bi bi-arrow-right-circle create-order-button-logo" style="margin-left: 20px;"></i>
    </button> 
    </form>
</div> <!-- col-3 d-flex -->




<!-- CLEAR FORM BUTTON -->
<div class="col-sm-4 col-12 d-flex justify-content-center m-sm-0 m-2 order-1">
    <button id="clear-form-button"
            type="button"
            class="nowrap btn btn-lg btn-outline-info toggle-btn-outline-info-box-shadow clear-form-button-js create-order-button d-flex align-items-center create-order-sm-size-buttons"
    >
        <i class="bi bi-x-circle create-order-button-logo" style="margin-right: 20px;"></i>
        <span>Clear</span>
    </button>
</div>




        <!-- ----- CANCEL BUTTON ----- -->
<div class="col-sm-4 col-12 d-flex justify-content-xl-start justify-content-center m-sm-0 m-2 order-2 order-sm-0">
    <button id="create-order-go-back"
            type="button" 
            class="nowrap btn btn-lg btn-outline-danger toggle-btn-outline-danger-box-shadow create-order-button d-flex align-items-center create-order-sm-size-buttons"
            data-action=""
    >

            <i class="bi bi-arrow-left-circle create-order-button-logo" style="margin-right: 20px;"></i>
            <span></span>

    </button>
</div>







</div>  <!-- row p-1 align-items-center -->


</div> <!-- card-body -->
<br><br><br>
';




/* Need to use foreach loop to echo the progress bar based on the location in the progress */
$progress_bar_step_1 = '
<div class="card-footer" style="padding-top: 0px;">

<div class="row align-items-center center justify-content-center d-flex whitetext" style="font-size: 24px;">
    <div class="col-3">Step 1</div>
    <div class="col-3">Step 2</div>
    <div class="col-3">Step 3</div>
    <div class="col-3">Finish</div>
</div>

<div class="progress bg-dark borderradius progress-bar-striped progress-bar-animated" role="progressbar" style="opacity: 0.5;">
    <div class="progress-bar progress-bar-striped bg-info progress-bar-animated borderradius w-25"></div>
</div>

</div> <!-- card-footer -->
';
$progress_bar_step_2 = '
<div class="card-footer">
<div class="row align-items-center center justify-content-center d-flex whitetext" style="font-size: 24px;">
    <div class="col-3">Step 1</div>
    <div class="col-3">Step 2</div>
    <div class="col-3">Step 3</div>
    <div class="col-3">Finish</div>
</div>
<div class="progress bg-dark borderradius progress-bar-striped progress-bar-animated" role="progressbar">
    <div class="progress-bar bg-dark progress-bar-striped progress-bar-animated" style="width: 25%"></div>
    <div class="progress-bar progress-bar-striped bg-info progress-bar-animated borderradius" style="width: 25%"></div>
</div>
</div> <!-- card-footer -->
';
$progress_bar_step_3 = '
<div class="card-footer">
    <div class="row align-items-center center justify-content-center d-flex whitetext" style="font-size: 24px;">
        <div class="col-3">Step 1</div>
        <div class="col-3">Step 2</div>
        <div class="col-3">Step 3</div>
        <div class="col-3">Finish</div>
    </div>
    <div class="progress bg-dark borderradius progress-bar-striped progress-bar-animated" role="progressbar">
        <div class="progress-bar bg-dark progress-bar-striped progress-bar-animated" style="width: 50%"></div>
        <div class="progress-bar progress-bar-striped bg-info progress-bar-animated borderradius" style="width: 25%"></div>
    </div> <!-- progress bar -->
</div> <!-- card-footer -->
';
$add_order_footer = '
</div> <!-- card -->
</div> <!-- row -->
</div> <!-- container fluid -->
</div> <!-- end of main content col-lg-10 col-12 -->
';


$add_order_display_added_products = '
<h1>Added products :</h1> 
<div id="added-products-window-container" class="text-white">
             
</div>     

';

$add_order_step_1 = '
<!-- ----------- Here starts the card body ----------- -->
<div class="card-body card-body-add-order"> 

<div class="alert alert-success borderradius">
    <div class="row m-1 text-black">
        <div class="col-sm-4 col-12 align-items-sm-start justify-content-sm-start align-items-center justify-content-center d-flex nowrap create-order-headline-text my-text-shadow">
            Create Order
        </div>
        <div class="col-sm-8 col-12 align-items-sm-end justify-content-sm-end align-items-center justify-content-center d-flex nowrap create-order-headline-text my-text-shadow">
            Step 1 - Add basic info
        </div>  
    </div>
</div>
<hr class="my-horizontal-line"></hr>    <!-- Línan -->
<hr class="my-horizontal-line-black"></hr>    <!-- Línan -->

<form id="create-order-step-1" class="needs-validation" novalidate>


<!-- FIRSTNAME - LASTNAME - EMAIL -->
<div class="row p-1 align-items-center justify-content-center d-flex">
<div class="col-lg-8 col-12">
<div class="row">
    <div class="col-4 d-flex align-items-center justify-content-center">
        <label for="validationDefault01" class="nowrap whitetext font-size-22px">Firstname:</label>
    </div>
    <div class="col-8">
        <input class="form-control bg-dark-subtle" 
        type="text" 
        name="firstname" 
        placeholder="Required field" 
        id="validationDefault01" 
        required>
        <div class="invalid-feedback">Name is required !</div>
    </div>
</div>
</div>
</div> <!-- row p-1 align-items-center -->

<br>

<div class="row p-1 align-items-center justify-content-center d-flex">
<div class="col-lg-8 col-12">
<div class="row">
    <div class="col-4 d-flex align-items-center justify-content-center">
        <label class="nowrap whitetext font-size-22px">Lastname:</label>
    </div>
    <div class="col-8">
        <input class="form-control bg-dark-subtle" 
        type="text" 
        name="lastname" 
        placeholder="Required field"
        required>
        <div class="invalid-feedback">Lastname is required !</div>
    </div>
</div>
</div>
</div> <!-- row p-1 align-items-center -->

<br>


<div class="row p-1 align-items-center justify-content-center d-flex">
<div class="col-lg-8 col-12">
<div class="row">
    <div class="col-4 d-flex align-items-center justify-content-center">
        <label class="nowrap whitetext font-size-22px">E-mail:</label>
    </div>
    <div class="col-8">
        <input class="form-control bg-dark-subtle" 
        type="text" 
        name="email" 
        placeholder="Required field"
        pattern="[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,4}$"
        required>
        <div class="invalid-feedback">Please enter a valid email address !</div>
<!--
This pattern allows the following characters before the @ symbol: 
lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), 
underscores (_), dots (.), percent signs (%), plus signs (+), 
and hyphens (-).

Similarly, after the @ symbol, it allows lowercase letters, 
uppercase letters, digits, dots, and hyphens. Then it requires a 
dot (.), followed by 2 to 4 lowercase or uppercase letters at the 
end of the string. -->

    </div>
</div>
</div>
</div> <!-- row p-1 align-items-center -->


<hr class="my-horizontal-line-black"></hr>    <!-- Línan -->
<hr class="my-horizontal-line"></hr>    <!-- Línan -->
';

/*  HERE START STEP 2 OF THE PROCESS */
$add_order_step_2 = '

<!-- ----------- Here starts the card body ----------- -->
<div class="card-body card-body-add-order">
<div class="alert alert-success borderradius">
    <div class="row m-1 text-black">
        <div class="col-8 align-items-start justify-content-start d-flex">
            <h2>Step 2 - Delivery Info</h2>
        </div>
        <div class="col-4 align-items-end justify-content-end d-flex">
            <h2>Create Order</h2>
        </div>  
    </div>
</div>


<hr class="my-horizontal-line"></hr>    <!-- Línan -->
<hr class="my-horizontal-line-black"></hr>    <!-- Línan -->

<form id="create-order-step-2" method="post">
<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">Address:</label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="address" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>

<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">Address 2:</label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="address2" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>


<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">Postalcode:</label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="postalcode" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>


<hr>

<!-- CITY - STATE - COUNTRY -->
<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">City:</label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="city" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>
<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">State:</label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="state" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>
<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">Country:</label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="country" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>

<hr>

<!-- USER ID AND ORDER STATUS -->
<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">
                    User ID:
                </label>
            </div>
            <div class="col-8">
                <input class="form-control bg-dark-subtle" type="text" name="user_id" placeholder="Not required field">
            </div>
        </div>
    </div>
</div>


<!-- ORDER STATUS -->
<div class="row p-1 align-items-center justify-content-center d-flex">
    <div class="col-lg-8 col-12">
        <div class="row">
            <div class="col-4 d-flex align-items-center justify-content-center">
                <label class="nowrap whitetext font-size-22px">
                    Select Order Status:
                </label>
            </div>
            <div class="col-8">
                <select class="form-select bg-dark-subtle" name="order_status">
                    <option value="made">Made</option>
                    <option value="confirmed">Confirmed</option>
                    <option value="processed">Processed</option>
                    <option value="delivered">Delivered</option>
                    <option value="cancelled">Cancelled</option>
                </select>
            </div>
        </div>
    </div>
</div>


    

<hr class="my-horizontal-line-black"></hr>    <!-- Línan -->
<hr class="my-horizontal-line"></hr>    <!-- Línan -->


';



/* 
$action = $_GET['action'] ?? $_POST['action'];

if($action === 'create-order-step-1') {
    echo $add_order_header;
    echo $add_order_step_1;
    echo $button_row;
    echo $progress_bar_step_1;
    echo $add_order_footer;
}
else if ($action === 'create-order-step-2') {
    echo $add_order_header;
    echo $add_order_step_2;
    echo $button_row;
    echo $progress_bar_step_2;
    echo $add_order_footer;
}
else if ($action === 'create-order-step-3') {
    echo $add_order_header;
    require_once 'create_order_items.php';
    echo $button_row;
    echo $progress_bar_step_3;
    echo $add_order_footer;
} */
?>
