          <!-- -------------------- ADMIN SÍÐAN --------------------- -->
        <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
      <!-- -------------------------------------------------------------- -->
    <!-- --------------------------- MADE 2023 ---------------------------- -->
 

<?php

use Mockery\Generator\StringManipulation\Pass\Pass;

error_reporting(E_ALL);
ini_set('display_errors', 1);
ob_start(); // Required for header("Location...")
session_start();

$base_url = "../";

if (!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}


// Redirect if not logged in
if (!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date']) ||
    (isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date'])) {
    header("Location: " . $base_url . "login/login.php?error=You need to be logged in to see this site");
    exit();
}

# Check if the page is requested with ajax or not
$is_ajax = (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest');

// Load the core parts of the page if it's not an ajax request (first load)
if (!$is_ajax) {
    include_once "$base_url" . "sidebar.php";
    include_once "$base_url" . "topnavbar.php";
}

// Include the file that defines the content variables
include_once 'create_order_info.php'; // <-- Add this line
include_once 'create_functions.php';
include_once "$base_url" . "database/database.php";






// Determine content to display based on the action
$content_to_display = [];
$formSubmitValue = '';

$action = $_GET['action'] ?? $_POST['action'] ?? "";

if (!$is_ajax) {
    echo '
    <div class="col-xl-10 col-12 offset-xl-2 kirsty-regular-italic offset vh-100 margin-top">
        <div id="main-content-container">';
}

if (!$is_ajax && $_SERVER['REQUEST_METHOD'] != 'GET') {
    include 'create_menu.php';
}


if ($_SERVER['REQUEST_METHOD'] === 'POST' || $_SERVER['REQUEST_METHOD'] === 'GET') {

    // Execute code based on the retrived $action variable
    switch ($action) {

        // ------------------ STEP 1 ----------------- //
        // ----- ----- create-order-step-1 ----- ----- //

        case 'create-order-step-1':

            $content_to_display = [$add_order_header, $add_order_step_1, $button_row, $progress_bar_step_1, $add_order_footer];

            break;
        
        // ------------------ STEP 2 ----------------- //
        // ----- ----- create-order-step-2 ----- ----- //

        case 'create-order-step-2':
            $content_to_display = [$add_order_header, $add_order_step_2, $button_row, $progress_bar_step_2, $add_order_footer];

            break;

        // ------------------ STEP 3 ----------------- //
        // ----- ----- create-order-step-3 ----- ----- //    
        case 'create-order-step-3':
            ob_start(); // Start output buffering
            require_once 'create_order_items.php';
            $create_order_items_content = ob_get_clean(); // Get the content from the buffer
            $content_to_display = [$add_order_header, $create_order_items_content, $button_row, $add_order_display_added_products, $progress_bar_step_3, $add_order_footer];
            break;

 
        case 'create-order-step-4':
            break;

        case 'go-to-index':
            include 'create_menu.php';
            break;

        case 'create_product':
            break;

        case 'create_user':
            break;

        default:
            include 'create_menu.php';
            break;
    }
    foreach ($content_to_display as $content) {
        echo $content;
    }
}



    
if (!$is_ajax) {
    echo '</div>
    </div> <!-- col-lg-10 col-12 -->';
}





/* 
            // Þetta er til að tjekka hvort infoið sé í session
            if (isset($_SESSION['step-2-data'])) {
                echo "<script>";
                foreach ($_SESSION['step-1-data'] as $key => $value) {
                    echo "console.log('$key: $value');";
                }
                foreach ($_SESSION['step-2-data'] as $key => $value) {
                    echo "console.log('$key: $value');";
                }
                echo "</script>";
            }
             */


/*     
    if (isset($_SESSION['create-order-step-1']) || isset($_SESSION['create-order-step-2'])) {
        echo "<script>";
        if (isset($_SESSION['create-order-step-1'])) {
            // CONSOLE LOG THE STEP-1-DATA
            foreach ($_SESSION['create-order-step-1'] as $key => $value) {
                echo "console.log('step 1 data:' + '$key: $value' + ' - php session storage');";
            } 
        } 
        if (isset($_SESSION['create-order-step-2'])) {
            // CONSOLE LOG THE STEP-2-DATA
            foreach ($_SESSION['create-order-step-2'] as $key => $value) {
                echo "console.log('step 2 data:' + '$key: $value' + ' - php session storage');";
            }
        }
        echo "</script>";
    } */
/*
                if (isset($_POST['formData'])) {
                if($formSubmitValue === 'create-order-step-2') {
                    // Parse the form data into an associative array
                    parse_str($_POST['formData'], $formDataArray);
                    $_SESSION["{$formSubmitValue}"] = $formDataArray;
                }

            }

     */

?>


