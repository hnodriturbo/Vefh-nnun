/* 
2. Using the Watcher Function:
The Watcher function approach uses an interval to check for 
changes to a specific HTML element or JavaScript variable. */


/* 
Create a function that will check the variable or HTML 
element at regular intervals:  */

/* --------- Það eru 4 aðrar functions í bc_methods ---------  */
   /* ---------- sem gera þetta nákvæmlega sama ---------- */
let previousPage = null;
function watchForChanges() {
  setInterval(() => {
    const currentPage = getTargetValue();
    if (currentPage !== previousPage) {
      previousPage = currentPage;
      updateBreadcrumb();
    }
  }, 500);
}

/* 
Implement the getTargetValue() function to retrieve the current 
page identifier from the target element or variable: */
function getTargetValue() {
  const targetElement = document.getElementById("hiddenElement");
  return targetElement ? targetElement.value : null;
}

/* 
Update the breadcrumb as needed by calling the updateBreadcrumb() 
function (same as in approach 1).*/
/* 

Start watching for changes by calling the watchForChanges() function 
when the page loads: */
document.addEventListener("DOMContentLoaded", function () {
  watchForChanges();
});