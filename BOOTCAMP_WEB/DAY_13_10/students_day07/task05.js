document.addEventListener("DOMContentLoaded", function () {
    var canvas = document.querySelector(".exercice footer canvas");
    var ctx = canvas.getContext("2d");

    ctx.beginPath();
    ctx.moveTo(6, 6);
    ctx.lineTo(14, 10);
    ctx.lineTo(6, 14);
    ctx.closePath();

    ctx.fillStyle = "#ffffff";
    ctx.fill();
    ctx.lineWidth = 1;
    ctx.strokeStyle = "#000000";
    ctx.stroke();

    var audio = document.querySelector(".exercice footer audio");
    var buttons = document.querySelectorAll(".exercice footer button");

    audio.src = "https://universal-soundbank.com/sounds/13631.mp3";

    canvas.addEventListener("click", function () {
        audio.play().catch(function (err) {
            console.error("Audio playback failed:", err);
        });
    });

    buttons[0].addEventListener("click", function () {
        audio.pause();
    });

    buttons[1].addEventListener("click", function () {
        audio.pause();
        audio.currentTime = 0;
    });
});