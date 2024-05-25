              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


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
include "order_functions.php";


?>

<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 offset-lg-2 kirsty-regular-italic offset vh-100 margin-top" style="font-size: 16px;">';
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- Row og col sem geymir Users table -->
        <div class="row">
          
               <!-- Cardið fyrir Users table -->
               <div class="card card-lg-width col-lg-10 col-12 mx-auto">
                    <div class="card-header d-flex justify-content-center">
                        <span class="alert alert-success rounded-pill minnborderradius center kirsty-bold-italic text-black my-text-shadow my-text-stroke" style="width: 95%; font-size: 36px;">List Of Your Orders</span>
                    </div>
                    <div class="card-body center">
                    <div class="table-responsive border table-custom" style="overflow-x: auto;">
                            <div class="mytable">
                                <table class="table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col">Order Status</th>
                                            <th scope="col">Order Unique ID</th>
                                            <th scope="col" style="width: 6%;">User ID</th>
                                            <th scope="col">Firstname</th>
                                            <th scope="col">E-mail</th>
                                            <!-- <th scope="col">Country</th> -->
                                            <th scope="col">Final Price</th>
                                            <th scope="col">Created At</th>
                                            <th scope="col" class="action-column">Action</th>
                                            <th scope="col" class="action-column">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <?php 
                                        /* Check if the page is set in the URL. Otherwise, set it to 1 */
                                        if (isset($_GET['page'])) {
                                            $page = $_GET['page'];
                                        } else {
                                            $page = 1;
                                        }

                                        /* Set how many orders should display per page */
                                        $perPage = 10;

                                        /* Get paginated orders */
                                        $paginatedOrders = getOrders($page, $perPage, null);

                                        /* Check if there are any orders to display */
                                        if ($paginatedOrders) {
                                            foreach ($paginatedOrders as $order_data) {
                                                /* Create an encrypted token using the encrypt_order_unique_id function */
                                                $encryptedToken = encrypt_order_unique_id($order_data['order_unique_id']);

                                                /* Determine CSS class to use with order_status */
                                                $order_status_class = getOrderStatusClass($order_data['order_status']);

                                                echo "<tr>";
                                                echo "<td class='$order_status_class'>" . $order_data['order_status'] . "</td>";
                                                echo "<td>" . $order_data['order_unique_id'] . "</td>";
                                                echo "<td>" . $order_data['user_id'] . "</td>";
                                                echo "<td>" . $order_data['firstname'] . "</td>";
                                                echo "<td>" . $order_data['email'] . "</td>";
                                                /* echo "<td>" . $order_data['address'] . "</td>"; */ /* GEYMA */
                                                /* echo "<td>" . $order_data['city'] . "</td>"; */ /* GEYMA */
                                                /* echo "<td>" . $order_data['country'] . "</td>"; */ /* GEYMA */
                                                echo "<td>" . $order_data['final_price'] . "</td>";
                                                echo "<td>" . $order_data['created_at'] . "</td>";
                                                echo "<td><a class='btn btn-secondary custom-btn' href='order_info.php?token=" . $encryptedToken . "&action=showinfo'>View</a></td>";
                                                echo "<td><a class='btn btn-danger custom-btn' href='order_info.php?token=" . $encryptedToken . "&action=delete'>Delete</a></td>";
                                                echo "</tr>";
                                            }
                                        } else {
                                            echo "<tr><td colspan='9'>No orders found</td></tr>";
                                        }
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
                                /* Round up the total number to find the number of pages to display */
                                $totalPages = ceil(countOrders() / $perPage);
                                
                                /* Previous link */
                                if($page > 1) {
                                    /* set the link active if page number is more then 1 - Set the link to currentPage - 1 to the previous page */
                                    echo '<li class="page-item bg-dark"><a class="page-link" href="orders.php?page=' . ($page - 1) . '">Previous Page</a></li>';
                                } else {
                                    /* set the link as disabled if page number is 1 - the link hrefs to nothing since there is no previous page */
                                    echo '<li class="page-item disabled"><a class="page-link" href="#">Previous Page</a></li>';
                                }
                                /* Make the page numbers */
                                for ($i=1; $i <= $totalPages; $i++) {
                                    if($page == $i) {
                                        /* If current page, set the page item as active */                                        
                                        echo '<li class="page-item active"><a class="page-link" href="orders.php?page=' . $i . '">' . $i . '</a></li>';
                                    } else {
                                        echo '<li class="page-item"><a class="page-link" href="orders.php?page=' . $i . '">' . $i . '</a></li>';
                                    }
                                }
                                /* Next link */
                                if ($page < $totalPages) {
                                    echo '<li class="page-item"><a class="page-link" href="orders.php?page=' . ($page + 1) . '">Next Page</a></li>';
                                } else {
                                    echo '<li class="page-item disabled"><a class="page-link" href="#">Next Page</a></li>';
                                }
                                ?>
                            </ul> <!-- pagination -->
                        </nav><!-- page navigation -->
                    </div> <!-- card-footer -->


                    <!-- Row og col-12 fyrir skilaboð sem koma í gegnum url -->
                    <?php
                    /* Check for msg in the URL and if so, display it in new row and col */
                    if(isset($_GET['message'])) {
                        $message = $_GET['message'];
                        echo '<div class="row">';
                            echo '<div class="col-12">';
                                echo "<div class='alert alert-success center'>$message</div>";
                            echo '</div>';
                        echo '</div>';
                    }
                    ?>
                </div> <!-- card -->
          
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->

