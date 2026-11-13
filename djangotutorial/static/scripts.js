document.addEventListener('DOMContentLoaded', () => {
    // 1. Gestion du menu hamburger mobile (votre code existant)
    const menuToggle = document.querySelector('.menu-toggle');
    const headerNav = document.querySelector('.header-nav');

    if (menuToggle && headerNav) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            headerNav.classList.toggle('active');
        });
    }
});