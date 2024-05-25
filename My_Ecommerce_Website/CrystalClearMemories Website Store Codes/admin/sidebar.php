              <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- --> 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap icons -->
    <link href="<?php echo "$base_url" ?>img/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="<?php echo "$base_url" ?>../../bootstrap/dist/css/bootstrap.min.css">
    <!-- Mitt eigið CSS -->
    <link rel='stylesheet' type='text/css' media='screen' href='<?php echo "$base_url" ?>css/sass.css'>
    <link rel='stylesheet' type='text/css' media='screen' href='<?php echo "$base_url" ?>css/mystyle.css'>
    <link rel='stylesheet' type='text/css' media='screen' href='<?php echo "$base_url" ?>css/buttons.css'>
    <!-- Notast við base_url í javascript líka -->
    <script> let base_url = '<?php echo $base_url; ?>'; </script>   
    <!-- Bootstrap og jquery -->
    <script src="<?php echo "$base_url"; ?>js/bootstrap/bootstrap.bundle.js"></script>
    <script src="<?php echo "$base_url"; ?>js/jquery/jquery.js"></script>
    <script src="<?php echo "$base_url"; ?>js/extras.js"></script>
    <script src="<?php echo "$base_url"; ?>js/create_spa.js"></script>

  
  
    <!-- Bý til font class -->
    <style>
      /* Font-face and custom-text styles */
      @font-face {
        font-family: 'customFont';
        src: url('<?php echo "$base_url" ?>font/Eastwood/Eastwood.woff2') format('woff2'),
            url('<?php echo "$base_url" ?>font/Eastwood/Eastwood.woff') format('woff'),
            url('<?php echo "$base_url" ?>font/Eastwood/Eastwood.ttf') format('truetype');
      }
      @font-face {
      font-family: 'kirstyRegular';
      src: url('<?php echo "$base_url" ?>font/kirsty/kirsty_rg.otf') format('opentype');
      }
      @font-face {
      font-family: 'kirstyRegularItalic';
      src: url('<?php echo "$base_url" ?>font/kirsty/kirsty_rg_it.otf') format('opentype');
      }
      @font-face {
      font-family: 'kirstyBold';
      src: url('<?php echo "$base_url" ?>font/kirsty/kirsty_bd.otf') format('opentype');
      }
      @font-face {
      font-family: 'kirstyBoldItalic';
      src: url('<?php echo "$base_url" ?>font/kirsty/kirsty_bd_it.otf') format('opentype');
      }
      .custom-text {
      font-family: 'customFont', sans-serif;
      }
      .kirsty-regular {
      font-family: 'kirstyRegular', sans-serif;
      }
      .kirsty-regular-italic {
      font-family: 'kirstyRegularItalic', sans-serif;
      }
      .kirsty-bold {
      font-family: 'kirstyBold', sans-serif;
      }
      .kirsty-bold-italic {
      font-family: 'kirstyBoldItalic', sans-serif;
      }
      </style>
    <!-- Titill síðunnar -->
    <title>Admin - Crystal 3D Pictures</title>
  
</head>


<body> 
  <div class="container-fluid"><!-- container utan um allt --> <!-- div lokast ekki -->
    <div class="row"><!-- rowið utan um allt --> <!-- div lokast ekki -->


      <div class="col-2 vh-100 d-xl-flex d-none  align-items-center justify-content-center position-fixed sidebar-margin">
        <div class="container-fluid backgroundsidebar">
          <div class="sidebar sidebar-colors mb-lg-0 d-xl-block d-none kirsty-bold-italic">
            
            <nav class="navbar navbar-expand-lg">

              <ul class="nav flex-column w-75 mx-auto align-items-center">

                <li class="nav-item">
                <div class="nav-link"><span>Admin</span></div>
                </li>

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>index.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Overview</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">
                
                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center nowrap" href="<?php echo $base_url ?>create/create_index.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Add - Create</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>orders/orders.php">
                    <i class="bi bi-card-list" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Orders</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>products/products.php">
                    <i class="bi bi-grid-3x3-gap-fill" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Products</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>categories/categories.php">
                    <i class="bi bi-box" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Categories</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>users/users.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Users</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>logs/logs.php">
                    <i class="bi bi-globe2" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Logs</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>admins/admins.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Admins</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="<?php echo $base_url ?>login/logout.php">
                    <i class="bi bi-box-arrow-left" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Log Out</span>
                  </a>
                </li>
              </ul><!-- nav flex-column w-75 mx-auto align-items-center -->
            </nav><!-- navbar navbar-expand-lg -->
            
          </div><!-- sidebar sidebar-colors mb-lg-0 d-none d-lg-block kirsty-bold-italic -->
        </div><!-- container-fluid backgroundsidebar -->
      </div> <!-- col-2 col-lg-2 vh-100 d-none d-lg-flex align-items-center justify-content-center position-fixed -->


