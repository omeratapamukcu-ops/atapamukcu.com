# Değişiklik Günlüğü

## 2026-08-31

- İlk SEO operasyon çalışma alanı ve 25 sorguluk portföy oluşturuldu.
- Query, canonical URL, intent, iş değeri, ülke, cihaz, öncelik ve ölçüm sıklığı eşleştirildi.
- GSC verisi bulunmadığı için başlangıç Top 3 skoru dürüstçe `UNKNOWN` bırakıldı.
- `/online-psikolog` title, meta description, H1, Article headline ve güncellik sinyali ana ticari intent ile eşleştirildi.
- Görünür FAQ ve FAQPage yanıtı online-only işletme gerçeğiyle birebir eşleştirildi.
- Ana sayfa, hakkımda, süreç, başlangıç, site haritası ve Antalya sayfalarındaki açık yüz yüze hizmet iddiaları kaldırıldı.
- Değişen URL'lerin sitemap `lastmod` değerleri 2026-08-31 olarak güncellendi.
- `git diff --check` geçti; 196 JSON-LD bloğu, sitemap XML, `ai-context.json`, local links, duplicate IDs, canonical, title/meta uzunluğu, FAQ görünür/schema eşleşmesi ve 25 sorgunun hedef URL'leri odaklı betikle doğrulandı.
- `ad_hoc_changed_behavior=PASS`, `canonical_suite=NOT_AVAILABLE`.
- Headless Chrome yerel ve canlı `/online-psikolog` sayfasında yeni H1, canonical ve FAQ marker'larını render etti. Sayfa kaynakları 200 döndü; sayfa kaynaklı JavaScript hatası gözlenmedi.
- Uygulama commit'i `82e08ee` olarak `origin/main` dalına gönderildi. Vercel production deployment `Ready` oldu; provider deployment ve public custom domain aynı yeni marker'ları gösterdi.
- Public domain üzerinde dokuz değişen route/surface için HTTP 200 ve içerik marker kontrolü geçti.
