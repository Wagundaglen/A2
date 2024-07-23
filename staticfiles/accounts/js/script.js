// JavaScript for accounts app
document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (event) {
            var password1 = document.getElementById('password1').value;
            var password2 = document.getElementById('password2').value;

            if (password1 !== password2) {
                event.preventDefault();
                alert('The two password fields didn\'t match');
            }
        });
    }
});
