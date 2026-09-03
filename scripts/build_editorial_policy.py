#!/usr/bin/env python3
"""Build the public editorial-policy page and connect it across the static site."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-03"
URL = "https://www.atapamukcu.com/editorial-ilkeler"
TITLE = "Editoryal İlkeler ve Kaynak Politikası | Psikolog Ata Pamukçu"
DESCRIPTION = "atapamukcu.com psikoloji içeriklerinin yazarlık, kaynak seçimi, güncelleme, klinik güvenlik, düzeltme ve yapay zekâ desteği ilkeleri."

MAIN = r'''<main id="main" class="editorial-policy" tabindex="-1">
  <section class="page-hero">
    <div class="container">
      <nav aria-label="Breadcrumb" class="breadcrumb"><a href="/">Ana Sayfa</a><span aria-hidden="true">›</span><span aria-current="page">Editoryal İlkeler</span></nav>
      <p class="eyebrow">ŞEFFAFLIK VE KLİNİK GÜVENLİK</p>
      <h1>Editoryal İlkeler ve Kaynak Politikası</h1>
      <p class="lead">Bu sayfa, atapamukcu.com’daki psikoloji içeriklerinin nasıl hazırlandığını, hangi kaynakların tercih edildiğini, ne zaman güncellendiğini ve okuyucunun güvenliğini korumak için hangi sınırların gözetildiğini açıklar.</p>
      <p class="article-meta"><strong>Yazar ve editoryal sorumlu:</strong> Psikolog Ata Pamukçu · <strong>Yayımlanma:</strong> 3 Eylül 2026 · <strong>Son gözden geçirme:</strong> 3 Eylül 2026</p>
    </div>
  </section>

  <article class="section article-content">
    <div class="container article-container">
      <section aria-labelledby="amac"><h2 id="amac">Amaç ve kapsam</h2>
        <p>Bu site, psikoloji kavramlarını günlük yaşamla ilişkilendiren genel bilgilendirme içerikleri ve online psikolojik destek süreci hakkında açıklamalar sunar. İçeriklerin amacı bir kişiye tanı koymak, kişiye özel tedavi önermek veya acil yardımın yerini almak değildir. Belirti benzerlikleri tek başına klinik değerlendirme anlamına gelmez.</p>
      </section>

      <section aria-labelledby="sorumluluk"><h2 id="sorumluluk">Yazarlık ve mesleki sorumluluk</h2>
        <p>İçeriklerin yazar ve editoryal sorumlusu <a href="/hakkimda">Psikolog Ata Pamukçu’dur</a>. Mesleki yaklaşım; Bağlamsal Davranış Bilimleri, Kabul ve Kararlılık Terapisi (ACT), Süreç Temelli Terapi (PBT), bilişsel-davranışçı yaklaşımlar ve işlevsel analizden yararlanır. Yetkinlik sınırını aşan veya tıbbi karar gerektiren konular ilgili sağlık uzmanlarına yönlendirilir.</p>
      </section>

      <section aria-labelledby="kaynak"><h2 id="kaynak">Kaynak seçimi ve iddia standardı</h2>
        <p>Klinik ve sağlıkla ilgili iddialarda kaynak önceliği şöyledir: güncel klinik kılavuzlar; Dünya Sağlık Örgütü ve ulusal sağlık kurumları gibi kamu sağlığı kaynakları; sistematik derleme ve meta-analizler; hakemli birincil araştırmalar; alanın temel mesleki kuruluşları. Ticari bloglar, kaynağı belirsiz özetler ve yalnızca popülerliğe dayanan içerikler klinik iddia dayanağı olarak kullanılmaz.</p>
        <p>Bir kaynağın sayfada yer alması, sayfadaki her cümleyi desteklediği anlamına gelmez. Kaynaklar ilgili iddianın kapsamına mümkün olduğunca yakın verilir; araştırma bulguları kesinlikten daha güçlü ifade edilmez. Çelişkili veya sınırlı kanıtta belirsizlik açıkça belirtilir.</p>
      </section>

      <section aria-labelledby="islev"><h2 id="islev">Tanı listesinden işlevsel anlayışa</h2>
        <p>İçerikler yalnız belirti sıralamayı hedeflemez. Mümkün olduğunda tetikleyici, düşünce ve duygu, davranış, kısa vadeli rahatlama ve uzun vadeli maliyet arasındaki döngü açıklanır. Böylece okur, kendi kendine tanı koymaya yönelmeden yaşantısındaki örüntüyü daha güvenli biçimde gözlemleyebilir.</p>
      </section>

      <section aria-labelledby="guvenlik"><h2 id="guvenlik">Klinik güvenlik sınırları</h2>
        <ul>
          <li>Genel egzersizler, kişiye özel değerlendirme veya terapi yerine geçmez.</li>
          <li>Maruz bırakma ve yoğun duygusal çalışma gibi uygulamalar herkese aynı şekilde önerilmez; güvenlik, işlev ve kişinin koşulları değerlendirilir.</li>
          <li>İlaç başlama, bırakma veya doz değişikliği konusunda yönlendirme yapılmaz; bu kararlar hekimle ele alınır.</li>
          <li>Kendine ya da başkasına zarar verme riski veya acil bir durum varsa internet içeriğiyle yetinilmemeli; Türkiye’de 112 aranmalı veya en yakın acil servise başvurulmalıdır.</li>
        </ul>
      </section>

      <section aria-labelledby="guncelleme"><h2 id="guncelleme">Yayın, güncelleme ve sürüm ilkesi</h2>
        <p>Yeni klinik kılavuz, önemli kanıt değişikliği, güvenlik sorunu, kapsamlı içerik düzenlemesi veya işlevsiz bağlantı saptandığında sayfa yeniden değerlendirilir. “Taze” görünmek amacıyla içerik değişmeden tarih yenilenmez. Görünür güncelleme tarihi ve yapılandırılmış verideki tarih birbiriyle uyumlu tutulur.</p>
      </section>

      <section aria-labelledby="yapayzeka"><h2 id="yapayzeka">Yapay zekâ ve otomasyon desteği</h2>
        <p>Araştırma envanteri, teknik kontrol, yazım denetimi, iç bağlantı analizi veya taslak geliştirme gibi işlerde otomasyon ve yapay zekâ araçlarından yararlanılabilir. Bu araçların çıktıları bağımsız otorite kabul edilmez. Klinik doğruluk, kaynakla eşleşme, dil, güvenlik ve yayımlanan son içerikten Ata Pamukçu sorumludur; otomatik üretilen metin incelemesiz yayımlanmaz.</p>
      </section>

      <section aria-labelledby="duzeltme"><h2 id="duzeltme">Düzeltme ve geri bildirim</h2>
        <p>Kaynak hatası, güncelliğini yitirmiş bilgi, erişilebilirlik sorunu veya yanıltıcı bir ifade fark ederseniz <a href="mailto:atapamukcu@gmail.com">atapamukcu@gmail.com</a> adresinden bildirebilirsiniz. Maddi hata doğrulandığında içerik düzeltilir; önemli kapsam değişikliklerinde sayfanın güncelleme tarihi de değiştirilir.</p>
      </section>

      <section aria-labelledby="gizlilik"><h2 id="gizlilik">Gizlilik ve ölçüm</h2>
        <p>Sitedeki içerik performansı, daha yararlı ve bulunabilir sayfalar üretmek için toplu arama ve kullanım verileriyle değerlendirilebilir. Formlar ve tarayıcı araçları için geçerli veri kullanımı ilgili sayfada ayrıca belirtilir. Ayrıntılar için <a href="/gizlilik">gizlilik ve analitik tercihleri</a> sayfasına bakabilirsiniz.</p>
      </section>

      <aside class="clinical-note" aria-label="Önemli sınır"><strong>Önemli:</strong> Buradaki bilgiler genel eğitim amaçlıdır. Kişisel bir değerlendirme için uygun bir sağlık profesyoneline başvurun; acil riskte 112’yi arayın.</aside>
    </div>
  </article>
</main>'''

SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "AboutPage",
            "@id": URL + "#webpage",
            "url": URL,
            "name": TITLE,
            "description": DESCRIPTION,
            "inLanguage": "tr-TR",
            "datePublished": TODAY,
            "dateModified": TODAY,
            "isPartOf": {"@id": "https://www.atapamukcu.com/#website"},
            "author": {"@id": "https://www.atapamukcu.com/#person"},
            "reviewedBy": {"@id": "https://www.atapamukcu.com/#person"},
            "mainEntity": {"@type": "Thing", "name": "atapamukcu.com editoryal ilkeleri"},
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": "https://www.atapamukcu.com/"},
                {"@type": "ListItem", "position": 2, "name": "Editoryal İlkeler", "item": URL},
            ],
        },
    ],
}


def replace_meta(text: str) -> str:
    text = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", text, count=1, flags=re.S)
    text = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESCRIPTION}">', text, count=1)
    text = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{URL}">', text, count=1)
    replacements = {
        "og:title": "Editoryal İlkeler ve Kaynak Politikası",
        "og:description": DESCRIPTION,
        "og:url": URL,
        "og:type": "website",
        "twitter:title": "Editoryal İlkeler ve Kaynak Politikası",
        "twitter:description": DESCRIPTION,
    }
    for key, value in replacements.items():
        attr = "property" if key.startswith("og:") else "name"
        text = re.sub(rf'<meta {attr}="{re.escape(key)}" content="[^"]*">', f'<meta {attr}="{key}" content="{value}">', text, count=1)
    text = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", text, flags=re.S)
    schema_tag = '<script type="application/ld+json">' + json.dumps(SCHEMA, ensure_ascii=False, separators=(",", ":")) + "</script>"
    return text.replace("</head>", "  " + schema_tag + "\n</head>", 1)


def add_footer_policy(text: str) -> str:
    if 'href="/editorial-ilkeler"' in text:
        return text
    pattern = r'(<p><a href="/hakkimda">Hakkımda</a></p>)'
    replacement = r'\1<p><a href="/editorial-ilkeler">Editoryal İlkeler</a></p><p><a href="/gizlilik">Gizlilik</a></p>'
    updated, count = re.subn(pattern, replacement, text, count=1)
    if not count:
        raise RuntimeError("Footer insertion point not found")
    return updated


def main() -> None:
    template = (ROOT / "site-haritasi.html").read_text(encoding="utf-8")
    page = replace_meta(template)
    page, count = re.subn(r"<main\b[\s\S]*?</main>", MAIN, page, count=1)
    if count != 1:
        raise RuntimeError("Could not replace main content")
    (ROOT / "editorial-ilkeler.html").write_text(page, encoding="utf-8")

    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        old = path.read_text(encoding="utf-8")
        new = add_footer_policy(old)
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed += 1

    sitemap = ROOT / "sitemap.xml"
    s = sitemap.read_text(encoding="utf-8")
    if URL not in s:
        entry = f'''  <url>\n    <loc>{URL}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.5</priority>\n  </url>\n'''
        s = s.replace("</urlset>", entry + "</urlset>")
        sitemap.write_text(s, encoding="utf-8")

    llms = ROOT / "llms.txt"
    l = llms.read_text(encoding="utf-8")
    if URL not in l:
        l += f"\n- [Editoryal İlkeler ve Kaynak Politikası]({URL}): Yazarlık, kaynak seçimi, güncelleme, güvenlik, düzeltme ve yapay zekâ desteği ilkeleri.\n"
        llms.write_text(l, encoding="utf-8")

    context_path = ROOT / "ai-context.json"
    context = json.loads(context_path.read_text(encoding="utf-8"))
    context["dateModified"] = TODAY
    context["editorialPolicy"].update({
        "publicPolicyUrl": URL,
        "authorAccountability": "Psikolog Ata Pamukçu is the author and editorially accountable person.",
        "sourcePriority": ["clinical guidelines", "public health institutions", "systematic reviews and meta-analyses", "peer-reviewed primary research"],
        "correctionsEmail": "atapamukcu@gmail.com",
        "aiAssistance": "Automation or AI may assist research, technical checks and drafting; outputs are reviewed for clinical accuracy, sources, safety and language before publication.",
    })
    pages = context.get("importantPages", [])
    if not any((isinstance(x, str) and x == URL) or (isinstance(x, dict) and x.get("url") == URL) for x in pages):
        pages.append({"name": "Editoryal İlkeler ve Kaynak Politikası", "url": URL, "role": "Public editorial and source policy"})
    context_path.write_text(json.dumps(context, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"editorial_page=created footer_pages_changed={changed}")


if __name__ == "__main__":
    main()
