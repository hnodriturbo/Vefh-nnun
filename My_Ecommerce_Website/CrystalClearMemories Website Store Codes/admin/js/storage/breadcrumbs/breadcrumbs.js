/*            <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->   */     





    /* --------------------------------------------------------------- */
  /* --------------- THIS BREADCRUMBS CODE WORKED ALMOST --------------- */
/* ----------------------------------------------------------------------- */

// það sem vantaði var smávægileg staðsetningarvandamál og vantaði logo arrow //

// Define the breadcrumb trails for different pages.
/* const breadcrumbPathways = {
    "index": [{name: "Admin Overview", link: "index.php"}],
    "CreateOrderStep1": [
        {name: "Home", link: "index.php"},
        {name: "Add Index", link: "add_index.php"},
        {name: "Create Order", link: "add_order.php"},
        {name: "Step 1 - Basic Info", link: "step1.php"}
    ] *//* ,
    "CreateOrderStep1": ["Admin Overview", "Add Index", "Create Order", "Step 1 - Basic Info"],
    "CreateOrderStep2": ["Admin Overview", "Add Index", "Create Order", "Step 1", "Step 2 - Delivery Info"],
    "CreateOrderStep3": ["Admin Overview", "Add Index", "Create Order", "Step 1", "Step 2", "Step 3 - Add Items"],
    "CreateOrderStep4": ["Admin Overview", "Add Index", "Create Order", "Step 1", "Step 2", "Step 3", "Step 4 - Overview And Confirmation"] */
/* }; */

/**
 * Update the breadcrumbs based on the provided page.
 * @param {string} currentPage - The name/key of the current page.
 */
/* 

function updateBreadcrumbs(currentPage) {
    // Fetch the trail for the current page or default to ["Home"] if not found.
    const currentBreadcrumbTrail = breadcrumbPathways[currentPage] || ["index"];
    // Select the breadcrumb container using jQuery.
    const breadcrumbUIContainer = $(".breadcrumb");
    // Empty out any existing breadcrumbs.
    breadcrumbUIContainer.empty(); 
    // Iterate over each breadcrumb in the current trail.
    currentBreadcrumbTrail.forEach((breadcrumb, index) => {
        let breadcrumbHTML = "";
        // If it's not the first or last breadcrumb, add an arrow icon.
        if (index !== 0 && index !== currentBreadcrumbTrail.length) {
            breadcrumbHTML += '<i class="bi bi-forward" style="color: white;"></i>';
        }
        // If it's the last breadcrumb, add it as plain text. Otherwise, make it a link.
        if (index === currentBreadcrumbTrail.length - 1) {
            breadcrumbHTML += breadcrumb.name;
        } else {
            breadcrumbHTML += `<a href="${base_url}${breadcrumb.link}">${breadcrumb.name}</a>`;
        }
        // Determine the class for the breadcrumb list item.
        // If it's the last breadcrumb, mark it as active.
        let listItemClass = index === currentBreadcrumbTrail.length - 1 ? "breadcrumb-item active" : "breadcrumb-item";
        // Append the breadcrumb to the container.
        breadcrumbUIContainer.append(`<li class="${listItemClass}">${breadcrumbHTML}</li>`);
    });
} */


       
/* 
            $(document).on('click', '#add-order-step-1', function() {
                console.log('add-order-step-1 button clicked');
                let actionInfo = $(this).data('action');
                $.post("add_action.php", {
                    action: actionInfo
                }, function(data) {
                    $("#main-content-container").html(data);
                    updateBreadcrumbs("CreateOrderStep1");
                });
            });

            $(document).on('click', '#add-order-step-2', function() {
                console.log('add-order-step-2 button clicked');
                let actionInfo = $(this).data('action');
                $.post("add_action.php", {
                    action: actionInfo
                }, function(data) {
                    $("#main-content-container").html(data);
                    updateBreadcrumbs("infoStep2");
                });
            });
        });
 */
/* ------------------------------------------------------------------------- */
   /* ---------------- When going forward is clicked ------------------- */
/* ------------------------------------------------------------------------- */
/* 
$(document).ready(function() {
    $(document).on('click', '#create-order-step-1', function() {
        let actionInfo = $(this).data('action');
        $.post("add_action.php", {
            action: actionInfo
        }, function(data) {
            $("#main-content-container").html(data);
            updateBreadcrumbs("CreateOrderStep1");
            window.history.pushState({ page: "CreateOrderStep1" }, '', '/Forritun/Coding/vefverslun/admin/add/add_order_info.php');
        });
    });

    $(document).on('click', '#create-order-step-2', function() {
        let actionInfo = $(this).data('action');
        $.post("add_action.php", {
            action: actionInfo
        }, function(data) {
            $("#main-content-container").html(data);
            updateBreadcrumbs("CreateOrderStep2");
            window.history.pushState({ page: "CreateOrderStep2" }, '', '/Forritun/Coding/vefverslun/admin/add/add_order_info.php');
        });
    });
 */
/* ------------------------------------------------------------------------- */
    /* ---------------- When back button is clicked ------------------- */
/* ------------------------------------------------------------------------- */

/*     window.addEventListener('popstate', function(event) {
        if (event.state) {
            let page = event.state.page;
            console.log(page);
            if (page === "CreateOrderStep1") {
                $.post("add_action.php", {
                    action: 'create-order-step-1'
                }, function(data) {
                    $("#main-content-container").html(data);
                    updateBreadcrumbs("CreateOrderStep1");
                });
            } 
            
            
            else if (page === "CreateOrderStep2") {
                $.post("add_action.php", {
                    action: 'create-order-step-2'
                }, function(data) {
                    $("#main-content-container").html(data);


                    updateBreadcrumbs("CreateOrderStep2");
                });
            } 
            
            
            else if (page === "add_index") {

                $.post('add_action.php', {
                    action: 'add_index'
                }, function(data) {
                    $('main-content-container').html(data);


                    updateBreadcrumbs('add_index')
                })
            }
        }
    }); */



/* 
const mainContent = document.getElementById("main-content-container");

async function updatePageContent(url, pushState=true) {
    try {
        const response = await fetch(url);
        const newContent = await response.text();
        
        const mainContent = document.getElementById("main-content-container");
        if (mainContent) {
            mainContent.innerHTML = newContent;

            const createOrderButton = document.getElementById("create-order-step-1");
            if (createOrderButton) {
                createOrderButton.addEventListener("click", function() {
                    updatePageContent("add_order_info.php");
                });
            }

        } else {
            console.error("Element with ID 'main-content-container' not found in the DOM.");
        }

        if (pushState) {
            history.pushState({url}, null, url);
        }


    } catch (error) {
        console.error("Failed to update page content:", error);
    }
}
 *//* 
$(document).ready(function() {
window.addEventListener("popstate", function(event) {
    if (event.state && event.state.action) {
        updatePageContent(event.state.action);
    }
});

document.getElementById("create-order-step-1").addEventListener("click", function() {
    updatePageContent("add_order_info.php?action=create-order-step-1");
});
document.getElementById("create-order-step-1").addEventListener("click", function() {
    updatePageContent("add_order_info.php?action=create-order-step-1");
});
}); */


