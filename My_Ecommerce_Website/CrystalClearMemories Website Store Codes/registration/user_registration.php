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
        if (empty($_POST["firstname"]) || empty($_POST["lastname"]) || empty($_POST["email"]) || empty($_POST["username"] || empty($_POST["password"]))) {
            exit("Values empty");
        } 
        else {
            $firstname = $_POST["firstname"];
            $lastname = $_POST["lastname"];
            $email = $_POST["email"];
            $username = $_POST["username"];
            $password = password_hash($_POST["password"], PASSWORD_DEFAULT);
            // variable = condition ? value_if_true : value_if_false
            $address = !empty($_POST["address"]) ? $_POST["address"] : null;
            $address2 = !empty($_POST["address2"]) ? $_POST["address2"] : null;
            $postalcode = !empty($_POST["postalcode"]) ? $_POST["postalcode"] : null;
            $city = !empty($_POST["city"]) ? $_POST["city"] : null;
            $country = !empty($_POST["country"]) ? $_POST["country"] : null;
            $other = !empty($_POST["other"]) ? $_POST["other"] : null;

            $stmt = $conn->prepare("INSERT INTO users (firstname, lastname, email, username, password, address, address2, postalcode, city, country, other) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
            if ($stmt) {
                $password = password_hash($_POST["password"], PASSWORD_DEFAULT);
                $stmt->bind_param("sssssssssss", $firstname, $lastname, $email, $username, $password, $address, $address2, $postalcode, $city, $country, $other);
                $stmt->execute();
    
                if ($stmt->error) {
                    echo "Villa kom upp: " . $stmt->errno . " - " . $stmt->error;
                }
                else {
                    $successMessage = "Til hamingju! Þú ert skráður notandi";
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
                <h1>Register</h1>
            </div>
        </div>

        <!-- Línan -->
        <hr class="my-horizontal-line">

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 

            <div class="col-1">
                <label class="text-align" style="color: #CCCCCC;">Firstname:</label>
            </div>
            <div class="col-5" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="firstname" placeholder="Type your firstname" aria-label="default input example">  
            </div>
            <div class="col-1">
                <label class="text-align" style="color: #CCCCCC;">Lastname:</label>
            </div>
            <div class="col-5" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="lastname" placeholder="Type your lastname" aria-label="default input example">  
            </div>

        </div>  

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="email" placeholder="Please type your email" aria-label="default input example">  
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

        
        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Address:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="address" placeholder="Type your address" aria-label="default input example">
            </div>
        </div>

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Address 2:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="address2" placeholder="Address 2" aria-label="default input example">
            </div>
        </div>

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Postal Code:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="postalcode" placeholder="Type your postalcode" aria-label="default input example">
            </div>
        </div>    

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">City:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="city" placeholder="Type your city" aria-label="default input example">
            </div>
        </div>

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Country:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="country" placeholder="Type your country" aria-label="default input example">
            </div>
        </div>

        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Other Information:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="other" placeholder="Other information" aria-label="default input example">
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