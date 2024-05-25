/* JS code for the event listener. Þetta á að vera smooth image appear */

/* Ég prófaði að hafa þetta ekki inni og image birtist samt smoothly */

document.addEventListener("DOMContentLoaded", function () {
    const myModal = document.getElementById("' . $modalId . '");
    const myInput = document.getElementById("' . $inputId . '");

    myModal.addEventListener("shown.bs.modal", () => {
        myInput.focus();
    });
});
