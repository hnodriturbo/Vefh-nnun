<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);
/* starta session og header virkar ekki nema hafa ob_start */
ob_start();
session_start();

/* Store the current URL in a session variable */
if (!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}

/* Athuga hvort viðkomandi sé loggaður inn og redirecta í samræmi við það */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: ../login/login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: ../login/login.php?error=You need to be logged in to see this site");
    exit();
}
$base_url = "../";
/* includa og bý til síðu */
include "../database/database.php";
include "../sidebar.php";
include "../topnavbar.php";
include '../database/encryption_functions.php';
include "products_functions.php";

?>

<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 16px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- Row og col sem geymir Users table -->
        <div class="row vh-100 justify-content-center align-items-center center d-flex">
            <div class="center">
               <!-- Cardið fyrir Users table -->
                <div class="card card-lg-width col-lg-10 col-12 mx-auto" style="margin-top: 100px;">
                    <div class="card-header d-flex justify-content-center">
                        <span class="row alert alert-success rounded-pill minnborderradius kirsty-bold-italic text-black my-text-shadow my-text-stroke" style="width: 95%; font-size: 36px;">
                        
                        <!-- whitetext orders-card-header-font-size -->
                        <div class="col-3  nowrap align-content-start d-flex">Welcome</div>
                        <div class="col-4"></div>
                        <div class="col-5  nowrap d-flex justify-content-end">List of your products:</div>

                            <div class="align-items-end"></div>
                        </span>
                    </div>
                    <div class="card-body">
                    <div class="table-responsive border table-custom" style="overflow-x: auto;">
                            <div class="mytable">
                                <table class="table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col">Product ID</th>
                                            <th scope="col">Image</th>
                                            <th scope="col">Name</th>
                                            <th scope="col">Description</th>
                                            <th scope="col">Price</th>
                                            <th scope="col">Category ID</th>
                                            <th scope="col" class="action-column">Action</th>
                                            <th scope="col" class="action-column">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>

                                        <?php
                                        /* Check if page is set in the url. Otherwise set the page to 1 */
                                        if(isset($_GET['page'])) {
                                            $currentPage = $_GET['page'];
                                        } else {
                                            $currentPage = 1;
                                        }
                                        $productsPerPage = 10;
                                        getPaginatedProducts($currentPage, $productsPerPage);
                                        ?>

                                    </tbody>
                                </table>
                            </div> <!-- mytable -->
                        </div> <!-- table-responsive -->
                    </div> <!-- card-body -->

                    <!-- Card footer --- PAGINATION -->                  
                    <div class="card-footer pb-5 d-flex justify-content-end">
                        <nav aria-label="Page navigation">
                            <ul class="pagination">
                                <?php 
                                /* Nota ceil til að rounda upp deilingu og finna út hvað margar síður eru */
                                $totalPages = ceil(countProducts() / $productsPerPage);
                                
                                /* Previous link */
                                if ($currentPage > 1) {
                                    /* set the link active if page number is more then 1 - Set the link to currentPage - 1 to the previous page */
                                    echo '<li class="page-item bg-dark"><a class="page-link" href="products.php?page=' . ($currentPage - 1) . '">Previous Page</a></li>';
                                } else {
                                    /* set the link as disabled if page number is 1 - the link hrefs to nothing since there is no previous page */
                                    echo '<li class="page-item disabled"><a class="page-link" href="#">Previous Page</a></li>';
                                }
                                
                                /* Make the page numbers */
                                for ($i=1; $i <= $totalPages; $i++) {
                                    /* Þegar i er jafnt og currentPage þá er page-item ACTIVE */
                                    if ($currentPage == $i) {
                                        echo '<li class="page-item active"><a class="page-link" href="products.php?page=' . $i . '">' . $i . '</a></li>';
                                    }
                                    /* í öll önnur skipti sem i keyrir þá er page-item ekki active */
                                    else {
                                        echo '<li class="page-item"><a class="page-link" href="products.php?page=' . $i . '">' . $i . '</a></li>';
                                    }
                                }

                                /* Next link */
                                if ($currentPage < $totalPages) {
                                    echo '
                                    <li class="page-item">
                                    <a class="page-link" href="products.php?page=' . ($currentPage + 1) . '">Next Page</a>
                                    </li>
                                    ';
                                } else {
                                    echo '
                                    <li class="page-item disabled"><a class="page-link" href="#">Next Page</a></li>
                                    ';
                                }
                                ?>
                            </ul> <!-- pagination -->
                        </nav><!-- page navigation -->
                    </div> <!-- card-footer -->

                    <!-- Row og col-12 fyrir skilaboð sem koma í gegnum url -->
                    <div class="row">
                        <div class="col-12">
                            <?php 
                            if(isset($_GET['message'])) {
                                $message = $_GET['message'];
                                echo "<div class='alert alert-success center'>$message</div>";
                            }
                            ?>
                        </div> <!-- col-12 -->
                    </div> <!-- row -->
                </div> <!-- card -->
            </div> <!-- center -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->