// atapamukcu.com — JavaScript

document.addEventListener('DOMContentLoaded', function () {

  // --- FAQ ACCORDION ---
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(function (item) {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', function () {
      // Toggle current
      const isActive = item.classList.contains('active');

      // Close all others
      faqItems.forEach(function (other) {
        other.classList.remove('active');
      });

      // Open current if it wasn't already open
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // --- TESTIMONIAL READ MORE ---
  const testimonialToggles = document.querySelectorAll('.testimonial-toggle');

  testimonialToggles.forEach(function (button) {
    button.addEventListener('click', function () {
      const card = button.closest('.testimonial-expandable');
      const isExpanded = card.classList.toggle('expanded');
      button.textContent = isExpanded ? 'Kısalt' : 'Devamını oku';
    });
  });

  // --- HEADER SCROLL EFFECT ---
  const header = document.getElementById('header');

  window.addEventListener('scroll', function () {
    if (window.scrollY > 10) {
      header.style.borderBottomColor = 'rgba(23, 54, 39, 0.15)';
    } else {
      header.style.borderBottomColor = 'rgba(23, 54, 39, 0.08)';
    }
  });

});
