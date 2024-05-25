
   /* ----------------------------------------------- */
/* ---------- Function to watch page changes ----------- */
   /* ----------------------------------------------- */
let lastKnownStep = '';
function watchStepChange() {
    if (currentStep !== lastKnownStep) {
        lastKnownStep = currentStep;
        updateBreadcrumbs(lastKnownStep);
    }
}
setInterval(watchStepChange, 1000);  // Check every second

   /* ----------------------------------------------- */
/* ---------- Function to watch page changes ----------- */
   /* ----------------------------------------------- */

let currentPage = '';
function checkForPageChange() {
  const newPage = ... // Logic to determine the current page or step.
  if (newPage !== currentPage) {
    currentPage = newPage;
    updateBreadcrumbs(currentPage);
  }
}
setInterval(checkForPageChange, 1000);  // Check every second.

   /* ----------------------------------------------- */
/* ---------- Function to watch page changes ----------- */
   /* ----------------------------------------------- */

let lastKnownStep = '';
function watchStepChange() {
    let currentStep;
    // For the input method:
    currentStep = document.getElementById('currentStep').value;
    // OR for the data attribute method:
    // currentStep = document.getElementById('breadcrumbTracker').getAttribute('data-step');
    if (currentStep !== lastKnownStep) {
        lastKnownStep = currentStep;
        updateBreadcrumbs(lastKnownStep);
    }
}
setInterval(watchStepChange, 1000);  // Check every second

   /* ----------------------------------------------- */
/* ---------- Function to watch page changes ----------- */
   /* ----------------------------------------------- */
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







          /* ------------------------------- */
        /* ----------------------------------- */
      /* --------------------------------------- */
    /* ------------------------------------------- */
  /* --------------- 4 GÓÐAR LEIÐIR ---------------- */
/* --------------------------------------------------- */

/* -------------- LEIÐ 1 --------------- */
/* 1. Using the Global JavaScript Variable with Event Emission: */

/* a) Setting the Variable: */
let currentStep = 'index';

/* b) Setting an Event Listener: */
document.addEventListener('stepChanged', function(e) {
    updateBreadcrumbs(e.detail.newStep);
});

/* c) Updating the Variable and Emitting an Event: */
function changeStep(step) {
    currentStep = step;
    document.dispatchEvent(new CustomEvent('stepChanged', { detail: { newStep: currentStep }}));
}

// Use this function to change the breadcrumb:
changeStep('infoStep1');


/* -------------- LEIÐ 2 --------------- */
/* 2. Using Hidden HTML Elements with MutationObserver: */

/* a. The HTML: */
/* <input type="hidden" id="currentStep" value="index"> */

/* b. The JS: */
const targetNode = document.getElementById('currentStep');

const observerOptions = {
  attributes: true,
  attributeFilter: ['value']
};

const callback = function(mutationsList) {
    for(let mutation of mutationsList) {
        if (mutation.type === 'attributes') {
            updateBreadcrumbs(targetNode.value);
        }
    }
};

const observer = new MutationObserver(callback);
observer.observe(targetNode, observerOptions);

// Use this function to change the breadcrumb:
function changeStep(step) {
    document.getElementById('currentStep').value = step;
}





/* -------------- LEIÐ 3 --------------- */
/* 3. Using the History API for SPAs: */
/* a) JavaScript: */
window.addEventListener('popstate', function(event) {
    let currentPage = window.location.pathname; 
    updateBreadcrumbs(currentPage);
});

// Assuming you have some routing mechanism to change the URL:
function goToPage(page) {
    window.history.pushState({}, '', page);
    updateBreadcrumbs(page);
}
// Use this function to navigate:
goToPage('/infoStep1');





/* 
Recommendation:
For SPAs, the History API method is usually the most suitable 
since it aligns with how SPAs work by manipulating browser 
history without full page reloads.

For regular sites or if you want to keep things simple and in 
the DOM, the Data Attributes method is clean and easy to understand. 
It has the benefit of storing state visibly in the DOM which can be 
inspected and debugged easily.

Global JavaScript Variable with Event Emission and Hidden HTML 
Elements with MutationObserver are also robust methods. The choice 
between them could depend on personal preference and project 
requirements.

A big deciding factor could be whether you prefer storing state in 
the DOM (which is more inspectable and ties closely with the visual 
representation of the page) or in JavaScript (which may offer 
more flexibility but is slightly removed from the DOM). */

