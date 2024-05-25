/* ----- Session Storage - Leið 1 ----- */
const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    //... (continue as needed)
};
/* Whenever the function is called get the currentPage from sessionStorage */
function updateBreadcrumbs() {
    /* USE sessionStorage.getItem TO FETCH THE BREADCRUMB INFO */
    const currentPage = sessionStorage.getItem('currentPage') || "index";
        //... (rest of breadcrumb logic, same as above)
}
/* Set the new currentPage into sessionStorage */
$(document).on('click', '#add-order-step-1', function() {
    sessionStorage.setItem('currentPage', "infoStep1");
    //... (your AJAX code)
    updateBreadcrumbs();
});
/* Set the new currentPage into sessionStorage */
$(document).on('click', '#add-order-step-2', function() {
    sessionStorage.setItem('currentPage', "infoStep2");
    //... (your AJAX code)
    updateBreadcrumbs();
});


  /* -------------------------------- */
/* ----- Session Storage - Leið 2 ----- *//*

Session Storage allows you to store data on the client side, which 
persists for the duration of the page session.

When a user navigates to a new page or state, update the session storage 
with the new page identifier:  */
function navigateTo(newPage) {
  sessionStorage.setItem('currentPage', newPage);
  updateBreadcrumb();
}
/* 
Implement the updateBreadcrumb() function to use the session storage 
to determine the breadcrumb trail to display (same as in approach 1).

Call the updateBreadcrumb() function when the page loads: */
document.addEventListener("DOMContentLoaded", function () {
  updateBreadcrumb();
});


/* ------------------------------------------------------------------------- */
/* ------------------------------------------------------------------------- */

// Storing current page to session storage
sessionStorage.setItem('currentPage', currentPage);

// Retrieving from session storage
const retrievedPage = sessionStorage.getItem('currentPage');

