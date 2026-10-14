document.addEventListener("DOMContentLoaded", function () {
    var box = document.querySelector(".exercice footer div");

    box.addEventListener("click", function () {
        var name = null;

        while (!name || name.trim() === "") {
            name = window.prompt("What's your name ?");
            if (name === null) { name = ""; }
        }
        name = name.trim();

        if (window.confirm("Are you sure that " + name + " is your name ?")) {
            window.alert("Hello " + name + " !");
            box.textContent = "Hello " + name + " !";
        }
    });
});