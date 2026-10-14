document.addEventListener("DOMContentLoaded", function () {
    var box = document.querySelector(".exercice footer div");
    var count = 0;

    box.addEventListener("click", function () {
        count++;
        box.textContent = count;
    });
});