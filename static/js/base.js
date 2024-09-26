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
const signupForm = document.getElementById('signup');
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


// Comment section
const commentInput = document.getElementById("comment");
const commentList = document.getElementById("comment-list");
const commentButton = document.getElementById("commentbtn");

// Add event listener to the button
commentButton.addEventListener('click', function() {
    console.log('Button clicked');
    addComment();
});

// Function to add a comment
function addComment() {
    console.log("Add Comment button clicked!");

    const li = document.createElement('li');
    li.innerText = "Test comment";  // Add a static comment
    commentList.appendChild(li);
    console.log("Static comment added");

    // Create the delete button (X)
    const span = document.createElement('span');
    span.innerHTML = '\u00d7';
    span.className = 'delete-btn';
    li.appendChild(span);

    commentInput.value = '';  // Clear the input field

    saveComments();
}



// Event listener for crossing out or deleting comments
commentList.addEventListener('click', function(e) {
    if (e.target.tagName === "SPAN") {
        e.target.parentElement.remove();  // Remove the comment (li element)
        saveComments();  // Save updated comment list
    }
}, false);

// Function to save comments to localStorage
function saveComments() {
    try {
        localStorage.setItem("comments", commentList.innerHTML);
    } catch (e) {
        console.error("Could not save comments to localStorage", e);
    }
}


// Function to load comments from localStorage on page load
function showComments() {
    commentList.innerHTML = localStorage.getItem("comments");
}

// Call showComments when the page loads to show saved comments
showComments();
