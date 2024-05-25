<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);
/* starta session og header virkar ekki nema hafa ob_start */
ob_start();
session_start();
/* Athuga hvort viðkomandi sé loggaður inn og redirecta í samræmi við það */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
/* includa og bý til síðu */
include "database.php";
include "sidebar.php";
include "topnavbar.php";

/* js.js er scripta sem á að gera image appear smoothly - en það er samt smooth án þess */
/* include "js/smoothImage.js"; */

/* sample url: products_action.php?source=products&product_id=prod_id&action=edit/delete */
$source = $_GET['source'];
$product_id = $_GET['product_id'];
$action = $_GET['action'];
$confirm = isset($_GET['confirm']) ? $_GET['confirm'] : '';

/* sample url: products_action.php?source=products&product_id=123&action=edit&error=errorMessage */
if(isset($_GET['error'])) {
    $error = $_GET['error'];
} else {
    $error = '';
}

/* ------ ÉG Á EFTIR AÐ GERA STAÐFESTINGU Á DELETION --------- */
/* ------ ÉG Á EFTIR AÐ GERA STAÐFESTINGU Á DELETION --------- */


/* ----- SÆKJA PRODUCT INFO OG SETJA Í ARRAY ----- */
function fetchProductInfo($product_id) {
    /* Opna tengingu */
    global $conn;
    /* bý til tómt array */
    $productInfo = array();
    /* prepare the query */
    $sql = "SELECT * FROM products WHERE product_id = ?";
    /* prepare the stmt */
    $stmt = $conn->prepare($sql);
    /* check if stmt conn errors */
    if(!$stmt) {
        header("Location: products.php?message=sql error in preparing the query");
        return $productInfo;
    }
    /* bind parameters */
    $stmt->bind_param("i", $product_id);
    /* run stmt með if */
    if($stmt->execute()) {
        /* put in result */
        $result = $stmt->get_result();
        /* check for num_rows is returned */
        if($result->num_rows === 0) {
            header("Location: products.php?message=sql no rows found");
            return $productInfo;
        } else {
            /* fetcha result to $row */
            $row = $result->fetch_assoc();
            /* put info to array */
            $productInfo['product_id'] = $row['product_id'];
            $productInfo['image'] = $row['image'];
            $productInfo['name'] = $row['name'];
            $productInfo['description'] = $row['description'];
            $productInfo['price'] = $row['price'];
            $productInfo['c_price'] = $row['c_price'];
            $productInfo['category_id'] = $row['category_id'];
            $productInfo['tags'] = $row['tags'];
        }
    }
    /* Close stmt */
    $stmt->close();
    /* return the array object and information */
    return $productInfo;
}

/* FUNCTION FOR FETCHING CATEGORY NAME */
function fetchCategoryName($category_id) {
    global $conn;

    $sql = "SELECT * FROM categories WHERE category_id = ?";

    $stmt = $conn->prepare($sql);
    if(!$stmt) {
        echo "conn error: " . $conn->error;
    }

    $stmt->bind_param("i", $category_id);

    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }

    $result = $stmt->get_result();
    if ($result->num_rows === 0) {
        echo "no rows found";
    }

    $row = $result->fetch_assoc();

    $categoryName = $row['name'];

    return $categoryName;

}


/* ---------- UPDATE PRODUCT------------ */
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if($source == 'products' && isset($product_id) && $action == 'view' && $confirm == 'confirm') {
        updateProduct($product_id);
        header("Location: products.php?message=Product $name updated successfully");
    }  
}
/* ---------- FUNCTINO TO UPDATE PRODUCT------------ */
function updateProduct($product_id) {
    global $conn;
    if(isset($_POST['updateProduct'])) {
        /* get the info from post */
        $image = $_POST['image'];
        $name = $_POST['name'];
        $description = $_POST['description'];
        $price = $_POST['price'];
        $c_price = $_POST['c_price'];
        $category_id = $_POST['category_id'];
        $tags = $_POST['tags'];

        /* get the product id */
        $product_id = $_GET['product_id'];

        /* undirbý $sql og set í $stmt */
        $sql = "UPDATE products SET image=?, name=?, description=?, price=?, c_price=?, category_id=?, tags=? WHERE product_id=?";
        $stmt = $conn->prepare($sql);
        if(!$stmt) {
            echo "sql conn error: " . $conn->error;
        }

        $stmt->bind_param("sssddisi", $image, $name, $description, $price, $c_price, $category_id, $tags, $product_id);

        if($stmt->execute()) {
            return true;
        } else {
            echo "sql query error: " . $stmt->error;
        }
        $stmt->close();
    }
}

/* FETCH PRODUCT INFO AND IMAGE - DISPLAY INFO FOR EDITING */
if ($source == 'products' && isset($_GET['product_id']) && $action == 'view') {
    // SÆKJA PRODUCT INFO
    $productInfo = fetchProductInfo($product_id);
    // SÆKJA CATEGORY NAME
    $category_id = $productInfo['category_id'];
    $categoryName = fetchCategoryName($category_id);
    // Get the URL for the full-size image
    $fullImageURL = 'img/products/' . $productInfo['image'];

    // Generate unique ID's for the modal and input element
    $modalId = 'productImageModal_' . $product_id;
    $inputId = 'myInput_' . $product_id;

    echo '
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <div class="container-fluid">
        <div class="row vh-100 justify-content-center align-items-center center mx-auto d-flex">
            <div class="col-lg-9 col-12 d-lg-flex justify-content-center align-items-center center mx-auto">
                <form action="products_action.php?source=products&product_id=' . $product_id . '&action=view&confirm=confirm" method="POST" name="updateProduct" class="w-100">
                    <div class="card card-lg-width w-100 mt-5">

                        <div class="card-header">
                            <h4 class="alert alert-success rounded-pill w-100 d-flex justify-content-center align-items-center center" style="font-size: 22px; cursor: default;">Edit Product Info</h4>
                        </div>

                        <div class="card-body">
                            <!-- --------- THUMBNAIL VERSION OF THE PICTURE -------- -->
                            <div class="row p-3 align-items-center">
                                <a href="' . $fullImageURL . '" data-bs-toggle="modal" data-bs-target="#productImageModal">
                                    <img src="' . $fullImageURL . '" alt="Product Image" class="img-thumbnail mythumbnail" style="cursor: pointer;">
                                </a>
                            </div>

                            <!-- PRODUCT ID - CATEGORY ID - CATEGORY -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                <label class="text-align nowrap" style="color: #CCCCCC;">Product Id:</label>
                                </div>
                                <div class="col-1" style="padding: 0;">
                                    <!-- Use <span> to display the product ID value -->
                                    <span class="bg-dark text-white" style="font-size: 22px;">-&nbsp;&nbsp;' . $productInfo['product_id'] . '&nbsp;&nbsp;-</span>
                                </div>
                                <div class="col-2">
                                    <label class="text-align nowrap" style="color: #CCCCCC;">Category Id:</label>
                                </div>
                                <div class="col-2" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="category_id" value="' . $productInfo['category_id'] . '" aria-label="default input example">
                                </div>
                                <div class="col-2">
                                <label class="text-align nowrap" style="color: #CCCCCC;">Category:</label>
                                </div>
                                <div class="col-2" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="category" value="' . $categoryName . '" aria-label="default input example">
                                </div>
                            </div>
                            
                            <!-- NAME & DESCRIPTION -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                <label class="text-align nowrap" style="color: #CCCCCC;">Product Name:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="name" value="' . $productInfo['name'] . '" aria-label="default input example">  
                                </div>
                            </div>
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                    <label class="text-align nowrap" style="color: #CCCCCC;">Description:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <textarea class="form-control bg-dark-subtle" name="description" rows="3" aria-label="default textarea example">' . $productInfo['description'] . '</textarea>
                                </div>
                            </div>

                            <!-- PRICE AND C_PRICE -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                    <label class="text-align nowrap" style="color: #CCCCCC;">Price:</label>
                                </div>
                                <div class="col-3" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="price" value="' . $productInfo['price'] . '" aria-label="default input example">
                                </div>
                                <div class="col-3">
                                <label class="text-align nowrap" style="color: #CCCCCC;">Cost Price:</label>
                                </div>
                                <div class="col-3" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="c_price" value="' . $productInfo['c_price'] . '" aria-label="default input example">
                                </div>
                            </div>

                            <!-- TAGS -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                <label class="text-align nowrap" style="color: #CCCCCC;">Tags:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="tags" value="' . $productInfo['tags'] . '" aria-label="default input example">
                                </div>
                            </div>

                        </div><!-- card-body -->

                        <!-- CARD FOOTER -->

                        <!-- HIDDEN INPUT FIELD THAT CONTAINS THE IMAGE URL -->
                        <div class="card-footer pb-5 d-flex justify-content-center">
                            <input type="hidden" name="image" value="' . $productInfo['image'] . '">
                            <button class="btn btn-outline-secondary" type="submit" name="updateProduct" style="width: 50%;">Confirm changes</button>
                        </div>

                    </div><!-- card card-lg-width w-100" -->
                    ';
                    
                if(isset($_GET['error'])) {
                    echo '
                    <div class="row p-3 align-items-center">
                        <div class="alert alert-success center">' . $error . '</div>
                    </div>
                    ';
                }
                echo '
                </form> <!-- form -->
            </div> <!-- col-lg-9 col-12 -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->

<!-- Product Image Modal -->
<div class="modal fade" id="productImageModal" tabindex="-1" role="dialog" aria-labelledby="productImageModalLabel" aria-hidden="true">

    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">

        <div class="modal-content">

            <div class="modal-header alert alert-success center">
                <h5 class="modal-title kirsty-regular-italic" id="productImageModalLabel">' . $productInfo['name'] . '</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>

            </div>
            <div class="modal-body text-center">
                <img src="' . $fullImageURL . '" alt="Product Image" class="img-fluid">
            </div>
        </div> <!-- modal-content -->
    </div> <!-- modal-dialog -->
</div> <!-- modal fade -->
    ';
}
?>