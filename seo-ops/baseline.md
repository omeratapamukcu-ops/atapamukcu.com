# Başlangıç Skoru, 31 Ağustos 2026

## Veri durumu

- Search Console API erişimi doğrulandı. `web` arama türünde, Türkiye ülke filtresiyle query + page + country + device kırılımı alındı.
- Ardışık dönemler: 4 Temmuz ile 31 Temmuz 2026 ve 1 Ağustos ile 28 Ağustos 2026.
- Ülke filtresi sonrası API sırasıyla 55 ve 196 ham satır döndürdü.
- Kritik 15 exact sorgunun mobile veya desktop satırı iki dönemde de bulunmadı. Düşük hacimli sorgular GSC'de anonimleştirilebildiği için bu durum sıfır gösterim veya sıralama dışı olma kanıtı değildir.
- Başlangıç portföy Top 3 kapsama oranı: `UNKNOWN`. Position tahmin edilmedi ve bilinmeyen sorgular 0 konum olarak sayılmadı.

## Ölçüm kapsamı

- 15 kritik sorgu, canonical hedefleriyle `rank-baseline.csv` dosyasına yazıldı.
- Mobile birincil KPI kırılımıdır; desktop yardımcı kırılım olarak saklandı.
- Google-selected URL, position, clicks, impressions ve CTR yalnız GSC exact satırı varsa doldurulur.
- Search Console average position evrensel veya anlık canlı sıra değildir.
- Önceki web-search snapshot'ları `gl=tr`, `hl=tr`, `pws=0` garantili olmadığı için sıra kanıtı sayılmaz.

## KPI şeması

- `top3_coverage = observed_top3_query_count / observed_query_count`
- Güncel mobile: 0 observed, 15 UNKNOWN, coverage `UNKNOWN`.
- Eşikler: Top 20, Top 10, Top 3.
- Koruma: Top 3 sorgu iki ardışık ölçümde gerilerse inceleme.
- Kalıcılık: üç ardışık güvenilir ölçüm veya iki dönemli GSC trendi.
- Dönüşüm: `seans_degerlendirme_cta_click` ve doğrulanabilirse nitelikli başvuru.

## Tekrar üretim

```bash
python3 seo-ops/scripts/measure_gsc_rank.py --write
```

Detaylı yöntem, SERP fallback güven kapıları ve veri sınırları `rank-measurement-spec.md` dosyasındadır. Yeni credential gerekmiyor. En yüksek etkili sonraki iş, günlük tekrar ölçümle GSC exact satırı oluşmasını izlemek ve ilk gözlem geldiğinde canonical eşleşmesi ile Top 20/10/3 durumunu değerlendirmektir.
