<?php 




/* --------------- FUNCTIONS FYRIR USERS.PHP --------------- */

/* Get Paginated Users Function */
function getPaginatedUsers($page, $perPage) {
    global $conn;
    // Finna út hvað margar rows skal skippa áður en náð er í tíu rows
    $offset = ($page - 1) * $perPage;
    /* Undirbý stmt, vel úr users         LIMIT startRow limit */
    $stmt = $conn->prepare("SELECT * FROM users LIMIT ?, ?");
    if (!$stmt) {
        echo "Error in preparing the query: " . $conn->error;
        return;
    }
    /* Bind the parameters */
    $stmt->bind_param('ii', $offset, $perPage);
    /* Keyri statementið */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }
    /* næ í niðurstöður */
    $result = $stmt->get_result();
    /* Athuga hvort niðurstöður hafi komið */
    if ($result->num_rows === 0) {
        echo "no rows found";
    }
    /* Keyri í gegnum result með row = $result->fetch_assoc() */
    while ($row = $result->fetch_assoc()) {
        /* set hvern column úr row í breytur */
        $user_id = $row['user_id'];
        $user_uid = $row['user_uid'];
        $firstname = $row['firstname'];
        $lastname = $row['lastname'];
        $email = $row['email'];
        $username = $row['username'];
        $city = $row['city'];
        $country = $row['country'];
        $other = $row['other'];

        echo "<tr>";
        echo "<td>$user_id</td>";
        echo "<td>$firstname</td>";
        echo "<td>$lastname</td>";
        echo "<td>$email</td>";
        echo "<td>$username</td>";
        echo "<td>$city</td>";
        echo "<td>$country</td>";
        echo "<td>$other</td>";
        echo "<td><a class='btn btn-secondary custom-btn' href='useraction.php?action=view&source=users&user_uid=" . $user_uid . "'> View </a></td>";
        echo "<td><a class='btn btn-danger custom-btn' href='useraction.php?action=delete&source=users&user_uid=" . $user_uid . "'> Delete </a></td>";
        echo "</tr>";
    }
}

//Function sem telur total rows úr users
function countUsers() {
    global $conn;
    $stmt = $conn->prepare("SELECT count(*) FROM users");
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    $count = $row[0];
    return $count;
}


/* --------------- FUNCTIONS FYRIR USERACTION.PHP --------------- */

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
    /* Bind the parameters */
    $stmt->bind_param('s', $user_uid);
    /* Keyri stmt */
    if($stmt->execute()) {
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
            echo "sql execution failed: " . $stmt->error;
        }
    }
    /* Close the stmt */
    $stmt->close();
    /* Returna arrayinu með userInfo */
    return $userInfo;
}

/* Update User Info Function */
function updateUserInfo($user_uid) {
    global $conn;
    if(isset($_POST['update'])) {
        /* Ná í allt info í gegnum post */
        $firstname = $_POST['firstname'];
        $lastname = $_POST['lastname'];
        $email = $_POST["email"];
        $username = $_POST["username"]; 
        $password = $_POST["password"];
        $address = $_POST["address"];
        $address2 = $_POST["address2"];
        $postalcode = $_POST["postalcode"];
        $city = $_POST["city"];
        $country = $_POST["country"];
        $other = $_POST["other"];

        $sql = "UPDATE users SET firstname=?, lastname=?, email=?, username=?, password=?, address=?, address2=?, postalcode=?, city=?, country=?. other=?";

        $stmt = $conn->prepare($sql);
        $stmt->bind_param("sssssssssss", $firstname, $lastname, $email, $username, $password, $adddress, $address2, $postalcode, $city, $country, $other);
        if($stmt->execute()) {
            return true;
        } else {
            echo "sql query error: " . $stmt->error;
        }
    $stmt->close();
    }
}


/*----------- delete user --------*/
function deleteUser($user_uid) {
    global $conn;
    $userInfo = fetchUserInfo($user_uid);

    // Debug statement to check user_uid
    echo "Deleting user with user_uid: " . $user_uid . "<br>";

    $sql = "DELETE FROM users WHERE user_uid = ?";

    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        echo "error: " . $conn->error;
        return false;
    }
    $stmt->bind_param("s", $user_uid);

    if($stmt->execute()) {
        $stmt->close();
        echo "User deleted successfully<br>"; // Debug statement
        return true;
    } else {
        echo "error in executing the query: " . $stmt->error;
        return false;
    }
    $conn->close();
}





?>