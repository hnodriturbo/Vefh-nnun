<?php 


function getPaginatedProducts($page, $perPage) {
    global $conn;
    // Finna út hvað margar rows skal skippa áður en náð er í tíu rows
    $offset = ($page - 1) * $perPage;
    /* Undirbý stmt, vel úr users         LIMIT startRow limit */
    $stmt = $conn->prepare("SELECT * FROM products LIMIT ?, ?");
    if(!$stmt) {
        echo "error in preparing the query: " . $conn->error;
    }
    /* Bind the parameters */
    $stmt->bind_param('ii', $offset, $perPage);
    /* Keyri statementið */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
    }
    /* næ í niðurstöður */
    $result = $stmt->get_result();
    /* Athuga hvort niðurstöður hafi komið */
    if ($result->num_rows === 0) {
        echo "no rows returned";
    }
    /* Lúppa í gegnum result */
    while ($row = $result->fetch_assoc()) {
        $product_id = $row['product_id'];
        $image = $row['image'];
        $name = $row['name'];
        $description = $row['description'];
        $price = $row['price'];
        $category_id = $row['category_id'];

        echo "<tr>";
        echo "<td>$product_id</td>";
        echo "<td><img src='img/products/$image' alt='Product Image' class='' style='height: 75px; width: 75px; border: none;'></td>";
        echo "<td>$name</td>";
        echo "<td>$description</td>";
        echo "<td>$price</td>";
        echo "<td>$category_id</td>";
        echo "<td>
        <a class='btn btn-secondary custom-btn' href='products_action.php?source=products&product_id=" . $product_id . "&action=view'>View</a>
            </td>";
        echo "<td>
        <a class='btn btn-danger custom-btn' href='products_action.php?source=products&product_id=" . $product_id . "&action=delete'>Delete</a>
            </td>";
        echo "</tr>";
       
    }
}
/* ---- EKKI AÐ NOTA Í AUGNABLIKINU ---- */
function getCategoryName($category_id) {
    global $conn;
    $stmt = $conn->prepare("SELECT name FROM categories WHERE category_id = ?");
    if (!$stmt) {
        echo "Error in preparing the query: " . $conn->error;
        return;
    }
    $stmt->bind_param("i", $category_id);
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }
    $result = $stmt->get_result();
    if ($result->num_rows === 0) {
        echo "no rows found";
    }
    else {
        $row = $result->fetch_assoc();
        $category_name = $row['name'];
        $stmt->close();
        return $category_name;
    }
}

/* Function sem telur hvað mörg rows eru í table database */
function countProducts() {
    global $conn;
    $stmt = $conn->prepare("SELECT count(*) FROM products");
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    /* set töluna í breytu */
    $count = $row[0];
    return $count;
}

?>