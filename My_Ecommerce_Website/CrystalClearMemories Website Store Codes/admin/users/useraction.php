<?php 
session_start();
ob_start();

/* Athuga hvort viðkomandi sé loggaður inn og redirecta í samræmi við það */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
/* set the base url to go up one folder and include the necessary files */
$base_url = "../";
require_once "../database/database.php";
require_once "../sidebar.php";
require_once "../topnavbar.php";
require_once "user_functions.php";
/* Næ í úr urli */
$action = $_GET['action'];
$source = $_GET['source'];

if (isset($_GET['user_uid'])) {
    $user_uid = $_GET['user_uid'];
}



/* ---------- UPDATE USER ------------ */
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if($action == 'edit' && $source == 'users' && isset($user_uid)) {
        updateUserInfo($user_uid);
        header("Location: users.php?message=User $username updated successfully");
    }
}


/*----- Htmlið sem sýnir alla reitina og userInfo er value þeirra --------*/
if ($action == 'view' && $source == 'users' && isset($_GET['user_uid'])) {
    /* sækja user */
    $userInfo = fetchUserInfo($user_uid);
    echo '
<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <!-- Container row og col-lg-8 sem breytist í col-12 á minni skjám -->
    <div class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-lg-9 col-12 d-lg-flex">
                <!-- Formið byrjar hérna og er utan um allt cardið -->
                <form action="useraction.php?action=edit&source=users&user_uid=' . $user_uid . '&confirm=confirm" method="POST" name=updateUser class="w-100">
                    <!-- Card sem fyllir upp í plássið (w-100) -->
                    <div class="card card-lg-width w-100" style="margin-top: 12vw;">
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill w-100 d-flex justify-content-center align-items-center center" style="font-size: 22px; cursor: default;">Edit User Profile</h4>
                        </div>
                        <div class="card-body">
                            <!-- Línan -->
                            <hr class="my-horizontal-line" style="color: blue;">
                            <!-- Row og 4 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Firstname:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="firstname" value="' . $userInfo['firstname'] . '" aria-label="default input example">  
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Username:</label>
                                </div>
                                <div class="col-5" style="padding: 0;"> 
                                    <input class="form-control bg-dark-subtle" type="text" name="username" value="' . $userInfo['username'] . '" aria-label="default input example" style="background-color: #F2F2F2;">
                                </div> 
                            </div> 
                            <!-- Row og 4 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                <label class="text-align" style="color: #CCCCCC;">Lastname:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="lastname" value="' . $userInfo['lastname'] . '" aria-label="default input example">  
                                </div>
                                <div class="col-1">
                                <label class="text-align" style="color: #CCCCCC;">Password:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="password" name="password" value="' . $userInfo['password'] . '" aria-label="default input example">
                                </div>
                            </div>
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
                                </div>
                                <div class="col-11" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="email" value="' . $userInfo['email'] . '" aria-label="default input example">  
                                </div>
                            </div> 
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Address:</label>
                                </div>
                                <div class="col-6" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="address" value="' . $userInfo['address'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Address 2:</label>
                                </div>
                                <div class="col-4" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="address2" value="' . $userInfo['address2'] . '" aria-label="default input example">
                                </div>
                            </div>
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                <label class="text-align" style="color: #CCCCCC;">Postal Code:</label>
                                </div>
                                <div class="col-2" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="postalcode" value="' . $userInfo['postalcode'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">City:</label>
                                </div>
                                <div class="col-4" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="city" value="' . $userInfo['city'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Country:</label>
                                </div>
                                <div class="col-3" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="country" value="' . $userInfo['country'] . '" aria-label="default input example">
                                </div>
                            </div>

                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center">
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Other:</label>
                                </div>
                                <div class="col-11" style="padding: 0;">
                                    <textarea class="form-control bg-dark-subtle" name="other" aria-label="textbox example" style="height: 5vw;">' . $userInfo['other'] . '</textarea>
                                </div>
                            </div>
                        </div><!-- card-body -->
                        <div class="card-footer pb-5 d-flex justify-content-center">
                        <!-- update takkinn -->
                        <button class="btn btn-outline-secondary" type="POST" name="update" style="width: 50%;">Update</button>
                        </div>
                    </div><!-- card card-lg-width w-100" style="margin-top: 12vw;" -->
                </form>
            </div> <!-- col-12 admin users table -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->
    
    ';
}



/* Ef ýtt er á confirm takkann */
if ($action == 'delete' && $source == 'users' && isset($_GET['user_uid']) && isset($_GET['confirm'])) {
    $user_uid = $_GET['user_uid'];
    if (deleteUser($user_uid)) {
        header("Location: users.php?message=User " . $userInfo['username'] . " has been deleted successfully");
    } else {
        /* header("Location: users.php?message=User was not deleted"); */
    }
    exit();
}
/* html card sem spyr um staðfestingu á hvort eigi að delete user */
if ($action == 'delete' && $source == 'users' && isset($_GET['user_uid'])) {
    $user_uid = $_GET['user_uid'];
    $userInfo = fetchUserInfo($user_uid);
    echo '
    <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
    <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
        <!-- Container fyrir skipulag contents -->
        <div class="container-fluid">
            <!-- Row og col sem geymir Users table -->
            <div class="row vh-100">
                <div class="align-items-center justify-content-center center h-100 w-100 mx-auto">
                    <!-- Cardið fyrir Users table -->
                    <div class="card card-lg-width col-lg-10 col-12 mx-auto justify-content-center align-content-center" style="margin-top: 100px;">
    
                    <div class="card-header bg-dark-subtle borderradius">
                        <h4 class="card-title text-center">Are you sure you want to delete user ' . $userInfo['username'] . '?</h4>
                    </div>

                    <div class="card-body mx-auto">
                        <br><br><br><br>
                    </div><!-- card-body -->

                    <div class="card-footer pb-5 d-flex justify-content-center align-items-center" style="border-top: 0px;">
                        <div class="col-2">
                            <a class="btn btn-danger btn-lg borderradius" href="useraction.php?action=delete&source=users&user_uid=<?php echo $user_uid; ?>&confirm=confirm" style="width: 200px; height: 50px;">Delete</a>
                        </div>
                
                        <div class="col-2"></div>
                
                        <div class="col-3">
                            <a class="btn btn-secondary btn-lg borderradius" href="users.php" style="width: 200px; height: 50px;">Cancel</a> 
                        </div>
                    </div>

                </div> <!-- card -->
            </div> <!-- col-12 admin users table -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->

    ';
}
?>