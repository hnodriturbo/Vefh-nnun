              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


<?php 

/* Function to retrive admin users */
function getAdminUsers() {
    global $conn;
    $stmt = $conn->prepare("SELECT * FROM admin_accounts LIMIT 10");
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
        echo "<td>$admin_password</td>";
        echo "<td>$admin_uid</td>";
        echo "</tr>";
    }
}



/* Function to retrive users */
function getUsers() {
    global $conn;
    $stmt = $conn->prepare("SELECT * FROM users LIMIT 10");
    $stmt->execute();
    $result = $stmt->get_result();
    while($row = $result->fetch_assoc()) {
        $user_id = $row['user_id'];
        $firstname = $row['firstname'];
        $lastname = $row['lastname'];
        $email = $row['email'];
        $username = $row['username'];
        $password = $row['password'];
        $address = $row['address'];
        $address2 = $row['address2'];
        $postalcode = $row['postalcode'];
        $city = $row['city'];
        $country = $row['country'];
        $other = $row['other'];
        
        echo "<tr>";
        echo "<td>$user_id</td>";
        echo "<td>$firstname</td>";
        echo "<td>$lastname</td>";
        echo "<td>$email</td>";
        echo "<td>$username</td>";
        echo "<td>$address</td>";
        echo "<td>$address2</td>";
        echo "<td>$postalcode</td>";
        echo "<td>$city</td>";
        echo "<td>$country</td>";
        echo "<td>$other</td>";
        echo "</tr>";
    }
}


/* Function to retrive logs */
function getLogs() {
    global $conn;

    $stmt = $conn->prepare("SELECT * FROM logs LIMIT 10");

    $stmt->execute();

    $result = $stmt->get_result();

    while($row = $result->fetch_assoc()) {
        $logs_id = $row['logs_id'];
        $user_id = $row['user_id'];
        $action = $row['action'];
        $date = $row['date'];

        echo "<tr>";
        echo "<td>$logs_id</td>";
        echo "<td>$user_id</td>";
        echo "<td>$action</td>";
        echo "<td>$date</td>";
        echo "</tr>";
    }
}


/* Function to retrive products */
function getProducts() {
    global $conn;
    /* undirbý tengingu */
    $stmt = $conn->prepare("SELECT * FROM products LIMIT 10");
    if (!$stmt) {
        echo "error in preparing the query: " . $conn->error;
        return;
    }
    /* executa queryið */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }
    $result = $stmt->get_result();
    if($result->num_rows === 0) {
        echo "no rows found";
    }
    while($row = $result->fetch_assoc()) {
        $product_id = $row['product_id'];
        $image = $row['image'];
        $name = $row['name'];
        $description = $row['description'];
        $price = $row['price'];
        $category_id = $row['category_id'];

        echo "<tr>";
        echo "<td>$product_id</td>";
        echo "<td>$image</td>";
        echo "<td>$name</td>";
        echo "<td>$description</td>";
        echo "<td>$price</td>";
        echo "<td>$category_id</td>";
        echo "</tr>";
    }
}



?>