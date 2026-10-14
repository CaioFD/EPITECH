document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("itemForm");
    var text = document.getElementById("itemText");
    var type = document.getElementById("itemType");
    var list = document.getElementById("itemList");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        if (text.value.trim() === "") { return; }

        var item = document.createElement("li");
        item.textContent = text.value.trim();
        item.classList.add(type.value);
        list.appendChild(item);
        text.value = "";
    });
});