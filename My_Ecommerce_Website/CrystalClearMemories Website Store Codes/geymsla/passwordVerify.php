<?php
/* Að ná í hashað password úr database */
function getHashFromDatabase($username) {
    // Assuming you have already established a MySQLi database connection
    $conn = new mysqli('localhost', 'your_username', 'your_password', 'your_database');

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare a query to retrieve the hash based on the provided username
    $query = "SELECT password_hash FROM users WHERE username = ?";
    $statement = $conn->prepare($query);

    // Bind the parameter to the prepared statement
    $statement->bind_param("s", $username);

    // Execute the statement
    $statement->execute();

    // Store the result
    $statement->store_result();

    // Fetch the result (assuming there's only one matching row)
    $statement->bind_result($passwordHash);
    $statement->fetch();

    // Close the statement and database connection
    $statement->close();
    $conn->close();

    // If a row was found, return the hash; otherwise, return null
    if ($passwordHash) {
        return $passwordHash;
    } else {
        return null;
    }
}

/* Að verifya password  */

function verifyLogin($username, $password) {
    // Assuming you have already established a MySQLi database connection
    $conn = new mysqli('localhost', 'your_username', 'your_password', 'your_database');

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare a query to retrieve the hash based on the provided username
    $query = "SELECT password_hash FROM users WHERE username = ?";
    $statement = $conn->prepare($query);

    // Bind the parameter to the prepared statement
    $statement->bind_param("s", $username);

    // Execute the statement
    $statement->execute();

    // Store the result
    $statement->store_result();

    // Fetch the result (assuming there's only one matching row)
    $statement->bind_result($passwordHash);
    $statement->fetch();

    // Close the statement and database connection
    $statement->close();
    $conn->close();

    // If a row was found, verify the password
    if ($passwordHash && password_verify($password, $passwordHash)) {
        // Password is correct, login successful
        return true;
    }

    // If no row was found or password verification failed, login unsuccessful
    return false;
}

// Usage example
$username = $_POST['username'];
$password = $_POST['password'];

if (verifyLogin($username, $password)) {
    // Login successful, perform further actions (e.g., session management, redirecting to a dashboard, etc.)
    echo "Login successful!";
} else {
    // Login unsuccessful, handle the error (e.g., display an error message, redirect back to the login page, etc.)
    echo "Invalid username or password.";
}



/* ------------- VALIDATE - CHECKUSERNAME - PASSWORD VERIFY */
if (isset($_POST['username']) && isset($_POST['password'])) {
    function validate($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    $username = validate($_POST['username']);
    $password = validate($_POST['password']);

    if (empty($username)) {
        header("Location: login.php?error=username_is_required");
        exit();
    } elseif (empty($password)) {
        header("Location: login.php?error=password_is_required");
        exit();
    }

    function fetchHashFromDatabase($username) {
        global $conn;

        /* SQL query */
        $sql = "SELECT password_hash FROM admin_accounts WHERE username = ?";
        
        /* Prepare statement */
        $stmt = $conn->prepare($sql);
        
        /* Bind the parameter */
        $stmt->bind_param("s", $username);
        
        /* Execute the statement */
        $stmt->execute();

        /* Store the result */
        $stmt->store_result();

        /* Bind the result to a variable */
        $stmt->bind_result($passwordHash);
        $stmt->fetch();

        $stmt->close();
        $conn->close();

        if ($passwordHash) {
            return $passwordHash;
        } else {
            return null;
        }
    }   

    function checkIfUsernameExists($username) {
        global $conn;

        /* Count the number of rows with the given username */
        $sql = "SELECT COUNT(*) FROM admin_accounts WHERE username = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();
        $stmt->bind_result($count);
        $stmt->fetch();

        $stmt->close();
        $conn->close();

        // If at least one row was found, return true; otherwise, return false
        if ($count > 0) {
            return true;
        }
        return false;
    }

    function validateLogin($username, $password) {
        $passwordHash = fetchHashFromDatabase($username);
        if ($passwordHash && password_verify($password, $passwordHash)) {
            return true;
        }
        return false;
    }

    // Usage example
    if (validateLogin($username, $password)) {
        // Login successful, perform further actions (e.g., session management, redirecting to a dashboard, etc.)
        echo "Login successful!";
    } else {
        // Login unsuccessful, handle the error (e.g., display an error message, redirect back to the login page, etc.)
        echo "Invalid username or password.";
    }
}


?>