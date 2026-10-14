document.addEventListener("DOMContentLoaded", function () {
    var paragraphs = document.querySelectorAll("p");

    for (var i = 0; i < paragraphs.length; i++) {
        (function (p) {
            p.addEventListener("mouseover", function () { p.classList.add("blue"); });
            p.addEventListener("mouseout", function () { p.classList.remove("blue"); });
            p.addEventListener("click", function () { p.classList.toggle("highlighted"); });
        })(paragraphs[i]);
    }
});