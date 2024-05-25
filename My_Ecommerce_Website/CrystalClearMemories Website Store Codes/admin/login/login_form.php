<!-- ----- FORM START ----- -->
<form action="login.php" method="POST" name="login">
        <div class="center">
        <!-- Cardið fyrir Users table -->
            <div class="card card-lg-width col-lg-10 col-12 mx-auto" style="margin-top: 100px;">
                <div class="card-header d-flex justify-content-center">
                    <h4 class="card-title text-center whitetext">Innskráning Admins</h4>
                </div>

                <div class="card-body">
                    <!-- Row -->
                    <div class="row p-3 align-items-center justify-content-center"> 
                        <div class="col">
                            <h1></h1>
                        </div>
                    </div>

                    <!-- Línan -->
                    <hr class="my-horizontal-line">

                
                    <!-- Row og 2 cols -->
                    <div class="row p-3 align-items-center"> 
                        <div class="col-3">
                            <label class="text-align" style="color: #CCCCCC;">Username:</label>
                        </div>
                        <div class="col-9" style="padding: 0;">
                            <input class="form-control bg-dark-subtle" type="text" name="username" placeholder="Please enter your username" aria-label="default input example" style="background-color: #F2F2F2;">
                        </div>          
                    </div>  
                    <!-- Row og 2 cols -->
                    <div class="row p-3 align-items-center"> 
                        <div class="col-3">
                            <label class="text-align" style="color: #CCCCCC;">Password:</label>
                        </div>
                        <div class="col-9" style="padding: 0;">
                            <input class="form-control bg-dark-subtle" type="password" name="password" placeholder="Please enter your password" aria-label="default input example">
                        </div>
                    </div>
                </div><!-- card-body -->

                <!-- login takkinn -->
                <div class="card-footer pb-5 d-flex justify-content-center">
                <button class="btn btn-outline-secondary" type="submit" name="login" style="width: 50%;">Login</button>
                </div>
            </div><!-- card -->
        </div> <!-- center -->
    </form>