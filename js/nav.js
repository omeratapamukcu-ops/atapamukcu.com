// Accessible mobile navigation for atapamukcu.com
(function () {
  function closeMenu(header, button) {
    header.classList.remove('nav-open');
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-label', 'Menüyü aç');
  }

  function setupNavigation() {
    document.querySelectorAll('.site-header').forEach(function (header, index) {
      const nav = header.querySelector('.nav-right');
      const logo = header.querySelector('.logo');
      if (!nav || !logo || header.querySelector('.nav-toggle')) return;

      if (!nav.id) nav.id = 'site-navigation-' + index;
      nav.setAttribute('aria-label', nav.getAttribute('aria-label') || 'Ana menü');

      const resourceLinks = [
        ['/site-haritasi', 'REHBER'],
        ['/araclar', 'ARAÇLAR'],
        ['/psikoloji-3', 'PSİKOLOJİ 3.0']
      ];
      const existingHrefs = Array.from(nav.querySelectorAll('a')).map(function (link) {
        return (link.getAttribute('href') || '').replace(/\/$/, '');
      });
      const missingResources = resourceLinks.filter(function (item) {
        return !existingHrefs.includes(item[0]);
      });
      if (missingResources.length) {
        const label = document.createElement('span');
        label.className = 'mobile-resource-label';
        label.textContent = 'REHBER VE KAYNAKLAR';
        nav.appendChild(label);
        missingResources.forEach(function (item) {
          const link = document.createElement('a');
          link.className = 'mobile-resource-link';
          link.href = item[0];
          link.textContent = item[1];
          nav.appendChild(link);
        });
      }

      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'nav-toggle';
      button.setAttribute('aria-controls', nav.id);
      button.setAttribute('aria-expanded', 'false');
      button.setAttribute('aria-label', 'Menüyü aç');
      button.innerHTML = '<span></span><span></span><span></span>';
      logo.insertAdjacentElement('afterend', button);

      button.addEventListener('click', function () {
        const willOpen = !header.classList.contains('nav-open');
        header.classList.toggle('nav-open', willOpen);
        button.setAttribute('aria-expanded', String(willOpen));
        button.setAttribute('aria-label', willOpen ? 'Menüyü kapat' : 'Menüyü aç');
      });

      nav.addEventListener('click', function (event) {
        if (event.target.closest('a')) closeMenu(header, button);
      });

      document.addEventListener('click', function (event) {
        if (header.classList.contains('nav-open') && !header.contains(event.target)) {
          closeMenu(header, button);
        }
      });

      document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && header.classList.contains('nav-open')) {
          closeMenu(header, button);
          button.focus();
        }
      });

      window.matchMedia('(min-width: 761px)').addEventListener('change', function (event) {
        if (event.matches) closeMenu(header, button);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupNavigation);
  } else {
    setupNavigation();
  }
})();
