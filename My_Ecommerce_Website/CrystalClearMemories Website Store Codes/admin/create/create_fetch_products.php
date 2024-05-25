<?php
require '../database/database.php'; // Include the database
require 'create_functions.php'; // Use the fetchProductsByCategory function that is inside this file

header('Content-Type: application/json');

// Check if product_id is posted
if (isset($_POST['product_id'])) {
    $productId = $_POST['product_id'];
    $product = fetchProductById($productId);
    echo json_encode($product);
}
// Otherwise, check if category_id is posted
elseif (isset($_POST['category_id'])) {
    $categoryId = $_POST['category_id'];
    $products = fetchProductsByCategory($categoryId);
    echo json_encode($products);
} 
// If neither is set, return an empty array
else {
    echo json_encode([]);
}
?>
