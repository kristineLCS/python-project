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

// Start of gallery slideshow
// let slideIndex = 0;
// const slides = document.querySelectorAll('.slides');
// const prevButton = document.querySelectorAll('.previous');
// const nextButton = document.querySelectorAll('.next');

// function showSlides(index) {
//     slides.forEach(slide => {
//         slide.classList.remove('active-slide');
//     });
//     slides[index].classList.add('active-slide');
// }

// function nextSlide() {
//     slideIndex = (slideIndex + 1) % slides.length;
//     showSlides(slideIndex);
// }

// function prevSlide() {
//     slideIndex = (slideIndex - 1 + slides.length) % slides.length;
//     showSlides(slideIndex);
// }

// Add event listeners for buttons
// nextButton.addEventListener('click', nextSlide);
// prevButton.addEventListener('click', prevSlide);

// Initialize first slide
// showSlides(slideIndex);
