<?php 

/* define('SECRET_KEY', 'Hnodri2529!'); */
// Function to encrypt the order_unique_id
function encrypt_order_unique_id($order_unique_id) {
    return urlencode(base64_encode(openssl_encrypt($order_unique_id, "AES-128-ECB", SECRET_KEY)));
}
/* Function to decrypt the encrypted token and get the order_unique_id */
function decrypt_order_unique_id($encryptedToken) {
    return openssl_decrypt(base64_decode(urldecode($encryptedToken)), "AES-128-ECB", SECRET_KEY);
}


?>