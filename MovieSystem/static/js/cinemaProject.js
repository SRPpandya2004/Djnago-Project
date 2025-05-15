const hamburgerMenuElement = document.getElementsByClassName("hamburger-menu")[0];
const navDivElement = document.getElementsByClassName("navigation-links-div")[0];


hamburgerMenuElement.addEventListener('click', (evt) => {
    evt.preventDefault();
    navDivElement.classList.toggle('active');
})


document.querySelectorAll(".navigation-links-div").forEach(n => n.addEventListener('click', () => {
    navDivElement.classList.remove('active');
}))