# Organik sıra ölçüm spesifikasyonu

## Amaç ve kapsam

Bu düzenek `query-portfolio.csv` içindeki öncelik, iş değeri ve dosya sırasına göre seçilen 15 kritik sorguyu canonical hedefleriyle izler. Birincil cihaz portföyde tanımlandığı gibi mobile, yardımcı kırılım desktop, ülke Türkiye'dir. Maps/local pack işletmenin online-only modeli nedeniyle KPI değildir.

## Birincil kaynak: Google Search Console

Çalıştırma:

```bash
python3 seo-ops/scripts/measure_gsc_rank.py --write
```

Sabit ölçüm sözleşmesi:

- Search Console property: `https://www.atapamukcu.com/`
- Search type: `web`
- Data state: `final`
- Country filter: `tur` (`TUR` olarak raporlanır)
- Dimensions: `query`, `page`, `country`, `device`
- Devices: `mobile` ve `desktop`
- Dönemler: veri gecikmesi için çalışma gününden üç gün önce biten 28 gün ve hemen önceki ardışık 28 gün
- Exact query eşleşmesi: Unicode casefold ve boşluk normalizasyonundan sonra tam eşleşme
- Bir sorgu ve cihaz için birden fazla URL varsa position, impression ağırlıklı hesaplanır; Google-selected URL en çok impression alan URL'dir
- OAuth dosyaları yalnız `~/.hermes/` altında okunur. Token, client secret veya bağlantı değeri repoya yazılmaz

GSC average position tarihsel, impression ağırlıklı bir performans metriğidir. Kişiselleştirilmemiş canlı Google sırası veya evrensel sıra diye sunulmaz. Düşük hacimli ve anonimleştirilmiş sorgular API satırlarından çıkabilir. Satır yoksa clicks, impressions, CTR, position, canonical match ve Top 20/10/3 değerleri `UNKNOWN` kalır; sıfır veya sıralama dışı diye yorumlanmaz.

## KPI

Birincil KPI:

`top3_coverage = observed_top3_query_count / observed_query_count`

Payda sıfırsa KPI `UNKNOWN` olur. Bilinmeyen sorgular paydaya sıfır konum gibi eklenmez. Kalıcı kazanım için en az üç ardışık güvenilir ölçüm veya iki dönemli GSC trendi aranır.

## SERP fallback sözleşmesi

İleride kullanım koşullarına uygun bir SERP kaynağı hazır olursa istek bağlamı açıkça şunları taşımalıdır:

- `gl=tr`
- `hl=tr`
- `pws=0`
- mobile ve desktop ayrı
- ads, organic ve local pack sonuç türleri ayrı
- hedef URL için final canonical host kontrolü

Sağlayıcı 403 döndürürse, proxy/kaynak konumu bilinmiyorsa, kişiselleştirme kapatılamıyorsa veya sonuç türü ayrıştırılamıyorsa position ve Top 3 `UNKNOWN` kaydedilir. Captcha/WAF bypass, kontrolsüz Google scraping, sahte SERP verisi ve satın alınmış/istenmiş API anahtarı kullanılmaz.

## 1 Eylül 2026 sonucu

- Önceki dönem: 5 Temmuz 2026 ile 1 Ağustos 2026
- Güncel dönem: 2 Ağustos 2026 ile 29 Ağustos 2026
- API erişimi başarılı, ülke filtresi sonrası ham satır sayısı sırasıyla 54 ve 195
- GSC fırsat envanterinden `kompülsiyon nedir` ve `kompulsiyon` sorguları kritik portföye eklendi; her ikisinin mobile ve desktop exact satırı gözlendi
- Mobile: 2 observed, 13 `UNKNOWN`, Top 3 sorgu 0, observed coverage yüzde 0
- `kompülsiyon nedir`: mobile 62 gösterim, 8,90 konum; desktop 4 gösterim, 11,00 konum; canonical eşleşmesi doğru
- `kompulsiyon`: mobile 39 gösterim, 10,62 konum; desktop 11 gösterim, 9,36 konum; canonical eşleşmesi doğru
- Erişim engeli yoktur. Kalan 13 exact sorgu GSC tarafından raporlanmadığı veya anonimleştirildiği için `UNKNOWN` kalır; kullanıcıdan yeni credential gerekmez

## Artefaktlar

- `scripts/measure_gsc_rank.py`: tekrar üretilebilir ölçüm
- `rank-baseline.csv`: 15 sorgu, iki dönem, iki cihaz, canonical hedef ve durum
- `rank-baseline-summary.json`: dönem, ham satır sayısı, coverage ve sınırlar
