# SEO Büyüme Çalışma Alanı

Bu dizin, atapamukcu.com organik SEO büyüme döngüsünün sürümlenebilir çalışma alanıdır. Gizli bilgi içermez.

## İşletme sınırı

Görüşmeler yalnızca online yapılır. Sabit ofis ve yüz yüze hizmet yoktur. Maps/local pack büyüme KPI'ı değildir.

## Dosyalar

- `query-portfolio.csv`: Sorgu portföyü ve sorgu, canonical URL eşlemesi.
- `measurements.csv`: Tarihli GSC ve kişiselleştirilmemiş SERP gözlemleri.
- `baseline.md`: Başlangıç ölçüm durumu ve KPI tanımları.
- `rank-measurement-spec.md`: GSC ölçüm sözleşmesi, SERP güven kapıları ve veri sınırları.
- `rank-baseline.csv`: Kritik 18 P0 sorgunun iki dönem ve iki cihaz baseline çıktısı.
- `rank-baseline-summary.json`: Top 3 coverage durumu ve ölçüm özeti.
- `scripts/measure_gsc_rank.py`: Credential değerlerini kaydetmeden GSC ölçümünü tekrar üretir.
- `competitors.md`: Sorgu bazlı ilk sonuç ve rakip öğrenimleri.
- `backlog.csv`: Etki, güven, efor ve ölçülebilirlik önceliği.
- `changelog.md`: Uygulanan SEO değişiklikleri ve doğrulama kanıtı.
- `sitewide-quality-standard.md`: Her sayfa için 12 yayın kapısı, konu kümeleri ve dönüşüm sırası.
- `research/sitewide-quality-inventory.csv`: Yeniden üretilebilir sayfa bazlı kalite envanteri.
- `research/sitewide-quality-inventory.md`: Envanterin insan tarafından okunabilir özeti ve öncelik sırası.
- `research/online-psikolog-brief.md`: İlk ticari cornerstone araştırma brief'i.

## Ölçüm kuralları

1. Ana KPI, ölçülebilir portföyde Top 3 kapsama oranıdır.
2. GSC konumu sorgu, URL, ülke, cihaz ve tarih aralığıyla saklanır; evrensel canlı sıra diye sunulmaz.
3. SERP snapshot, kalıcı kazanım sayılmaz. Üç ardışık ölçüm veya GSC trendi gerekir.
4. Organik sonuçlar ile Maps/local pack ayrılır.
5. `position` bilinmiyorsa boş bırakılır; tahmin yazılmaz.
6. Kritik sorgular günlük, geniş portföy haftalık rotasyonla ölçülür.

## Kritik sorgu ölçümünü çalıştırma

```bash
python3 seo-ops/scripts/measure_gsc_rank.py --write
```

GSC satırı bulunmayan exact sorgular `UNKNOWN` kalır. Bunlar sıfır gösterim, sıralama dışı veya Top 3 dışında kabul edilmez.
