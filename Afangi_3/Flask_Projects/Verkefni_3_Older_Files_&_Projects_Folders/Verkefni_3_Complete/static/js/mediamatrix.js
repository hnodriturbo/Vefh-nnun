
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

/*     
    // Setup page Not Found Redirect Countdown
    if (document.getElementById('countdown')) {
        setupPageNotFoundRedirect();
    }
 */
    // This is for the timeout of the flash messages with the class name .alert
    window.setTimeout(function() {
        $(".alert").fadeTo(2000, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 20000);  // Adjust the time here to control after how long the alert should disappear
});



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