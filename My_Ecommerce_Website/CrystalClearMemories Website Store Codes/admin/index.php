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
    header("Location: login/login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login/login.php?error=You need to be logged in to see this site");
    exit();
}
$base_url = "";
require_once "database/database.php";
require_once "sidebar.php";
require_once "topnavbar.php";
require_once "overview_functions.php";



?>


    <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
    <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
        <!-- Container fyrir skipulag contents -->
        <div class="container-fluid">

            <!-- Row og col sem geymir Users table -->
            <div class="row">
                <div class="d-flex align-items-center justify-content-center col-lg-10 col-12 mx-auto">

                    <!-- Cardið fyrir Users table -->
                    <div class="card card-lg-width" style="margin-top: 70px;">
                        
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius w-100">Users List</h4>

                        </div>
                      
                        <div class="card-body">
                            <div class="table-responsive border">
                                <div class="mytable">
                                    <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                        <thead>
                                            <tr>
                                                <th scope="col">User id</th>
                                                <th scope="col">Firstname</th>
                                                <th scope="col">Lastname</th>
                                                <th scope="col">E-mail</th>
                                                <th scope="col">Username</th>
                                                <th scope="col">Address</th>
                                                <th scope="col">Address2</th>
                                                <th scope="col">Postalcode</th>
                                                <th scope="col">City</th>
                                                <th scope="col">Country</th>
                                                <th scope="col">Other</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <?php getUsers(); ?>
                                        </tbody>
                                    </table>
                                </div> <!-- mytable -->
                            </div> <!-- table-responsive -->
                        </div> <!-- card-body -->
                        <div class="card-footer pb-5 d-flex justify-content-end">
                            <a href="users/users.php">
                                <button type="button" class="btn btn-outline-secondary justify-content-center">Open Users List</button>
                            </a>
                        </div> <!-- card-footer -->
                        
                    </div> <!-- card -->

                </div><!-- d-flex align-items-center justify-content-center h-100 col-10 mx-auto -->
            </div><!-- row users table -->

            <div class="row">
                <div class="col-lg-6 col-12">
                    <div class="card card-lg-width">
                    <div class="card-header">
                    <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius w-100">Admin Users List</h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive border">
                            <div class="mytable">
                                <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                    <tr>
                                        <th scope="col">Admin ID</th>
                                        <th scope="col">Name</th>
                                        <th scope="col">Email</th>
                                        <th scope="col">Username</th>
                                        <th scope="col">Password</th>
                                        <th scope="col" class="nowrap">Admin UID</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <?php getAdminUsers(); ?>
                                    </tbody>
                                </table>
                                </div>
                            </div>
                        </div>
                        <div class="card-footer pb-5 d-flex justify-content-end">
                            <a class="btn btn-outline-secondary" href="admins/admins.php">Open Admin Users</a>
                        <!-- <button type="button" class="btn btn-outline-secondary">Open Admin Users List</button> -->
                        </div>
                    </div>
                </div> <!-- col-6 admin users table -->

                <!-- Logs table -->
                <div class="col-lg-6 col-12">
                    <div class="card card-lg-width">
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius w-100">Logs</h4>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive border">
                                <div class="mytable">
                                    <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                        <thead>
                                        <tr>
                                            <th scope="col">Logs ID</th>
                                            <th scope="col">User ID</th>
                                            <th scope="col">Action</th>
                                            <th scope="col">Date</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        <?php getLogs(); ?>
                                        </tbody>
                                    </table>
                                    </div>
                                </div>
                            </div>
                            <div class="card-footer pb-5 d-flex justify-content-end">
                            <a class="btn btn-outline-secondary" href="logs/logs.php">Open Logs</a>
                            </div>
                        </div><!-- card-body -->
                    </div><!-- card card-lg-width -->
                </div> <!-- col-6 logs table -->
                
            </div><!-- row -->
        </div><!-- container fluid -->
            
        
    </div> <!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->
