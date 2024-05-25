<?php 


/* ------------------------------------------------------------------- */
 /* - THIS CLASS FINDS FROM ORDERS TABLE AND RETURNS IT AS AN ARRAY - */
/* ------------------------------------------------------------------- */

class OrderMapper {

    // Database connection and other ORM-related methods

    
    /* Function to get all the orders */
    public function getAllOrders() {
        /* Implement the logic to fetch an order by ID from the 
        database and return an array of order object */
    }

    /* Function to find order by using order_unique_id */
    public function getOrder($order_unique_id) {
        /* Implement the logic to fetch an order by ID from the 
        database and return an array of order object */
    }


    /* Function to find order by using order_status */
    public function getOrdersByOrderStatus($order_status) {
        /* Implement the logic to fetch orders by status from the database 
        and return an array of Order objects */
    }


    /* Function to find order by using user_id */
    public function getOrdersByUserId($user_id) {
        /* Implement the logic to fetch orders by user ID from the database 
        and return an array of Order objects */
    }

    /* Add more methods for querying orders as needed 
    (e.g., findAll, updateOrder, etc.) */



}






/* ------------------------------------------------------------------------ */
 /* - THIS CLASS FINDS FROM ORDER_ITEMS TABLE AND RETURNS IT AS AN ARRAY - */
/* ------------------------------------------------------------------------ */

class OrderItemsMapper {

    // Database connection and other ORM-related methods
    public function getOrderItems($order_unique_id) {
/* Implement the logic to fetch from order_items table by ID and return an Order object */
    }

    

}






/* -------------------------------------------------------------------------- */
 /* - THIS CLASS FINDS FROM ORDER_PROCESS TABLE AND RETURNS IT AS AN ARRAY - */
/* -------------------------------------------------------------------------- */
class OrderProcessMapper {
    // Database connection and other ORM-related methods
    public function getOrderProcess($order_unique_id) {

    }
    // Implement methods to fetch order process data based on order ID, order unique ID, etc.
}

?>