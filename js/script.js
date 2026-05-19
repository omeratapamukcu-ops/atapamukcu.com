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

  // --- LAZY SUBSTACK EMBED ---
  const substackMount = document.querySelector('[data-substack-embed]');

  function loadSubstackEmbed() {
    if (!substackMount || substackMount.dataset.loaded === 'true') return;
    substackMount.dataset.loaded = 'true';
    substackMount.innerHTML = '<iframe src="https://atapamukcu.substack.com/embed" width="100%" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no" loading="lazy" title="Psikoloji 3.0 Substack abonelik formu"></iframe>';
  }

  if (substackMount) {
    if ('IntersectionObserver' in window) {
      const substackObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            loadSubstackEmbed();
            substackObserver.disconnect();
          }
        });
      }, { rootMargin: '200px 0px' });
      substackObserver.observe(substackMount);
    } else {
      window.addEventListener('load', function () {
        setTimeout(loadSubstackEmbed, 4000);
      });
    }
  }

});
