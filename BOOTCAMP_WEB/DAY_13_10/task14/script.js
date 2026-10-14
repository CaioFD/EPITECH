document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("itemForm");
    var text = document.getElementById("itemText");
    var type = document.getElementById("itemType");
    var list = document.getElementById("itemList");

    var searchForm = document.getElementById("searchForm");
    var searchType = document.getElementById("searchType");
    var searchWords = document.getElementById("searchWords");
    var searchNot = document.getElementById("searchNot");
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

    function matches(item) {
        var wantedType = searchType.value;
        if (wantedType !== "all" && !item.classList.contains(wantedType)) {
            return false;
        }

        var words = searchWords.value.trim().toLowerCase();
        if (words === "") { return true; }

        var contains = item.textContent.toLowerCase().indexOf(words) !== -1;
        return searchNot.checked ? !contains : contains;
    }

    searchForm.addEventListener("submit", function (event) {
        event.preventDefault();
        var items = list.children;
        for (var i = 0; i < items.length; i++) {
            if (matches(items[i])) {
                items[i].classList.remove("hidden");
            } else {
                items[i].classList.add("hidden");
            }
        }
    });

    resetButton.addEventListener("click", function () {
        searchWords.value = "";
        searchNot.checked = false;
        searchType.value = "all";

        var items = list.children;
        for (var i = 0; i < items.length; i++) {
            items[i].classList.remove("hidden");
        }
    });
});