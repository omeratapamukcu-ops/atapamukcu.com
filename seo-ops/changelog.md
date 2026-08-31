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
- `/online-psikolog` hero ve gövde CTA'ları açık `data-analytics-event` işaretleyicisiyle `seans_degerlendirme_cta_click` KPI olayına bağlandı; mevcut `whatsapp_click` ve `appointment_start` olayları geriye dönük karşılaştırma için korundu.
- Yerel ve canlı tarayıcı tıklamasında üç olayın GA4 kuyruğuna yalnızca genel `event_surface` ve `transport_type` parametreleriyle düştüğü doğrulandı; URL, telefon, e-posta, WhatsApp mesajı veya sağlık içeriği taşınmadı.
- CTA ölçümü commit `cb4dba2` ile yayınlandı; public HTML'de iki CTA marker'ı ve canlı JavaScript'te olay işleyicisi doğrulandı.
- Canlı `/online-psikolog` Lighthouse sonucu: Performance 94, Accessibility 95, Best Practices 100, SEO 100; LCP 2,8 sn, CLS 0 ve TBT 130 ms.
- `/online-psikolog` sayfasına APA 2024 Telepsikoloji Uygulama Rehberi ile Thomas ve arkadaşlarının 2021 hakemli videokonferans psikoterapi derlemesini içeren görünür kaynakça eklendi; sonuç garantisi vermeyen uygunluk sınırı açıklandı.
- Eski aylık regresyon betiğinin daha yeni `dateModified/lastmod` değerlerini hata sayması düzeltildi; tarihler artık 2026-08-05 tabanının gerisine düşmediği sürece kabul ediliyor ve yeni CTA KPI olayı test ediliyor.
- `monthly_seo=PASS`, `analytics_events=6 privacy_guard=PASS`, `verify_evergreen=PASS`, kaynak bölümü, duplicate ID, JavaScript/Python sözdizimi ve `git diff --check` doğrulamaları geçti.
- Rakip yapı karşılaştırmasında bulunan hızlı karar özeti boşluğu, `/online-psikolog` hero alanına yalnızca doğrulanmış dört bilgi eklenerek kapatıldı: yalnızca online, ücretsiz değerlendirme, özel alan/internet ve acil yardım sınırı.
- GA4 için analitik depolama varsayılan `denied` yapıldı; kabul/ret paneli, kalıcı tarayıcı tercihi, ayarları yeniden açma, reklam sinyallerini kapatma ve ret durumunda erişilebilir `_ga` çerezlerini silme eklendi.
- CTA olayları onay yokken gönderilmeyecek biçimde sınırlandı. Yerel tarayıcı testinde onaysız tıklama 0 olay, izin sonrası üç beklenen olay, ret sonrası `analytics_storage: denied` ve test `_ga` çerezinin silinmesi doğrulandı.
- `/gizlilik` sayfası ve sitemap kaydı oluşturuldu; ölçülen olaylar, gönderilmeyen hassas alanlar, çerezler, Google hizmet sağlayıcısı ve tercih geri çekme yolu görünür biçimde açıklandı.
- Klinik E‑E‑A‑T envanteri `seo-ops/research/clinical-eeat-audit.md` altında kaydedildi. En yüksek riskli `/panik-atak-aninda-ne-yapmali` sayfasındaki sonuç garantileri ve kendi kendine tıbbi ayırıcı tanı çağrışımları ihtiyatlı dille değiştirildi.
- Panik anı sayfasına görünür yazar, güncelleme tarihi, editoryal sorumluluk, NIMH/NHS kaynakçası, 112/acil servis sınırı ve onaya bağlı CTA ölçümü eklendi; sitemap `lastmod` güncellendi.
- B010, en yüksek güvenlik riski bulunan `/depresyon` ile başlatıldı. Sayfa bazlı iddia envanteri oluşturuldu; WHO ve NIMH kaynakları, görünür yazar ve editoryal sorumluluk, kendine zarar/intihar riski için 112 ve acil servis sınırı, kendi kendine tanı uyarısı, gerçek `dateModified`/sitemap `lastmod` ve iki CTA için onaya bağlı `seans_degerlendirme_cta_click` marker'ı eklendi.
- B010 kapsamında `/anksiyete-nedir` sayfası WHO, NHS ve APA kaynaklarıyla gözden geçirildi. Görünür yazar ve editoryal sorumluluk, kaynakça, kendi kendine tanı ve tıbbi ayırıcı değerlendirme sınırı, 112/acil servis sınırı, gerçek `dateModified`/sitemap `lastmod` ve iki CTA için onaya bağlı `seans_degerlendirme_cta_click` marker'ı eklendi. URL ve canonical korunurken yalnızca-online hizmet modeli görünür hale getirildi.
- B010 kapsamında `/travma` sayfası WHO, NIMH, VA National Center for PTSD ve hakemli dissosiyasyon derlemesiyle gözden geçirildi. Travma ile TSSB ayrımı, süre/sıkıntı/işlev kaybı ve profesyonel değerlendirme sınırı, dissosiyasyonun zorunlu çekirdek belirti olmadığı, güvenlik kapısı olmadan travma maruziyeti uygulanmaması ve 112/acil servis sınırı görünür hale getirildi. Article `citation`, gerçek `dateModified`, sitemap `lastmod`, görünür yazar/editoryal sorumluluk ve iki consent-gated CTA marker'ı birlikte güncellendi; URL ve canonical korundu.
- B010 `/sosyal-kaygi` ile tamamlandı. Sayfa NHS, NICE CG159 ve hakemli bilişsel model derlemesiyle gözden geçirildi; belirti ve tanı sınırı, kaçınma, güvenlik davranışları, öz-odaklı dikkat ve olay sonrası değerlendirme iddiaları kaynaklandırıldı. Güvenlik değerlendirmesi olmadan exposure talimatı verilmemesi, tıbbi/psikiyatrik ayırıcı değerlendirme sınırı ve 112/acil servis sınırı görünür hale getirildi. Article `citation` ve `speakable`, gerçek `dateModified`, sitemap `lastmod`, görünür yazar/editoryal sorumluluk, kaynakça ve iki consent-gated CTA marker'ı birlikte güncellendi; URL ve canonical korundu.
