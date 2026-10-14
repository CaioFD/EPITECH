document.addEventListener("DOMContentLoaded", function () {
    var footer = document.querySelector(".exercice footer");
    var firstBox = footer.querySelector("div");
    var link = firstBox.querySelector("a");
    var secondBox = null;

    function getCookie(name) {
        var parts = document.cookie.split(";");
        for (var i = 0; i < parts.length; i++) {
            var pair = parts[i].trim().split("=");
            if (pair[0] === name) { return pair[1]; }
        }
        return null;
    }

    function setCookie(name, value, days) {
        var date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = name + "=" + value +
            ";expires=" + date.toUTCString() + ";path=/";
    }

    function deleteCookie(name) {
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/";
    }

    function showSecondBox() {
        if (secondBox) { return; }
        secondBox = document.createElement("div");
        var button = document.createElement("button");
        button.textContent = "Delete the cookie";
        button.addEventListener("click", function () {
            deleteCookie("acceptsCookies");
            footer.removeChild(secondBox);
            secondBox = null;
            firstBox.style.display = "";
        });
        secondBox.appendChild(button);
        footer.appendChild(secondBox);
    }

    function refresh() {
        if (getCookie("acceptsCookies") === "true") {
            firstBox.style.display = "none";
            showSecondBox();
        } else {
            firstBox.style.display = "";
        }
    }

    link.addEventListener("click", function (event) {
        event.preventDefault();
        setCookie("acceptsCookies", "true", 1);
        refresh();
    });

    refresh();
});