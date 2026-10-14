document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("itemForm");
    var text = document.getElementById("itemText");
    var type = document.getElementById("itemType");
    var tagsInput = document.getElementById("itemTags");
    var list = document.getElementById("itemList");

    var searchForm = document.getElementById("searchForm");
    var searchTypes = document.getElementById("searchTypes");
    var searchWords = document.getElementById("searchWords");
    var searchNot = document.getElementById("searchNot");
    var searchTags = document.getElementById("searchTags");
    var searchWithoutTags = document.getElementById("searchWithoutTags");
    var resetButton = document.getElementById("resetSearch");

    function split(value) {
        var parts = value.split(",");
        var out = [];
        for (var i = 0; i < parts.length; i++) {
            var p = parts[i].trim().toLowerCase();
            if (p !== "") { out.push(p); }
        }
        return out;
    }

    function getTags(item) {
        var data = item.getAttribute("data-tags");
        return data ? data.split("|") : [];
    }

    function renderTags(item) {
        var old = item.querySelectorAll(".tag");
        for (var i = 0; i < old.length; i++) { item.removeChild(old[i]); }

        var tags = getTags(item);
        var button = item.querySelector(".add-tag");
        for (var j = 0; j < tags.length; j++) {
            var span = document.createElement("span");
            span.className = "tag";
            span.textContent = tags[j];
            item.insertBefore(span, button);
        }
    }

    function addTags(item, newTags) {
        var tags = getTags(item);
        for (var i = 0; i < newTags.length; i++) {
            if (tags.indexOf(newTags[i]) === -1) { tags.push(newTags[i]); }
        }
        item.setAttribute("data-tags", tags.join("|"));
        renderTags(item);
    }

    function createItem(content, itemType, tags) {
        var item = document.createElement("li");

        var label = document.createElement("span");
        label.className = "content";
        label.textContent = content;
        item.appendChild(label);

        var button = document.createElement("button");
        button.type = "button";
        button.className = "add-tag";
        button.textContent = "+ tag";
        button.addEventListener("click", function () {
            var value = window.prompt("New tag(s), comma separated:");
            if (value) { addTags(item, split(value)); }
        });
        item.appendChild(button);

        item.classList.add(itemType);
        item.setAttribute("data-tags", "");
        addTags(item, tags);

        return item;
    }

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        if (text.value.trim() === "") { return; }

        list.appendChild(createItem(text.value.trim(), type.value, split(tagsInput.value)));
        text.value = "";
        tagsInput.value = "";
    });

    function selectedTypes() {
        var out = [];
        for (var i = 0; i < searchTypes.options.length; i++) {
            if (searchTypes.options[i].selected) {
                out.push(searchTypes.options[i].value);
            }
        }
        return out;
    }

    function matches(item) {
        var types = selectedTypes();
        if (types.length > 0) {
            var ok = false;
            for (var i = 0; i < types.length; i++) {
                if (item.classList.contains(types[i])) { ok = true; }
            }
            if (!ok) { return false; }
        }

        var content = item.querySelector(".content").textContent.toLowerCase();
        var words = split(searchWords.value);
        if (words.length > 0) {
            var found = false;
            for (var j = 0; j < words.length; j++) {
                if (content.indexOf(words[j]) !== -1) { found = true; }
            }
            if (searchNot.checked ? found : !found) { return false; }
        }

        var tags = getTags(item);
        var wanted = split(searchTags.value);
        for (var k = 0; k < wanted.length; k++) {
            if (tags.indexOf(wanted[k]) === -1) { return false; }
        }

        var excluded = split(searchWithoutTags.value);
        for (var l = 0; l < excluded.length; l++) {
            if (tags.indexOf(excluded[l]) !== -1) { return false; }
        }

        return true;
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
        searchTags.value = "";
        searchWithoutTags.value = "";
        searchNot.checked = false;
        for (var i = 0; i < searchTypes.options.length; i++) {
            searchTypes.options[i].selected = false;
        }
        var items = list.children;
        for (var j = 0; j < items.length; j++) {
            items[j].classList.remove("hidden");
        }
    });
});