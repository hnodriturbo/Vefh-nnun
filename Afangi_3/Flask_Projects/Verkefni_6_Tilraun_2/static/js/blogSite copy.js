/////////////////////////////////////*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////////////////-\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
////////////////////////////////////---\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
//////////////////                                      \\\\\\\\\\\\\\\\\\
/////////////////         Author: Hreiðar Pétursson      \\\\\\\\\\\\\\\\\
////////////////                                          \\\\\\\\\\\\\\\\
///////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
//////////////                                              \\\\\\\\\\\\\\
/////////////           ----- Skilaverkefni 6 -----          \\\\\\\\\\\\\
////////////                                                  \\\\\\\\\\\\
///////////     Description: This Script file enhances the     \\\\\\\\\\\
//////////   websites features using Javascript for modifying   \\\\\\\\\\
/////////     & add features to it & enhance the website by      \\\\\\\\\
////////  controlling the interactive features of it and style    \\\\\\\\
/////// the website better by using this script for enhancements   \\\\\\\
////// website or by adding features & help in making this a useful \\\\\\
/////                     and interactive website                    \\\\\
////                                                                  \\\\
////////////////////////////////////---\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////////////////-\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////////////////////////*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


/* The DomContentLoaded is loaded at the end of the loading of the page (eg. Last)*/
document.addEventListener('DOMContentLoaded', function () {


    handleSidebarResize();

    const toggleSidebarBtn = document.getElementById('toggleSidebarBtn');
    
    if (toggleSidebarBtn) {
        toggleSidebarBtn.addEventListener('click', toggleSidebar);
    }


});




function handleSidebarResize() {
    function adjustSidebar() {
        const offcanvasElement = document.getElementById('offcanvasDark');
        if (window.innerWidth >= 992) {
            // Show the offcanvas as a sidebar
            offcanvasElement.classList.add('show');
            offcanvasElement.style.visibility = 'visible';
            offcanvasElement.removeAttribute('tabindex');
        } else {
            // Reset offcanvas behavior
            offcanvasElement.classList.remove('show');
            offcanvasElement.style.visibility = 'hidden';
            offcanvasElement.setAttribute('tabindex', '-1');
        }
    }

    // Initial call to adjust the sidebar based on the current window size
    adjustSidebar();
    // Add event listener to adjust the sidebar on window resize
    window.addEventListener('resize', adjustSidebar);
}






function toggleSidebar() {
    const mainRow = document.getElementById('mainRow');
    const contentColumn = document.getElementById('contentColumn');
    const sidebarColumn = document.getElementById('sidebarColumn');

    if (mainRow.classList.toggle('full-width-content')) {
        setTimeout(() => {
            contentColumn.classList.remove('col-lg-10');
            contentColumn.classList.add('col-lg-12');
        }, 10); // Small delay to ensure smooth transition
        setTimeout(() => {
            sidebarColumn.classList.add('d-none');
        }, 500); // Timeout matches the CSS transition duration
    } else {
        sidebarColumn.classList.remove('d-none');
        setTimeout(() => {
            contentColumn.classList.remove('col-lg-12');
            contentColumn.classList.add('col-lg-10');
        }, 10); // Small delay to ensure smooth transition
    }
}




////// ----------- Here are storage codes below ----------- //////


/* 
function toggleSidebar() {
    const mainRow = document.getElementById('mainRow');
    const contentColumn = document.getElementById('contentColumn');
    const sidebarColumn = document.getElementById('sidebarColumn');

    if (mainRow.classList.toggle('full-width-content')) {

        setTimeout(() => {
            contentColumn.classList.remove('col-lg-10');
            contentColumn.classList.add('col-lg-12');
        }, 500);


        setTimeout(() => {
            sidebarColumn.classList.remove('d-lg-block')
            sidebarColumn.classList.add('d-none');
        }, 500);

    }
    else {
        contentColumn.classList.remove('col-lg-12');
        contentColumn.classList.add('col-lg-10');
        setTimeout(() => {
            sidebarColumn.classList.add('d-lg-block')
            sidebarColumn.classList.remove('d-none');
        }, 500);
    }
}
 */





/* 
function initializeSidebarToggle() {
    const openSidebarBtn = document.getElementById('open-sidebar-btn');
    const closeSidebarBtn = document.getElementById('close-sidebar-btn');
    const sidebar = document.getElementById('offcanvasSidebar');

    openSidebarBtn.addEventListener('click', function() {
        const bsOffcanvas = new bootstrap.Offcanvas(sidebar);
        bsOffcanvas.show();
    });

    closeSidebarBtn.addEventListener('click', function() {
        const bsOffcanvas = bootstrap.Offcanvas.getInstance(sidebar);
        bsOffcanvas.hide();
    });
}
 */


