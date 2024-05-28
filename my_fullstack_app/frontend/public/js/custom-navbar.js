


// public/js/custom-navbar.js


// public/js/custom-navbar.js
/* 
window.addEventListener('load', function() {
    // Function to toggle classes based on screen size
    function toggleNavbarBrandClass() {
        const navbarBrand = document.querySelector('.navbar-brand');
        if (navbarBrand) { // Ensure the element exists
            if (window.innerWidth < 768) {
                navbarBrand.classList.remove('me-auto');
                navbarBrand.classList.add('ms-auto');
            } else {
                navbarBrand.classList.remove('ms-auto');
                navbarBrand.classList.add('me-auto');
            }
        }
    }

    // Throttle function
    function throttle(fn, wait) {
        let time = Date.now();
        return function() {
            if ((time + wait - Date.now()) < 0) {
                fn();
                time = Date.now();
            }
        };
    }

    // Call the function initially
    toggleNavbarBrandClass();

    // Add throttled event listener for window resize
    window.addEventListener('resize', throttle(toggleNavbarBrandClass, 200));
});
 */










/* 
window.addEventListener('load', function() {
    // Function to toggle classes based on screen size
    function toggleNavbarBrandClass() {
        const navbarBrand = document.querySelector('.navbar-brand');
        if (navbarBrand) { // Ensure the element exists
            if (window.innerWidth < 768) {
                navbarBrand.classList.remove('me-auto');
                navbarBrand.classList.add('ms-auto');
                console.log('changed navbar-brand from me-auto to ms-auto')
            } else {
                navbarBrand.classList.remove('ms-auto');
                navbarBrand.classList.add('me-auto');
            }
        }
    }

    // Call the function initially
    toggleNavbarBrandClass();

    // Add event listener for window resize
    window.addEventListener('resize', toggleNavbarBrandClass);
});
 */