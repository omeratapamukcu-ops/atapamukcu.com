(function(){
  // Remove values saved by the previous implementation. Tool input and output
  // now remain only in page memory and disappear when the page is closed.
  try {
    localStorage.removeItem('kaygiDongusuHaritasi');
    localStorage.removeItem('panikAtakAniPlani');
  } catch(e) {}

  function val(id){
    var el = document.getElementById(id);
    return el ? el.value.trim() : '';
  }
  function show(text){
    var out = document.getElementById('out');
    var result = document.getElementById('result');
    if (out) out.textContent = text;
    if (result) result.style.display = 'block';
  }
  window.buildMap = function(){
    var text = [
      'Tetikleyici: ' + val('trigger'),
      '',
      'Zihinden geçen senaryo: ' + val('thought'),
      '',
      'Bedende olanlar: ' + val('body'),
      '',
      'Yaptığım şey: ' + val('action'),
      '',
      'Kısa vadede sağladığı şey: ' + val('relief'),
      '',
      'Uzun vadeli maliyet: ' + val('cost'),
      '',
      'Kısa not: Bu döngüde ilk bakılacak yer çoğu zaman davranışın kısa vadede neyi rahatlattığıdır.'
    ].join('\n');
    show(text);
  };
  window.buildPlan = function(){
    var text = [
      'Panik atak anı planım',
      '',
      '1. Hatırlatma: ' + val('reminder'),
      '',
      '2. Kontrol davranışı: ' + val('avoid'),
      '',
      '3. Küçük adım: ' + val('step'),
      '',
      '4. Atak sonrası: ' + val('after'),
      '',
      'Not: Amaç paniği zorla durdurmak değil, alarm dalgasını büyüten davranışları azaltmaktır.'
    ].join('\n');
    show(text);
  };
  window.copyResult = function(){
    var out = document.getElementById('out');
    if (!out) return;
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(out.textContent);
  };
})();
