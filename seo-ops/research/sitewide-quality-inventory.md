# Site Çapında İçerik ve SEO Kalite Envanteri

Bu rapor `python3 scripts/audit_site_quality.py` ile yeniden üretilebilir. Puan bir sıralama tahmini değil; sayfa içi kalite kapılarının kapsama oranıdır.

## Kapsam
- HTML sayfası: **83**
- Editoryal/klinik sayfa: **70**
- İç link hedefi bulunamayan rota: **0**
- Sayfa türleri: clinical-guide=68, guided-practice=1, home=1, interactive-tool=3, learning-path=1, service=2, trust-or-navigation=6, utility=1

## Site çapında açıklar
- `depth`: 38 sayfa
- `sources`: 23 sayfa
- `visible_date`: 20 sayfa
- `date_modified`: 14 sayfa
- `author`: 3 sayfa
- `schema`: 2 sayfa
- `canonical`: 1 sayfa
- `inbound`: 1 sayfa
- `breadcrumb`: 1 sayfa

## En düşük puanlı ilk 30 sayfa

| Sayfa | Tür | Kelime | Inbound | Puan | Açıklar |
|---|---|---:|---:|---:|---|
| `/psikoloji-3` | clinical-guide | 175 | 81 | 67 | author;visible_date;sources;depth |
| `/baslangic` | clinical-guide | 202 | 82 | 67 | author;visible_date;sources;depth |
| `/psikolojik-surec-haritasi` | clinical-guide | 344 | 7 | 67 | visible_date;date_modified;sources;depth |
| `/terapi-surecinde-dongu-analizi` | clinical-guide | 347 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/anda-kalma` | clinical-guide | 374 | 1 | 67 | visible_date;date_modified;sources;depth |
| `/surec-temelli-terapi` | clinical-guide | 377 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/basarisizlik-korkusu` | clinical-guide | 387 | 1 | 67 | visible_date;date_modified;sources;depth |
| `/mukemmeliyetcilik` | clinical-guide | 396 | 4 | 67 | visible_date;date_modified;sources;depth |
| `/takinti-hastaligi` | clinical-guide | 436 | 3 | 67 | visible_date;date_modified;sources;depth |
| `/tssb` | clinical-guide | 459 | 3 | 67 | visible_date;date_modified;sources;depth |
| `/uyku-sorunlari` | clinical-guide | 508 | 3 | 67 | visible_date;date_modified;sources;depth |
| `/iliski-sorunlari` | clinical-guide | 521 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/sosyal-kaygi-neden-olur` | clinical-guide | 549 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/ucak-korkusu` | clinical-guide | 613 | 2 | 67 | visible_date;date_modified;sources;depth |
| `/404` | utility | 27 | 0 | 75 | canonical;schema;inbound |
| `/surec` | clinical-guide | 219 | 4 | 75 | author;visible_date;depth |
| `/gizlilik` | trust-or-navigation | 222 | 82 | 75 | schema;breadcrumb;depth |
| `/antalya-panik-atak-psikolog` | clinical-guide | 471 | 3 | 75 | visible_date;sources;depth |
| `/antalya-sosyal-kaygi-psikolog` | clinical-guide | 473 | 5 | 75 | visible_date;sources;depth |
| `/antalya-kaygi-psikolog` | clinical-guide | 635 | 5 | 75 | visible_date;sources;depth |
| `/panik-bozukluk` | clinical-guide | 767 | 5 | 75 | visible_date;date_modified;sources |
| `/sosyal-fobi` | clinical-guide | 796 | 3 | 75 | visible_date;date_modified;sources |
| `/act-bdt-farki` | clinical-guide | 390 | 3 | 83 | sources;depth |
| `/editorial-ilkeler` | clinical-guide | 523 | 82 | 83 | sources;depth |
| `/antalya-okb-psikolog` | clinical-guide | 653 | 5 | 83 | sources;depth |
| `/araclar` | trust-or-navigation | 196 | 81 | 92 | depth |
| `/ogrenme-yollari/kaygi` | learning-path | 346 | 7 | 92 | depth |
| `/kabul-ve-kararlilik-terapisi` | clinical-guide | 485 | 6 | 92 | depth |
| `/bdt-nedir` | clinical-guide | 507 | 6 | 92 | depth |
| `/cbt-nedir` | clinical-guide | 552 | 4 | 92 | depth |

## Doğrulama notları
- Yinelenen title ve description alanları CSV'de ayrı sütunlardır.
- Kaynak kontrolü görünür bir kaynak başlığı ile harici bağlantının birlikte bulunmasını ister.
- Klinik rehberlerde derinlik eşiği 700 kelimedir; bu eşik tek başına kalite kanıtı değildir.
- Aktif SEO deneylerindeki sayfalar bu envanterle değiştirilmez; değişiklik sırası deney kayıtlarıyla birlikte yönetilir.
