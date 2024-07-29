// globeScript.js

window.onload = function() {
    var canvas = document.getElementById('globeCanvas');
    var context = canvas.getContext('2d');

    // Example: Draw a simple circle to represent the globe
    context.fillStyle = 'blue';
    context.beginPath();
    context.arc(250, 250, 200, 0, Math.PI * 2, true); // x, y, radius, startAngle, endAngle, anticlockwise
    context.fill();
};
