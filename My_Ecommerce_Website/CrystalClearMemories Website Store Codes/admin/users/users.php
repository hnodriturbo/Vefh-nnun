<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

ob_start();
session_start();

/* Store the current URL in a session variable */
if (!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}

/* set the base url */
$base_url = "../";

if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: " . $base_url . "login/login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: " . $base_url . "login/login.php?error=You need to be logged in to see this site");
    exit();
}
/* Go up one folder and include the necessary files */

require_once "../database/database.php";
require_once "../sidebar.php";
require_once "../topnavbar.php";
require_once "user_functions.php";


?>

<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 16px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- Row og col sem geymir Users table -->
        <div class="row">
            <div class="align-items-center justify-content-center center h-100 w-100 mx-auto">
                <!-- Cardið fyrir Users table -->
                <div class="card card-lg-width col-lg-10 col-12 mx-auto justify-content-center align-content-center" style="margin-top: 100px;">
                    <div class="card-header">
                    <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius" style="width: 95%;">Users List</h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive border" style="overflow-x: auto;">
                            <div class="mytable">
                                <table class="table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col" class="">User id</th>
                                            <th scope="col" class="">Firstname</th>
                                            <th scope="col" class="">Lastname</th>
                                            <th scope="col" class="">E-mail</th>
                                            <th scope="col" class="">Username</th>
                                            <th scope="col" class="">City</th>
                                            <th scope="col" class="">Country</th>
                                            <th scope="col" class="">Other</th>
                                            <th scope="col" class="action-column">Action</th>
                                            <th scope="col" class="action-column">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                     <!-- Ef síða er skráð þá setja hana - annars set page to 1 -->
                                        <?php
                                        if(isset($_GET['page'])) {
                                            $currentPage = $_GET['page'];
                                        } else {
                                            $currentPage = 1;
                                        }
                                        // Ef síða er skráð þá setja hana - annars set page to 1
                                        $currentPage = isset($_GET['page']) ? $_GET['page'] : 1;
                                        $usersPerPage = 10;
                                        getPaginatedUsers($currentPage, $usersPerPage);
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
                                /* Nota ceil til að rounda deilingunni og finna út hvað margar síður eru */
                                /* (totalNotendur / hvadMargirPerSíðu) */
                                $totalPages = ceil(countUsers() / $usersPerPage);

                                /* Display "previous" link */
                                if ($currentPage > 1) {
                                    /* Ef síða er meira en 1 þá er linkurinn active */
                                    echo '<li class="page-item bg-dark"><a class="page-link" href="users.php?page=' . ($currentPage - 1) . '">Previous Page</a></li>';
                                } 
                                else {
                                    /* Ef síðan er númer 1 er previous takkinn disabled */
                                    echo '<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>';
                                }

                                /* Sýna síðunúmerin sjálf */
                                for ($i=1; $i <= $totalPages; $i++) {
                                    if ($currentPage == $i) {
                                        echo '<li class="page-item active"><a class="page-link" href="users.php?page=' . $i . '">' . $i . '</a></li>';
                                        $active = ' active';
                                    } else {
                                        echo '<li class="page-item"><a class="page-link" href="users.php?page=' . $i . '">' . $i . '</a></li>';
                                        $active = '';
                                    }
                                    /* echo '<li class="page-item' . ($active) . '"><a class="page-link" href="users.php?page=' . $i . '">' . $i . '</a></li>';  */
                                }

                                /* Display "next" link */
                                if ($currentPage < $totalPages) {
                                    echo '
                                    <li class="page-item">
                                    <a class="page-link" href="users.php?page=' . ($currentPage + 1) . '">Next Page</a>
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
                            if (isset($_GET['message'])) {
                                $message = $_GET['message'];
                                echo "<div class='alert alert-success center'>$message</div>";
                            }
                            ?>
                        </div> <!-- col-12 -->
                    </div> <!-- row -->
                </div> <!-- card -->
            </div> <!-- d-flex align-items-center justify-content-center h-100 col-lg-10 col-12 mx-auto -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->
