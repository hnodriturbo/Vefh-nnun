              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->
 
    




<!-- Navbarið sem er efst á síðunni - Það expandar niður og er með leit -->
<nav class="navbar bg-dark fixed-top kirsty-bold-italic limited-height" id="topNavbar" data-bs-theme="dark" style="opacity: 0.9;">
  <div class="container-fluid p-0 m-0">

              <!-- This is the row for all displaying content on the navbar - Page title, Breadcrumbs and Navbar Toggler Icon -->
              <div class="row w-100 p-0 m-0">

                <div> <!-- This must be within a div so the toggler icon works when clicked to toggle down the navbar -->
                  <a class="navbar-brand navbar-dark position-absolute font-size-30px navbar-main-title" href="#">
                    Admin síða Crystal 3D Pictures
                  </a>
                </div>

                <!-- col-xl-10 col-12 for the breadcrumbs and toggler icon -->
                <div class="col-xl-10 col-12 offset-xl-2">
                  <div class="col-xl-10 col-12 offset-xl-1">
                    <!-- JS handles the breadcrumbs and pushes the <li> and <i> into breadcrumb nav container -->
                    <nav aria-label="breadcrumb">
                      <ol class="breadcrumb">

                      </ol>
                    </nav>
                  </div>
                  
                          <!-- HERE IS THE TOGGLER ICON THAT DROPS DOWN THE NAVBAR -->
                    <!-- Navbar toggler button to show/hide the collapsible content -->
                  <button class="navbar-toggler position-absolute" style="right: 15px; top: 10px;" 
                          type="button" 
                          data-bs-toggle="collapse" 
                          data-bs-target="#navbarTogglerDemo01" 
                          aria-controls="navbarTogglerDemo02" 
                          aria-expanded="false" 
                          aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon" style="font-size: 20  px;"></span>
                  </button>

                </div> <!-- End of col-xl-10 col-12 offset-xl-2 main container of the navbar -->
              </div> <!-- End of the top row for the navbar -->



 
 

    <!-- Container for all content displaying when navbar is expanded-->      
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <ul class="navbar-nav p-3"> <!-- me-auto mb-2 mb-lg-0 -->

        <li class="nav-item">
          <a class="nav-link active p-3" aria-current="page" href="#">
            Admin Overview
          </a>
        </li>

        <li class="nav-item">
          <a class="nav-link p-3" href="#">Vefverslun</a>
        </li>

        <li class="nav-item">
          <a class="nav-link p-3" href="#">Útskráning</a>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle p-3" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu items
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="index.php">Overview</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="products.php">Products</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="orders.php">Orders</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="users.php">Users</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="categories.php">Categories</a></li>
            <li><hr class="dropdown-divider"></li>
            
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle p-3" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Leita
          </a>
          <ul class="dropdown-menu">
            <form role="search">
              <div class="row">
                <div class="col-lg-5 col-md-10">
                  <div class="row">
                    <div class="col-12">
                      <ul>
                        <input type="checkbox" id="products" name="products" value="Products">
                        <label for="products">Products</label>

                        <input type="checkbox" id="users" name="users" value="Users">
                        <label for="users">Users</label>

                        <input type="checkbox" id="orders" name="orders" value="Orders">
                        <label for="orders">Orders</label>

                        <input type="checkbox" id="everything" name="everything" value="Everything">
                        <label for="everything">Everything</label>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-5 col-md-10">
                  <div class="row">
                    <div class="col-12">

                      <input class="form-control" name="search" type="search" placeholder="Search" aria-label="Search">
                      <button class="btn btn-secondary" type="submit" style="width: 100%;">Search</button>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </ul>
        </li>

      </ul><!-- navbar-nav -->
    </div><!-- collapse navbar-collapse -->
        
  </div><!-- container-fluid -->

</nav><!-- navbar bg-dark fixed-top kirsty-regular-italic -->

                     
  <!-- GEYMA ÞETTA AÐEINS -->              
<!--  <nav style="--bs-breadcrumb-divider: url(&#34;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8'%3E%3Cpath d='M2.5 0L1 1.5 3.5 4 1 6.5 2.5 8l4-4-4-4z' fill='%236c757d'/%3E%3C/svg%3E&#34;);" aria-label="breadcrumb">
<ol class="breadcrumb">
<li class="breadcrumb-item"><a href="#">Home</a></li>
<i class="bi bi-forward" style="color: white;"></i>
<li class="breadcrumb-item"><a href="#">Library</a></li>
<i class="bi bi-forward" style="color: white;"></i>
<li class="breadcrumb-item active" aria-current="page">Data</li>
</ol>
</nav> -->