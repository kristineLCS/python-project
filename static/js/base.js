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