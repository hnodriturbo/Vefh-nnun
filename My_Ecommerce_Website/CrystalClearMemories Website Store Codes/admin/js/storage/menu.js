// menu.js

// Function to load content dynamically
function loadContent(url) {
    var container = document.getElementById("content-container");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        container.innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
  }
  
  // Add event listeners to menu items
  var overviewLink = document.getElementById("overview-link");
  overviewLink.addEventListener("click", function() {
    loadContent("overview.html");
  });
  
  var productsLink = document.getElementById("products-link");
  productsLink.addEventListener("click", function() {
    loadContent("products.html");
  });
  
  // Add event listeners to other menu items in a similar manner




  // Function to toggle the offcanvas based on screen size
function toggleOffcanvas() {
  var offcanvas = document.getElementById('offcanvas');
  var screenWidth = window.innerWidth || document.documentElement.clientWidth;

  if (screenWidth <= 992) { // Adjust this breakpoint as needed
    offcanvas.classList.add('show');
  } else {
    offcanvas.classList.remove('show');
  }
}

// Toggle the offcanvas initially
toggleOffcanvas();

// Add event listener for window resize
window.addEventListener('resize', toggleOffcanvas);

  