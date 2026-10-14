document.addEventListener("DOMContentLoaded", function () {
    var button = document.querySelector("button");
    if (!button) { return; }

    button.addEventListener("click", function () {
        var paragraphs = document.querySelectorAll("p");
        for (var i = 0; i < paragraphs.length; i++) {
            paragraphs[i].style.display = "none";
        }
    });
});