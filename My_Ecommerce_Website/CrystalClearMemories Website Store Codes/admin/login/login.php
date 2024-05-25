              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


<?php 
ob_start();
session_start();

$base_url = "../";
/* Includa */
/* C:\Users\hreis\OneDrive\Desktop\Skóli\Forritun\vefverslun\admin\login\login_functions.php
 */
include_once "login_functions.php";
include_once "../database/database.php";
include_once "../topnavbar.php";

echo "<br><br><br><br><br>" . $_SESSION['requested_url'];

/* If error comes through the url retrive it and store in $error */
$error = $_GET['error'] ?? '';

$page_state = 'default';

/* If the submit button is pressed then do this */
if($_SERVER["REQUEST_METHOD"] == "POST") {
    if(isset($_POST['username']) && isset($_POST['password'])) {
        $username = validate($_POST['username']);
        $password = validate($_POST['password']);
        }
        if(empty($username)) {
            $page_state = 'login_error';
            $error = 'Username is required !';
           /*  include_once "login_form.php"; */
            /* header("Location: login.php?error=username is required"); */
            
        }

        /* kemur password you entered is not correct þegar password field er empty.. ? */
        else if(empty($password)) {
            $page_state = 'login_error';
            $error = 'Password is required !';   
            
        }

        if(checkIfUsernameExists($username)) {
            /* Fetch password */
            $hashedPassword = fetchHashFromDatabase($username);
            
            /* Validate the login credentials */
            if(validateLogin($username, $password)) {

                /* Sæki admin row með fetchAdmin og set í adminInfo */
                $adminInfo = fetchAdminInfo($username);

                /* Set session and cookies with admin_uid and login date */
                $_SESSION['admin_uid'] = $adminInfo['admin_uid'];

                $_SESSION['login_date'] = date("Y-m-d H:i:s");
                $cookie_expiry = time() + 3600; /* Ein klst er 3600 sek */

                /* Set cookies */
                setcookie('admin_uid', $adminInfo['admin_uid'], $cookie_expiry);
                setcookie('username', $username, $cookie_expiry);
                setcookie('name', $adminInfo['name'], $cookie_expiry);
                setcookie('login_date', $_SESSION['login_date'], $cookie_expiry);

                $page_state = 'logged_in';
            } 
            else {
                $page_state = 'login_error';
                $error = 'Password you entered is not correct';
            }
        } 
        else {
            /* notendanafn er ekki til */
            $page_state = 'login_error';
            $error = 'Username does not exist !';
        }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap icons -->
    <link href="<?php echo "$base_url" ?>img/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="<?php echo "$base_url" ?>../../bootstrap/dist/css/bootstrap.min.css">
    <!-- Mitt eigið CSS -->
    <link rel='stylesheet' type='text/css' media='screen' href='<?php echo "$base_url" ?>css/sass.css'>
    <link rel='stylesheet' type='text/css' media='screen' href='<?php echo "$base_url" ?>css/mystyle.css'>
    <link rel='stylesheet' type='text/css' media='screen' href='<?php echo "$base_url" ?>css/buttons.css'>
    <!-- Notast við base_url í javascript líka -->
    <script> let base_url = '<?php echo $base_url; ?>'; </script>   
    <!-- Bootstrap og jquery -->
    <script src="<?php echo "$base_url"; ?>js/bootstrap.bundle.js"></script>
    <script src="<?php echo "$base_url"; ?>js/jquery.js"></script>
    <script src="<?php echo "$base_url"; ?>js/extras.js"></script>
    <script src="<?php echo "$base_url"; ?>js/breadcrumbs.js"></script>
    <!-- Bý til font class -->
    <style>
      /* Font-face and custom-text styles */
      @font-face {
      font-family: 'kirstyBoldItalic';
      src: url('<?php echo "$base_url" ?>font/kirsty/kirsty_bd_it.otf') format('opentype');
      }
      .kirsty-bold-italic {
      font-family: 'kirstyBoldItalic', sans-serif;
      }
    </style>
    <!-- Titill síðunnar -->
    <title>Admin - Crystal Clear Memories</title>
</head>
<body>
<!-- Container fyrir skipulag contents -->
<div class="container-fluid kirsty-bold-italic">
<!-- Row og col sem geymir Admin table -->
<div class="row vh-100 justify-content-center align-items-center">
<div class="col-lg-8 col-12">
<div class="row justify-content-center">
<div class="col-12">
    <?php switch ($page_state):
        case 'logged_in': ?>
            <h1 class="whitetext center">You have been logged in</h1>
            <?php   
                // Redirect the user back to the original requested page
                if (isset($_SESSION['requested_url'])) {
                    $redirect_url = $_SESSION['requested_url'];
                    unset($_SESSION['requested_url']);
                    header("Refresh: 3; url=" . $redirect_url);
                    exit();
                } else {
                    // If no url was set, then redirect to index.php
                    header("refresh:3;url=" . $base_url . "index.php");
                    exit();
                }
            break;
        case 'login_error':
            include_once "login_form.php";
            break;
        default:
            include_once "login_form.php";
            break;
        endswitch; ?>
</div><!-- col -->
</div><!-- row -->
<!-- Hérna eru villuskilaboðin -->
<?php if (!empty($error)) {
        echo '
        <div class="row justify-content-center">
            <div class="col-8">
                <div class="alert alert-danger center" role="alert">
                    ' . $error . '
                </div>
            </div>
        </div>
        ';
} 
?>
</div> <!-- col-lg-8 col-12 d-lg-flex -->
</div><!-- row -->
</div><!-- container-fluid -->
</body>