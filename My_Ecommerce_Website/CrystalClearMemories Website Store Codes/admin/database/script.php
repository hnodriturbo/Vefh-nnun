<?php
// Include the database connection file
require_once 'database.php';


// Check the connection
if (!$conn) {
    die("Database connection failed: " . mysqli_connect_error());
}

// Function to generate random values for quantity and price
function getRandomQuantity()
{
    return rand(1, 3);
}

function getRandomPrice()
{
    return rand(15000, 30000);
}

// Query to fetch orders from the "orders" table
$sql = "SELECT order_id, order_unique_id FROM orders";
$result = mysqli_query($conn, $sql);

if ($result) {
    while ($row = mysqli_fetch_assoc($result)) {
        $order_id = $row['order_id'];
        $order_unique_id = $row['order_unique_id'];

        // Generate two rows for each order
        for ($i = 0; $i < 2; $i++) {
            $product_id = rand(1, 7);
            $quantity = getRandomQuantity();
            $price = getRandomPrice();

            // Insert rows into "order_items" table
            $insert_sql = "INSERT INTO order_items (order_unique_id, order_id, product_id, quantity, price)
                           VALUES ('$order_unique_id', $order_id, $product_id, $quantity, $price)";

            $insert_result = mysqli_query($conn, $insert_sql);

            if (!$insert_result) {
                echo "Error inserting data: " . mysqli_error($conn);
            }
        }
    }
} else {
    echo "Error fetching data: " . mysqli_error($conn);
}

// Close the database connection
mysqli_close($conn);
?>
