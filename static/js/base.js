// Start of sidebar
const showSidebar = document.getElementById('showsidebar');
const hideSidebar = document.getElementById('hidesidebar');
const mySideBar = document.getElementById('mysidebar');
const sideBar = document.querySelector('.sidebar');
const nav = document.querySelector('nav');

showSidebar.addEventListener('click', showSidebarBtn);
function showSidebarBtn() {
    mySideBar.style.width = '250px';
    mySideBar.style.display = 'flex';
}

hideSidebar.addEventListener('click', hideSidebarBtn);
function hideSidebarBtn() {
    mySideBar.style.width = '0';
    mySideBar.style.display = 'none';
}
// End of sidebar


// Sign-up validation 
const signup = document.getElementById('signup');
const email = document.getElementById('email');
const password = document.getElementById('password');
const emailError = document.getElementById('email-error');
const passwordError = document.getElementById('password-error');
const formError = document.getElementById('form-error');


const validation = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

formError.style.display = 'none';

email.addEventListener('input', function() {
    if (validation.test(email.value)) {
        email.classList.add('valid');
        email.classList.remove('invalid');
        emailError.style.display = 'none';
    } else {
        email.classList.add('invalid');
        email.classList.remove('valid');
        emailError.style.display = 'block';
    }

});

password.addEventListener('input', function() {
    if (password.value.length >= 8) {
        password.classList.add('valid');
        password.classList.remove('invalid');
        passwordError.style.display = 'none';
    } else {
        password.classList.add('invalid');
        password.classList.remove('valid');
        passwordError.style.display = 'block';
    }
})

signupForm.addEventListener('submit', function(event) {
    let inputValid = true; // Flag to check if the form is valid

    // Check email validity
    if (!validation.test(email.value)) {
        email.classList.add('invalid');
        emailError.style.display = 'block';
        inputValid = false;
    }

    // Check password length
    if (password.value.length < 8) {
        password.classList.add('invalid');
        passwordError.style.display = 'block';
        inputValid = false;
    }

    if (!inputValid) {
        event.preventDefault(); // Stops form submission
        formError.style.display = 'block'; // Show the form-wide error message
    } else {
        formError.style.display = 'none'; // Hide the form-wide error if all inputs are valid
    }
});
