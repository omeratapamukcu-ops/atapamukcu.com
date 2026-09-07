# Site Çapında İçerik ve SEO Kalite Envanteri

Bu rapor `python3 scripts/audit_site_quality.py` ile yeniden üretilebilir. Puan bir sıralama tahmini değil; sayfa içi kalite kapılarının kapsama oranıdır.

## Kapsam
- HTML sayfası: **82**
- Editoryal/klinik sayfa: **70**
- İç link hedefi bulunamayan rota: **0**
- Sayfa türleri: clinical-guide=68, guided-practice=1, home=1, interactive-tool=3, learning-path=1, service=2, trust-or-navigation=6

## Site çapında açıklar
- `depth`: 30 sayfa
- `sources`: 14 sayfa
- `visible_date`: 12 sayfa
- `date_modified`: 7 sayfa
- `author`: 3 sayfa
- `schema`: 1 sayfa
- `breadcrumb`: 1 sayfa

## En düşük puanlı ilk 30 sayfa

| Sayfa | Tür | Kelime | Inbound | Puan | Açıklar |
|---|---|---:|---:|---:|---|
| `/psikoloji-3` | clinical-guide | 175 | 80 | 67 | author;visible_date;sources;depth |
| `/baslangic` | clinical-guide | 202 | 81 | 67 | author;visible_date;sources;depth |
| `/psikolojik-surec-haritasi` | clinical-guide | 344 | 7 | 67 | visible_date;date_modified;sources;depth |
| `/terapi-surecinde-dongu-analizi` | clinical-guide | 347 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/surec-temelli-terapi` | clinical-guide | 377 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/takinti-hastaligi` | clinical-guide | 436 | 3 | 67 | visible_date;date_modified;sources;depth |
| `/iliski-sorunlari` | clinical-guide | 521 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/ucak-korkusu` | clinical-guide | 613 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/surec` | clinical-guide | 219 | 4 | 75 | author;visible_date;depth |
| `/gizlilik` | trust-or-navigation | 340 | 81 | 75 | schema;breadcrumb;depth |
| `/antalya-panik-atak-psikolog` | clinical-guide | 471 | 3 | 75 | visible_date;sources;depth |
| `/antalya-kaygi-psikolog` | clinical-guide | 635 | 5 | 75 | visible_date;sources;depth |
| `/panik-bozukluk` | clinical-guide | 767 | 5 | 75 | visible_date;date_modified;sources |
| `/act-bdt-farki` | clinical-guide | 390 | 3 | 83 | sources;depth |
| `/editorial-ilkeler` | clinical-guide | 523 | 81 | 83 | sources;depth |
| `/araclar` | trust-or-navigation | 196 | 80 | 92 | depth |
| `/ogrenme-yollari/kaygi` | learning-path | 346 | 7 | 92 | depth |
| `/kabul-ve-kararlilik-terapisi` | clinical-guide | 485 | 6 | 92 | depth |
| `/bdt-nedir` | clinical-guide | 507 | 6 | 92 | depth |
| `/cbt-nedir` | clinical-guide | 552 | 4 | 92 | depth |
| `/kisisellestirilmis-terapi` | clinical-guide | 555 | 1 | 92 | depth |
| `/okb-belirtileri` | clinical-guide | 577 | 6 | 92 | depth |
| `/davranissal-aktivasyon` | clinical-guide | 630 | 6 | 92 | depth |
| `/karar-verememe` | clinical-guide | 648 | 1 | 92 | depth |
| `/kendini-sabote-etmek` | clinical-guide | 660 | 3 | 92 | depth |
| `/travma-belirtileri` | clinical-guide | 666 | 2 | 92 | depth |
| `/kaygi-dongusu` | clinical-guide | 676 | 14 | 92 | depth |
| `/kabul-ne-demek` | clinical-guide | 681 | 4 | 92 | depth |
| `/sosyal-kaygi-belirtileri` | clinical-guide | 681 | 4 | 92 | depth |
| `/travma-kacinma` | clinical-guide | 687 | 2 | 92 | depth |

## Doğrulama notları
- Yinelenen title ve description alanları CSV'de ayrı sütunlardır.
- Kaynak kontrolü görünür bir kaynak başlığı ile harici bağlantının birlikte bulunmasını ister.
- Klinik rehberlerde derinlik eşiği 700 kelimedir; bu eşik tek başına kalite kanıtı değildir.
- Aktif SEO deneylerindeki sayfalar bu envanterle değiştirilmez; değişiklik sırası deney kayıtlarıyla birlikte yönetilir.
