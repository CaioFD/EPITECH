document.addEventListener("DOMContentLoaded", function () {
    var input = document.getElementById("listItem");
    var button = document.querySelector("button");
    if (!input || !button) { return; }

    button.addEventListener("click", function () {
        if (input.value.trim() === "") { return; }

        var item = document.createElement("div");
        item.textContent = input.value;
        input.parentNode.insertBefore(item, input.nextSibling);
        input.value = "";
    });
});