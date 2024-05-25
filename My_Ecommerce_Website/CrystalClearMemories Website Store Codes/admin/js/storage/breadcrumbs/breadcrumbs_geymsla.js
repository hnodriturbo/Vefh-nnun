/*            <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->   */     



const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    "items": ["Home", "Order Items", "Step 3"],
    "overview": ["Home", "Order Overview", "Step 4"]
};

let currentState = "index";  // starts with the initial view

function updateBreadcrumbs(state) {
    const trail = breadcrumbTrails[state] || ["Home"];
    const breadcrumbContainer = document.querySelector(".breadcrumb");
    
    breadcrumbContainer.innerHTML = ""; // Clear current breadcrumbs

    trail.forEach((crumb, index) => {
        const li = document.createElement("li");
        li.className = "breadcrumb-item";

        // Insert the forward icon if it's not the last crumb and not the first
        if (index !== 0 && index !== trail.length - 1) {
            const icon = document.createElement("i");
            icon.className = "bi bi-forward";
            li.appendChild(icon);
        }

        if (index === trail.length - 1) {
            li.classList.add("active");
            li.textContent = crumb;
        } else {
            const a = document.createElement("a");
            a.href = "#";
            a.textContent = crumb;
            li.appendChild(a);
        }
        
        breadcrumbContainer.appendChild(li);
    });
}

// Whenever the state of your SPA changes, call the updateBreadcrumbs with the new state:
// For instance:
// updateBreadcrumbs("infoStep1");

        






/* ----------------------------------------------------------------------- */
        /* ----------------- Breadcrumb Icons--------------------- */        
                /* -------------------------------------- */    
            

document.addEventListener('DOMContentLoaded', function() {

    var breadcrumbItems = document.querySelectorAll('.breadcrumb-item:not(:first-child)');

    
    breadcrumbItems.forEach(function(item) {

        var icon = document.createElement('i');
        icon.className = 'bi bi-forward';  

    
        item.querySelector('a').insertBefore(icon, item.querySelector('a').firstChild);
    });
});


    /* ---------------------------------------------------------------- */
    /* ------------- þessi kóði kom annar frá bottanum ------------ */
    /* ---------------------------------------------------------------- */

    const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    "items": ["Home", "Order Items", "Step 3"],
    "overview": ["Home", "Order Overview", "Step 4"]
};

let currentState = "index";  

function updateBreadcrumbs(state) {
    const trail = breadcrumbTrails[state] || ["Home"];
    const breadcrumbContainer = document.querySelector(".breadcrumb");
    
    breadcrumbContainer.innerHTML = ""; 

    trail.forEach((crumb, index) => {
        const li = document.createElement("li");
        li.className = "breadcrumb-item";

    
        if (index !== 0 && index !== trail.length - 1) {
            const icon = document.createElement("i");
            icon.className = "bi bi-forward";
            li.appendChild(icon);
        }

        if (index === trail.length - 1) {
            li.classList.add("active");
            li.textContent = crumb;
        } else {
            const a = document.createElement("a");
            a.href = "#";
            a.textContent = crumb;
            li.appendChild(a);
        }
        
        breadcrumbContainer.appendChild(li);
    });
}

// Whenever the state of your SPA changes, call the updateBreadcrumbs with the new state:
// For instance:
updateBreadcrumbs("infoStep1");
                
                
                
                
                
                
                
                
                
                
    /* ---------------------------------------------------------------- */
/* --------------- þessi kóði kom fyrstur frá bottanum ---------------- */
    /* ---------------------------------------------------------------- */
    
const breadcrumbTrailsFirstVersionFromTheBot = {
    '/': ['Home'], 
    'add_index.php': ['Home', 'Create'],
    'add_order_info': ['Home', 'Create', 'Create New Order', 'Step 1 - Add basic info', 'Step 2 - Add Product Items To Order'],

    
    "/folder1/page1.php": ["Home", "Folder1", "Page1 in Folder1"],
    "/folder1/folder2/page2.php": ["Home", "Folder1", "Folder2", "Page2 in Folder2"],
    
};

function updateBreadcrumbs(currentPage) {
    const trail = breadcrumbTrails[currentPage] || ["Home"] ;
    const breadcrumbContainer = document.querySelector(".breadcrumb");
    
    breadcrumbContainer.innerHTML = ""; 

    trail.forEach((crumb, index) => {
        const li = document.createElement("li");
        li.className = "breadcrumb-item";

        
        if (index !== 0 && index !== trail.length - 1) {
            const icon = document.createElement("i");
            icon.className = "bi bi-forward";
            li.appendChild(icon);
        }

        if (index === trail.length - 1) {
            li.classList.add("active");
            li.textContent = crumb;
        } else {
            const a = document.createElement("a");
            a.href = "#";
            a.textContent = crumb;
            li.appendChild(a);
        }
        
        breadcrumbContainer.appendChild(li);
    });
}

window.onload = function() {
    updateBreadcrumbs(window.location.pathname);
}



    /* -------------------- Breadcrumbs code in progress --------------------- */
/* ------------------------------------------------------------------------- */

const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    "items": ["Home", "Order Items", "Step 3"],
    "overview": ["Home", "Order Overview", "Step 4"]
};

function updateBreadcrumbs(state) {
    const trail = breadcrumbTrails[state] || ["Home"];
    const breadcrumbContainer = $("nav[aria-label='breadcrumb'] .breadcrumb");

    
    breadcrumbContainer.empty(); // Clear current breadcrumbs

    trail.forEach((crumb, index) => {
        let content = "";
        
        // Insert the forward icon if it's not the last crumb and not the first
        if (index !== 0 && index !== trail.length - 1) {
            content += '<i class="bi bi-forward"></i>';
        }

        if (index === trail.length - 1) {
            content += crumb;
        } else {
            content += `<a href="#">${crumb}</a>`;
        }

        let liClass = index === trail.length - 1 ? "breadcrumb-item active" : "breadcrumb-item";
        
        breadcrumbContainer.append(`<li class="${liClass}">${content}</li>`);
    });
}

/* These are my working functions with added execution of updateBreadcrumbs */
$(document).ready(function() {

    $(document).on('click', '#add-order-step-1', function() {
        console.log('add-order-step-1 button clicked');
        let actionInfo = $(this).data('action');
        $.post("add_action.php", {
            action: actionInfo
        }, function(data) {
            $("#main-content-container").html(data);
            updateBreadcrumbs("infoStep1");
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
/* ------------------------------------------------------------------------------ */
/* ------------------------------------------------------------------------------ */
/* ------------------------------------------------------------------------------ */









/* IT IS POSSIBLE TO USE THIS ONE */

const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    "items": ["Home", "Order Items", "Step 3"],
    "overview": ["Home", "Order Overview", "Step 4"]
};

function updateBreadcrumbs(state) {
    const trail = breadcrumbTrails[state] || ["Home"];
    const breadcrumbContainer = $(".breadcrumb");
    
    breadcrumbContainer.empty(); // Clear current breadcrumbs

    trail.forEach((crumb, index) => {
        let content = "";
        
        // Insert the forward icon if it's not the last crumb and not the first
        if (index !== 0 && index !== trail.length - 1) {
            content += '<i class="bi bi-forward"></i>';
        }

        if (index === trail.length - 1) {
            content += crumb;
        } else {
            content += `<a href="#">${crumb}</a>`;
        }

        let liClass = index === trail.length - 1 ? "breadcrumb-item active" : "breadcrumb-item";
        
        breadcrumbContainer.append(`<li class="${liClass}">${content}</li>`);
    });
}

$(document).ready(function() {

    $(document).on('click', '#add-order-step-1', function() {
        console.log('add-order-step-1 button clicked');
        let actionInfo = $(this).data('action');
        $.post("add_action.php", {
            action: actionInfo
        }, function(data) {
            $("#main-content-container").html(data);
            updateBreadcrumbs("infoStep1");
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




/* ---------------------------------------------------------------- */






/* 
$(document).ready(function() { */
    /* --------------------------------------------------------------- */
  /* --------------- THIS BREADCRUMBS CODE WORKED ALMOST --------------- */
/* ----------------------------------------------------------------------- */

// það sem vantaði var smávægileg staðsetningarvandamál og vantaði logo arrow //
/* 
const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    "items": ["Home", "Order Items", "Step 3"],
    "overview": ["Home", "Order Overview", "Step 4"]
};

function updateBreadcrumbs(state) {
    const trail = breadcrumbTrails[state] || ["Home"];
    const breadcrumbContainer = $(".breadcrumb");
    
    breadcrumbContainer.empty(); 

    trail.forEach((crumb, index) => {
        let content = "";
        
      
        if (index !== 0 && index !== trail.length - 1) {
            content += '<i class="bi bi-forward"></i>';
        }

        if (index === trail.length - 1) {
            content += crumb;
        } else {
            content += `<a href="#">${crumb}</a>`;
        }

        let liClass = index === trail.length - 1 ? "breadcrumb-item active" : "breadcrumb-item";
        
        breadcrumbContainer.append(`<li class="${liClass}">${content}</li>`);
    });
}


        $(document).ready(function() {

            $(document).on('click', '#add-order-step-1', function() {
                console.log('add-order-step-1 button clicked');
                let actionInfo = $(this).data('action');
                $.post("add_action.php", {
                    action: actionInfo
                }, function(data) {
                    $("#main-content-container").html(data);
                    updateBreadcrumbs("infoStep1");
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
/* ------------------------------------------------------------------------- */
/* ------------------------------------------------------------------------- */


    



/* THIS IS TO POST VALUES INTO THE add_action.php AND GET RESPONSE FROM SERVER */
        /* AND TRANSITION INTO NEXT STEP - ER EKKI KOMINN SVONA LANGT */

/*     // Transition from Step 1 to Step 2
    $("#add-order-items").click(function() {
        $.post("add_action.php", {
            action: 'add-order-items',
            firstname: $(".order-firstname").val(),
            lastname: $(".order-lastname").val(),
            email: $(".order-email").val(),
            address: $(".address").val(),
            address2: $(".order-address2").val(),
            postalcode: $("order-postalcode").val(),
            city: $("order-city").val(),
            state: $("order-state").val(),
            country: $("order-country").val()

        }, function(data) {
            // Store the received data in the step1Data array
            addOrderInfo.push(data);

            $("#add-order-step-1").hide();
            $("#add-order-step-2").show();
        }, "json"); // We expect the server response to be in JSON format
    });

    // Transition back to Step 1 from Step 2
    $("#goToStep1").click(function() {
        $("#step2").hide();
        $("#step1").show();
    });

    // Finalize the order
    $("#finalizeOrder").click(function() {
        // Store Step 2 data (order items) using class selectors
        let itemData = {
            product_id: $(".item-product_id").val(),
            quantity: $(".item-quantity").val(),
            // ... add other fields as needed
        };

        step2Data.push(itemData);
        finalizeOrder();
    });
 */



/* });  */ /* Document ready function */














/* 
    $("#add-order-step-2").click(function() {
        let firstname = $(".order-firstname").val();
        let lastname = $(".order-lastname").val();
        let email = $(".order-email").val();
        let address = $(".order-address").val();
        let address2 = $(".order-address2").val();
        let postalcode = $(".order-postalcode").val();
        let city = $(".order-city").val();
        let state = $(".order-state").val();
        let country = $(".order-country").val();
        $.post("add_action.php", {
            action: 'proceed_to_step2',
            firstname: firstname,
            lastname: lastname,
            email: email,
            address: address,
            address2: address2,
            postalcode: postalcode,
            city: city,
            state: state,
            country: country
        }, function(data) {
            $("#orderProcess").html(data);
        });
    });
    let orderData = {};  
let orderItems = []; 
    $("#goToStep2").click(function() {
        orderData = {
            firstname: $(".order-firstname").val(),
            lastname: $(".order-lastname").val(),
            email: $(".order-email").val(),
        };
        $("#step1").hide();
        $("#step2").show();
    });
    $("#goToStep1").click(function() {
        $("#step2").hide();
        $("#step1").show();
    });
    $("#finalizeOrder").click(function() {
        orderItems.push({
            product_id: $(".item-product_id").val(),
            quantity: $(".item-quantity").val(),
        });
        finalizeOrder();
    });

 */


/* 
function handleServerResponse(data) {
    switch (data.action) {
        case "redirect":
            window.location.href = data.url;
            break;
        default:
            $("#main-content-container").html(data.content);
            break;
    }
}
 */
/* document.addEventListener('click', function(event) {
    if (event.target.id === "add-order-step-2") {
        console.log("Clicked using document listener");
    }
}); */
