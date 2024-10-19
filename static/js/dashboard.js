let currentSlide = 0;
const slides = document.querySelectorAll('.slider-slide');
const totalSlides = slides.length;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.add('active');
    if (i === index) {
      slide.classList.add('active');
    }
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  showSlide(currentSlide);
}

// Initialize first slide
showSlide(currentSlide);

// Automatically change slides every 5 seconds
setInterval(nextSlide, 5000);


// display registration box
let closeButton2 = document.querySelector('.formintro img')
let regpageform2 = document.querySelector('.regpageform')
let shadow2 = document.querySelector('.shadow')
let registerforlaunch = document.querySelectorAll('.registerforlaunch')

if (closeButton2){
    closeButton2.addEventListener('click', () => {
        regpageform2.style.display = 'none'
        shadow2.style.display = 'none'
    })
}

// registerforlaunch.addEventListener('click', () => {
//   print('registerforlaunch')
//   regpageform2.style.display = 'block';
// });



registerforlaunch.forEach((a) => {
    a.addEventListener('click', () => {
      regpageform2.style.display = 'block';
      shadow2.style.display = 'block';
    });
  });



  
// HANDLE FLASH MESSAGES ON DASHBOARD STARTS HERE
let flashGeneraldash = document.querySelector('#flashmessage')
// let flashGeneral = document.querySelector('.alert strong')
if(flashGeneraldash){
    setTimeout(() => {
        flashGeneraldash.style.display = 'none'
    }, 5000);
}
// HANDLE FLASH MESSAGES ON DASHBOARD ENDS HERE


// COPY STAFF ID TO CLIPBOARD CONFIG STARTS HERE
let copyreferallink2 = document.querySelector('.copyreferallink2');

copyreferallink2.addEventListener('click', async() => {
  let referallinkproper2 = copyreferallink2.previousElementSibling.value
  // let referallinkproper2 = copyreferallink2.nextElementSibling.value
  console.log(referallinkproper2)
  try {
    await navigator.clipboard.writeText(referallinkproper2);
    confirm(`${referallinkproper2} has been copied to your Clipboard`)
  } catch (err) {
    console.error('Failed to copy: ', err);
  }

})
