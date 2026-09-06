// atapamukcu.com — JavaScript

document.addEventListener('DOMContentLoaded', function () {

  // --- ANALYTICS AND MARKETING CONSENT ---
  const analyticsConsentKey = 'atap_analytics_consent';
  const marketingConsentKey = 'atap_marketing_consent';
  const metaPixelId = '2107772050122070';

  function readAnalyticsConsent() {
    try { return window.localStorage.getItem(analyticsConsentKey); }
    catch (error) { return null; }
  }

  function hasAnalyticsConsent() {
    return readAnalyticsConsent() === 'granted';
  }

  function readMarketingConsent() {
    try { return window.localStorage.getItem(marketingConsentKey); }
    catch (error) { return null; }
  }

  function hasMarketingConsent() {
    return readMarketingConsent() === 'granted';
  }

  function setGoogleConsent(command, value) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('consent', command, {
      analytics_storage: value,
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
  }

  function clearAnalyticsCookies() {
    document.cookie.split(';').forEach(function (cookie) {
      const name = cookie.split('=')[0].trim();
      if (name === '_ga' || name.indexOf('_ga_') === 0) {
        document.cookie = name + '=; Max-Age=0; path=/; SameSite=Lax';
        document.cookie = name + '=; Max-Age=0; path=/; domain=.atapamukcu.com; SameSite=Lax';
      }
    });
  }

  function clearMetaCookies() {
    ['_fbp', '_fbc'].forEach(function (name) {
      document.cookie = name + '=; Max-Age=0; path=/; SameSite=Lax';
      document.cookie = name + '=; Max-Age=0; path=/; domain=.atapamukcu.com; SameSite=Lax';
    });
  }

  function isMetaAllowlistedPage() {
    const allowedPaths = ['/', '/index.html'];
    const allowedQueryKeys = [
      'fbclid', 'gclid', 'utm_campaign', 'utm_content', 'utm_medium',
      'utm_source', 'utm_term'
    ];
    const hasUnknownQuery = Array.from(new URLSearchParams(window.location.search).keys())
      .some(function (key) { return !allowedQueryKeys.includes(key); });

    return allowedPaths.includes(window.location.pathname) &&
      !hasUnknownQuery && !window.location.hash;
  }

  function loadMetaPixel() {
    if (!hasMarketingConsent() || !isMetaAllowlistedPage() || window.__metaPixelLoaded) return;

    window.__metaPixelLoaded = true;
    (function (f, b, e, v, n, t, s) {
      if (f.fbq) return;
      n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n;
      n.push = n;
      n.loaded = true;
      n.version = '2.0';
      n.queue = [];
      t = b.createElement(e);
      t.async = true;
      t.src = v;
      s = b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t, s);
    })(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

    window.fbq('set', 'autoConfig', false, metaPixelId);
    window.fbq('consent', 'grant');
    window.fbq('init', metaPixelId);
    window.fbq('track', 'PageView');
  }

  const savedAnalyticsConsent = readAnalyticsConsent();
  const savedMarketingConsent = readMarketingConsent();
  setGoogleConsent('default', savedAnalyticsConsent === 'granted' ? 'granted' : 'denied');

  function applyConsent(analyticsValue, marketingValue, panel) {
    try {
      window.localStorage.setItem(analyticsConsentKey, analyticsValue);
      window.localStorage.setItem(marketingConsentKey, marketingValue);
    } catch (error) {}
    setGoogleConsent('update', analyticsValue);
    if (analyticsValue === 'denied') clearAnalyticsCookies();
    if (marketingValue === 'granted') loadMetaPixel();
    else {
      if (window.fbq) window.fbq('consent', 'revoke');
      clearMetaCookies();
    }
    panel.hidden = true;
  }

  function showAnalyticsConsent(showDetails) {
    let panel = document.getElementById('analytics-consent');
    if (!panel) {
      panel = document.createElement('section');
      panel.id = 'analytics-consent';
      panel.className = 'analytics-consent';
      panel.setAttribute('aria-label', 'Çerez tercihleri');
      panel.innerHTML = '<div class="consent-summary"><strong>Gizliliğiniz</strong><p>Deneyimi iyileştirmek ve reklam performansını ölçmek için isteğe bağlı çerezler kullanıyoruz.</p><a href="/gizlilik">Detaylar</a></div><div class="analytics-consent-actions"><button type="button" data-analytics-consent="denied" data-marketing-consent="denied">Reddet</button><button type="button" data-open-consent-settings>Ayarlar</button><button type="button" class="consent-accept" data-analytics-consent="granted" data-marketing-consent="granted">Kabul et</button></div><div class="consent-details" hidden><label><span><strong>İstatistik</strong><small>Site kullanımını anlamamıza yardımcı olur.</small></span><input type="checkbox" data-consent-analytics></label><label><span><strong>Reklam ölçümü</strong><small>Ana sayfadaki reklam ve WhatsApp yönlendirme performansını ölçer.</small></span><input type="checkbox" data-consent-marketing></label><div class="consent-detail-actions"><button type="button" data-close-consent-settings>Geri</button><button type="button" class="consent-accept" data-save-consent>Seçimi kaydet</button></div></div>';
      document.body.appendChild(panel);
      panel.addEventListener('click', function (event) {
        const preset = event.target.closest('button[data-analytics-consent][data-marketing-consent]');
        if (preset) {
          applyConsent(preset.dataset.analyticsConsent, preset.dataset.marketingConsent, panel);
          return;
        }
        if (event.target.closest('[data-open-consent-settings]')) {
          openConsentDetails(panel);
          return;
        }
        if (event.target.closest('[data-close-consent-settings]')) {
          closeConsentDetails(panel);
          return;
        }
        if (event.target.closest('[data-save-consent]')) {
          const analyticsValue = panel.querySelector('[data-consent-analytics]').checked ? 'granted' : 'denied';
          const marketingValue = panel.querySelector('[data-consent-marketing]').checked ? 'granted' : 'denied';
          applyConsent(analyticsValue, marketingValue, panel);
        }
      });
    }
    panel.hidden = false;
    if (showDetails === true) openConsentDetails(panel);
    else closeConsentDetails(panel);
  }

  function openConsentDetails(panel) {
    panel.classList.add('show-details');
    panel.querySelector('.consent-details').hidden = false;
    panel.querySelector('[data-consent-analytics]').checked = hasAnalyticsConsent();
    panel.querySelector('[data-consent-marketing]').checked = hasMarketingConsent();
  }

  function closeConsentDetails(panel) {
    panel.classList.remove('show-details');
    panel.querySelector('.consent-details').hidden = true;
  }

  const settingsButton = document.createElement('button');
  settingsButton.type = 'button';
  settingsButton.className = 'analytics-settings';
  settingsButton.textContent = 'Çerezler';
  settingsButton.addEventListener('click', function () { showAnalyticsConsent(true); });
  document.body.appendChild(settingsButton);

  if (!savedAnalyticsConsent || !savedMarketingConsent) showAnalyticsConsent(false);
  loadMetaPixel();

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

  // --- PRIVACY-SAFE CTA MEASUREMENT ---
  // Only generic interaction metadata is sent. Link URLs, phone numbers,
  // email addresses, WhatsApp message text and form/health content are excluded.
  function sendAnalyticsEvent(eventName, parameters) {
    if (!hasAnalyticsConsent()) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () {
      window.dataLayer.push(arguments);
    };
    if (!window.__ctaAnalyticsConfigured) {
      window.gtag('config', 'G-M1K0Q69Q2Z');
      window.__ctaAnalyticsConfigured = true;
    }
    window.gtag('event', eventName, parameters);
  }

  function getEventSurface(element) {
    if (element.closest('header')) return 'header';
    if (element.closest('footer')) return 'footer';
    if (element.closest('.article-cta')) return 'article_cta';
    if (element.closest('.article-hero')) return 'hero';
    return 'content';
  }

  document.addEventListener('click', function (event) {
    const link = event.target.closest('a[href]');
    if (!link) return;

    const href = link.getAttribute('href') || '';
    const normalizedHref = href.toLowerCase();
    const eventParameters = {
      event_surface: getEventSurface(link),
      transport_type: 'beacon'
    };

    if (normalizedHref.startsWith('tel:')) {
      sendAnalyticsEvent('phone_click', eventParameters);
      return;
    }

    if (normalizedHref.startsWith('mailto:')) {
      sendAnalyticsEvent('email_click', eventParameters);
      return;
    }

    if (normalizedHref.includes('wa.me/') || normalizedHref.includes('whatsapp.com/')) {
      sendAnalyticsEvent('whatsapp_click', eventParameters);

      // This is only a redirect click. It is not a sent message, lead or appointment.
      if (hasMarketingConsent() && isMetaAllowlistedPage() && window.fbq) {
        window.fbq('trackCustom', 'WhatsAppCTAClick');
      }

      const explicitEvent = link.dataset.analyticsEvent;
      if (explicitEvent === 'seans_degerlendirme_cta_click') {
        sendAnalyticsEvent(explicitEvent, eventParameters);
      }

      const visibleLabel = (link.textContent || '').toLocaleLowerCase('tr-TR');
      const startsAppointment = link.classList.contains('btn-primary') ||
        visibleLabel.includes('randevu') ||
        visibleLabel.includes('değerlendirme');

      if (startsAppointment) {
        sendAnalyticsEvent('appointment_start', eventParameters);
      }
    }
  });

  // A booking/form integration may dispatch this only after it has confirmed
  // success: document.dispatchEvent(new CustomEvent('appointment:complete')).
  // No completion is inferred from a click.
  document.addEventListener('appointment:complete', function () {
    sendAnalyticsEvent('appointment_complete', {
      completion_source: 'verified_success',
      transport_type: 'beacon'
    });
  });

});
