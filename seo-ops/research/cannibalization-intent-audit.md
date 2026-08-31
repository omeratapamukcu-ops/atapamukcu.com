# B012: Online ve Antalya Sayfaları Cannibalization ve Intent Denetimi

Tarih: 2026-08-31

## 0. Kapsam ve kanıt sınırı

İncelenen canonical URL'ler:

1. `/online-psikolog`
2. `/antalya-psikolog`
3. `/online-terapi-nasil-isler`
4. `/antalya-online-psikolog`

Denetim; HTML title, meta description, H1/H2, canonical, JSON-LD `headline`, `name`, `about`, internal link anchor'ları, repo içi inbound linkler, `query-portfolio.csv` hedefleri ve normalize edilmiş görünür gövde metni üzerinden programatik yapıldı. GSC sorgu ve sayfa verisi mevcut değildir. Bu nedenle Google'ın hangi sorguda hangi URL'yi seçtiği ve gerçek keyword cannibalization doğrulanmış değildir. Buradaki `confirmed` etiketi yalnızca site içi intent veya metadata çakışmasını, `likely` güçlü yapısal riski, `possible` ise ölçüm gerektiren ihtimali ifade eder.

Arama proxy'sinde görülen sonuçlar kişiselleştirilmemiş Google `gl=tr, hl=tr, pws=0` sıralaması değildir ve ilk 3 kanıtı olarak kullanılmamıştır. Yalnızca format öğrenimi sağladı: commercial sonuçlar uzman seçimi, uygunluk ve randevu yolunu; informational sonuçlar teknik gereksinim, mahremiyet, adımlar ve yüz yüze karşılaştırmasını öne çıkarıyor.

## 1. Programatik başlangıç bulguları

| URL | Başlangıç H1 sinyali | Schema tipi | Repo inbound link | Başlangıç ana sorun |
|---|---|---:|---:|---|
| `/online-psikolog` | “Online Psikolog Görüşmesi Nasıl İlerler?” | Article | 6 | Ana commercial sayfa, H1/title ile process informational niyetine kayıyordu. |
| `/antalya-psikolog` | “Antalya Psikolog: Ata Pamukçu ile Psikolojik Destek” | WebPage + Service | 8 | Commercial sahiplik doğruydu; yalnızca-online hizmet gerçeği title/H1/schema adında yeterince ayırt edici değildi. |
| `/online-terapi-nasil-isler` | “Online Terapi (Online Psikolojik Destek) Nasıl İşler?” | Article | 7 | Process informational sahiplik netti; portföyde iki informational long-tail yanlışlıkla commercial URL'ye atanmıştı. |
| `/antalya-online-psikolog` | “Online Psikolojik Destek Süreci” | Article | 7 | Antalya primary entity'si H1/schema headline'da görünmüyor, generic process sayfasıyla rekabet ediyordu. |

Başlangıç normalize gövde token Jaccard benzerlikleri:

- `/online-psikolog` ile `/online-terapi-nasil-isler`: 0,188
- `/online-psikolog` ile `/antalya-psikolog`: 0,198
- `/online-psikolog` ile `/antalya-online-psikolog`: 0,179
- `/antalya-psikolog` ile `/online-terapi-nasil-isler`: 0,222
- `/antalya-psikolog` ile `/antalya-online-psikolog`: 0,232
- `/online-terapi-nasil-isler` ile `/antalya-online-psikolog`: 0,228

Bu oranlar tek başına duplicate content göstermez. Risk, gövde benzerliğinden çok aynı “nasıl işler, kimler için uygun, ilk görüşme” başlıklarının commercial ve informational URL'lerde eşzamanlı primary framing olarak kullanılmasından kaynaklanıyordu.

## 2. Query ownership kararı

| URL | Primary intent | Sahip olduğu sorgu ailesi | Sahip olmaması gereken sorgu ailesi |
|---|---|---|---|
| `/online-psikolog` | Ulusal commercial/transactional | online psikolog, online psikolojik destek, online psikolog fiyatları, online psikolog nasıl seçilir | online terapi nasıl işler, teknik gereksinimler, online terapi güvenli mi |
| `/antalya-psikolog` | Antalya commercial/transactional, yalnızca online hizmet | Antalya psikolog, Antalya online psikolog, Antalya psikolog online | genel süreç rehberi, yüz yüze/harita/ofis intent'i |
| `/online-terapi-nasil-isler` | Ulusal informational process | online terapi nasıl işler, online görüşme nasıl yapılır, online terapi güvenli mi, teknik hazırlık ve mahremiyet | terapist seçimi veya Antalya commercial ana sorguları |
| `/antalya-online-psikolog` | Antalya supporting informational/commercial | Antalya'dan online psikolojik desteğe nasıl başlanır, Antalya'dan online görüşmeye hazırlık | “Antalya psikolog” veya “Antalya online psikolog” ana commercial sahipliği |

## 3. Overlap matrisi

| URL çifti | Durum | Kanıt | Karar |
|---|---|---|---|
| `/online-psikolog` ↔ `/online-terapi-nasil-isler` | `confirmed` site içi intent overlap, Google cannibalization `unconfirmed` | Ana commercial sayfanın eski title/H1'i “nasıl ilerler” diyordu. Portföyde “online psikolog görüşmesi nasıl yapılır” ve “online terapi güvenli mi” commercial URL'ye atanmıştı. | Commercial framing `/online-psikolog` üzerinde; process long-tail'ler `/online-terapi-nasil-isler` üzerinde toplandı. Karşılıklı doğal internal link eklendi. |
| `/antalya-psikolog` ↔ `/antalya-online-psikolog` | `likely` | İki URL de Antalya + online psikolog/destek terimlerini kullanıyor; supporting sayfanın eski title'ı commercial exact-match'ti. | `/antalya-psikolog` ana commercial owner kaldı. Supporting sayfa “Antalya’dan online desteğe başlama” rehberi olarak ayrıştırıldı. |
| `/online-terapi-nasil-isler` ↔ `/antalya-online-psikolog` | `likely` | Başlangıçta iki sayfa da generic process H1/H2, uygunluk ve teknik adımlar taşıyordu; gövde Jaccard 0,228. | Ulusal sayfa genel process ve güvenlik sorularını, Antalya supporting sayfa şehirden katılım ve başlangıç hazırlığını sahipleniyor. |
| `/online-psikolog` ↔ `/antalya-psikolog` | `possible` | Hizmet, sorun alanları ve uygunluk içeriği doğal olarak örtüşüyor; biri ulusal, diğeri Antalya commercial. | Coğrafi scope title/H1/schema'da açıklandı. URL veya canonical değiştirilmedi. |
| `/online-psikolog` ↔ `/antalya-online-psikolog` | `possible` | Her ikisi online hizmeti anlatıyor; biri national service, diğeri Antalya supporting guide. | Supporting sayfadan ulusal ana hizmet sayfasına “Türkiye geneli online psikolog desteği” anchor'ı verildi. |
| `/antalya-psikolog` ↔ `/online-terapi-nasil-isler` | düşük risk | Biri Antalya commercial, diğeri national process informational; gövde ortaklığı hizmetin doğasından geliyor. | Mevcut canonical'lar korundu, URL konsolidasyonu gerekmedi. |

## 4. Uygulanan geri alınabilir paket

- `/online-psikolog`: title, meta description, Open Graph, Twitter, H1, hero lead, ilk H2, Article `headline`, `description` ve `about` commercial/transactional hizmet intent'ine çevrildi.
- `/antalya-psikolog`: title, meta, Open Graph, H1, eyebrow, WebPage adı/açıklaması ve Service adı/türü yalnızca-online Antalya commercial intent'iyle hizalandı.
- `/antalya-online-psikolog`: title, meta, social meta, H1, ilk H2, lead, breadcrumb ve Article `headline/about` “Antalya’dan online desteğe başlama” supporting intent'ine çevrildi; `dateModified` eklendi.
- `/online-terapi-nasil-isler`: içerik üretimi yapılmadı; yalnızca commercial ve Antalya supporting hedeflere giden anchor'lar doğal ve intent-açık hale getirildi.
- `/online-psikolog` ve `/antalya-psikolog` sayfalarından ilgili informational rehberlere bağlamsal linkler eklendi.
- Portföyde iki process query `/online-terapi-nasil-isler` hedefine taşındı ve Antalya supporting long-tail eklendi.
- URL, canonical, redirect, noindex, hreflang, CTA event adı, consent davranışı, YMYL kaynak/yazar/güvenlik blokları değiştirilmedi.

## 5. AEO/GEO ve E-E-A-T etkisi

Schema headline/about ile görünür H1 artık her URL'nin entity ve intent rolünü aynı yönde anlatıyor. Soru-cevap ve process içeriği silinmedi; yalnızca primary ownership ayrıştırıldı. Mevcut yazar, kaynakça, acil yardım sınırı, ücretsiz değerlendirme CTA'sı, consent gate ve `seans_degerlendirme_cta_click` davranışı korunmuştur. Yeni FAQ veya doğrulanmamış klinik iddia üretilmemiştir.

## 6. Ölçüm ve karar kapısı

GSC erişimi sağlandığında 28 günlük ve önceki 28 günlük pencerede şu kırılımlar izlenmeli:

1. Sorgu + page: Google'ın seçtiği URL.
2. Ülke: TUR.
3. Cihaz: öncelikle mobile, ayrıca desktop.
4. Tıklama, gösterim, CTR, ortalama konum.
5. GA4 consent sonrası `seans_degerlendirme_cta_click` ve mümkünse nitelikli başvuru.

Ana karar sorguları:

- `online psikolog` → beklenen owner `/online-psikolog`
- `Antalya online psikolog` → beklenen owner `/antalya-psikolog`
- `online terapi nasıl işler` ve `online terapi güvenli mi` → beklenen owner `/online-terapi-nasil-isler`
- `Antalya'dan online psikolojik desteğe nasıl başlanır` → beklenen owner `/antalya-online-psikolog`

İki ardışık ölçüm penceresinde Google'ın beklenmeyen URL'yi seçmesi, impressions'ın URL'ler arasında dağılması veya aynı sorguda URL değişiminin sürmesi halinde yeniden değerlendirme yapılmalı. Bu kanıt olmadan 301, canonical konsolidasyonu, URL silme veya noindex önerilmez.
