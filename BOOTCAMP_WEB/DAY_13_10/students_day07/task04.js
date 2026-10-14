document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".exercice footer button");
    var select = document.querySelector(".exercice footer select");
    var plus = buttons[0];
    var minus = buttons[1];
    var size = parseFloat(window.getComputedStyle(document.body).fontSize);

    function apply() {
        document.body.style.fontSize = size + "px";
    }

    plus.addEventListener("click", function () {
        size += 2;
        apply();
    });

    minus.addEventListener("click", function () {
        if (size > 2) {
            size -= 2;
            apply();
        }
    });

    select.addEventListener("change", function () {
        if (select.value !== "") {
            document.body.style.backgroundColor = select.value;
        }
    });
});