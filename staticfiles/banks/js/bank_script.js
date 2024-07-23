// JavaScript for banks app
document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (event) {
            var capacity = document.getElementById('capacity').value;

            if (capacity < 0) {
                event.preventDefault();
                alert('Ensure this value is greater than or equal to 0.');
            }
        });
    }
});
