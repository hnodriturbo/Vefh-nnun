              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->


<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);
/* starta session og header virkar ekki nema hafa ob_start */
ob_start();
session_start();

/* Store the current URL in a session variable */
if (!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}

/* Athuga hvort viðkomandi sé loggaður inn og redirecta í samræmi við það */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: ../login/login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: ../login/login.php?error=You need to be logged in to see this site");
    exit();
}
$base_url = "";
/* includa og bý til síðu */
include "database/database.php";
include 'database/encryption_functions.php';

function getOrderItems($order_unique_id) {
    global $conn;
    $sql = "SELECT * FROM order_items WHERE order_unique_id = ?";
    $stmt = $conn->prepare($sql);
    if(!$stmt) {
        echo "Error in preparing the query: " . $conn->error;
        return false;
    }
    $stmt->bind_param("s", $order_unique_id);
    if(!$stmt->execute()) {
        echo "Error in executing the query: " . $stmt->error;
        return false;
    }
    $result = $stmt->get_result();
    if($result->num_rows === 0) {
        // Return an empty array instead of echoing and returning false
        return [];
    }
    $order_items_data = [];
    while ($row = $result->fetch_assoc()) {
        /* þessi bætir allri röðinni aftast í order_items_data */
        $order_items_data[] = [
            'order_items_id' => $row['order_items_id'],
            'order_unique_id' => $row['order_unique_id'],
            'product_id' => $row['product_id'],
            'quantity' => $row['quantity'],
            'price' => $row['price'],
            'total_price' => $row['total_price'],
            'order_id' => $row['order_id'],
        ];
        
    }
    return $order_items_data;
}
$order_unique_id = '0482d882-2f8d-11ee-8d1e-88a4c2119c31';

$order_items_data = getOrderItems($order_unique_id);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Order Items</title>
    <!-- Add the Bootstrap CSS link here -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Order Items</h1>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Order Item ID</th>
                    <th>Order Unique ID</th>
                    <th>Product ID</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Total Price</th>
                    <th>Order ID</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($order_items_data as $order_item) { ?>
                    <tr>
                        <td><?php echo $order_item['order_items_id']; ?></td>
                        <td><?php echo $order_item['order_unique_id']; ?></td>
                        <td><?php echo $order_item['product_id']; ?></td>
                        <td><?php echo $order_item['quantity']; ?></td>
                        <td><?php echo $order_item['price']; ?></td>
                        <td><?php echo $order_item['total_price']; ?></td>
                        <td><?php echo $order_item['order_id']; ?></td>
                    </tr>
                <?php } ?>
            </tbody>
        </table>
    </div>

    <!-- Add the Bootstrap JS and jQuery scripts here -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
