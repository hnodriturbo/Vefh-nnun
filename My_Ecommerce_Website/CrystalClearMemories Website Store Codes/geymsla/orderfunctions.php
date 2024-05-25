<?php 


/* ----- GET INFO FROM ORDER_ITEMS TABLE ----- */
function getOrderItems($order_unique_id) {
    global $conn;
    // Validate and sanitize the input to prevent SQL injection
    /* $order_unique_id = mysqli_real_escape_string($conn, $order_unique_id); */
    $sql = "SELECT * FROM order_items WHERE order_unique_id = ?";
    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        echo "error in preparing the query: " . $conn->error;
    }
    /* Bind parameters and execute the stmt */
    $stmt->bind_param("s", $order_unique_id);
    $stmt->execute();
    /* check for error in executing */
    if ($stmt->errno) {
        echo "error in executing the query: " . $stmt->error;
    }
    /* Fetch the result */
    $result = $stmt->get_result();
    /* Fetch the row */
    $row = $result->fetch_assoc();

    // Create an array to hold the order items data
    $orderItems = [];

    /* Store the row data in the $orderItems array */
    if($row) {
        $orderItems[] = [
            'order_items_id' => $row['order_items_id'],
            'order_unique_id' => $row['order_unique_id'],
            'product_id' => $row['product_id'],
            'quantity' => $row['quantity'],
            'price' => $row['price'],
            'total_price' => $row['total_price'],
            'order_id' => $row['order_id'],
        ];
    }
    return $orderItems;
}

/* ----- GET INFO FROM ORDER_PROCESS TABLE ----- */
function getOrderProcess($order_unique_id) {
    global $conn;
    // Validate and sanitize the input to prevent SQL injection
    /* $order_unique_id = mysqli_real_escape_string($conn, $order_unique_id); */
    $sql = "SELECT * FROM order_process WHERE order_unique_id = ?";
    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        echo "error in preparing the query: " . $conn->error;
    }
    /* Bind parameters and execute the stmt */
    $stmt->bind_param("s", $order_unique_id);
    $stmt->execute();
    /* check for error in executing */
    if ($stmt->errno) {
        echo "error in executing the query: " . $stmt->error;
    }
    /* Fetch the result */
    $result = $stmt->get_result();

    /* Fetch the row */
    $row = $result->fetch_assoc();

    // Create an array to hold the order process data
    $orderProcessData = [];

    /* If a row is returned put the columns and info in the array */
    if($row) {
        $orderProcessData[] = [
            'order_process_id' => $row['order_process_id'],
            'order_unique_id' => $row['order_unique_id'],
            'order_id' => $row['order_id'],
            'card_holder_name' => $row['card_holder_name'],
            'card_number' => $row['card_number'],
            'card_expiry_month' => $row['card_expiry_month'],
            'card_expiry_year' => $row['card_expiry_year'],
            'cvv' => $row['cvv'],
            'transaction_id' => $row['transaction_id'],
            'payment_status' => $row['payment_status'],
            'created_at' => $row['created_at'],
            'final_price' => $row['final_price'],
        ];
    }

    /* Return the order process data */
    return $orderProcessData;
}


?>