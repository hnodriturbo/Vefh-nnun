            <!-- -------------- ADMIN SÍÐAN ---------------- -->
        <!-- --------------- HREIÐAR PÉTURSSON ---------------- -->
    <!-- --------------------------------------------------------- -->
<!-- --------------------------- MADE 2023 -------------------------- -->


<?php 


/* Validater */
function validate($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

/* These methods are typically used when retrieving multiple columns
or when you need to bind and fetch values for further processing.    
$stmt->store_result();
$stmt->bind_result($passwordHash);
$stmt->fetch();
*/

/* Functionið sem sækir hashaða lykilorðið í database útfrá username */
function fetchHashFromDatabase($username) {
    global $conn;
    /* sql skipun */
    $sql = "SELECT password FROM admin_accounts WHERE username = ?";
    /* undirbúningur  */
    $stmt = $conn->prepare($sql);
    /* Læsi breytuna inn í statementið */
    $stmt->bind_param("s", $username);
    /* framkvæmi */
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $stmt->close();
    /* Hægt að skila með if clause eða or clause */
    $password = $row['password'] ?? null;
    return $password;
}  
function checkIfUsernameExists($username) {
    global $conn;
    /* Telja hvað mörg rows eru til með tiltekið username */
    $sql = "SELECT COUNT(*) FROM admin_accounts WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    /* geyma niðurstöðu (meira notað þegar fetchað er multiple rows) */
    $stmt->store_result();
    $stmt->bind_result($count);
    $stmt->fetch();
    $stmt->close();
    // If at least one row was found, return true; otherwise, return false
    return $count > 0;

}

/* Bera saman hashaða lykilorðið við innslegið lykilorðið */
function validateLogin($username, $password) {
    $passwordHash = fetchHashFromDatabase($username);
    /* Ef passwordHash skilar lykilorði frá gagnagrunn og pass_verify matchar þau þá return true */
    if($passwordHash && password_verify($password, $passwordHash)) {
        return true;
    }
    return false;
}
/* Sækja admin row úr database og setja info í array */
function fetchAdminInfo($username) {
    global $conn;

    $sql = "SELECT * FROM admin_accounts WHERE username = ?";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();

    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $stmt->close();
    $adminInfo = array(
        'admin_id' => $row['admin_id'] ?? null,
        'name' => $row['name'] ?? null,
        'email' => $row['email'] ?? null,
        'username' => $row['username'] ?? null,
        'admin_uid' => $row['admin_uid'] ?? null
    );
    return $adminInfo;
}













?>