# P0/P1 Internal Link Otoritesi Denetimi

Tarih: 2026-08-31

## Kapsam ve yöntem

`query-portfolio.csv` içindeki aktif P0/P1 sorguların hedeflediği 11 benzersiz canonical URL, repository kökündeki 82 statik HTML sayfasında programatik olarak tarandı. Her hedef için self-link hariç inbound link, benzersiz kaynak sayfası, anchor çeşitliliği ve `root-relative`, `relative`, `absolute` href biçimi çıkarıldı. Header, footer ve breadcrumb dışındaki gövde linkleri bağlamsal kabul edildi. Bu sınıflandırma kart ve ilgili sayfa bloklarını da kapsar; dolayısıyla sayı, paragraf içi editoryal link sayısıyla birebir aynı değildir.

Canlı sıra veya GSC performans verisi bu denetimin girdisi değildir. Bulgular sıralama artışı kanıtlamaz; yalnızca iç bağlantı yapısını ve uygulanabilir otorite açıklarını gösterir.

## Başlangıç envanteri

| Hedef | Link | Kaynak | Anchor çeşidi | Href biçimi | Durum |
|---|---:|---:|---:|---|---|
| `/online-psikolog` | 26 | 25 | 4 | 9 root-relative, 17 relative | Güçlü, fakat 23 link aynı “Online görüşmeler” anchor'ını kullanıyor |
| `/antalya-psikolog` | 3 | 3 | 3 | 3 root-relative | Zayıf ana ticari hedef |
| `/genel-kaygi` | 21 | 21 | 8 | 4 root-relative, 17 relative | Güçlü |
| `/panik-atak` | 13 | 11 | 7 | 7 root-relative, 6 relative | Güçlü |
| `/okb` | 8 | 7 | 6 | 4 root-relative, 4 relative | Yeterli |
| `/sosyal-kaygi` | 10 | 9 | 4 | 5 root-relative, 5 relative | Güçlü |
| `/travma` | 2 | 2 | 2 | 1 root-relative, 1 relative | Kritik zayıf klinik hedef |
| `/depresyon` | 5 | 5 | 3 | 2 root-relative, 3 relative | Yeterli |
| `/act-nedir` | 11 | 9 | 3 | 11 root-relative | Güçlü, anchor yoğunlaşması var |
| `/pbt-nedir` | 11 | 9 | 4 | 11 root-relative | Güçlü, anchor yoğunlaşması var |
| `/bdt-nedir` | 5 | 5 | 3 | 4 root-relative, 1 relative | Yeterli |

## Bulgular

1. Orphan hedef yoktur. En belirgin açık `/travma` sayfasındadır. Denetim öncesinde yalnızca ana sayfa ve site haritasından link alıyor, konuya yakın `travma-belirtileri`, `tssb` ve `travma-kacinma` sayfalarından link almıyordu.
2. `/antalya-psikolog` üç üst düzey kaynak alıyordu ancak konuyla doğrudan örtüşen `/antalya-online-psikolog` sayfasından link almıyordu. Online-only işletme gerçeği nedeniyle bu ilişki kullanıcı için açıklayıcı ve güvenlidir.
3. `/online-psikolog` link sayısı yüksek olsa da anchor dağılımı tekdüzedir. 26 linkin 23'ü “Online görüşmeler” anchor'ını kullanır. Bugünkü pakette toplu anchor değişikliği yapılmadı; görünür metni sırf çeşitlilik için yeniden yazmak düşük güvenli ve gereksizdir.
4. Relative ve root-relative href biçimleri birlikte kullanılmaktadır. Taranan hedeflerde absolute iç link yoktur ve mevcut iki biçim de statik kök sayfalarda doğru çözülür. Yalnız biçim birliği için toplu değişiklik yapmak kullanıcı değerine kıyasla geniş diff üreteceğinden uygulanmadı. Yeni linklerde root-relative biçim kullanıldı.
5. `/act-nedir` ve `/pbt-nedir` sayıları güçlüdür, ancak “ACT nedir” ve “PBT nedir” anchor'ları yoğunlaşmıştır. Bu turda yaklaşım cluster'ı yeniden yazılmadı.

## Etki, güven, efor önceliği

| Paket | Etki | Güven | Efor | Karar |
|---|---:|---:|---:|---|
| Üç travma alt sayfasından `/travma` ana rehberine bağlamsal link | 5 | 5 | 1 | Uygulandı |
| `/antalya-online-psikolog` içinden `/antalya-psikolog` hizmet çerçevesine link | 5 | 5 | 1 | Uygulandı |
| `/online-psikolog` site geneli anchor çeşitlendirmesi | 2 | 2 | 4 | Ertelendi, toplu görünür metin değişikliği haklı değil |
| Tüm relative href'leri root-relative yapma | 1 | 4 | 4 | Reddedildi, teknik sorun yok ve geniş diff üretir |

## Uygulanan güvenli paket

- `travma-belirtileri.html` içinden `/travma`, anchor: “travma sonrası tepkiler”.
- `tssb.html` içinden `/travma`, anchor: “travma sonrası tepkiler ve TSSB”.
- `travma-kacinma.html` içinden `/travma`, anchor: “travma sonrası tepkiler”.
- `antalya-online-psikolog.html` içinden `/antalya-psikolog`, anchor: “Antalya merkezli online destek”.

Paket sonrası beklenen yapısal sonuç: `/travma` 5 benzersiz kaynağa, `/antalya-psikolog` 4 benzersiz kaynağa çıkar. Bu bir internal linking iyileştirmesidir; GSC ve sıra verisi olmadan performans artışı iddia edilmez.