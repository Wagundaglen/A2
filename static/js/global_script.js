// Global JavaScript for the project
document.addEventListener('DOMContentLoaded', function () {
    console.log('Global script loaded');

    // Sample global functionality
    var buttons = document.querySelectorAll('button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            alert('Button clicked!');
        });
    });
});
