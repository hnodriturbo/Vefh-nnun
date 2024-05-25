function validateFullName(inputField) {
    let isValid = inputField.val().trim() !== '';
    inputField.toggleClass('is-invalid', !isValid);
    inputField.toggleClass('is-valid', isValid);
}

function validateEmail(inputField) {
    let isValid = inputField.val().trim() !== '' && inputField.is(':valid');
    inputField.toggleClass('is-invalid', !isValid);
    inputField.toggleClass('is-valid', isValid);
}

function validateCheckboxes(checkboxName) {
    let checkboxes = $(`input[name="${checkboxName}"]`);
    let isValid = checkboxes.is(':checked');
    checkboxes.removeClass('is-invalid is-valid').addClass(isValid ? 'is-valid' : 'is-invalid');
}

// Full Name Validation
$('#speakerName').on('focus keyup', function() {
    validateFullName($(this));
});

// Email Validation
$('#speakerEmail').on('focus keyup', function() {
    validateEmail($(this));
});

// Checkbox Validation - assuming the name of your checkboxes is 'dayOptions'
$('input[name="dayOptions"]').on('click', function() {
    validateCheckboxes('dayOptions');
});

// You can create similar bindings for other input fields as needed.

// Form submission should not be allowed until all fields are valid.
$('#speakerRegistrationForm').on('submit', function(e) {
    e.preventDefault(); // Prevent the default form submission.

    // Perform the validation for all fields
    validateFullName($('#speakerName'));
    validateEmail($('#speakerEmail'));
    validateCheckboxes('dayOptions');

    // Check if the form is valid
    let formIsValid = !$(this).find('.is-invalid').length;
    if(formIsValid) {
        console.log('Form is valid. Ready to submit.');
        // Here you would typically submit the form or perform other actions.
    } else {
        console.log('Form is not valid.');
        // Handle the invalid form case, perhaps by scrolling to the first invalid input.
    }
});