<?php 

class OrdersController {
    private $orderMapper;

    public function __construct(OrderMapper $orderMapper) {
        $this->orderMapper = $orderMapper;
    }
    
    public function showAllOrders() {
        $orders = $this->orderMapper->getAllOrders();

        // Perform some additional logic if needed
        // Render the view with the list of all orders

    }    
    
    public function showOrderDetails($order_unique_id) {
        $order = $this->orderMapper->getOrder($order_unique_id);

        // Perform some additional logic if needed
        // Render the view with the order details
    }
    
    // Add more methods for other functionalities related to orders

}


class OrdersActionController {
    private $orderMapper;
    private $orderItemMapper;
    private $orderProcessMapper;

    public function __construct(OrderMapper $orderMapper, OrderItemsMapper $orderItemMapper, OrderProcessMapper $orderProcessMapper) {
        $this->orderMapper = $orderMapper;
        $this->orderItemMapper =  $orderItemMapper;
        $this->orderProcessMapper = $orderProcessMapper;
    }
    
    public function showEditOrderInfo($order_unique_id) {

        $order = $this->orderMapper->getOrder($order_unique_id);

        /* Perform some addidional logic if needed */

        /* render the view with view of same logic used in orders_action.php */
    }

    public function updateOrderInfo($order_unique_id, $arrayWithTheNewOrderInfo) {
        /* Kannski rename þetta function í updateOrdersTable */

        /* Start by fetching the order and storing as an object inside $order */
        $order = $this->orderMapper->getOrder($order_unique_id);

        /* Update the order object with the $arrayWithTheNewOrderInfo */



    }
    /* Function that shows the order_items.php */
    public function showOrderItems($order_unique_id) {
        $order_items_info = $this->orderItemMapper->getOrderItems($order_unique_id);
    }
    /* Function that shows the order_process.php */
    public function showOrderProcess($order_unique_id) {
        $orderProcessInfo = $this->orderProcessMapper->getOrderProcess($order_unique_id);

    }
}




?>