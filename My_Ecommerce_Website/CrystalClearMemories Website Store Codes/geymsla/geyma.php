<!--     Online link to bootstrap
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css">
 -->
   <!--   Þessi takki togglar navbar upp og niður held ég -->
   
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" onclick="toggleSidebar()">
      <span class="navbar-toggler-icon"></span>
    </button>

    <!-- Takki sem togglar offcanvas -->
    <button class="btn btn-primary position-absolute" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas" aria-controls="offcanvas">
        Button with data-bs-target
    </button>


    

<!--    
<nav class="navbar navbar-expand-lg navbar-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">Link 1</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link 2</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link 3</a>
      </li>
    </ul>
  </div>
</nav>
 -->
 
 <!-- Þetta er leið til að gera gegnsæjan bakgrunnsmynd -->   
<!-- style="background-image: linear-gradient(rgba(33, 37, 41, 0.9), rgba(33, 37, 41, 0.9)), url('img/backgroundsidebar.jpg');" -->




    <!-- ---------------- Offcanvas sem ég ætla geyma aðeins -->

    <!-- Takki sem togglar offcanvas -->
    <button class="btn btn-primary position-absolute" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas" aria-controls="offcanvas">
        Button with data-bs-target
    </button>



                    <!-- OFFCANVAS -->
<!-- -------------------------------------------------------------------- -->



<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasLabel">Offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="index.php"> <!-- Added btn-lg class -->
        <i class="bi bi-person-circle" style="padding: 10px;"></i>
        <span>Overview</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="products.php">
        <i class="bi bi-card-list" style="padding: 10px;"></i>
        <span>Products</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="orders.php">
        <i class="bi bi-card-list" style="padding: 10px;"></i>
        <span>Orders</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="users.php">
        <i class="bi bi-person-circle" style="padding: 10px;"></i>
        <span>Users</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="categories.php">
        <i class="bi bi-box" style="padding: 10px;"></i>
        <span>Categories</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="logout.php">
        <i class="bi bi-box-arrow-left" style="padding: 10px;"></i>
        <span>Log Out</span>
      </a>
    </li>
              

  </div>
</div>





<nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ">
        <div class="container-fluid">
          <div class="navbar-dark">
            <a class="navbar-brand" href="javascript:void(0)">Admin</a>
            
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
            <span class="sr-only">Toggle navigation</span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end">
            <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link" href="javscript:void(0)" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="material-icons">person</i>
                  
                  <p class="d-lg-none d-md-block">
                    Some Actions
                  </p>
                </a>
                
              </li>
             
            </ul>
          </div>
        </div>
      </nav>
 <!-- 
   <div class="pos-f-t">
  <div class="collapse" id="navbarToggleExternalContent">
    <div class="bg-dark p-4">
      <h4 class="text-white">Collapsed content</h4>
      <span class="text-muted">Toggleable via the navbar brand.</span>
    </div>
  </div>
  <nav class="navbar navbar-dark bg-dark">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
  </nav>
</div>
  
 -->




 echo '
<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <!-- Container row og col-lg-8 sem breytist í col-12 á minni skjám -->
    <div class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-lg-9 col-12 d-lg-flex">
                <!-- Formið byrjar hérna og er utan um allt cardið -->
                <form action="products_action.php?source=products&product_id=' . $product_id . '&action=edit&confirm=confirm" method=POST name=updateProduct class="w-100">
                    <!-- Card sem fyllir upp í plássið (w-100) -->
                    <div class="card card-lg-width w-100" style="margin-top: 12vw;">
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill w-100 d-flex justify-content-center align-items-center center" style="font-size: 22px; cursor: default;">Edit Product Info</h4>
                        </div>
                        <div class="card-body">
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Product Name:</label>
                                </div>
                                <div class="col-11" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="product_name" value="' . $productInfo['name'] . '" aria-label="default input example">  
                                </div>
                            </div> 
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Description:</label>
                                </div>
                                <div class="col-6" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="product_description" value="' . $productInfo['description'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Price:</label>
                                </div>
                                <div class="col-4" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="product_price" value="' . $productInfo['price'] . '" aria-label="default input example">
                                </div>
                            </div>
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Cost Price:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="product_c_price" value="' . $productInfo['c_price'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Category Id:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="product_category_id" value="' . $productInfo['category_id'] . '" aria-label="default input example">
                                </div>
                            </div>

                        </div><!-- card-body -->
                        <div class="card-footer pb-5 d-flex justify-content-center">
                        <!-- update takkinn -->
                        <button class="btn btn-outline-secondary" type="POST" name="update" style="width: 50%;">Update</button>
                        </div>
                    </div><!-- card card-lg-width w-100" style="margin-top: 12vw;" -->
                </form> <!-- form -->
            </div> <!-- col-12 admin users table -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->
    
    
    
    
    ';
<?php

    while($row = $result->fetch_assoc()) {
    // ... Other code ...
  
    $order_status = $row['order_status'];
  
    // Determine the CSS class based on the order status
    $status_class = '';
    switch ($order_status) {
      case 'Pending':
        $status_class = 'status-pending';
        break;
      case 'Processing':
        $status_class = 'status-processing';
        break;
      case 'Completed':
        $status_class = 'status-completed';
        break;
      case 'Cancelled':
        $status_class = 'status-cancelled';
        break;
      default:
        // Use a default class for unknown status or handle it as needed
        $status_class = 'status-default';
    }
  
    // Add the CSS class to the <td> element
    echo "<td class='$status_class'>$order_status</td>";
  
    // ... Rest of the code ...
  }

?>
  



  













