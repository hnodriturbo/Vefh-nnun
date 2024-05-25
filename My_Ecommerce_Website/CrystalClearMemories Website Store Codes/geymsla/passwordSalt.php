<?php
// Function to generate a salted hash of a password
function generate_salt_and_hash($password) {
    // Generate a random salt
    $salt = bin2hex(random_bytes(16));
    
    // Hash the password with the generated salt
    $hashed_password = password_hash($password, PASSWORD_DEFAULT, ['salt' => $salt]);
    
    return array('salt' => $salt, 'hash' => $hashed_password);
}

// Function to verify a password against a stored salt and hash
function verify_password($password, $salt, $hashed_password) {
    // Generate a hash of the password attempt with the stored salt
    $hashed_attempt = password_hash($password, PASSWORD_DEFAULT, ['salt' => $salt]);
    
    // Compare the stored hash with the newly generated hash
    return password_verify($hashed_attempt, $hashed_password);
}

// Example usage
$password = "mysecretpassword";

// Generate a salted hash of the password
$password_data = generate_salt_and_hash($password);

// Print the salt and hashed password
echo "Salt: " . $password_data['salt'] . "\n";
echo "Hashed Password: " . $password_data['hash'] . "\n";

// Verify a password attempt
$password_attempt = "wrongpassword";

// Verify the password attempt against the stored salt and hash
$password_matched = verify_password($password_attempt, $password_data['salt'], $password_data['hash']);

// Print the result
if ($password_matched) {
    echo "Password matched!";
} else {
    echo "Password did not match!";
}

/* ----------------------------------------------------------------------------- */

// Assuming you have established a database connection

// Generate a salted hash of the password
function generate_salt_and_hash($password) {
    // Generate a random salt
    $salt = bin2hex(random_bytes(16));

    // Hash the password with the generated salt
    $hashed_password = password_hash($password, PASSWORD_DEFAULT, ['salt' => $salt]);

    return array('salt' => $salt, 'hash' => $hashed_password);
}

// Store the salt and hashed password in the database
function store_password($username, $password) {
    $password_data = generate_salt_and_hash($password);
    $salt = $password_data['salt'];
    $hashed_password = $password_data['hash'];

    // Insert the salt and hashed password into the database
    $query = "INSERT INTO users (username, salt, hashed_password) VALUES (?, ?, ?)";
    $stmt = $pdo->prepare($query);
    $stmt->execute([$username, $salt, $hashed_password]);
}

// Retrieve the salt and hashed password from the database
function retrieve_password($username, $password) {
    // Retrieve the salt and hashed password from the database
    $query = "SELECT salt, hashed_password FROM users WHERE username = ?";
    $stmt = $pdo->prepare($query);
    $stmt->execute([$username]);
    $row = $stmt->fetch();

    if ($row) {
        $salt = $row['salt'];
        $hashed_password = $row['hashed_password'];

        // Verify the password attempt against the stored salt and hash
        return verify_password($password, $salt, $hashed_password);
    }

    return false;
}


?>
