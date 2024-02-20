const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('show');
        }
        else {
            entry.target.classList.remove('show')
        }
        
    })
});


const scrollDelay = document.querySelectorAll('.container');
scrollDelay.forEach((el) => observer.observe(el));

const homeDelay = document.querySelectorAll('.home');
homeDelay.forEach((el) => observer.observe(el));


const observer1 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('showBlank');
        }
        else {
            entry.target.classList.remove('showBlank')
        }
        
    })
});

const blankDelay = document.querySelectorAll('.blank');
blankDelay.forEach((el) => observer1.observe(el));


// Booking date starts from tommorow
let date = new Date();
date.setDate(date.getDate() + 1); 
let tomorrow = date.toISOString().split('T')[0];

const bookingDateInput = document.querySelector('#date');
bookingDateInput.setAttribute('min', tomorrow);



//Prevent blank form submission
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form');

    form.addEventListener('submit', function(event) {
      const fName = document.getElementById('fName').value;
      const lName = document.getElementById('lName').value;
      const email = document.getElementById('email').value;
      const number = document.getElementById('number').value;
      const date = document.getElementById('date').value;
      const service = document.getElementById('service').value;

      if (!fName || !lName || !email || !number || !date || !service) {
        alert('Please fill in all fields.');
        event.preventDefault();
      }
    });
  });
