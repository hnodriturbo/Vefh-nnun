<?php 

/* Generate cart unique uuid */
function generateUUID()
{
    return sprintf('%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
        mt_rand(0, 0xffff), mt_rand(0, 0xffff), mt_rand(0, 0xffff),
        mt_rand(0, 0x0fff) | 0x4000, mt_rand(0, 0x3fff) | 0x8000,
        mt_rand(0, 0xffff), mt_rand(0, 0xffff), mt_rand(0, 0xffff)
    );
}

// Usage:
$cartUniqueId = generateUUID();


/* 
In a web application, you need to maintain the cart_unique_id value across multiple 
requests so that you can access the same cart throughout the user's browsing session. 
There are several ways to achieve this:

Session Storage: You can store the cart_unique_id in a session variable on the server-side. 
Sessions provide a way to store user-specific information that can be accessed across 
different page requests. Each user will have their own session, and you can use the session 
variable to keep track of the cart_unique_id for that particular user.

Cookies: You can also store the cart_unique_id in a cookie on the user's browser. 
Cookies are small pieces of data that are stored on the user's device and sent back to the 
server with each request. By setting a cookie with the cart_unique_id, you can access it on 
subsequent page requests and maintain the same cart for that user.

Here's an example of how you can use sessions or cookies in PHP to maintain the 
cart_unique_id value:
 */



/* Using Sessions: */
// Start the session
session_start();

// Check if the cart_unique_id is already set in the session
if (!isset($_SESSION['cart_unique_id'])) {
    // Generate a new cart_unique_id
    $cartUniqueId = generateUUID();

    // Store the cart_unique_id in the session
    $_SESSION['cart_unique_id'] = $cartUniqueId;
} else {
    // Retrieve the cart_unique_id from the session
    $cartUniqueId = $_SESSION['cart_unique_id'];
}



/* Using Cookies: */
// Check if the cart_unique_id cookie is already set
if (!isset($_COOKIE['cart_unique_id'])) {
    // Generate a new cart_unique_id
    $cartUniqueId = generateUUID();

    // Set the cart_unique_id cookie with an expiration time (e.g., 1 day)
    setcookie('cart_unique_id', $cartUniqueId, time() + 86400, '/');
} else {
    // Retrieve the cart_unique_id from the cookie
    $cartUniqueId = $_COOKIE['cart_unique_id'];
}
/* 
In both cases, the generateUUID() function generates a new UUID that will be used as 
the cart_unique_id for the user's cart. The function ensures that the same UUID is 
not generated twice, providing uniqueness.

Using sessions or cookies allows you to maintain the cart_unique_id value across 
different page requests, ensuring that the user's cart remains consistent during 
their browsing session.
 */


?>