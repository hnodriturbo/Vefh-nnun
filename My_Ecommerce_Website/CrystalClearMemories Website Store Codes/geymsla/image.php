<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['btn_save'])) {
        $product_name = $_POST['product_name'];
        $details = $_POST['details'];
        $price = $_POST['price'];
        $c_price = $_POST['c_price'];
        $product_type = $_POST['product_type'];
        $brand = $_POST['brand'];
        $tags = $_POST['tags'];

        // Picture coding
        $picture_name = $_FILES['picture']['name'];
        $picture_type = $_FILES['picture']['type'];
        $picture_tmp_name = $_FILES['picture']['tmp_name'];
        $picture_size = $_FILES['picture']['size'];

        // Define allowed file types (you can add more if needed)
        $allowed_types = array('image/jpeg', 'image/jpg', 'image/png', 'image/gif');

        // Define maximum file size in bytes (50 MB in this case)
        $max_file_size = 50000000;

        // Check if the file type is allowed
        if (!in_array($picture_type, $allowed_types)) {
            echo "Error: Only JPEG, JPG, PNG, and GIF images are allowed.";
        } elseif ($picture_size > $max_file_size) {
            echo "Error: The image size is too large. Please upload an image with a size less than 50 MB.";
        } else {
            // Generate a unique name for the image using the current timestamp to avoid overwriting files with the same name
            $pic_name = time() . "_" . $picture_name;
            $target_directory = "product_images/";
            $target_file_path = $target_directory . $pic_name;

            // Move the uploaded file to the desired location on the server
            if (move_uploaded_file($picture_tmp_name, $target_file_path)) {
                // File uploaded successfully, you can now proceed with saving other product details to the database
                echo "Product details saved successfully!";
                // ... Your code to save other product details in the database goes here ...
            } else {
                echo "Error uploading the file.";
            }
        }
    }
    ?>