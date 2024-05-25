<?php 
    /* -------------- HREIÐAR PÉTURSSON -------------- */
   /* ------------------------------------------------- */
  /* --------------------------------------------------- */
 /* ---------- MY FUNCTIONS FOR ADDING STUFF ------------ */
/* ------------------------------------------------------- */

require_once '../database/database.php';


function addToOrdersTable($order_info) {
    global $conn; 

    // Ensure all keys are set, set to NULL otherwise
    $keys = ['user_id', 'firstname', 'lastname', 'email', 'address', 'address2', 'postalcode', 'city', 'state', 'country', 'final_price', 'order_status'];
    foreach($keys as $key) {
        if(!isset($order_info[$key]) || empty($order_info[$key])) {
            $order_info[$key] = null;
        }
    }

    $sql = "INSERT INTO orders (user_id, firstname, lastname, email, address, address2, postalcode, city, state, country, final_price, order_status) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    $stmt = $conn->prepare($sql);

    if (!$stmt) {
        // handle error, for example:
        die("Failed to prepare statement: " . $conn->error);
    }

    $types = "isssssisssis";
    $stmt->bind_param($types, ...array_values($order_info));

    $executed = $stmt->execute(); // This will return true on success, false on failure
    $stmt->close();

    return $executed;
}

function getCategories() {
    global $conn;
    $sql = "SELECT * FROM categories";
    $result = mysqli_query($conn, $sql);

    $categories = [];
    while ($row = mysqli_fetch_assoc($result)) {
        $categories[] = $row;
    }
    return $categories;

}
function fetchProductsByCategory($category_id) {
    global $conn;
    
    $sql = "SELECT * FROM products WHERE category_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, 'i', $category_id);
    mysqli_stmt_execute($stmt);
    
    $result = mysqli_stmt_get_result($stmt);
    $products = mysqli_fetch_all($result, MYSQLI_ASSOC);
    
    mysqli_stmt_close($stmt);
    
    return $products;
}
function fetchProductById($productId) {
    global $conn;

    // SQL query to fetch product by ID
    $sql = "SELECT * FROM products WHERE product_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, 'i', $productId);
    mysqli_stmt_execute($stmt);

    $result = mysqli_stmt_get_result($stmt);
    $product = mysqli_fetch_assoc($result);

    mysqli_stmt_close($stmt);

    return $product;
}


/************************************************************
 * Orders Table:
 * =============
 * order_id:         Automatically generated, Non-nullable.
 * order_unique_id:  Automatically generated, Non-nullable.
 * user_id:          Nullable.
 * firstname:        Non-nullable.
 * lastname:         Non-nullable.
 * email:            Non-nullable.
 * address:          Nullable.
 * address2:         Nullable.
 * postalcode:       Nullable.
 * city:             Nullable.
 * state:            Non-nullable.
 * country:          Nullable.
 * final_price:      Sums all total_price columns from related rows in order_items. Non-nullable.
 * created_at:       Automatically generated, Non-nullable.
 * order_status:     Non-nullable.
 *
 * Order Items Table:
 * ==================
 * order_items_id:   Automatically generated, Non-nullable.
 * order_unique_id:  Referencing order_unique_id in orders table, Non-nullable.
 * order_id:         Non-nullable.
 * product_id:       Non-nullable.
 * quantity:         Non-nullable.
 * price:            Nullable, but if not provided during insertion, fetched from the 'products' table based on product_id.
 * total_price:      Calculation of quantity and price columns, Non-nullable.
 *
 * Triggers:
 * =========
 * 1. Before inserting into order_items, if no price is provided, fetch it from the 'products' table and always compute the 'total_price'.
 * 2. After any modification (insert, delete, update) in order_items, the 'final_price' column in 'orders' table is updated to reflect the sum of 'total_price' from all related order_items.
 */


/**************************************************//*
 * TRIGGERS OVERVIEW:
 * ---------------------------
 * 
 * 1. before_order_item_insert:
 * - If no price is provided during insertion, fetches the standard product price.
 * - If a price is manually provided (e.g., for a discount), it uses the manually provided price.
 * - Always calculates total_price (quantity * price).
 * 
 * 2. before_order_item_update:
 * - If quantity or price changes, recalculates total_price.
 * 
 * 3. after_order_item_insert, after_order_item_update, and after_order_item_delete:
 * - Recalculates final_price in orders table based on the summed total_price of related items in order_items table.
 */






















?>