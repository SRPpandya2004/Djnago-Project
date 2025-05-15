document.addEventListener("DOMContentLoaded", function() {
    const slider = document.querySelector('.slider');
    const slides = slider.querySelectorAll('img');
    const totalSlides = slides.length;
    let currentIndex = 0;
  
    // Function to show current slide
    function showSlide(index) {
      // Reset all slides
      slides.forEach((slide) => {
        slide.style.transform = `translateX(-${index * 100}%)`;
      });
    }
  
    // Function to move to next slide
    function nextSlide() {
      currentIndex = (currentIndex + 1) % totalSlides;
      showSlide(currentIndex);
    }
  
    // Function to move to previous slide
    function prevSlide() {
      currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
      showSlide(currentIndex);
    }
  
    // Automatic slide change every 5 seconds
    setInterval(nextSlide, 5000);
  
    // Event listeners for navigation buttons
    document.getElementById('nextBtn').addEventListener('click', nextSlide);
    document.getElementById('prevBtn').addEventListener('click', prevSlide);
  });
  