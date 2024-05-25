<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    
    <title>Password matcher</title>
</head>

<body>
<div class="container-fluid">
  <div class="row justify-content-center mt-5">
    <div class="col-md-6">

      <form>

        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" class="form-control" id="username" required>
        </div>

        <div class="form-group">
          <label for="password1">New Password</label>
            <!-- required at the back makes the field required and form cannot be submitted if it is not filled  -->
            <!-- onkeyup keyrir comparepasswords() every time a key is pressed and checks the passwords -->
            <!-- til dæmis hægt að gera javascript sem athugar hvort lykilorð séu eins eða ef það á að fylla -->
            <!-- út á einhvern spes hátt þá er hægt að gera function sem athugar fieldið. -->
          <input type="password" class="form-control" id="password1" onkeyup="comparePasswords()" required>
        </div>

        <div class="form-group">
          <label for="password2">Confirm New Password</label>
          <input type="password" class="form-control" id="password2" onkeyup="comparePasswords()" required>
        </div>

        <div class="row">
          <div class="col">
            <div id="password-match" class="text-danger"></div>
          </div>
        </div>

        <div class="row mt-3">
          <div class="col text-center">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </div>
        
      </form>
    </div>
  </div>
</div>

<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<script>
function comparePasswords() {
  var password1 = document.getElementById("password1").value;
  var password2 = document.getElementById("password2").value;
  var matchDiv = document.getElementById("password-match");

  if (password1 === password2) {
    matchDiv.innerHTML = "Passwords match.";
    matchDiv.className = "text-success";
    document.querySelector("button[type='submit']").disabled = false;
  } else {
    matchDiv.innerHTML = "Passwords do not match.";
    matchDiv.className = "text-danger";
    document.querySelector("button[type='submit']").disabled = true;
  }
}

</script>

</body>
</html>




<!-- ---------- REQUIRED ATTRIBUTE IN INPUT FIELDS -------- -->
<!--    
The required attribute can be used with various input types, including 
text fields, checkboxes, radio buttons and dropdown lists.

When the required attribute is applied to an input field, it enforces 
client-side form validation. If the user tries to submit the form without 
filling out the required field, a validation error will be triggered, 
and the form submission will be blocked. The user will be prompted to 
provide the required information before they can successfully submit the form.
<input type="text" required>
 -->

<!-- ------------------ ONKEYUP EVENT --------------- -->
<!--
The onkeyup event is built into HTML and is used as an attribute on HTML elements. 
It allows you to specify a JavaScript function that will be executed when a key is 
released while the input field has focus.

Here's an example of how you can use the onkeyup attribute in an input field:
<input type="text" onkeyup="myFunction()">
In the above code, the onkeyup attribute is set to "myFunction()", which means that 
the JavaScript function named myFunction will be called every time a key is released 
while typing in the input field.
 -->