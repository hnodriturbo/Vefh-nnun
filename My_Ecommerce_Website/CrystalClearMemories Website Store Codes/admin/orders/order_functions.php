              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->

        
<?php 

/* ----------------------------------------------------------- */
 /* -- COUNT ALL THE ROWS IN ORDERS TABLE FOR PAGE DISPLAY -- */
/* ----------------------------------------------------------- */
function countOrders() {
    global $conn;
    $sql = "SELECT count(*) FROM orders";
    $stmt = $conn->prepare($sql);
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    $count = $row[0];
    return $count;
}
/* ----------------------------------------------------------- */
 /* -- USE THE ORDER STATUS TO RETURN STRING FOR CSS CLASS -- */
/* ----------------------------------------------------------- */
function getOrderStatusClass($selectedOrderStatus) {
    switch ($selectedOrderStatus) {
        case 'Made':
            return ' status-made';
        case 'Confirmed':
            return ' status-confirmed';
        case 'Processed':
            return ' status-processed';
        case 'Delivered':
            return ' status-delivered';
        case 'Cancelled':
            return ' status-cancelled';
        default:
            return ' status-made';
    }
}




/* --------- GET BOTH ORDER AND ORDERS FROM ORDERS TABLE ----------- */
function getOrders($page = null, $perPage = null, $order_unique_id = null) {
    global $conn;
    /* if order_unique id is provided, fetch a single row */
    if($order_unique_id) {
        $sql = "SELECT * FROM orders WHERE order_unique_id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("s", $order_unique_id);
    } else {
        /* if a page is provided and how many rows perPage */
        if ($page && $perPage) {
            $offset = ($page - 1) * $perPage;
            $stmt = $conn->prepare("SELECT * FROM orders LIMIT ?, ?");
            $stmt->bind_param("ii", $offset, $perPage);
        } else {
            /* Fetch all orders in case the others fail */
            $stmt = $conn->prepare("SELECT * FROM orders");
        }
    }
    $stmt->execute();
    $result = $stmt->get_result();
    if($result->num_rows === 0) {
        echo "no rows returned";
        return false;
    }
    $order_data = [];
    while ($row = $result->fetch_assoc()) {
            /* ----- Manipulate the output of the date ----- */
            $timestamp = strtotime($row['created_at']);
            $formattedDate = date('d-m-Y', $timestamp);
            /* Create Associative array to hold the data for each order */
            $order_data = [
                'order_id' => $row['order_id'],
                'order_unique_id' => $row['order_unique_id'],
                'user_id' => $row['user_id'],
                'firstname' => $row['firstname'],
                'lastname' => $row['lastname'],
                'email' => $row['email'],
                'address' => $row['address'],
                'address2' => $row['address2'],
                'postalcode' => $row['postalcode'],
                'city' => $row['city'],
                'state' => $row['state'],
                'country' => $row['country'],
                'final_price' => $row['final_price'],
                'order_status' => $row['order_status'],
                'created_at' => $formattedDate
            ];
            $orders_data[] = $order_data;
    }
    return $orders_data;
}


/* --------- UPDATE ORDERS TABLE ----------- */
function updateOrdersTable($order_unique_id) {
    if(isset($_POST['update_orders_table'])) {
        global $conn;
        /* Get the info from the POST that can be edited */
        $firstname = $_POST['firstname'];
        $lastname = $_POST['lastname'];
        $email = $_POST['email'];
        $address = $_POST['address'];
        $address2 = $_POST['address2'];
        $postalcode = $_POST['postalcode'];
        $city = $_POST['city'];
        $state = $_POST['state'];
        $country = $_POST['country'];
        $order_status = $_POST['order_status'];
        /* Prepare the statement */
        $sql = "UPDATE orders SET firstname=?, lastname=?, email=?, address=?, address2=?, postalcode=?, city=?, state=?, country=?, order_status=? WHERE order_unique_id=?";
        $stmt = $conn->prepare($sql);
        if(!$stmt) {
            /* Get the existing url string  */
            $query_string = $_SERVER['QUERY_STRING'];
            $query_string .= '&message=There was an error in preparing the query';
            header("Location: order_info.php?$query_string");
        }
        $stmt->bind_param("sssssssssss", $firstname, $lastname, $email, $address, $address2, $postalcode, $city, $state, $country, $order_status, $order_unique_id);
        if($stmt->execute()) {
            return true;
        } else {
            return false;
        }
        $stmt->close();
    }
}


/* Delete order function - Á EFTIR AÐ BREYTA OG BÆTA VIÐ ORDER_ITEMS OG ORDER_PROCESS */
function deleteOrder($encryptedToken) {
    /* Make the order unique id from the encryptedToken */
    $order_unique_id = decrypt_order_unique_id($encryptedToken);
    global $conn;
    $sql = "DELETE from orders WHERE order_unique_id = ?";
    $stmt = $conn->prepare($sql);
    if(!$stmt) {
        echo "error in preparing the query: " . $conn->error;
    }
    $stmt->bind_param("s", $order_unique_id);
    $stmt->execute();
    if($stmt->errno) {
        header("Location: order_info.php?token=' . $encryptedToken . '&action=showinfo&message=Error in executing the query: ' . $stmt->error . '");
    }
    /* Check for affected rows */
    if($stmt->affected_rows === 0) {
        header("Location: order_info.php?token=' . $encryptedToken . '&action=showinfo&message=Deletion error! No rows were affected");
    }
    $stmt->close();
    return true;
}


/* ----------------------------------------------------------- */
    /* -- FETCH THE ORDER_PROCESS ROW OF SELECTED ORDER -- */
/* ----------------------------------------------------------- */

function getOrderProcessInfo($order_unique_id) {
    global $conn;
    $sql = "SELECT * FROM order_process WHERE order_unique_id = ?";
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
        echo "No row returined";
        return false;
    }
    /* Fetch associated row into $row */
    $row = $result->fetch_assoc();

    $order_process_info = [
        /* Set every column of the table into variables */
        $order_process_id = $row['order_process_id'],
        $order_unique_id = $row['order_unique_id'],
        $order_id = $row['order_id'],
        $card_holder_name = $row['card_holder_name'],
        $card_number = $row['card_number'],
        $card_expiry_month = $row['card_expiry_month'],
        $card_expiry_year = $row['card_expiry_year'],
        $cvv = $row['cvv'],
        $transaction_id = $row['transaction_id'],
        /* pending - completed - failed */
        $payment_status = $row['payment_status'],
        $created_at = $row['created_at'],
        $final_price = $row['final_price']
    ];
    return $order_process_info;
}

/* --------- UPDATE ORDER_PROCESS TABLE ----------- */
function updateOrderProcessTable($order_unique_id) {
    if (isset($_POST['update_order_process_table'])) {
        global $conn;
        /* Get the info from the POST that can be edited */
        $card_holder_name = $_POST['card_holder_name'];
        $card_number = $_POST['card_number'];
        $card_expiry_month = $_POST['card_expiry_month'];
        $card_expiry_year = $_POST['card_expiry_year'];
        $cvv = $_POST['cvv'];
        $transaction_id = $_POST['transaction_id'];
        $payment_status = $_POST['payment_status'];
        $final_price = $_POST['final_price'];
        /* Prepare the statement */
        $sql = "UPDATE order_process SET card_holder_name=?, card_number=?, card_expiry_month=?, card_expiry_year=?, cvv=?, transaction_id=?, payment_status=?, final_price=? WHERE order_unique_id=?";
        $stmt = $conn->prepare($sql);
        if (!$stmt) {
            /* Get the existing url string */
            $query_string = $_SERVER['QUERY_STRING'];
            $query_string .= '&message=There was an error in preparing the query';
            header("Location: order_process_action.php?$query_string");
            exit; // Exit the function to avoid further execution in case of error
        }
        $stmt->bind_param("sssssssss", $card_holder_name, $card_number, $card_expiry_month, $card_expiry_year, $cvv, $transaction_id, $payment_status, $final_price, $order_unique_id);
        if ($stmt->execute()) {
            $stmt->close();
            return true;
        } else {
            $stmt->close();
            return false;
        }
    }
}






/* ---------------------------------------------------------------- */
 /* ----------------- ORDER_ITEMS.PHP FUNCTIONS ------------------ */
/* ---------------------------------------------------------------- */

/* Get all products from order_items table */
function getAllProductsFromOrderItemsData($order_items_data) {
    $products_data = [];
    /* Loop through order_items_data as order_item_data */
    foreach ($order_items_data as $order_item_data) {
        /* Set the product_id */
        $product_id = $order_item_data['product_id'];
        /* Use the product_id to get product related to the order_item row */
        $order_items_product = getProduct($product_id);
        /* If the order_items_product was found */
        if ($order_items_product) {
            /* Set the found product into products_data */
            $products_data[] = $order_items_product;
        }
    }
    /* Return all the products that were put into products_data */
    return $products_data;
}

/* Loop order_items_data and return related order_items row using $order_unique_id and $product_id */
function getOrderItemData($order_items_data, $order_unique_id, $product_id) {
    foreach ($order_items_data as $order_item_data) {
        if ($order_item_data['order_unique_id'] == $order_unique_id && $order_item_data['product_id'] == $product_id) {
            return $order_item_data;
        }
    }
    /* return null if no product is found */
    return null;
}


/* function sem nær í nafn á category eftir product id */
function getCategoryName($category_id) {
    global $conn;
    try {
        $sql = "SELECT name FROM categories WHERE category_id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $category_id);
        $stmt->execute();
        $result = $stmt->get_result();
        $row = $result->fetch_assoc();
        return $row ? $row['name'] : "Couldn't get category name";
    } catch (Exception $e) {
        return "Couldn't get category name";
    }
}

/* ----------- HÉRNA ERU FUNCTIONS SEM ÉG ÞARF AÐ NOTA FYRIR ORDER ITEMS ---------- */
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
/* Function fetching related product and returning it */
function getProduct($product_id) {
    global $conn;
    $sql = "SELECT * FROM products WHERE product_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $product_id);
    $stmt->execute();
    $result = $stmt->get_result();
    if($result->num_rows === 0) {
        echo "no rows returned";
        return false;
    }
    $row = $result->fetch_assoc();
    $productInfo = [
        'product_id' => $row['product_id'],
        'image' => $row['image'],
        'name' => $row['name'],
        'description' => $row['description'],
        'price' => $row['price'],
        'c_price' => $row['c_price'],
        'category_id' => $row['category_id'],
        'tags' => $row['tags']
    ];
    return $productInfo;
}
function getNewTotalPrice($product_id, $order_unique_id) {
    global $conn;
    $sql = "SELECT total_price FROM order_items WHERE product_id = ? AND order_unique_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("is", $product_id, $order_unique_id);
    $stmt->execute();
    $result = $stmt->get_result();
    if($result->num_rows === 0) {
        echo "no rows returned";
        return false;
    } else {
        $row = $result->fetch_assoc();
        $new_total_price = $row['total_price'];
        return $new_total_price;
    }
    
}

function changeQuantityOrderItems($new_quantity, $order_unique_id, $product_id) {
    global $conn; 
    $sql = "UPDATE order_items SET quantity = ? WHERE order_unique_id = ? AND product_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('isi', $new_quantity, $order_unique_id, $product_id);
    if ($stmt->execute()) {
        $stmt->close();
        return true;
    } else {
        echo "Execute failed: " . $stmt->error;
        $stmt->close();
        return false;
    }
}


function deleteOrderItemFromOrder($order_unique_id, $product_id) {
/* 
    global $conn;
    $sql = "DELETE FROM order_items WHERE order_unique_id = ? AND product_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("si", $order_unique_id, $product_id);
    if($stmt->execute()) {
        $stmt->close();
        return true;
    } else {
        echo "Execute failed: " . $stmt->error;
        $stmt->close();
        return false;
    }
 */


/* MEÐAN ÉG ER AÐ VINNA MEÐ TAKKANA LÆT ÉG ÞETTA FUNCTION VERA TRUE */
    return true;
}

/* ---------------------------------------------------------------------------- */
  /* FUNCTION FETCHING ALL ORDER INFORMATION INCLUDING RELATED PRODUCTS INFO */
    /* ------------------------------------------------------------------ */
           /* ORDER_INFO - ORDER_ITEMS_DATA - PRODUCTS_DATA */
function fetchOrderDetails($token) {

    /* Make an empty array */
    $order_details = [];

    /* First use the token to decrypt the order_unique_id */
    $order_details['order_unique_id'] = decrypt_order_unique_id($token);
    if(!$order_details['order_unique_id']) {
        die('Failed to decrypt token.');
    }

    /* Use the unique_id to get the order info from "orders" table - shipping details */
    $order_details['order_info'] = getOrders(null, null, $order_details['order_unique_id']);
    if(!$order_details['order_info']) {
        die('Failed to fetch order_info data.'); 
    }
    /* Use the unique_id to get all rows from the order_items table wich holds all ordered items */
    $order_details['order_items_data'] = getOrderItems($order_details['order_unique_id']);
    if(!$order_details['order_items_data']) {
        die('Failed to fetch order_items data.'); 
    }
    /* Use each product_id from order_items rows to fetch each related product info  */
    $order_details['products_data'] = getAllProductsFromOrderItemsData($order_details['order_items_data']);
    if(!$order_details['products_data']) {
        die('Failed to fetch products_data data.'); 
    }

    return $order_details;
}


function addToLogs($action, $message, $type) {
    global $conn;

    $allowedTypes = ['users', 'guests', 'admin', 'warning', 'error', 'other'];
    if(!in_array($type, $allowedTypes)) {
        $type = 'other';
    }

    /* Get user id from session or cookie */
    $user_id = $_SESSION['user_id'] ?? $_COOKIE['user_id'] ?? null;

    $sql = "INSERT INTO logs (user_id, action, message, type) VALUES (?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("isss", $user_id, $action, $message, $type);

    if($stmt->execute()) {
        return true;
    } else {
        return false;
    }

}

addToLogs('Product Deletion', 'Admin deleted product with ID: 123.', 'admin');
addToLogs('User Registration', 'New user with email: user@example.com registered successfully.', 'users');
addToLogs('Cart Addition', 'Guest added product with ID: 456 to the cart.', 'guests');




?>