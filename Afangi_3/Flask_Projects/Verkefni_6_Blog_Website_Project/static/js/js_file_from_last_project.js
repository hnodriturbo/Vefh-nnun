
////////////////////////////////////---\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////        Author: Hreiðar Pétursson        \\\\\\\\\\\\\\\\
///////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
/////////////              -- Skilaverkefni 3 --            \\\\\\\\\\\\\\
///// Description: This script enhances the website with interactive \\\\\
////  features using Bootstrap's JavaScript and custom functionality. \\\\
/// It includes setup for tooltips, infinite scrolling for dynamically \\\
//   loading content, and functionality for handling user interactions  \\
//////////////////// with the accordion component. \\\\\\\\\\\\\\\\\\\\\\\



/* Virkar einfalt þegar dom er hlaðið að þá bara hlaða þessum functions */
/* en sérð neðar að þessi functions eru aldeilis pakki */
document.addEventListener('DOMContentLoaded', function () {


    // First set up tooltips
    if (document.getElementById('tooltip')) {
        setupTooltips();
    }
    

    // Then activate infinite scrolling feature --- Ég lagði mikla vinnu í þetta function !!
    if (document.getElementById('listingRow')) {
        setupInfiniteScrolling();
    }
    loadMoreButton.addEventListener('click', function() {
        fetchMoreListings();  // Manually load more items when the button is clicked
    });
/*     
    if (document.querySelector('.automatic-scrolling')) {
        console.log('i found a element with the automatic-scrolling as a class')
        scrollIndexPageCategoriesRows();
    }
 */
    // Click event listener for accordion
    document.addEventListener('click', function (event) {
        closeAccordionItemsIfClickedOutside(event);
    });


    // This is for the timeout of the flash messages with the class name .alert
    window.setTimeout(function() {
        $(".alert").fadeTo(2000, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 20000);  // Adjust the time here to control after how long the alert should disappear






});



function setupInfiniteScrolling() {
    const listingRow = document.getElementById('listingRow');
    if (!listingRow) {
        console.log('Listing row not found');
        return; // Exit if the listing row is not found
    }

    let currentPage = 1;
    let fetching = false; // Flag to prevent multiple simultaneous requests
    let hasMore = true; // Flag to stop requests if no more data

    const app_route = listingRow.getAttribute('data-app-route'); // 'popular' or 'top_rated'
    const item_type = listingRow.getAttribute('data-item-type'); // 'movie' or 'tv'
    const apiEndpoint = listingRow.getAttribute('data-api-endpoint'); // Get the API endpoint from data attribute

    console.log('app_route:', app_route);
    console.log('item_type:', item_type);
    console.log('API Endpoint:', apiEndpoint);

    const loadMoreButton = document.getElementById('loadMoreButton');
    if (!loadMoreButton) {
        console.log('Load More button not found');
        return; // Exit if no button found
    }

    let autoLoad = true;

    function fetchMoreListings() {
        if (fetching || !hasMore) return;
        console.log('Fetching page:', currentPage + 1); // Log the page being fetched
        fetching = true;
        currentPage++;
    
        let endpoint = `/ajax/listings/${item_type}/${app_route}?page=${currentPage}`;
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                if (data.html) {
                    listingRow.insertAdjacentHTML('beforeend', data.html);
                    manageLoadMoreButton();
                } else {
                    loadMoreButton.style.display = 'none';
                    hasMore = false;
                }
                fetching = false;
            })
            .catch(error => {
                console.error('Error loading items:', error);
                fetching = false;
            });
    }
    
    

    function manageLoadMoreButton() {
        // Check if automatic loading should stop and manual button should show
        if (currentPage % 5 === 0 && hasMore) {
            loadMoreButton.classList.remove('d-none')
            loadMoreButton.classList.add('d-block')
            // loadMoreButton.style.display = 'block';
            autoLoad = false; // Stop automatic loading when button is displayed
        } else {
            if (hasMore) {
                // If there is more data to load and not a 5th page, hide button and continue auto-load
                loadMoreButton.classList.remove('d-block')
                loadMoreButton.classList.add('d-none')
                
                // loadMoreButton.style.display = 'none';
                autoLoad = true;
            } else {
                // If no more data is available, hide the button permanently
                loadMoreButton.classList.remove('d-block')
                loadMoreButton.classList.add('d-none')
                // loadMoreButton.style.display = 'none';
                autoLoad = false; // No more loading is necessary
            }
        }
    }
    

    function nearBottomOfPage() {
        const currentScrollPosition = window.scrollY + window.innerHeight;
        const threshold = document.documentElement.scrollHeight - 200;
        return currentScrollPosition >= threshold;
    }

    function handleScroll() {
        if (autoLoad && nearBottomOfPage()) {
            fetchMoreListings();
        }
    }

    window.addEventListener('scroll', handleScroll);
    loadMoreButton.addEventListener('click', function() {
        fetchMoreListings();
        loadMoreButton.style.display = 'none';
        autoLoad = true; // Re-enable autoLoad after manual button press
    });

    manageLoadMoreButton();
}









// No need for this anymore because i inject error messages through flash in base.html
/* 
function setupPageNotFoundRedirect() {
    const countdownElement = document.getElementById('countdown');
    if (countdownElement) {  // Ensure the element exists on the page
        let seconds = 10;
        const interval = setInterval(() => {
            seconds -= 1;
            countdownElement.textContent = ` ${seconds}`;
            if (seconds <= 0) {
                clearInterval(interval);
                window.location.href = '/';
            }
        }, 1000);
    }
}
 */

/**
 * Setup video controls for the trailer modal
 */

/* 
function setupVideoPlaybackControls() {
    const trailerModal = document.getElementById('trailerModal');
    const trailerIframe = document.getElementById('trailerIframe');

    // Reset the video when the modal is hidden
    if (trailerModal) {
        trailerModal.addEventListener('hide.bs.modal', function () {
            trailerIframe.src = ""; // Clear the source
        });
    }

    // Optional: Re-assign the src when the modal is shown again (if necessary)
    trailerModal.addEventListener('show.bs.modal', function () {
            trailerIframe.src = `https://www.youtube.com/embed/${trailerModal.getAttribute('data-trailer-key')}`;
    });
}


 */



function closeAccordionItemsIfClickedOutside(event) {
    const accordion = document.getElementById('myAccordion');
    if (accordion && !accordion.contains(event.target)) {
        const accordionItems = document.querySelectorAll('#myAccordion .collapse.show');
        accordionItems.forEach(item => {
            new bootstrap.Collapse(item, { toggle: false }).hide();
        });
    }
}



// This shows the counted votes when mouse hovers over the rating of an item in itemn_details.html
function setupTooltips() {
    const selector = '[data-bs-toggle="tooltip"]';
    const elements = [].slice.call(document.querySelectorAll(selector));
    elements.forEach(function (element) {
        new bootstrap.Tooltip(element, {
            trigger: 'hover' // Show tooltip on hover
        });
    });
}







/* 
function fetchMoreListings() {
    if (fetching) return;
    fetching = true;

    // let endpoint = `${apiEndpoint}?page=${currentPage}`; // Construct the correct API endpoint
    currentPage++;

    base_url = `https://api.themoviedb.org/3`
    let endpoint = `/ajax/listings/${item_type}/${app_route}?page=${currentPage}`;  // This should match the Flask route
    
    console.log(`Fetching from endpoint: ${endpoint}`);
    fetch(endpoint)

        // .then(response => response.json())

        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })


        .then(data => {
            if (data.html) {
                listingRow.insertAdjacentHTML('beforeend', data.html);
                
                manageLoadMoreButton();
            } else {
                loadMoreButton.style.display = 'none';
                hasMore = false;
            }
            fetching = false;
        })


        .catch(error => {
            console.error('Error loading items:', error);
            fetching = false;
        });
} // End of fetchMoreListings
 */







/* 
function scrollIndexPageCategoriesRows() {
    const scrollContainer = document.querySelector('.automatic-scrolling'); // Selects the container

    function startScroll() {
        let scrollStep = 3; // Controls the scroll speed
        scrollContainer.scrollBy({ left: scrollStep, behavior: 'smooth' });
    }

    let scrollInterval = setInterval(startScroll, 1); // Initiates the scrolling

    scrollContainer.addEventListener('mouseover', function() {
        clearInterval(scrollInterval); // Stops scrolling when mouse is over the container
    });

    scrollContainer.addEventListener('mouseout', function() {
        scrollInterval = setInterval(startScroll, 1); // Resumes scrolling when mouse leaves the container
    });
}


 */


// Available endpoints according to my navigation_system.py : 

// discover/movie?with_genres=SomeNumberOfGenreForMoviesListings
// discover/tv?with_genres=SomeNumberOfGenreForTVShowsListings
// movie/popular
// movie/top_rated
// tv/popular
// tv/top_rated
/* 
function setupInfiniteScrolling() {

    const listingRow = document.getElementById('listingRow');
    if (!listingRow) {
        console.log('Listing row not found');
        return; // Exit if the listing row is not found
    }

    let currentPage = 1;
    let fetching = false; // Flag to prevent multiple simultaneous requests
    let hasMore = true; // Flag to stop requests if no more data
    


    const app_route = listingRow.getAttribute('data-app-route'); // 'popular' or 'top_rated' or '
    const item_type = listingRow.getAttribute('data-item-type'); // 'movie' or 'tv'
    const apiEndpoint = listingRow.getAttribute('data-api-endpoint'); // Get the API endpoint from data attribute
    console.log('app_route:', app_route); 
    console.log('item_type:', item_type); 
    console.log('API Endpoint:', apiEndpoint); // Check what this logs



    const loadMoreButton = document.getElementById('loadMore');
    if (!loadMoreButton) {
        console.log('Load More button not found');
        return; // Exit if no button found
    }

    let autoLoad = true;


    function fetchMoreListings() {
        if (isFetching) return;
        isFetching = true;
    
        let endpoint = `/ajax/listings/${item_type}/${app_route}?page=${page}`;
    
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                if (data.html) {
                    listingRow.insertAdjacentHTML('beforeend', data.html);
                    page++;
                    manageLoadMoreButton();
                } else {
                    loadMoreButton.style.display = 'none';
                }
                isFetching = false;
            })
            .catch(error => {
                console.error('Error loading items:', error);
                isFetching = false;
            });
    }

    // Managing of the LoadMoreButton
    function manageLoadMoreButton() {
        if (page % 5 === 0) {
            loadMoreButton.style.display = 'block';
            autoLoad = false;
        } else {
            loadMoreButton.style.display = 'none';
            autoLoad = true;
        }
    }
    // Check if user is near the bottom of the page
    function nearBottomOfPage() {
        const currentScrollPosition = window.scrollY + window.innerHeight;
        const threshold = document.documentElement.scrollHeight - 200;
        return currentScrollPosition >= threshold;
    }

    // Handle the scrolling function
    function handleScroll() {
        if (autoLoad && nearBottomOfPage()) {
            fetchMoreListings();
        }
    }

    // At last I put event listener for the scroll and the margin from function nearBottomOfPage :)
    window.addEventListener('scroll', handleScroll);
    loadMoreButton.addEventListener('click', function() {
        fetchMoreListings();
        loadMoreButton.style.display = 'none';
        autoLoad = true; // Re-enable autoLoad after manual button press
    });

} */










/* 
    // This function basicly creates the same card as in listings.html
    function createCardHtml(item) {
        const titleOrName = item.title || item.name;
        const imageUrl = `https://image.tmdb.org/t/p/w780${item.poster_path}`;
        const overview = item.overview.length > 150 ? item.overview.substring(0, 150) + '...' : item.overview;
        const releaseDate = item.release_date || item.first_air_date || 'N/A';
        const detailsUrl = `/details/${item.title ? 'movie' : 'tv'}/${item.id}`;

        return `
            <div class="col-sm-6 col-md-3 mb-4">
                <div class="card bg-secondary h-100 border-radius-15">
                    <div class="d-flex justify-content-center" style="max-height: 100%;">
                        <div style="width: 300px; height: 300px; overflow: hidden; border-radius: 15px;">
                            <img src="${imageUrl}" class="card-img-top img-fluid" alt="${titleOrName}" style="object-fit: cover; width: 100%; height: 100%;">
                        </div>
                    </div>
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title bold-text">${titleOrName}</h5>
                        <p class="card-text">${overview}</p>
                        <div class="mt-1">
                            <p class="card-text semi-bold-text">Release Date: ${releaseDate}</p>
                        </div>
                    </div>
                    <div class="card-footer">
                        <a href="${detailsUrl}" class="btn btn-dark w-100">See More Details</a>
                    </div>
                </div>
            </div>
        `;

    } // End of function createCardHtml

 */

/* 
This setup allows your application to dynamically adjust to user interactions based on the structured navigation data. It keeps your code organized and makes it easier to add new categories or types of content.

### JavaScript for Infinite Scrolling

To integrate infinite scrolling, you’ll need some frontend JavaScript that fetches the next page of data when the user scrolls near the bottom of the page. Here’s a basic outline of how you might approach this:

```javascript
document.addEventListener('scroll', function() {
    const scrollTop = document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight;
    const clientHeight = document.documentElement.clientHeight;

    // Check if scrolled to the bottom of the page
    if (scrollTop + clientHeight >= scrollHeight - 5) {
        // Assume a function that fetches the next page and updates the content
        fetchNextPage();
    }
});

function fetchNextPage() {
    // Increment the page number
    const nextPage = parseInt(currentPage) + 1;

    // Fetch new data using the API endpoint (you need to modify the server to handle this)
    fetch(`/api/data?page=${nextPage}`)
    .then(response => response.json())
    .then(data => {
        // Append new data to the existing content
        const items = data.results;
        const container = document.getElementById('item-container');
        items.forEach(item => {
            const div = document.createElement('div');
            div.innerHTML = item.title; // Adjust based on your data structure
            container.appendChild(div);
        });
        // Update the current page
        currentPage = nextPage;
    })
    .catch(err => console.error('Error fetching data:', err));
}


*/