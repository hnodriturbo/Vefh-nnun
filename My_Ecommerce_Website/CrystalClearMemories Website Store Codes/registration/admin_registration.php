<?php
/* Góð leið til að prenta út hvað er inn í _POST */
/* 
echo "<pre>";
print_r($_POST);
echo "</pre>";
*/
    /* Innleiði database tengingu */
    include "../database.php";
    /* Innleiði sidebar og topnavbar inná síðuna */
    include "../sidebar.php";
    include "../topnavbar.php";
    $successMessage = "";
    //if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if(isset($_POST["submit"])) {
        if (empty($_POST["name"]) || empty($_POST["email"]) || empty($_POST["username"]) || empty($_POST["password"])) {
            exit("Values empty");
        }
        else {
            $stmt = $conn->prepare("INSERT INTO admin_accounts (name, email, username, password) VALUES (?, ?, ?, ?)");
            if ($stmt) {
                $password = password_hash($_POST["password"], PASSWORD_DEFAULT);
                $stmt->bind_param("ssss", $_POST["name"], $_POST["email"], $_POST["username"], $password);
                $stmt->execute();
    
                if ($stmt->error) {
                    echo "Villa kom upp: " . $stmt->errno . " - " . $stmt->error;
                }
                else {
                    $successMessage = "Til hamingju! Þú ert skráður með admin réttindi";
                }
            }        
            else {
                echo "Einhver villa hefur komið upp";
            }
            $stmt->close();
        }
    }
    else {
        "Einhver villa hefur komið upp";
    }
    $conn->close(); 
?>

<!-- ---------- Hér byrjar síðan ---------- -->


<!-- Container -->
<div class="container text-center flex-column" style="width:1000px" id="form-container">

    <!-- Hér byrjar formið -->
    <form action="" method="post" name="submit">

        <!-- Row -->
        <div class="row p-3 align-items-center justify-content-center"> 
            <div class="col">
                <h1>Admin Registration</h1>
            </div>
        </div>

        <!-- Línan -->
        <hr class="my-horizontal-line">

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Name:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="name" placeholder="Vinsamlegast sláðu inn nafnið þitt" aria-label="default input example">  
            </div>
        </div>  

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="email" placeholder="Vinsamlegast sláðu inn e-mailið þitt" aria-label="default input example">  
            </div>
        </div>  

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Username:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="username" placeholder="Veldu þér notendanafn" aria-label="default input example" style="background-color: #F2F2F2;">
            </div>          
        </div>  

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Password:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="password" name="password" placeholder="Veldu þér lykilorð" aria-label="default input example">
            </div>
        </div>

        <!-- Auka row fyrir bil -->
        <div class="row align-items-center">
            <br>
        </div>
        <!-- Row með submit takkanum -->
        <div class="row align-items-center">
            <div class="col">
            <input class="btn btn-primary" name="submit" type="submit" value="submit" style="width: 350px">
            </div>
        </div>
    </form>



<!-- Tókst skilaboðin -->

    <div class="row p-3 align-items-center" style="padding: 0;">
        <div class="col align-items-center" style="padding: 0;">
            <?php echo $successMessage; ?>
        </div>
    </div>
</div>



<!-- <div id="message" style="display: none;">Thank you for submitting!</div>
 -->