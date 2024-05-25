<?php 
session_start();

include "../database/database.php";

// unset all of the session variables
$_SESSION = array();

// delete the session cookie
if(isset($_COOKIE[session_name()])) {
    setcookie(session_name(), '', time() - 3600, '/');
}

// Destroy the session
session_destroy();

echo "<h1>You have been logged out</h1>";
header("refresh:3;url=login.php");
exit();

?>