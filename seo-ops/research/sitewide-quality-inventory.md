# Site Çapında İçerik ve SEO Kalite Envanteri

Bu rapor `python3 scripts/audit_site_quality.py` ile yeniden üretilebilir. Puan bir sıralama tahmini değil; sayfa içi kalite kapılarının kapsama oranıdır.

## Kapsam
- HTML sayfası: **83**
- Editoryal/klinik sayfa: **71**
- İç link hedefi bulunamayan rota: **0**
- Sayfa türleri: clinical-guide=69, guided-practice=1, home=1, interactive-tool=3, learning-path=1, service=2, trust-or-navigation=6

## Site çapında açıklar
- `depth`: 21 sayfa
- `sources`: 5 sayfa
- `visible_date`: 3 sayfa
- `date_modified`: 2 sayfa
- `schema`: 1 sayfa
- `author`: 1 sayfa

## En düşük puanlı ilk 30 sayfa

| Sayfa | Tür | Kelime | Inbound | Puan | Açıklar |
|---|---|---:|---:|---:|---|
| `/kullanim-sartlari` | clinical-guide | 295 | 82 | 58 | schema;visible_date;date_modified;sources;depth |
| `/surec-temelli-terapi` | clinical-guide | 376 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/surec` | clinical-guide | 219 | 4 | 75 | author;visible_date;depth |
| `/act-bdt-farki` | clinical-guide | 389 | 3 | 83 | sources;depth |
| `/editorial-ilkeler` | clinical-guide | 523 | 82 | 83 | sources;depth |
| `/araclar` | trust-or-navigation | 195 | 81 | 92 | depth |
| `/ogrenme-yollari/kaygi` | learning-path | 346 | 7 | 92 | depth |
| `/kabul-ve-kararlilik-terapisi` | clinical-guide | 484 | 6 | 92 | depth |
| `/bdt-nedir` | clinical-guide | 506 | 6 | 92 | depth |
| `/cbt-nedir` | clinical-guide | 551 | 4 | 92 | depth |
| `/kisisellestirilmis-terapi` | clinical-guide | 554 | 1 | 92 | depth |
| `/okb-belirtileri` | clinical-guide | 574 | 6 | 92 | depth |
| `/davranissal-aktivasyon` | clinical-guide | 627 | 6 | 92 | depth |
| `/karar-verememe` | clinical-guide | 645 | 1 | 92 | depth |
| `/kendini-sabote-etmek` | clinical-guide | 657 | 3 | 92 | depth |
| `/travma-belirtileri` | clinical-guide | 665 | 2 | 92 | depth |
| `/kaygi-dongusu` | clinical-guide | 676 | 14 | 92 | depth |
| `/sosyal-kaygi-belirtileri` | clinical-guide | 678 | 4 | 92 | depth |
| `/kabul-ne-demek` | clinical-guide | 680 | 4 | 92 | depth |
| `/travma-kacinma` | clinical-guide | 686 | 2 | 92 | depth |
| `/ofke-kontrolu` | clinical-guide | 695 | 2 | 92 | depth |
| `/kompulsiyon-nedir` | clinical-guide | 949 | 6 | 92 | sources |
| `/araclar/panik-atak-ani-plani` | interactive-tool | 185 | 3 | 100 | — |
| `/araclar/kaygi-dongusu-haritasi` | interactive-tool | 212 | 8 | 100 | — |
| `/araclar/islevsel-takip` | interactive-tool | 331 | 9 | 100 | — |
| `/gizlilik` | trust-or-navigation | 362 | 82 | 100 | — |
| `/uygulamalar/kacinma-haritasi` | guided-practice | 413 | 12 | 100 | — |
| `/hakkimda` | trust-or-navigation | 522 | 82 | 100 | — |
| `/antalya-online-psikolog` | trust-or-navigation | 545 | 2 | 100 | — |
| `/online-terapi-nasil-isler` | trust-or-navigation | 586 | 3 | 100 | — |

## Doğrulama notları
- Yinelenen title ve description alanları CSV'de ayrı sütunlardır.
- Kaynak kontrolü görünür bir kaynak başlığı ile harici bağlantının birlikte bulunmasını ister.
- Klinik rehberlerde derinlik eşiği 700 kelimedir; bu eşik tek başına kalite kanıtı değildir.
- Aktif SEO deneylerindeki sayfalar bu envanterle değiştirilmez; değişiklik sırası deney kayıtlarıyla birlikte yönetilir.
