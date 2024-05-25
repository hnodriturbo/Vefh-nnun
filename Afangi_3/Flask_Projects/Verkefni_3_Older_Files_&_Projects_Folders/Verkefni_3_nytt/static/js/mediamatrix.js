
////////////////////////////////////---\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////////        Author: Hreiðar Pétursson        \\\\\\\\\\\\\\\\
///////////////         Course:  Vefhönnun Áfangi 3        \\\\\\\\\\\\\\\
/////////////              -- Skilaverkefni 3 --            \\\\\\\\\\\\\\
///// Description: This script enhances the website with interactive \\\\\
////  features using Bootstrap's JavaScript and custom functionality. \\\\
/// It includes setup for tooltips, infinite scrolling for dynamically \\\
//   loading content, and functionality for handling user interactions  \\
//////////////////// with the accordion component. \\\\\\\\\\\\\\\\\\\\\\\


/* Skilaboð til Danna þegar þú lest þetta skjal */

/* 
Sannleikurinn er sá að auðvitað fékk ég hjálp frá gervigreind til að finna
út úr ýmsum göllum í þessari hönnun en ég er farinn að kunna svolítið í
javascript sem er geggjað og langaði mér að nýta þetta víst við erum að
kynna okkur að nota API í gegnum python og flask. Ég ætlaði upphaflega
bara að hafa tooltips þegar músin fer yfir einkunn á mynd eða þátt að þá
kemur upp lítill gluggi hjá músinni sem segir hversu mörg atvkæði voru
kosin fyrir viðkomandi titil. Svo langaði mér bara gera meira og meira
og niðurstaðan var þetta, infinite scrolling og það var flókið en mér
tókst það fyrir rest. Ég vonandi er bara búinn klára öll verkefnin með
þessari síðu sem ég gerði en ég ákvað að gera frekar flotta og fullkomna
síðu. Vona þér líki við hana og þú skemmtir þér við að lesa kóðann.
*/


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
    


    // Click event listener for accordion
    document.addEventListener('click', function (event) {
        closeAccordionItemsIfClickedOutside(event);
    });

    
    // Setup page Not Found Redirect Countdown
    if (document.getElementById('countdown')) {
        setupPageNotFoundRedirect();
    }


});






/* 
    // Initialize Swiper
    if (document.querySelector('.swiper-container')) {
        new Swiper('.swiper-container', {
            loop: true,
            pagination: { el: '.swiper-pagination' },
            navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
            scrollbar: { el: '.swiper-scrollbar' },
        
        });
        console.log(Swiper)
    }

    // Activate auto-scrolling if carousel is present
    if (document.getElementById('carouselContainer')) {
        setupAutoScrolling();
    }

 */



/* 
function setupAutoScrolling() {
    let scrollInterval;
    const startAutoScroll = () => {
        scrollInterval = setInterval(() => {
            let scrollWidth = $('.swiper-wrapper').width();
            $('.swiper-wrapper').animate({scrollLeft: '+=' + scrollWidth}, 1000, function() {
                // Check if scrolled to the end
                if ($('.swiper-wrapper').scrollLeft() + $('.swiper-container').width() >= $('.swiper-wrapper')[0].scrollWidth) {
                    clearInterval(scrollInterval);
                    setTimeout(startAutoScroll, 10000); // Pause for 10 seconds
                }
            });
        }, 2000);
    };

    startAutoScroll();
}

 */







/* 
    // Initialize carousels
    if (document.getElementById('carouselContainer')) {
        setupCarousels();
    }
 */
/* 
    $('.carousel').carousel({
        pause: "hover",
        interval: 5000  // Adjust time interval or disable auto-playing
    });
     */

/* 
$(document).ready(function() {
    $('#itemCarousel').hover(
        function() { $(this).carousel('pause'); },
        function() { $(this).carousel('cycle'); }
    );

    // Configure to only advance one item at a time
    $('.carousel').carousel({
        interval: false
    });

    // Implement "Load More" functionality if needed
});
 */
/* 
function setupCarousels() {
    $('.carousel').carousel({
        interval: 5000,
        wrap: true
    });
}

 */
function setupInfiniteScrolling() {
    
    let page = 1;
    
    /* const item_type = document.getElementById('listingRow').dataset.listingType; */

    const loadMoreButton = document.getElementById('loadMore');
    
    const listingRow = document.getElementById('listingRow');

    let isFetching = false;

    if (!loadMoreButton) {
        console.log('Load More button not found');
        return; // Exit if no button found
    }

    let autoLoad = true;

    function fetchMoreListings() {
        if (isFetching) return; // Prevent multiple simultaneous fetches
        isFetching = true;

        const pathSegments = window.location.pathname.split('/');
        const item_type = pathSegments[2];  // e.g., 'tv'
        const category = pathSegments[3];   // e.g., 'genre'
        const genre_id = pathSegments[4];   // e.g., '12345' (only present if applicable)
    
        let endpoint = `/ajax/listings/${item_type}?page=${page}`;
        if (category) {
            endpoint += `&category=${category}`;
        }
        if (genre_id) {
            endpoint += `&genre_id=${genre_id}`;
        }
    
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    data.forEach(item => {
                        const cardHtml = createCardHtml(item);
                        listingRow.insertAdjacentHTML('beforeend', cardHtml);
                    });
                    page++
                    manageLoadMoreButton();
                }
                else {
                    loadMoreButton.style.display = 'none'; // Hide if no more items
                }
                isFetching = false;
            })
            .catch(error => {
                console.error('Error loading items: ', error);
                isFetching = false
            });
    }

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


    // Managing of the LoadMoreButton
    function manageLoadMoreButton() {
        if (page % 2 === 0 && page >= 4) {
            loadMoreButton.style.display = 'block'; // Show load more button every 5 pages
            autoLoad = false;
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

}




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






function closeAccordionItemsIfClickedOutside(event) {
    // Check if the click happened outside of the accordion
    const isClickInsideAccordion = document.getElementById('myAccordion').contains(event.target);
  
    // If click is not inside a accordion then close it
    if (!isClickInsideAccordion) {
        // Close all accordion items
        const accordionItems = document.querySelectorAll('#myAccordion .collapse.show');
        accordionItems.forEach(item => {
            new bootstrap.Collapse(item, {
                toggle: false
            }).hide();
        });
    }
}






function setupTooltips() {
    const selector = '[data-bs-toggle="tooltip"]';
    const elements = [].slice.call(document.querySelectorAll(selector));
    elements.forEach(function (element) {
        new bootstrap.Tooltip(element, {
            trigger: 'hover' // Show tooltip on hover
        });
    });
}



















// ***** ***** Storage Code ***** ***** //
    // ***** ***** Storage Code ***** ***** //
        // ***** ***** Storage Code ***** ***** //
            // ***** ***** Storage Code ***** ***** //
                // ***** ***** Storage Code ***** ***** //
                    // ***** ***** Storage Code ***** ***** //
                // ***** ***** Storage Code ***** ***** //
            // ***** ***** Storage Code ***** ***** //
        // ***** ***** Storage Code ***** ***** //
    // ***** ***** Storage Code ***** ***** //
// ***** ***** Storage Code ***** ***** //






/* 
    // This tells whether user is near the bottom
    function nearBottomOfPage() {
        const pageOffset = window.scrollY + window.innerHeight;
        const scrollPosition = window.innerHeight + window.scrollY;
        const threshold = document.body.offsetHeight - 200; // 200px from the bottom
        return scrollPosition >= threshold;
    }
     */





/* 

var swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    // If you want pagination
    pagination: {
      el: '.swiper-pagination',
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    // And if you need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });
 */







/* 
// Enables the infinite scrolling feature, allowing users to load more content as they scroll near the bottom of the page.
function setupInfiniteScrolling() {
    let currentPage = 1;
    let isLoading = false;
    const rowContainer = document.querySelector('#listingRow'); // ADJUST MAYBE
    const listingType = rowContainer.getAttribute('data-listing-type'); // Dynamic handling of listings


    // This tells whether user is near the bottom
    function nearBottomOfPage() {
        const scrollPosition = window.innerHeight + window.scrollY;
        const threshold = document.body.offsetHeight - 200; // 200px from the bottom
        return scrollPosition >= threshold;
    }

    async function fetchMoreListings() {
        if (isLoading || !nearBottomOfPage()) return;
        isLoading = true;

        currentPage++; // Increment the page count to fetch the next page

        fetch(`/ajax/listings/${listingType}?page=${currentPage}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                if (data.items && Array.isArray(data.items) && data.items.length) {
                    data.items.forEach(item => {
                        const cardHTML = createCardHtml(item);
                        rowContainer.insertAdjacentHTML('beforeend', cardHTML);
                    });
                } else {
                    console.log('No more items to load.'); // Handle end of data or empty array
                    window.removeEventListener('scroll', handleScroll); // Remove scroll listener if no more data
                }
                isLoading = false;
            })
            .catch(error => {
                console.error('Error fetching more listings:', error);
                isLoading = false;
            });
    } // End of async function fetchMoreListings()

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

    // Handle the scrolling function
    function handleScroll() {
        if (nearBottomOfPage()) {
            fetchMoreListings();
        }
    }
    // At last I put event listener for the scroll and the margin from function nearBottomOfPage :)
    window.addEventListener('scroll', handleScroll);

} // End of function setupInfiniteScrolling()

 */






/* 


function setupInfiniteScrolling() {
    let currentPage = 1;
    let isLoading = false;
    const rowContainer = document.querySelector('#listingRow'); // Ensure this matches your container
    const listingType = rowContainer.getAttribute('data-listing-type'); // Dynamic type retrieval

    function isNearBottom() {
        const buffer = 200; // Distance from the bottom to trigger loading more items
        const currentScrollPosition = window.scrollY + window.innerHeight;
        const threshold = document.documentElement.scrollHeight - buffer;
        return currentScrollPosition >= threshold;
    }

    async function fetchMoreListings() {
        if (isLoading || !isNearBottom()) return;
        
        isLoading = true; // Set the loading state

        // Construct the API URL dynamically based on the endpoint building in the python data.py function
        let url = `/ajax/listings/${listingType}?category=${category}&page=${currentPage}`;
        if (category === 'genre' && genreId) {
            url = `/ajax/listings/${listingType}?category=genre&genre_id=${genreId}&page=${currentPage}`;
        } else {
            url = `/ajax/listings/${listingType}?category=${category}&page=${currentPage}`;
        }
        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.items && Array.isArray(data.items)) {
                    data.items.forEach(item => {
                        const cardHTML = createCardHtml(item);
                        rowContainer.insertAdjacentHTML('beforeend', cardHTML);
                    });
                    currentPage++; // Only increment the page if there are items
                } else {
                    console.error('No items or incorrect data format received:', data);
                }
                isLoading = false; // Reset loading state
            })
            .catch(error => {
                console.error('Error fetching more listings: ', error);
                isLoading = false;
            });
    }

    function handleScroll() {
        if (isNearBottom()) {
            fetchMoreListings();
        }
    }

    window.addEventListener('scroll', handleScroll);
}





 */









/* 
function setupInfiniteScrolling(listingType, category, genreId) {
    let currentPage = 1;
    let isLoading = false;
    const rowContainer = document.querySelector('#listingRow');

    function isNearBottom() {
        const buffer = 200;
        const currentScrollPosition = window.scrollY + window.innerHeight;
        const threshold = document.documentElement.scrollHeight - buffer;
        return currentScrollPosition >= threshold;
    }

    function fetchMoreListings() {
        if (isLoading || !isNearBottom()) return;
        
        isLoading = true;

        let url = `/ajax/listings/${listingType}?category=${category}&page=${currentPage}`;
        if (genreId) {
            url += `&genre_id=${genreId}`;  // Add genre ID if available
        }

        fetch(url)
            .then(response => {
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                return response.json();
            })
            .then(data => {
                if (data && data.length > 0) {
                    data.forEach(item => {
                        const cardHTML = createCardHtml(item);
                        rowContainer.insertAdjacentHTML('beforeend', cardHTML);
                    });
                    currentPage++;
                } else {
                    console.error('No items or incorrect data format received:', data);
                }
                isLoading = false;
            })
            .catch(error => {
                console.error('Error fetching more listings:', error);
                isLoading = false;
            });
    }

    window.addEventListener('scroll', fetchMoreListings);
}

 */


















/* 
let seconds = 5;
const countdownElement = document.getElementById('countdown');
const interval = setInterval(() => {
    seconds -= 1;
    countdownElement.textContent = ` ${seconds}`;
    if (seconds <= 0) {
        clearInterval(interval);
        window.location.href = '/';
    }
}, 1000);


 */









/* 
    // At last I put event listener for the scroll and the margin from function nearBottomOfPage :)
    window.addEventListener('scroll', () => {
        if (nearBottomOfPage()) {
            fetchMoreListings();
        }
    });
 */

/* 

// Initial activation for existing elements
document.addEventListener('DOMContentLoaded', function () {
    enableTooltips('[data-bs-toggle="tooltip"]'); 
});


 */


/* 
async function fetchMoreListings() {
    if (isLoading) return;
    isLoading = true;

    currentPage ++; // Increment the page count to fetch the next page

    fetch(`/ajax/listings/${listingType}?page=${currentPage}`)
        .then(response => response.json())
        .then(data => {
            if (data.items && Array.isArray(data.items)) {
                data.items.forEach(item => {
                    const cardHTML = createCardHtml(item);
                    rowContainer.insertAdjacentHTML('beforeend', cardHTML);
                });
            } else {
                console.error('No items or incorrect data format received:', data);
            }
            isLoading = false;
        })
        .catch(error => {
            console.error('Error fetching more listings: ', error);
            isLoading = false;
        });
} // End of async function fetchMoreListings()

 */

/* 
// Enables the infinite scrolling feature, allowing users to load more content as they scroll near the bottom of the page.
function setupInfiniteScrolling() {
    let currentPage = 1;
    let isLoading = false;
    const rowContainer = document.querySelector('#listingRow'); // Use ID for specific targeting
    const listingType = rowContainer.getAttribute('data-listing-type');

    function nearBottomOfPage() {
        const lastCard = rowContainer.lastElementChild; // Get the last element in the container
        const lastCardOffset = lastCard.offsetTop + lastCard.clientHeight;
        const pageOffset = window.pageYOffset + window.innerHeight;
        console.log('Last Card Offset:', lastCardOffset, 'Page Offset:', pageOffset);
        return pageOffset >= lastCardOffset - 20; // More sensitive triggering
    }

    async function fetchMoreListings() {
        console.log('Checking if loading or bottom:', isLoading, nearBottomOfPage());
        if (isLoading || !nearBottomOfPage()) return;
        isLoading = true;
        console.log('Fetching page:', currentPage + 1);
        currentPage++;

        fetch(`/ajax/listings/${listingType}?page=${currentPage}`)
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok.');
                return response.json();
            })
            .then(items => {
                console.log('Items received:', items.length);
                if (!items.length) {
                    window.removeEventListener('scroll', handleScroll); // No more items to load
                    return;
                }
                items.forEach(item => {
                    const cardHTML = createCardHtml(item);
                    rowContainer.insertAdjacentHTML('beforeend', cardHTML);
                });
                isLoading = false;
            })
            .catch(error => {
                console.error('Error fetching more listings:', error);
                isLoading = false;
            });
    }

    function handleScroll() {
        if (nearBottomOfPage()) {
            fetchMoreListings();
        }
    }

    window.addEventListener('scroll', handleScroll);
}


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
}
 */

/* 
function enableTooltips(selector) {
    const elements = [].slice.call(document.querySelectorAll(selector));
    elements.map(function (element) {
        return new bootstrap.Tooltip(element, {
            trigger: 'hover' // This specifies that the tooltip should show on hover
        });
    });
}

 */







/* document.addEventListener('DOMContentLoaded', function () {
    const navButtons = document.querySelectorAll('.my-navbtn-styles');

    navButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Use data-target attribute instead of href
            const targetSelector = this.getAttribute('data-target');
            const target = document.querySelector(targetSelector);
            
            if (target) {
                const isOpen = target.classList.contains('show');
                
                if (!isOpen) {
                    const parentAccordion = target.getAttribute('data-bs-parent');
                    const siblingCollapses = document.querySelectorAll(`${parentAccordion} .collapse.show`);
                    
                    siblingCollapses.forEach(collapse => {
                        new bootstrap.Collapse(collapse, { toggle: true });
                    });
                }
            } else {
                console.error('Invalid target for accordion toggle:', targetSelector);
            }
        });
    });
});
 */

/* document.addEventListener('DOMContentLoaded', function () {
    // Assuming 'document.body' is the static parent element present at page load.
    // You can replace 'document.body' with a closer static parent if known.
    document.body.addEventListener('click', function (event) {
        const button = event.target.closest('.my-navbtn-styles');

        if (button) {
            const targetSelector = button.getAttribute('data-target');
            const target = document.querySelector(targetSelector);

            if (target) {
                const isOpen = target.classList.contains('show');
                
                if (!isOpen) {
                    const parentAccordion = target.getAttribute('data-bs-parent');
                    const siblingCollapses = document.querySelectorAll(`${parentAccordion} .collapse.show`);
                    
                    siblingCollapses.forEach(collapse => {
                        new bootstrap.Collapse(collapse, { toggle: true });
                    });
                }
            } else {
                console.error('Invalid target for accordion toggle:', targetSelector);
            }
        }
    });
});
 */
