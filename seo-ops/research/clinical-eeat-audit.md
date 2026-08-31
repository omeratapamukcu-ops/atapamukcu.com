# Klinik Cornerstone E‑E‑A‑T Denetimi

Tarih: 2026-08-31

## Kapsam

25 sorguluk portföydeki benzersiz hedef sayfalar görünür kaynakça, görünür yazar/editoryal sorumluluk ve `dateModified` sinyalleri açısından tarandı. Ana sayfa ve ticari/yolculuk sayfaları klinik kaynakça gereksiniminde içerik rehberlerinden ayrı değerlendirildi.

## Güçlü durumda olan rehberler

- `/online-psikolog`
- `/genel-kaygi`
- `/panik-atak`
- `/okb`
- `/act-nedir`
- `/pbt-nedir`
- `/bdt-nedir`
- `/kaygi-dongusu`

Bu sayfalarda görünür kaynakça ile yazar/editoryal sorumluluk sinyali bulunuyor.

## Kaynak veya güncellik boşluğu bulunan klinik sayfalar

| Sayfa | Görünür kaynakça | Görünür yazar/editoryal sorumluluk | `dateModified` | Öncelik |
|---|---:|---:|---:|---|
| `/panik-atak-aninda-ne-yapmali` | Başlangıçta yoktu; giderildi | Başlangıçta yoktu; giderildi | Başlangıçta yoktu; giderildi | P0 tamamlandı |
| `/anksiyete-nedir` | Yok | Yok | Yok | P1 |
| `/depresyon` | Yok | Yok | Yok | P1 |
| `/travma` | Yok | Var | Yok | P1 |
| `/sosyal-kaygi` | Yok | Var | Yok | P1 |

## En yüksek riskli bulgu ve uygulama

`/panik-atak-aninda-ne-yapmali`, akut sağlık kaygısıyla okunabilecek bir sayfa olmasına rağmen “atağın hızlı geçmesini sağlar”, “en etkili şey”, “gerçek değildir”, kesin süre ve sonuç garantisi içeren ifadeler barındırıyordu. Ayrıca yeni veya farklı göğüs ağrısını panik olarak yorumlama riskini yeterince sınırlandırmıyordu.

Uygulanan düzeltmeler:

- Yeni, alışılmadık veya şiddetli belirtiler için 112/acil servis sınırı görünür hale getirildi.
- Kesin sonuç vaatleri ve kendi kendine tıbbi ayırıcı tanı çağrışımı kaldırıldı.
- Topraklama ve nefes önerileri seçenek ve kişisel farklılık diliyle sınırlandı.
- Görünür yazar, güncelleme tarihi, editoryal sorumluluk ve kaynakça eklendi.
- NIMH ve NHS kurumsal kaynakları kullanıldı.
- CTA, onaya bağlı `seans_degerlendirme_cta_click` ölçümüne bağlandı.

## Sıradaki güvenli sıra

1. `/anksiyete-nedir`
2. `/depresyon`
3. `/travma`
4. `/sosyal-kaygi`

Her sayfada önce iddia envanteri çıkarılmalı; ardından kaynak, yazar, tarih ve güvenlik sınırı aynı değişiklik paketinde ele alınmalıdır. Kaynak eklemeden yalnızca tarih güncellenmemelidir.
