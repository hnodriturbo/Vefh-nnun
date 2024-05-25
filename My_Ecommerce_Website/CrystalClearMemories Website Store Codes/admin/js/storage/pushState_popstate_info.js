
/* 
When you use window.history.pushState(), you are not making a new request 
to the server. You are simply changing the URL displayed in the address bar.

Here is how pushState() works: */

window.history.pushState(stateObject, title, url);
/* 
stateObject - An object representing the state of the page. It can be any 
serializable object (i.e., an object that can be turned into a string). 
This is useful for storing information that should be available when the 
user navigates back to this state.

title - The new title for the document. Note that most browsers currently 
ignore this parameter, although they may use it in the future.

url - The new URL for the document. This can be a full URL or just a relative path.
*//* 
Using pushState() will not trigger the browser's usual navigation process and 
won't cause the page to reload. Instead, it will just change the URL in the 
address bar. When the user clicks the back button, the browser will navigate 
to the previous URL, and you can listen for this event using the popstate event. */

/* Add an event listener for the 'popstate' event on the window object. 
The 'popstate' event is fired when the user navigates through the browsing 
history (for example, by clicking the browser's back or forward button, or 
by refreshing the page). */

window.addEventListener('popstate', function(event) {
    /* Check if the event object has a 'state' property. The 'state' property 
    contains any state data that was previously pushed onto the history using 
    the history.pushState() method. */
    if (event.state) {
        // If the 'state' property exists, retrieve the value of the 'action' 
        // property from the 'state' object.
        let action = event.state.action;
        /* Call the loadContent() function with the retrieved 'action' value as 
        the parameter. This function typically loads new content into the page 
        based on the specified action. */
        loadContent(action);
    } else {
        /* If the 'state' property does not exist (for example, when the user 
        directly accesses the page without any previous navigation history), 
        call the loadContent() function with the argument 'go-to-index'. This 
        typically loads the default or index content into the page. */
        loadContent('go-to-index');
    }
});


    