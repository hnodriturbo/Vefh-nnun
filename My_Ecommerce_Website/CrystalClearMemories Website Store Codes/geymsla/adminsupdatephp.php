<?php 
$name = "";
$email = "";
$username = "";
$password = "";
$admin_uid = "";

/* Uppfæra database info */
if (isset($_GET['admin_id'])) {
    $admin_id = $_GET['admin_id'];

    if (isset($_POST["update"])) {
        if (empty($_POST["name"]) || empty($_POST["email"]) || empty($_POST["username"]) || empty($_POST["password"])) {
            exit("Values empty");
        } else {
            $name = $_POST["name"];
            $email = $_POST["email"];
            $username = $_POST["username"]; 
            $password = $_POST["password"];

            $sql = "UPDATE `admin_accounts` SET `name`=?, `email`=?, `username`=?, `password`=? WHERE `admin_id`=?";
        
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("ssssi", $name, $email, $username, $password, $admin_id);

            if ($stmt->execute()) {
                header("Location: admins.php");
            } else {
                echo "Error updating record: " . $stmt->error;
            }
        }
    }
} else {
    echo "admin_id er ekki í URL-inu";
}


/* function sem fetchar user og setur í array */
function fetchUserInfo($user_uid) {
    /* Opna tengingu */
    global $conn;
    /* Bý til tómt array */
    $userInfo = array();
    /* Prepare the query */
    $sql = "SELECT * FROM users WHERE user_uid = ?";
    /* Prepare the statement */
    $stmt = $conn->prepare($sql);
    /* Check if the statement was prepared successfully */
    if (!$stmt) {
        echo "Error in preparing statement: " . $conn->error;
        return $userInfo; // Return an empty array on failure
    }
    /* Bind the parameter */
    $stmt->bind_param('s', $user_uid);
    /* Execute the statement */
    if ($stmt->execute()) {
        /* Sæki niðurstöðu með stmt og set í $result */
        $result = $stmt->get_result();
        // check if a row is returned
        if ($result->num_rows > 0) {
            /* Fetcha niðurstöðuna og set í $row */
            $row = $result->fetch_assoc();
            /* Geymi svo user info í array */
            $userInfo['firstname'] = $row['firstname'];
            $userInfo['lastname'] = $row['lastname'];
            $userInfo['email'] = $row['email'];
            $userInfo['username'] = $row['username'];
            $userInfo['password'] = $row['password'];
            $userInfo['address'] = $row['address'];
            $userInfo['address2'] = $row['address2'];
            $userInfo['postalcode'] = $row['postalcode'];
            $userInfo['city'] = $row['city'];
            $userInfo['country'] = $row['country'];
            $userInfo['other'] = $row['other'];
        } else {
            echo "No user found with user_uid: " . $user_uid;
        }
    } else {
        echo "SQL execution failed: " . $stmt->error;
    }
    /* Close the stmt */
    $stmt->close();
    /* Return the array with userInfo */
    return $userInfo;
}

?>