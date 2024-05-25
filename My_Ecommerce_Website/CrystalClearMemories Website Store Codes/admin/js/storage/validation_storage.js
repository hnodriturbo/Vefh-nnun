
function validateInput(inputField) {
    inputField.get(0).setCustomValidity(''); // Clear any custom validity messages
    inputField.removeClass('is-invalid'); // Remove the 'is-invalid' class
    inputField.removeClass('is-valid'); // Remove the 'is-valid' class

    // Validate the specific input field that triggered the event
    if (inputField.get(0).checkValidity()) {
        inputField.addClass('is-valid'); // Add the 'is-valid' class
    } else {
        inputField.addClass('is-invalid'); // Add the 'is-invalid' class
    }
}

$('.needs-validation .form-control').on('focus', function() {
    let inputField = $(this);

    validateInput(inputField); // Validate immediately on focus

    input.on('input', function() {
        validateInput(inputField); // Validate on further input
    });

    // Remove the input event handler when the field loses focus
    inputField.on('blur', function() {
        inputField.off('input');
    });
});    
$(document).on('focus', '.needs-validation .form-control', function() {
    
    $(this).on('input', function () {
        let input = $(this);
        let form = input.closest('.needs-validation');
        form.addClass('was-validated'); // Mark the form as having been validated

        // Validate the specific input field that triggered the event
        if (this.checkValidity()) {
            input.removeClass('is-invalid');
            input.addClass('is-valid');
        } else {
            input.removeClass('is-valid');
            input.addClass('is-invalid');
        }
    });
});
// Remove the input event listener when the field loses focus
$(document).on('blur', '.needs-validation .form-control', function() {
    $(this).off('input');
})


$('.needs-validation .form-control').on('focus', function() {
    let input = $(this);
    input.on('input', function() {
        let form = input.closest('.needs-validation');
        form.addClass('was-validated');

        // Validate the specific input field that triggered the event
        if (this.checkValidity()) {
            input.removeClass('is-invalid'); // Remove the 'is-invalid' class
            input.addClass('is-valid'); // Add the 'is-valid' class
        } else {
            input.removeClass('is-valid'); // Remove the 'is-valid' class
            input.addClass('is-invalid'); // Add the 'is-invalid' class
        } 
    });
});

    // Validate the specific input field that triggered the event
    if(this.checkValidity()) {
        this.setCustomValidity(''); // Clear any custom validation messages
        this.classList.remove('is-invalid'); // Remove the 'is-invalid' class        
    } else {
        this.setCustomValidity('This field is required');
        this.classList.add('is-invalid');
    }
    
    let formElement = $(this).closest('.needs-validation');
    if (formElement.length) {
      let form = formElement[0];
      if (form.checkValidity()) {
        form.classList.remove('was-validated');
      } else {
        form.classList.add('was-validated');
      }
    }
    