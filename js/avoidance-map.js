(function () {
  'use strict';
  var form = document.getElementById('avoidanceForm');
  if (!form) return;

  var fields = [
    ['aSituation', 'Durum'],
    ['aInside', 'Uzaklaşmak istediğim iç deneyim'],
    ['aAction', 'Yaptığım / yapmadığım şey'],
    ['aShort', 'Kısa vadede sağladığı'],
    ['aLong', 'Uzun vadeli maliyet'],
    ['aValue', 'Önemli yön / değer'],
    ['aTiny', 'Yüzde 10 daha esnek adım']
  ];
  var output = document.getElementById('avoidOutput');
  var result = document.getElementById('avoidResult');
  var status = document.getElementById('avoidStatus');
  var clear = document.getElementById('avoidClear');

  function buildText() {
    var lines = ['KAÇINMA HARİTAM', ''];
    fields.forEach(function (field) {
      var value = document.getElementById(field[0]).value.trim();
      lines.push(field[1] + ': ' + (value || '—'), '');
    });
    lines.push('Not: Amaç kaygıyı zorla düşürmek değil, seçilen küçük davranışta esneyebilmektir.');
    return lines.join('\n');
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (!form.reportValidity()) return;
    output.textContent = buildText();
    result.hidden = false;
    status.textContent = 'Harita oluşturuldu. Bu sayfa girdilerinizi sunucuya göndermez veya kalıcı kaydetmez.';
    result.setAttribute('tabindex', '-1');
    result.focus({ preventScroll: true });
    var motion = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    result.scrollIntoView({ behavior: motion, block: 'start' });
  });

  document.getElementById('avoidCopy').addEventListener('click', function () {
    if (result.hidden) {
      status.textContent = 'Önce gerekli alanları doldurup haritayı oluşturun.';
      return;
    }
    var text = output.textContent;
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () {
        status.textContent = 'Harita panoya kopyalandı.';
      }).catch(function () { status.textContent = 'Kopyalama başarısız. Metni seçerek kopyalayabilirsiniz.'; });
    } else {
      status.textContent = 'Tarayıcı otomatik kopyalamaya izin vermedi. Metni seçerek kopyalayabilirsiniz.';
    }
  });

  document.getElementById('avoidPrint').addEventListener('click', function () {
    if (result.hidden) {
      status.textContent = 'Yazdırmadan önce haritayı oluşturun.';
      return;
    }
    document.body.classList.add('print-avoidance');
    window.print();
    document.body.classList.remove('print-avoidance');
  });

  window.addEventListener('afterprint', function () {
    document.body.classList.remove('print-avoidance');
  });

  clear.addEventListener('click', function () {
    form.reset();
    output.textContent = '';
    result.hidden = true;
    result.removeAttribute('tabindex');
    status.textContent = 'Form ve oluşturulan harita temizlendi.';
    document.getElementById('aSituation').focus();
  });
})();
