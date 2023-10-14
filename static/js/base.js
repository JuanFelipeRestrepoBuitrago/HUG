const navbar = document.getElementById('navbar');
const mobileMenu = document.getElementById('menuMobile');
const buttonMobileMenu = document.getElementById('buttonMenuMobile');
let prevScrollPos = window.scrollY;

/**
 * Hides the mobile menu
 *
 */
function hideMobileNav() {
    // Esconder el menu mobile
    mobileMenu.classList.add('inactive');
}

/**
 * Hides the navbar when the user scrolls down and shows it when the user scrolls up
 *
 * @see https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp
 */
window.onscroll = function() {
    // Get the current scroll position
    let currentScrollPos = window.scrollY;

    // If the user scrolls down, hide the navbar
    if (prevScrollPos > currentScrollPos) {
        navbar.classList.remove('hidden');
    // If the user scrolls up, show the navbar
    } else {
        navbar.classList.add('hidden');
    }

    // Hide the mobile menu
    hideMobileNav();

    // Set the previous scroll position
    prevScrollPos = currentScrollPos;
};

/**
 * Shows and hides the mobile menu
 *
 */
buttonMobileMenu.addEventListener('click', () => {
    // Toggle the mobile menu
    mobileMenu.classList.toggle('inactive');
});

// Hides the mobile menu when the user clicks outside of it
document.addEventListener('click', function(event) {
    // If the user clicks outside of the mobile menu, hide it
    if (!mobileMenu.contains(event.target) && mobileMenu !== event.target && !buttonMobileMenu.contains(event.target) && buttonMobileMenu !== event.target) {
        hideMobileNav();
    }
});