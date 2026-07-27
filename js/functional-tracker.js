(function () {
  'use strict';
  var form = document.getElementById('trackerForm');
  if (!form) return;

  var records = [];
  var table = document.getElementById('trackerTable');
  var rows = document.getElementById('trackerRows');
  var empty = document.getElementById('trackerEmpty');
  var status = document.getElementById('trackerStatus');
  var dateInput = document.getElementById('tDate');
  function localDate() {
    var now = new Date();
    var year = now.getFullYear();
    var month = String(now.getMonth() + 1).padStart(2, '0');
    var day = String(now.getDate()).padStart(2, '0');
    return year + '-' + month + '-' + day;
  }
  dateInput.value = localDate();

  function value(id) { return document.getElementById(id).value.trim(); }
  function addCell(row, text) {
    var cell = document.createElement('td');
    cell.textContent = text || '—';
    row.appendChild(cell);
  }
  function render() {
    rows.replaceChildren();
    records.forEach(function (record) {
      var row = document.createElement('tr');
      addCell(row, record.date + '\n' + record.context);
      addCell(row, record.trigger + (record.inside ? '\nİç deneyim: ' + record.inside : ''));
      addCell(row, record.action);
      addCell(row, 'Kısa: ' + record.shortTerm + '\nUzun: ' + (record.longTerm || '—'));
      addCell(row, record.next || '—');
      rows.appendChild(row);
    });
    var hasRecords = records.length > 0;
    table.hidden = !hasRecords;
    empty.hidden = hasRecords;
  }
  function csvCell(value) {
    var text = String(value || '');
    // Prevent spreadsheet applications from interpreting a user-entered value as a formula.
    if (/^[\t\r\n ]*[=+\-@]/.test(text)) text = "'" + text;
    return '"' + text.replace(/"/g, '""') + '"';
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (!form.reportValidity()) return;
    records.push({
      date: value('tDate'), context: value('tContext'), trigger: value('tTrigger'),
      inside: value('tInside'), action: value('tAction'), shortTerm: value('tShort'),
      longTerm: value('tLong'), next: value('tNext')
    });
    render();
    form.reset();
    dateInput.value = localDate();
    status.textContent = records.length + ' kayıt bu oturuma eklendi. Sayfa yenilenirse kayıtlar silinir.';
  });

  document.getElementById('downloadCsv').addEventListener('click', function () {
    if (!records.length) { status.textContent = 'İndirmek için önce en az bir kayıt ekleyin.'; return; }
    var headers = ['Tarih', 'Bağlam', 'Tetikleyici', 'Düşünce-duygu-beden', 'Davranış', 'Kısa vadeli sonuç', 'Uzun vadeli sonuç', 'Sonraki küçük adım'];
    var lines = [headers.map(csvCell).join(',')];
    records.forEach(function (r) {
      lines.push([r.date, r.context, r.trigger, r.inside, r.action, r.shortTerm, r.longTerm, r.next].map(csvCell).join(','));
    });
    var blob = new Blob(['\ufeff' + lines.join('\r\n')], { type: 'text/csv;charset=utf-8' });
    var url = URL.createObjectURL(blob);
    var link = document.createElement('a');
    link.href = url;
    link.download = 'islevsel-takip-' + localDate() + '.csv';
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(function () { URL.revokeObjectURL(url); }, 0);
    status.textContent = 'CSV dosyası indirildi.';
  });

  document.getElementById('printTracker').addEventListener('click', function () {
    if (!records.length) { status.textContent = 'Yazdırmak için önce en az bir kayıt ekleyin.'; return; }
    document.body.classList.add('print-tracker');
    window.print();
    document.body.classList.remove('print-tracker');
  });

  window.addEventListener('afterprint', function () {
    document.body.classList.remove('print-tracker');
  });

  document.getElementById('clearTracker').addEventListener('click', function () {
    if (!records.length) { status.textContent = 'Temizlenecek kayıt yok.'; return; }
    if (!window.confirm('Bu oturumdaki tüm kayıtlar silinsin mi? Bu işlem geri alınamaz.')) return;
    records = [];
    render();
    status.textContent = 'Bu oturumdaki kayıtlar temizlendi.';
  });

  render();
})();
