

/* ----------- Leið 1 - Hidden HTML ----------- */

/* This is just used to store info in the html */
/* Needed to be in every page i make */
/* <input type="hidden" id="currentPage" value="index"> */

function updateBreadcrumbs() {
    const currentPage = $("#currentPage").val();
        //... (rest of breadcrumb logic, same as above)
    };
$(document).on('click', '#add-order-step-1', function() {
    $("#currentPage").val("infoStep1");
    //... (your AJAX code)
    updateBreadcrumbs();
});
$(document).on('click', '#add-order-step-2', function() {
    $("#currentPage").val("infoStep2");
    //... (your AJAX code)
    updateBreadcrumbs();
});


  /* ----------- Leið 2 - Hidden HTML ------------ */
/* ------------ and watch for changes -------------- */

/* 2. Hidden HTML Elements and Watch for Changes: *//*
This approach is similar to the Watcher function but uses the 
MutationObserver API to detect changes in the DOM.


Create a hidden input element with an initial value representing 
the default page identifier: */

/* <input type="hidden" id="hiddenElement" value="index" /> *//* 

Update the hidden input element value when the user navigates to 
a new page or state: */

function navigateTo(newPage) {
  const hiddenElement = document.getElementById("hiddenElement");
  hiddenElement.value = newPage;
}

/* Implement the updateBreadcrumb() function (same as in approach 1). *//* 

Use a MutationObserver to watch for changes to the hidden input 
element and call the updateBreadcrumb() function when it changes: */
const observer = new MutationObserver(function (mutationsList) {
  for (let mutation of mutationsList) {
    if (mutation.type === "attributes" && mutation.attributeName === "value") {
      updateBreadcrumb();
    }
  }
});

const hiddenElement = document.getElementById("hiddenElement");
observer.observe(hiddenElement, { attributes: true });

document.addEventListener("DOMContentLoaded", function () {
  updateBreadcrumb();
});





  /* ----------- Leið 3 - Hidden HTML ----------- */
   /* Another Common Way: Using Data Attributes: */

/* <body data-current-step="index"> */

/* JavaScript of using data attributes in the HTML: */
function updateBreadcrumbsFromDataAttr() {
  let step = document.body.getAttribute('data-current-step');
  updateBreadcrumbs(step);
}

function changeStep(step) {
  document.body.setAttribute('data-current-step', step);
  updateBreadcrumbsFromDataAttr();
}

// You can also listen for changes on the attribute if required:
const bodyObserverOptions = {
attributes: true,
attributeFilter: ['data-current-step']
};

const bodyCallback = function(mutationsList) {
  for(let mutation of mutationsList) {
      if (mutation.type === 'attributes') {
          updateBreadcrumbsFromDataAttr();
      }
  }
};

const bodyObserver = new MutationObserver(bodyCallback);
bodyObserver.observe(document.body, bodyObserverOptions);