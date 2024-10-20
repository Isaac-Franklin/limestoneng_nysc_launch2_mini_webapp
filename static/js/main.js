const countDownDate = new Date('Dec 31, 2024 00:00:00').getTime();

// Update the countdown every second
const countdownInterval = setInterval(() => {
    // Get today's date and time
    const now = new Date().getTime();
    
    // Find the distance between now and the countdown date
    const distance = countDownDate - now;
    
    // Time calculations for days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in the respective elements
    document.getElementById('days').innerHTML = days;
    document.getElementById('hours').innerHTML = hours;
    document.getElementById('minutes').innerHTML = minutes;
    document.getElementById('seconds').innerHTML = seconds;
    
    // If the countdown is finished, display a message
    if (distance < 0) {
        clearInterval(countdownInterval);
        document.getElementById('countdown').innerHTML = "<h2>Countdown Finished</h2>";
    }
}, 1000);


// display registration box starts here

let registerforlaunch2 = document.querySelectorAll('.registerforlaunch')
let regpageform = document.querySelector('.regpageform')
let shadow = document.querySelector('.shadow')
registerforlaunch2.forEach(e => e.addEventListener('click', () => {
  regpageform.style.display = 'block';
  shadow.style.display = 'block';
}));

// display registration box ends here


// close registration box starts here

let closeButton2 = document.querySelector('.formintro img')

if (closeButton2){
    closeButton2.addEventListener('click', () => {
        regpageform.style.display = 'none'
        shadow.style.display = 'none'
    })
}

// close registration box ends here



// COPY REFERRAL CODE TO CLIPBOARD CONFIG STARTS HERE

let copyreferallink2 = document.querySelectorAll('.copyreferallink2');

copyreferallink2.forEach((e)=>{
    if (e){
        e.addEventListener('click', async() => {console.log('countDownDate')

            let referallinkproper2 = e.nextElementSibling.value
            try {
              await navigator.clipboard.writeText(referallinkproper2);
              confirm(`${e.nextElementSibling.nextElementSibling.value}has been copied to your Clipboard`)
            } catch (err) {
              console.error('Failed to copy: ', err);
            }
        
        })   
    }    
  })

// COPY REFERRAL CODE TO CLIPBOARD CONFIG ENDS HERE
