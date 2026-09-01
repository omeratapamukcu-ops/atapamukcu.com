# Başlangıç Skoru, 1 Eylül 2026

## Veri durumu

- Search Console API erişimi doğrulandı. `web` arama türünde, Türkiye ülke filtresiyle query + page + country + device kırılımı alındı.
- Ardışık dönemler: 5 Temmuz ile 1 Ağustos 2026 ve 2 Ağustos ile 29 Ağustos 2026.
- Ülke filtresi sonrası API sırasıyla 54 ve 195 ham satır döndürdü.
- GSC fırsat envanterinden kritik portföye alınan `kompülsiyon nedir` ve `kompulsiyon` sorgularının mobile ve desktop satırları gözlendi. Kalan 13 exact sorgu `UNKNOWN`; bu durum sıfır gösterim veya sıralama dışı olma kanıtı değildir.
- Güncel mobile portföy Top 3 kapsama oranı, yalnız gözlenen iki sorgu arasında yüzde 0'dır. Bilinmeyen sorgular 0 konum olarak sayılmadı.

## Ölçüm kapsamı

- 15 kritik sorgu, canonical hedefleriyle `rank-baseline.csv` dosyasına yazıldı.
- Mobile birincil KPI kırılımıdır; desktop yardımcı kırılım olarak saklandı.
- Google-selected URL, position, clicks, impressions ve CTR yalnız GSC exact satırı varsa doldurulur.
- Search Console average position evrensel veya anlık canlı sıra değildir.
- Önceki web-search snapshot'ları `gl=tr`, `hl=tr`, `pws=0` garantili olmadığı için sıra kanıtı sayılmaz.

## KPI şeması

- `top3_coverage = observed_top3_query_count / observed_query_count`
- Güncel mobile: 2 observed, 13 `UNKNOWN`, observed coverage yüzde 0.
- `kompülsiyon nedir`: mobile 62 gösterim, 0 tıklama, yüzde 0 CTR, 8,90 ortalama konum; canonical eşleşmesi doğru.
- `kompulsiyon`: mobile 39 gösterim, 0 tıklama, yüzde 0 CTR, 10,62 ortalama konum; canonical eşleşmesi doğru.
- Eşikler: Top 20, Top 10, Top 3.
- Koruma: Top 3 sorgu iki ardışık ölçümde gerilerse inceleme.
- Kalıcılık: üç ardışık güvenilir ölçüm veya iki dönemli GSC trendi.
- Dönüşüm: `seans_degerlendirme_cta_click` ve doğrulanabilirse nitelikli başvuru.

## Tekrar üretim

```bash
python3 seo-ops/scripts/measure_gsc_rank.py --write
```

Detaylı yöntem, SERP fallback güven kapıları ve veri sınırları `rank-measurement-spec.md` dosyasındadır. Yeni credential gerekmiyor. `/kompulsiyon-nedir` CTR/intent paketi için erken sinyal 15 Eylül, tam 28 günlük değerlendirme 29 Eylül 2026 tarihinde yapılacaktır; kalan exact sorgular günlük ölçümde `UNKNOWN`dan gözlenebilir duruma geçtikçe kapsama hesabına alınacaktır.
