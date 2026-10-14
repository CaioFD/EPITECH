document.addEventListener("DOMContentLoaded", function () {
    var box = document.querySelectorAll(".exercice footer div")[0];
    var square = box.querySelector("canvas");
    var output = document.querySelectorAll(".exercice footer div")[1];

    box.style.position = "relative";
    square.style.position = "absolute";
    square.style.cursor = "move";

    var dragging = false;
    var offsetX = 0;
    var offsetY = 0;

    function setPos(x, y) {
        var maxX = box.clientWidth - square.offsetWidth;
        var maxY = box.clientHeight - square.offsetHeight;
        x = Math.max(0, Math.min(maxX, x));
        y = Math.max(0, Math.min(maxY, y));
        square.style.left = x + "px";
        square.style.top = y + "px";
        output.textContent = "New coordinates => {x:" + Math.round(x) +
            ", y:" + Math.round(y) + "}";
    }

    square.addEventListener("mousedown", function (event) {
        dragging = true;
        offsetX = event.clientX - parseFloat(square.style.left || 0);
        offsetY = event.clientY - parseFloat(square.style.top || 0);
        event.preventDefault();
    });

    document.addEventListener("mousemove", function (event) {
        if (!dragging) { return; }
        setPos(event.clientX - offsetX, event.clientY - offsetY);
    });

    document.addEventListener("mouseup", function () {
        dragging = false;
    });

    setPos(0, 0);
});