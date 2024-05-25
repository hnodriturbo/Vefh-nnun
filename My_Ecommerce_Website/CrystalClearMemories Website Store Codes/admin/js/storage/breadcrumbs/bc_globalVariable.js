/* 
1. Using a Global JavaScript Variable:
You can set a global variable in the JavaScript code that changes 
depending on the current page or view. Then you can use this 
variable to update the breadcrumb accordingly.

Declare the global variable in your script, initially set to the 
default page identifier:
 */

let currentPage = "index";

/* When a user navigates to a new page or state, update the global 
variable with the new page identifier: */
function navigateTo(newPage) {
  currentPage = newPage;
  updateBreadcrumb();
}

/* Implement the updateBreadcrumb() function that uses the currentPage 
variable to determine the breadcrumb trail to display: */
function updateBreadcrumb() {
  const breadcrumbTrails = {
    "index": ["Home"],
    "infoStep1": ["Home", "Order Info", "Step 1"],
    "infoStep2": ["Home", "Order Info", "Step 2"],
    //... continue as needed
  };

  const trail = breadcrumbTrails[currentPage] || ["Home"];
  const breadcrumbElement = document.getElementById("breadcrumb");
  breadcrumbElement.innerHTML = "";

  trail.forEach((crumb, index) => {
    let crumbElement;
    if (index < trail.length - 1) {
      crumbElement = document.createElement("a");
      crumbElement.href = "#" + trail[index];
    } else {
      crumbElement = document.createElement("span");
    }
    crumbElement.innerHTML = crumb;
    breadcrumbElement.appendChild(crumbElement);
    if (index < trail.length - 1) {
      const separator = document.createElement("i");
      separator.className = "separator";
      separator.innerHTML = ">";
      breadcrumbElement.appendChild(separator);
    }
  });
}

/* 
Call the updateBreadcrumb() function when the page loads and 
whenever the currentPage variable is updated: */

document.addEventListener("DOMContentLoaded", function () {
  updateBreadcrumb();
});