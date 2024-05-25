<!-- Þessi síða er eign Hreiðars -->
<!-- Búið til þann 13 júli 2023 -->
    <!-- admins.php -->
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
include "../orders/orders_functions.php";
/* Functionið til að fetcha úr gagnagrunninum */
function getAdminUsers() {
    global $conn;

    $stmt = $conn->prepare("SELECT * FROM admin_accounts");

    $stmt->execute();

    $result = $stmt->get_result();

}
function getPaginatedAdminUsers($page, $perPage) {
    global $conn;

    // Calculate the offset based on the current page and number of admin users per page
    $offset = ($page - 1) * $perPage;

    $stmt = $conn->prepare("SELECT * FROM admin_accounts LIMIT ?, ?");
    $stmt->bind_param("ii", $offset, $perPage);

    $stmt->execute();

    $result = $stmt->get_result();


    while ($row = $result->fetch_assoc()) {
        $admin_id = $row['admin_id'];
        $admin_name = $row['name'];
        $admin_email = $row['email'];
        $admin_username = $row['username'];
        $admin_password = $row['password'];
        $admin_uid = $row['admin_uid'];

        echo "<tr>";
        echo "<td>$admin_id</td>";
        echo "<td>$admin_name</td>";
        echo "<td>$admin_email</td>";
        echo "<td>$admin_username</td>";
        echo "<td>$admin_uid</td>";
        echo "<td>
        <a class='btn btn-outline-secondary' href='admins_action.php?action=edit&source=admins&admin_uid=" . $admin_uid . "'>Edit</a>
        <a class='btn btn-outline-secondary btn-danger' href='admins_action.php?action=delete&source=admins&admin_uid=" . $admin_uid . "'>Delete</a>
        </td>";
        echo "</tr>";

    }
}
function countAdminUsers() {
    global $conn;
    $stmt = $conn->prepare("SELECT COUNT(*) FROM admin_accounts");
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    return $row[0]; // Return the total count
}

?>

<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- Row og col sem geymir Users table -->
        <div class="row">
            <div class="align-items-center justify-content-center center h-100 w-100 mx-auto">
                <!-- Cardið fyrir Users table -->
                <div class="card card-lg-width col-lg-10 col-12 mx-auto justify-content-center align-content-center" style="margin-top: 100px;">
                    <div class="card-header">
                    <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius" style="width: 95%;">Admins Users List</h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive">
                            <div class="mytable">
                            <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                <thead>
                                <tr>
                                    <th scope="col">Admin ID</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Email</th>
                                    <th scope="col">Username</th>
                                    <th scope="col" class="nowrap">Admin UID</th>
                                    <th scope="col">Action</th>
                                </tr>
                                </thead>
                                <tbody>
                                    <?php
                                    if(isset($_GET['page'])) {
                                        $currentPage = $_GET['page'];
                                    } else {
                                        $currentPage = 1;
                                    }
                                    // Set the current page and number of admin users per page
                                    $currentPage = isset($_GET['page']) ? $_GET['page'] : 1;

                                    $usersPerPage = 10;
                                    
                                    getPaginatedAdminUsers($currentPage, $usersPerPage);
                                    ?>
                                </tbody>

                            </table>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer pb-5 d-flex justify-content-end">
                    <nav aria-label="Page navigation bg-dark">
                        <ul class="pagination bg-dark">
                            <?php
                            /* The ceil() function ensures that any fractional result is rounded up to the nearest whole number */
                            $totalPages = ceil(countAdminUsers() / $usersPerPage);

                            // Display "Previous" link
                            if ($currentPage > 1) {
                                echo '<li class="page-item bg-dark"><a class="page-link" href="admins.php?page=' . ($currentPage - 1) . '">Previous Page</a></li>';
                            } else {
                                echo '<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>';
                            }

                            // Display page numbers
                            for ($i = 1; $i <= $totalPages; $i++) {
                                /* echo li class="klasi byrjar - if currentpage true þá active annars '' */
                                echo '<li class="page-item' . ($currentPage == $i ? ' active' : '') . '"><a class="page-link" href="admins.php?page=' . $i . '">' . $i . '</a></li>';
                            }

                            // Display "Next" link
                            if ($currentPage < $totalPages) {
                                echo '<li class="page-item"><a class="page-link" href="admins.php?page=' . ($currentPage + 1) . '">Next Page</a></li>';
                            } else {
                                echo '<li class="page-item disabled"><a class="page-link" href="#">Next</a></li>';
                            }
                            ?>
                        </ul>
                    </nav>

                    </div>
                    <div class="row">
                        <div class="col-12">
                            <?php
                            if (isset($_GET['message'])) {
                                $message = $_GET['message'];
                                echo "<div class='alert alert-success center'>$message</div>";
                            }
                            ?>
                        </div>
                    </div>
                </div><!-- card -->
            </div> <!-- d-flex align-items-center justify-content-center h-100 col-lg-10 col-12 mx-auto -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->
