document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("itemForm");
    var text = document.getElementById("itemText");
    var type = document.getElementById("itemType");
    var list = document.getElementById("itemList");

    var searchForm = document.getElementById("searchForm");
    var searchType = document.getElementById("searchType");
    var resetButton = document.getElementById("resetSearch");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        if (text.value.trim() === "") { return; }

        var item = document.createElement("li");
        item.textContent = text.value.trim();
        item.classList.add(type.value);
        list.appendChild(item);
        text.value = "";
    });

    searchForm.addEventListener("submit", function (event) {
        event.preventDefault();
        var wanted = searchType.value;
        var items = list.children;

        for (var i = 0; i < items.length; i++) {
            if (items[i].classList.contains(wanted)) {
                items[i].classList.remove("hidden");
            } else {
                items[i].classList.add("hidden");
            }
        }
    });

    resetButton.addEventListener("click", function () {
        var items = list.children;
        for (var i = 0; i < items.length; i++) {
            items[i].classList.remove("hidden");
        }
    });
});