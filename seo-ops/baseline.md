# Başlangıç Skoru, 31 Ağustos 2026

## Veri durumu

- Search Console sorgu ve sayfa export'u veya API erişimi repo içinde bulunamadı.
- Bu nedenle tıklama, gösterim, CTR, ortalama konum, Google'ın seçtiği URL ve portföy Top 3 kapsama oranı henüz hesaplanamaz.
- Başlangıç portföy skoru: `UNKNOWN`, sıfır diye varsayılmadı.
- Web search backend'iyle yedi sınırlı snapshot alındı. Bunlar gl=tr, hl=tr, pws=0 garantili Google ölçümü olmadığı için yalnız keşif sinyalidir.

## Snapshot özeti

- Ölçülen non-brand sorgu: 6.
- İlk 5 içinde gözlenen atapamukcu.com sonucu: 0.
- Bu bulgu kalıcı sıralama veya index durumu kanıtı değildir.
- Marka sorgusu: backend çıktısı yetersiz.

## KPI şeması

- `top3_coverage = top3_query_count / measured_active_query_count`
- Eşikler: Top 20, Top 10, Top 3.
- Koruma: Top 3 sorgu iki ardışık ölçümde gerilerse inceleme.
- Dönüşüm: `seans_degerlendirme_cta_click` ve doğrulanabilirse nitelikli başvuru.

## Bir sonraki sağlam baseline

GSC'de son 28 gün ile önceki 28 gün, query + page + country + device kırılımında alınmalı. Marka ve non-brand ayrılmalı. Ortalama konum evrensel canlı sıra olarak sunulmamalı.
