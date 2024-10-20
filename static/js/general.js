const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});



let registerforlaunch3 = document.querySelector('.registerforlaunch3')
let regpageform2 = document.getElementsByClassName('regpageform')
registerforlaunch3.addEventListener('click', () => {
  console.log('dsdsdsds')
  regpageform2.style.display = 'block';
  shadow2.style.display = 'block';
});
