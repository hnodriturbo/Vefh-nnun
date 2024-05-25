<?php 
ob_start();
session_start();
error_reporting(E_ALL);
ini_set('display_errors', 1);

include "database.php";
include "sidebar.php";
include "topnavbar.php";
/* Tómar breytur svo þær komi ekki sem undefined variables */
$name = "";
$email = "";
$username = "";
$password = "";
$admin_uid = "";

/* Sæki admin id, source og action úr urlinu */
$admin_uid = $_GET['admin_uid'];
$source = $_GET['source'];
$action = $_GET['action'];
$confirm = $_GET['confirm'];

/* Function til að fetcha row úr admin_accounts database og setja info í array */
function fetchAdminUser($admin_uid) {
    /* Sækja upplýsingarnar um valinn notanda */
    global $conn;
    // Initialize the result array
    $adminUser = array();
    // Prepare the SQL query
    $sql = "SELECT * FROM admin_accounts WHERE admin_uid=?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $admin_uid);
    // Execute the query
    if ($stmt->execute()) {
        $result = $stmt->get_result();
        // Check if a record was found
        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            // Store the admin user information in the result array
            $adminUser['name'] = $row['name'];
            $adminUser['email'] = $row['email'];
            $adminUser['username'] = $row['username'];
            $adminUser['password'] = $row['password'];
            $adminUser['admin_uid'] = $row['admin_uid'];
        }
    } else {
        echo "Error executing query: " . $stmt->error;
    }
    // Close the statement
    $stmt->close();
    // Return the admin user information
    return $adminUser;
}

                /* ------------- UPDATE ADMIN USERS ------------- */

/* Ef smellt er á submit keyrist updateAdminUser */
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if($action == "edit" && $source == "admins" && $confirm == "confirm" && isset($admin_uid)) {
        updateAdminUser($admin_uid);
        header("Location: admins.php?message=User $username updated successfully.php");
    }
}
/* Uppfæra admin_accounts user info */
function updateAdminUser($admin_uid) {
    global $conn;
    if (isset($_POST["update"])) {
        /* Næ í upplýsingarnar úr POST fields */
        $name = $_POST["name"];
        $email = $_POST["email"];
        $username = $_POST["username"]; 
        $password = $_POST["password"];
        /* Undirbý sql query */
        $sql = "UPDATE admin_accounts SET name=?, email=?, username=?, password=? WHERE admin_uid=?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("sssss", $name, $email, $username, $password, $admin_uid);
        /* Framkvæmi */
        $stmt->execute();
        /* Ef gengur ekki þá error */
        if (!$stmt->execute()) {
            echo "Error updating admin user: " . $stmt->error;
            exit();
        }
        /* Loka */
        $stmt->close();
        
    }
}
/* ---------- EDIT ADMIN USER INPUT FIELDS HTML ------------ */
if ($action == 'edit' && $source == 'admins' && isset($_GET['admin_uid'])) {

    /* function sem sækir admin row úr database og setur info í adminUser */
    $adminUser = fetchAdminUser($admin_uid);

    echo '
    
    
    <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
        <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
            <!-- Container fyrir skipulag contents -->
            <div class="container-fluid">

            

                <!-- Row og col sem geymir Admin table -->
                <div class="row justify-content-center">
                    <div class="col-lg-6 col-12 d-lg-flex">

                        
                            <div class="card card-lg-width" style="margin-top: 12vw;">

                            <div class="card-header">
                            <h4 class="btn btn-dark btn-outline-secondary rounded-pill w-100 d-flex justify-content-center align-items-center center" style="width: 100%; height: 100%; font-size: 22px;">Breyta ' . $adminUser['name'] . '</h4>

                            </div>

                                <div class="card-body">
                                    <!-- Row -->
                                    <div class="row p-3 align-items-center justify-content-center"> 
                                        <div class="col">
                                            <h1></h1>
                                        </div>
                                    </div>

                                    <!-- Línan -->
                                    <hr class="my-horizontal-line">
                                    <form action="action.php?action=edit&source=admins&admin_uid=' . $admin_uid . '&confirm=confirm" method="POST" name="update">
                        

                                    <!-- Row og 2 cols -->
                                    <div class="row p-3 align-items-center"> 
                                        <div class="col-3">
                                            <label class="text-align" style="color: #CCCCCC;">Name:</label>
                                        </div>
                                        <div class="col-9" style="padding: 0;">
                                            <input class="form-control bg-dark-subtle" type="text" name="name" value="' . $adminUser['name'] . '" aria-label="default input example">  
                                        </div>
                                    </div>  
                                    <!-- Row og 2 cols -->
                                    <div class="row p-3 align-items-center"> 
                                        <div class="col-3">
                                            <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
                                        </div>
                                        <div class="col-9" style="padding: 0;">
                                            <input class="form-control bg-dark-subtle" type="text" name="email" value="' . $adminUser['email'] . '" aria-label="default input example">  
                                        </div>
                                    </div>  
                                    <!-- Row og 2 cols -->
                                    <div class="row p-3 align-items-center"> 
                                        <div class="col-3">
                                            <label class="text-align" style="color: #CCCCCC;">Username:</label>
                                        </div>
                                        <div class="col-9" style="padding: 0;">
                                            <input class="form-control bg-dark-subtle" type="text" name="username" value="' . $adminUser['username'] . '" aria-label="default input example" style="background-color: #F2F2F2;">
                                        </div>          
                                    </div>  
                                    <!-- Row og 2 cols -->
                                    <div class="row p-3 align-items-center"> 
                                        <div class="col-3">
                                            <label class="text-align" style="color: #CCCCCC;">Password:</label>
                                        </div>
                                        <div class="col-9" style="padding: 0;">
                                            <input class="form-control bg-dark-subtle" type="password" name="password" value="' . $adminUser['password'] . '" aria-label="default input example">
                                        </div>
                                    </div>

                                </div><!-- card-body -->
                        
                                <div class="card-footer pb-5 d-flex justify-content-center">
                                <!-- update takkinn -->
                                <button class="btn btn-outline-secondary" type="POST" name="update" style="width: 50%;">Update</button>
                                </div>
                            </div>
                        </form>
                
                    </div> <!-- col-12 admin users table -->
                </div><!-- row -->
            </div><!-- container-fluid -->
        </div> <!-- col-lg-10 col-12 -->
    
    ';
}



/* ------------------ DELETE ADMINS USER ----------------- */
function deleteAdminUser($admin_uid) {
    global $conn;
    $adminUser = fetchAdminUser($admin_uid);
    $admin_uid = $_GET['admin_uid'];

    $sql = "DELETE FROM admin_accounts WHERE admin_uid = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $admin_uid);
    $stmt->execute();
    if ($stmt->execute()) {
        header("Location: admins.php?message=User ". $adminUser['name'] ." has successfully been deleted.");
        exit(); 
    } else {
        header("Location: admins.php?message=Deletion was not successful.");
        exit();
    }
    $conn->close();
}

if ($action == 'delete' && $source == 'admins' && isset($_GET['admin_uid']) && isset($_GET['confirm'])) {
    deleteAdminUser($admin_uid);
    header("Location: admins.php?message=User ". $adminUser['name'] ." deleted successfully.php");
}
/* ---------- DELETE ADMINS ---------- */
if ($action == 'delete' && $source == 'admins' && isset($_GET['admin_uid'])) {
    echo '
    
    
    <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
        <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset vh-100 align-items-center" style="font-size: 13px;">
            <!-- Container fyrir skipulag contents -->
            <div class="container-fluid">  

                <!-- Row og col sem geymir Admin table -->
                <div class="row">
                    <div class="col-lg-6 col-12 d-lg-flex mx-auto">

                        
                            <div class="card card-lg-width" style="width: 100%;">

                                <div class="card-header bg-dark-subtle">
                                    
                                <h4 class="card-title text-center">Delete ' . $adminUser['name'] . ' ?</h4>
                                </div>

                                <div class="card-body mx-auto">

                                    <!-- Línan -->
                                    <hr class="my-horizontal-line">
                                    <!-- Línan -->
                                    <hr class="my-horizontal-line">
                                    <!-- Línan -->
                                    <hr class="my-horizontal-line">

                                    <a class="btn btn-danger btn-lg" href="action.php?action=delete&source=admins&admin_uid=' . $admin_uid . '&confirm=confirm">Delete</a>
                                    <a class="btn btn-secondary btn-lg" href="admins.php">Cancel</a>
                        
                                </div><!-- card-body -->
                        
                                <div class="card-footer pb-5 d-flex justify-content-center align-items-center">

                                </div>
                            </div>
                        </form>

                    </div> <!-- col-12 admin users table -->
                </div><!-- row -->
            </div><!-- container-fluid -->
        </div> <!-- col-lg-10 col-12 -->
    
    ';
}

// Redirect back to the appropriate page
/* 
if ($source === 'admins') {
    header("Location: admins.php");
} elseif ($source === 'users') {
    header("Location: users.php");
} 
 */
?>


