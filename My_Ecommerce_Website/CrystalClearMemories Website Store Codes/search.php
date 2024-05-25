<?php
// Establish database connection using PDO
$servername = "your_servername";
$username = "your_username";
$password = "your_password";
$dbname = "vefverslun";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    echo "Database connection failed: " . $e->getMessage();
    exit;
}

// Retrieve search query from form submission
$searchQuery = $_GET['searchQuery'];

// Retrieve checkboxes selections
$selectedTables = isset($_GET['tables']) ? $_GET['tables'] : [];

// Prepare SQL statement
$tables = implode(", ", $selectedTables);
$stmt = $conn->prepare("SELECT * FROM ($tables) WHERE column_name LIKE :query");
$stmt->bindValue(':query', '%' . $searchQuery . '%', PDO::PARAM_STR);

// Execute the query
$stmt->execute();

// Fetch all results
$results = $stmt->fetchAll(PDO::FETCH_ASSOC);

// Pagination settings
$resultsPerPage = 10;
$totalResults = count($results);
$totalPages = ceil($totalResults / $resultsPerPage);

// Retrieve the current page number
$page = isset($_GET['page']) ? $_GET['page'] : 1;

// Calculate the starting and ending indexes of the results for the current page
$startIndex = ($page - 1) * $resultsPerPage;
$endIndex = $startIndex + $resultsPerPage - 1;
if ($endIndex >= $totalResults) {
    $endIndex = $totalResults - 1;
}

// Retrieve the results for the current page
$resultsPage = array_slice($results, $startIndex, $resultsPerPage);

// Display results in a table
echo "<table>";
echo "<tr><th>Column 1</th><th>Column 2</th><th>Column 3</th></tr>";

foreach ($resultsPage as $result) {
    echo "<tr>";
    echo "<td>" . $result['column1'] . "</td>";
    echo "<td>" . $result['column2'] . "</td>";
    echo "<td>" . $result['column3'] . "</td>";
    echo "</tr>";
}

echo "</table>";

// Pagination links
echo "<div>";
for ($i = 1; $i <= $totalPages; $i++) {
    echo "<a href='search.php?page=$i&searchQuery=$searchQuery&tables=" . implode(",", $selectedTables) . "'>$i</a> ";
}
echo "</div>";

// Close the database connection
$conn = null;
?>




<!-- pagination -->
<div class="row">
                                            <div class="col-2">
                                            <button type="button" class="btn btn-outline-secondary justify-content-center">Open Users List</button>
                                            </div>
                                            <div class="col-10 p-0">
                                                <ul class="pagination pagination-sm justify-content-end">
                                                    <li class="page-item">
                                                        <a class="page-link" href="#">Previous</a>
                                                    </li>
                                                    <li class="page-item active">
                                                        <a class="page-link" href="#">1</a>
                                                    </li>
                                                    <li class="page-item">
                                                        <a class="page-link" href="#">2</a>
                                                    </li>
                                                    <li class="page-item">
                                                        <a class="page-link" href="#">3</a>
                                                    </li>
                                                    <li class="page-item">
                                                        <a class="page-link" href="#">Next</a>
                                                    </li>
                                                </ul>
                                            </div>                                  
                                        </div>