/*            <!-- -------------------- ADMIN SÍÐAN --------------------- -->
            <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
          <!-- -------------------------------------------------------------- -->
        <!-- --------------------------- MADE 2023 ---------------------------- -->   */     


/* TABLE OF CONTENTS: */

// 1. MY ANIMATED GLOWING BUTTONS






      /* --------------------------------------------------------------- */
    /* ----------------- MY ANIMATED GLOWING BUTTONS --------------------- */
  /* ----------------------------------------------------------------------- */

     /*  To create the continuous animation effect, the setInterval() function is used.  */
/*  It calls the toggleFromClassToClass() function every 1000 milliseconds (1.000 seconds).  */
          /*  This makes button's class to go back and forth automatically between  */
           /*  .btn-danger and .btn-outline-danger making it a smooth transition. */
                        /* This gives the appearance of an animation.  */


/* Function to toggle the specified classes on the button element */
function toggleFromClassToClass(buttonElement, defaultClass, alternateClass) {
    buttonElement.classList.toggle(defaultClass);
    buttonElement.classList.toggle(alternateClass);
}


/* Get references to the button elements by their respective IDs */
const buttonDanger = document.getElementById('toggle-btn-danger');
const buttonSecondary = document.getElementById('toggle-btn-secondary');
const buttonWarning = document.getElementById('toggle-btn-warning');
const buttonInfo = document.getElementById('toggle-btn-info');
const buttonOutlineWarning = document.getElementById('toggle-btn-outline-warning');

/* Function to enable glowing effect on the specified button element */
function enableGlowing(buttonElement, defaultClass, alternateClass, interval) {
    setInterval(() => toggleFromClassToClass(buttonElement, defaultClass, alternateClass), interval);
}



/* This is to be used in the html to enable the glowing effect */
/* enableGlowing(buttonDanger, 'btn-danger', 'btn-outline-danger', 1000); 
enableGlowing(buttonSecondary, 'btn-secondary', 'btn-outline-secondary', 500);
enableGlowing(buttonWarning, 'btn-warning', 'btn-outline-warning', 1000);
enableGlowing(buttonInfo, 'btn-info', 'btn-outline-info', 500); */
/* function(buttonElement, defaultClass, alternateClass, interval); */

/* smá útskýring á setInterval hérna: */
/* setInterval(() => {
    // Your code or function to be executed repeatedly goes here
}, interval); */
/*  It continuously runs until it is cleared using clearInterval().  */

