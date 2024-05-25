$(document).ready(function () {


  function validateInput(inputField) {
      // If the input has data-validate=true, then check its validity
      if (inputField.data('validate')) {
          let validity = inputField.get(0).checkValidity();
          inputField.removeClass('is-invalid is-valid').addClass(validity ? 'is-valid' : 'is-invalid');
      }
  }


  // Function to validate checkbox groups
  function validateCheckboxGroup(checkboxGroup) {
    let isChecked = checkboxGroup.find('input[type="checkbox"]:checked').length > 0;
    if (isChecked) {
        checkboxGroup.find('input[type="checkbox"]').removeClass('is-invalid').addClass('is-valid');
    } else {
        checkboxGroup.find('input[type="checkbox"]').removeClass('is-valid').addClass('is-invalid');
    }
    return isChecked;
  }


  // Attach event handlers to checkboxes for active validation
  $('.checkbox-group input[type="checkbox"]').on('change', function() {
      validateCheckboxGroup($(this).closest('.checkbox-group'));
  });


  // Set up validation or automatic valid state on focus
  $('.needs-validation .form-control, .needs-validation .form-check-input').on('focus', function() {
    let inputField = $(this);
    if (inputField.data('validate')) {
        // Validate on input for fields that require validation
        validateInput(inputField);
        inputField.on('input change', function() { // Added 'change' for radio buttons
            validateInput(inputField);
        }).on('blur', function() {
            inputField.off('input change'); // Added 'change' for radio buttons
        });
    } else {
        // Automatically set to valid for fields that don't require validation
        inputField.addClass('is-valid');
    }
  });


  // Form submission handler
    $('#speakerRegistrationForm').on('submit', function(e) {
      let formIsValid = true;

    // Validate each input field that requires validation
    $(this).find('.form-control[data-validate=true]').each(function() {
        validateInput($(this));
        if (!this.checkValidity()) {
            formIsValid = false;
        }
    });

    // Check for at least one checkbox checked in each group
      // Validate checkboxes on submit
    $('.checkbox-group').each(function() {
      if (!validateCheckboxGroup($(this))) {
          formIsValid = false;
      }
    });

    // Radio buttons are validated by the browser by default, as long as they share the same 'name' attribute

    // Prevent form submission if the form is not valid
    if (!formIsValid) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $('.is-invalid').first().offset().top
        }, 1000);
    }
  });




});