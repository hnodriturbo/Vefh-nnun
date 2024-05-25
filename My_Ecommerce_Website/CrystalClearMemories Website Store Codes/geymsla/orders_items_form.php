<?php 
echo '
<form action="update_quantity.php" method="post">
    <!-- BUTTON ROW -->
    <div class="row p-1">
        <!-- COLUMN 1 -->
        <div class="col-lg-6 col-6 d-flex justify-content-end p-0">
            <button type="submit" class="btn btn-outline-secondary toggle-btn-outline-secondary-box-shadow w-100" href="#">
                Change quantity
            </button>
        </div>
        <!-- COLUMN 2 -->
        <div class="col-lg-6 col-6 d-flex justify-content-end">
            <button class="btn btn-secondary w-25" type="button" onclick="decreaseQuantity()">
                -
            </button>

            <!-- Hidden input field to store the updated quantity value -->
            <input type="hidden" name="quantity" id="quantity" value="' . $order_item_data['quantity'] . '">

            <span class="whitetext center d-flex" id="display-quantity" style="padding-left: 20px; padding-right: 20px;">
                    ' . $order_item_data['quantity'] . '
            </span>

            <button class="btn btn-secondary w-25" type="button" onclick="increaseQuantity()">
                +
            </button>
        </div>
    </div>
</form>
';

?>