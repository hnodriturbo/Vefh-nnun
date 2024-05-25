
<?php $categories = getCategories(); ?>
<div class="card-body card-body-add-order">
       <div class="alert alert-success borderradius">
              <div class="row m-1 text-black">
                     <div class="col-8 align-items-start justify-content-start d-flex">
                     <h2>Step 3 - Add Products To Order</h2>
                     </div>
                     <div class="col-4 align-items-end justify-content-end d-flex">
                     <h2>Create Order</h2>
                     </div>  
              </div>
       </div>
       <hr class="my-horizontal-line"></hr>    <!-- Línan -->
       <hr class="my-horizontal-line-black"></hr>    <!-- Línan -->


       <!-- CATEGORY DROPDOWN -->
       <div class="row p-3 align-items-center"> 
              <div class="col-3">
                     <label class="text-align nowrap" style="color: #CCCCCC;">Category:</label>
              </div>
              <div class="col-9" style="padding: 0;">
                     <select class="form-control bg-dark-subtle" name="category" id="category-dropdown">
                            <option value="">Select a Category</option>
                            <?php
                            foreach ($categories as $category) {
                            echo '<option value="' . $category['category_id'] . '">' . $category['name'] . '</option>';
                            }
                            ?>
                     </select>
              </div>
       </div>

       <!-- Þetta er containerinn sem productin birtast í þegar category er valið -->
       <div id="product-window-container" class="text-white">

       </div>


                            





<hr class="my-horizontal-line-black"></hr>    <!-- Línan -->
<hr class="my-horizontal-line"></hr>    <!-- Línan -->

