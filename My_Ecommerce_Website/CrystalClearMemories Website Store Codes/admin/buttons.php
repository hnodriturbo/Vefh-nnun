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
$base_url = "";
/* includa og bý til síðu */
include "database/database.php";
include "sidebar.php";
include "topnavbar.php";
include 'database/encryption_functions.php';

?>

 <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 16px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- BUTTON TESTING -->
        <div class="row vh-100 p-1 align-items-center justify-content-center center">
            <div class="col">
                <div class="row">

                    <div class="col-3">
                        <!-- JAVASCRIPT TOGGLE FROM BTN-DANGER TO BTN-OUTLINE DANGER AND BACK CONSTANTLY -->
                        <button id="toggle-btn-danger" class="btn btn-danger">JS btn-danger</button>
                    </div>
                    <div class="col-3">
                        <!-- JAVASCRIPT TOGGLE FROM BTN-SECONDARY TO BTN-OUTLINE SECONDARY AND BACK CONSTANTLY -->
                        <button id="toggle-btn-secondary" class="btn btn-secondary">JS btn-secondary</button>
                    </div>
                    <div class="col-3">
                        <!-- JAVASCRIPT TOGGLE FROM BTN-WARNING TO BTN-OUTLINE-WARNING AND BACK CONSTANTLY -->
                        <button id="toggle-btn-warning" class="btn btn-warning">JS btn-warning</button>
                    </div>
                    <div class="col-3">
                        <!-- JAVASCRIPT TOGGLE FROM BTN-DANGER TO BTN-OUTLINE DANGER AND BACK CONSTANTLY -->
                        <button id="toggle-btn-info" class="btn btn-info">JS btn-info</button>
                    </div>
                </div>
                <div class="row">


<div class="col-6">
    <!-- JAVASCRIPT TOGGLE FROM BTN-SECONDARY TO BTN-OUTLINE SECONDARY AND BACK CONSTANTLY -->
    <button id="toggle-btn-outline-warning" class="btn btn-outline-warning w-100">JS Delete Item</button>
</div>

</div>

                <div class="row">  
                    <br><br><br>
                </div>
                <div class="row">
                    <div class="col-12">
                        <!-- HÉRNA NOTA ÉG CSS EINGÖNGU TIL AÐ GERA GLOWING EFFECT MEÐ BOX SHADOW OG KEYFRAMES -->
                        <button class="btn btn-outline-info toggle-btn-outline-info-box-shadow w-75">
                            btn-outline-info keyframe box-shadow glowing
                        </button> 
                        <button class="btn btn-outline-secondary toggle-btn-outline-secondary-box-shadow w-75">
                            test outline secondary box shadow
                        </button>
                    </div>

                    <div class="row">  
                        <br><br><br>
                    </div> 

                    <div class="row">         
                    </div>

                    <div class="col-12">
                        <!-- TAKKI SEM TOGGLAR CSS BTN-INFO TIL BTN-OUTLINE INFO EN HÉR NOTA ÉG BARA KEYFRAMES CSS -->
                        <button class="btn btn-info toggle-btn-info-to-btn-outline-info w-75">Info Button</button>    
                    </div><!-- col-12 -->


                </div>
            </div>
        </div>
    </div>
</div>


<!-- ABSOLUTE NEED TO INCLUDE THE JS FILE AT THE END TO LOAD LAST -->
<script src="js/extras.js"></script>
<!-- AFTER INCLUDING THE FILE I CAN USE THE enableGlowing FUNCTION -->
<script>
    /* Each function is enabled using (buttonElement, defaultClass, alternateClass, interval) */
    enableGlowing(buttonDanger, 'btn-danger', 'btn-outline-danger', 1000);
    enableGlowing(buttonSecondary, 'btn-secondary', 'btn-outline-secondary', 500);
    enableGlowing(buttonWarning, 'btn-warning', 'btn-outline-warning', 1000);
    enableGlowing(buttonInfo, 'btn-info', 'btn-outline-info', 500);

    enableGlowing(buttonOutlineWarning, 'btn-outline-warning', 'btn-outline-info', 1500);
</script>




