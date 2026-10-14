document.addEventListener("DOMContentLoaded", function () {
    var box = document.querySelector(".exercice footer div");
    var buffer = "";

    document.addEventListener("keydown", function (event) {
        if (event.key === "Backspace") {
            buffer = buffer.slice(0, -1);
        } else if (event.key.length === 1) {
            buffer += event.key;
        }

        if (buffer.length > 42) {
            buffer = buffer.slice(-42);
        }
        box.textContent = buffer;
    });
});