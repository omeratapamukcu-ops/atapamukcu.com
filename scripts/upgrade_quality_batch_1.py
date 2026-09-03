#!/usr/bin/env python3
"""Upgrade the first six low-scoring clinical guides without touching active experiments."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODIFIED = "2026-09-03"
MARKER = 'data-quality-wave="2026-09-03-1"'

PAGES = {
    "ozgul-fobi.html": {
        "published": "2026-05-19",
        "marker": '<div class="faq-list article-faq">',
        "citations": [
            "https://www.nhs.uk/mental-health/conditions/phobias/",
            "https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/facing-your-fears/",
        ],
        "html": '''<section data-quality-wave="2026-09-03-1">
          <h2>Korku ile fobi arasındaki fark yalnız yoğunluk değildir</h2>
          <p>Belirli bir nesne ya da durumdan korkmak tek başına özgül fobi anlamına gelmez. Klinik değerlendirmede korkunun sürekliliği, gerçek tehlikeyle orantısı, kişinin yaşamını ne ölçüde düzenlediği ve kaçınmanın işlev kaybına yol açıp açmadığı birlikte ele alınır. Örneğin köpek görünce gerilmek ile köpek görme ihtimali yüzünden yürümeyi, parkları ve ziyaretleri bırakmak aynı şey değildir.</p>
          <p>Bedensel alarm çok güçlü olabilir: çarpıntı, titreme, baş dönmesi, nefesin hızlanması veya kaçma isteği görülebilir. Bu tepkiler “tehlike gerçekten büyük” kanıtı gibi hissedilse de alarmın şiddeti ile dış dünyadaki risk her zaman aynı değildir. Kişiye özel değerlendirme; tıbbi durumları, travma öyküsünü, panik belirtilerini ve korkunun bağlamını ayırt etmeyi gerektirir.</p>
          <h2>Güvenlik davranışını nasıl fark edebilirsiniz?</h2>
          <p>Kaçınma yalnız ortama hiç girmemek değildir. Yanında mutlaka birini götürmek, çıkışa yakın durmak, sürekli nabız kontrol etmek, karşılaşmayı zihinde defalarca prova etmek veya dikkati tamamen dağıtmaya çalışmak da kısa vadeli güvenlik sağlayabilir. İşlevsel soru şudur: “Bu davranış bugün beni korurken yarın aynı durumla baş edebileceğime dair ne öğretiyor?”</p>
          <p>Kademeli üstüne gitme bir cesaret testi değildir. Basamaklar kişinin hedefi, fiziksel güvenliği ve taşıyabileceği zorluk düzeyiyle hazırlanır. Amaç korkuyu zorla sıfırlamak değil; korku varken esnek hareket edebilme kapasitesini artırmaktır. Bayılma riski, tıbbi hassasiyet, travma bağlantısı veya yoğun işlev kaybı varsa kendi başına deneme yerine profesyonel değerlendirme daha güvenlidir.</p>
          <div class="article-sources"><h2>Kaynaklar ve ileri okuma</h2><ul>
            <li><a href="https://www.nhs.uk/mental-health/conditions/phobias/" target="_blank" rel="noopener noreferrer">NHS — Phobias: belirtiler, türler ve destek seçenekleri</a></li>
            <li><a href="https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/facing-your-fears/" target="_blank" rel="noopener noreferrer">NHS Every Mind Matters — Korkularla kademeli yüzleşme çerçevesi</a></li>
          </ul><p>Kaynaklar genel psikoeğitim çerçevesini destekler; kişiye özel değerlendirme yerine geçmez.</p></div>
        </section>''',
    },
    "kisisellestirilmis-terapi.html": {
        "published": "2026-05-20",
        "marker": '<div class="sss"><h2>Sık Sorulan Sorular</h2>',
        "citations": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC6350520",
            "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1002849/full",
            "https://contextualscience.org/processbased_therapy_pbt_competencies",
        ],
        "html": '''<section data-quality-wave="2026-09-03-1">
          <h2>Kişiselleştirme pratikte neyi değiştirir?</h2>
          <p>İki kişi aynı “kaygı” sözcüğünü kullansa bile döngüleri farklı olabilir. Birinde belirsizliği azaltmak için sürekli kontrol etme, diğerinde eleştirilme ihtimalinden kaçınma, bir başkasında bedensel duyumları tehlike diye yorumlama öne çıkabilir. Kişiselleştirme, yöntemleri rastgele karıştırmak değil; değiştirilebilir süreçler hakkında ortak bir hipotez kurmak ve bunu görüşmeler boyunca sınamaktır.</p>
          <p>Bu nedenle ilk formülasyon son karar değildir. Kişinin aktardıkları, günlük örnekler, davranış örüntüleri ve izlenen sonuçlar yeni bilgi sağladıkça harita güncellenir. Bir müdahale yararlı değilse yalnız “yeterince çabalamadınız” denmez; hedeflenen süreç, uygulama biçimi, bağlam ve ölçüm yeniden değerlendirilir.</p>
          <h2>Kişiselleştirme ile kanıta dayalı çalışma çelişir mi?</h2>
          <p>Çelişmek zorunda değildir. Süreç temelli yaklaşım, etkili yöntemlerden vazgeçmek yerine hangi yöntemin hangi değişim sürecini, kim için ve hangi bağlamda hedeflediğini açıklamaya çalışır. Kişinin tercihi ve değerleri önemlidir; fakat güvenlik, mesleki yetkinlik ve mevcut kanıt sınırları korunur.</p>
          <p>İzlem de kişiye göre seçilir. Yalnız belirti şiddeti değil; kaçınmanın azalması, önemli etkinliklere katılım, uyku düzeni, ilişki davranışları veya değer odaklı adımlar gibi işlevsel göstergeler izlenebilir. Toplanan bilgi tanı koyan otomatik bir skor değildir; görüşmedeki ortak kararları besleyen veridir.</p>
          <div class="article-sources"><h2>Kaynaklar ve ileri okuma</h2><ul>
            <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6350520" target="_blank" rel="noopener noreferrer">Hofmann &amp; Hayes (2019) — The Future of Intervention Science: Process-Based Therapy</a></li>
            <li><a href="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1002849/full" target="_blank" rel="noopener noreferrer">Ong, Hayes &amp; Hofmann (2022) — Süreç temelli BDT vaka örneği</a></li>
            <li><a href="https://contextualscience.org/processbased_therapy_pbt_competencies" target="_blank" rel="noopener noreferrer">Association for Contextual Behavioral Science — PBT yetkinlikleri ve kaynakları</a></li>
          </ul></div>
        </section>''',
    },
    "karar-verememe.html": {
        "published": "2026-05-20",
        "marker": '<div class="sss"><h2>Sık Sorulan Sorular</h2>',
        "citations": [
            "https://doi.org/10.1007/s10608-018-9964-z",
            "https://doi.org/10.1111/bjc.12534",
        ],
        "html": '''<section data-quality-wave="2026-09-03-1">
          <h2>Karar sorunu mu, kesinlik arayışı mı?</h2>
          <p>Karar verememe bazen seçeneklerin gerçekten yetersiz olmasından kaynaklanır; bazen de amaç iyi bir karar vermekten “yanlış karar vermeyeceğinden yüzde yüz emin olmaya” kayar. İkinci durumda daha fazla araştırma başlangıçta yararlı görünür, fakat yeni bilgi yeni ihtimaller üreterek kararı daha da geciktirebilir. Sürekli karşılaştırma, başkalarından güvence alma ve karar verildikten sonra tekrar tekrar kontrol etme bu döngünün güvenlik davranışları olabilir.</p>
          <p>Belirsizliğe tahammülsüzlük ile kronik kararsızlık arasında ilişki gösteren çalışmalar vardır; ancak bu, her kararsızlığın bir bozukluk olduğu veya tek bir nedeni bulunduğu anlamına gelmez. Maddi risk, geri döndürülemez sonuçlar, aile baskısı, bilgi eksikliği, dikkat sorunları ve depresif yavaşlama gibi başka etkenler de değerlendirilmelidir.</p>
          <h2>Kararı küçültmek ne demektir?</h2>
          <p>Aceleyle seçim yapmak yerine kararın geri döndürülebilir ve geri döndürülemez parçaları ayrılır. Önce küçük bir deneme, sınırlı süreli seçim veya bilgi toplamak için son tarih belirlenebilir. “Doğru seçenek hangisi?” sorusuna ek olarak “Hangi belirsizliği taşımaya razıyım ve hangi değer doğrultusunda ilerlemek istiyorum?” sorusu kullanılır.</p>
          <p>Basit bir gözlem için üç sütun açabilirsiniz: <strong>karar</strong>, <strong>kesinlik kazanmak için yaptığım davranış</strong>, <strong>bu davranışın kısa ve uzun vadeli sonucu</strong>. Bu kayıt kendi kendine tanı aracı değildir. İş, sağlık, hukuki veya yüksek maddi risk içeren kararlarda ilgili uzmanlık desteği ayrıca gerekir.</p>
          <div class="article-sources"><h2>Kaynaklar ve ileri okuma</h2><ul>
            <li><a href="https://doi.org/10.1007/s10608-018-9964-z" target="_blank" rel="noopener noreferrer">Rosser (2019) — Belirsizliğe tahammülsüzlük üzerine sistematik derleme</a></li>
            <li><a href="https://doi.org/10.1111/bjc.12534" target="_blank" rel="noopener noreferrer">Intolerance of Uncertainty Causally Affects Indecisiveness — British Journal of Clinical Psychology</a></li>
          </ul><p>Bu çalışmalar grup düzeyinde bulgular sunar; tek bir kişinin neden karar veremediğini tek başına açıklamaz.</p></div>
        </section>''',
    },
    "kendini-sabote-etmek.html": {
        "published": "2026-05-20",
        "marker": '<div class="sss"><h2>Sık Sorulan Sorular</h2>',
        "citations": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC6350520",
            "https://contextualscience.org/processbased_therapy_pbt_competencies",
        ],
        "html": '''<section data-quality-wave="2026-09-03-1">
          <h2>“Kendini sabote etme” bir tanı değildir</h2>
          <p>Bu ifade günlük dilde kullanışlı olsa da açıklama gibi davranıp araştırmayı erken bitirebilir. “Neden yine kendimi sabote ettim?” sorusu kişiyi kusurlu bir karakter anlatısına götürebilir. İşlevsel yaklaşım daha somut sorar: Hangi durumda ne hissettim, ne yaptım, davranış o anda neyi azalttı ve daha sonra bana neye mal oldu?</p>
          <p>Örneğin bir başvuru formunu göndermemek dışarıdan hedefe zarar vermek gibi görünür. Davranış o anda reddedilme, yetersiz görünme veya başarılı olursa artacak sorumluluk ihtimalinden uzaklaştırıyorsa kısa vadede anlaşılır bir işlev taşır. Uzun vadede fırsat kaybı ve “yapamıyorum” anlatısını güçlendirebilir. Aynı görünen davranışın işlevi kişiden kişiye değişir.</p>
          <h2>Döngüyü suçlamadan nasıl inceleyebilirsiniz?</h2>
          <p>Tek bir yakın örnek seçin ve beş soruya kısa yanıt verin: Öncesinde ne oldu? Zihnim ve bedenim ne üretti? Tam olarak ne yaptım ya da yapmadım? Hemen ardından ne hafifledi? Bir hafta sonra maliyeti ne oldu? Amaç davranışı haklı çıkarmak değil, değiştirilebilir bağlantıyı görünür kılmaktır.</p>
          <p>Sonraki adım “bir daha asla yapmayacağım” sözü değil, kaçınmayı biraz azaltan ölçülebilir bir davranıştır: dosyayı beş dakika açmak, taslağı tek kişiye göndermek veya başvuru için bir son saat belirlemek gibi. Yoğun çökkünlük, dikkat güçlüğü, travma tepkisi, madde kullanımı ya da güvenlik riski varsa sorun yalnız motivasyon başlığı altında ele alınmamalıdır.</p>
          <div class="article-sources"><h2>Kaynaklar ve ileri okuma</h2><ul>
            <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6350520" target="_blank" rel="noopener noreferrer">Hofmann &amp; Hayes (2019) — Değişim süreçleri ve işlevsel analiz çerçevesi</a></li>
            <li><a href="https://contextualscience.org/processbased_therapy_pbt_competencies" target="_blank" rel="noopener noreferrer">Association for Contextual Behavioral Science — Bireysel süreç ağı ve PBT yetkinlikleri</a></li>
          </ul><p>Kaynaklar “kendini sabote etme”yi ayrı bir tanı olarak tanımlamaz; sayfadaki işlevsel analiz çerçevesinin dayanağını açıklar.</p></div>
        </section>''',
    },
    "travma-belirtileri.html": {
        "published": "2026-05-19",
        "marker": '<section class="faq">\n            <h2>Sık Sorulan Sorular</h2>',
        "citations": [
            "https://www.nice.org.uk/guidance/ng116/chapter/Recommendations",
            "https://www.nice.org.uk/guidance/ng116",
        ],
        "html": '''<section data-quality-wave="2026-09-03-1">
          <h2>Travma sonrası tepki ile TSSB aynı şey değildir</h2>
          <p>Zorlayıcı bir olayın ardından yeniden yaşantılama, kaçınma, irkilme, uyku güçlüğü, öfke, suçluluk veya duygusal uyuşma görülebilir. Bu tepkilerin varlığı tek başına travma sonrası stres bozukluğu tanısı koydurmaz. Süre, şiddet, işlev kaybı, olayın niteliği, kişinin güvenliği ve başka ruhsal ya da tıbbi açıklamalar birlikte değerlendirilir.</p>
          <p>Bazı kişiler ayrıntıları istemeden hatırlar; bazıları olayla ilişkili konuşma, yer, kişi veya bedensel duyumlardan uzaklaşır. Bazılarında ilişkilere yakınlaşma zorlaşır ya da dünya sürekli güvensizmiş gibi hissedilir. Belirtilerin görünümü yaşa, kültüre, tekrar eden travmaya ve olay sonrasında güvenliğin yeniden kurulup kurulmadığına göre değişebilir.</p>
          <h2>Ne zaman profesyonel değerlendirme düşünülmeli?</h2>
          <p>Tepkiler günlük yaşamı belirgin biçimde daraltıyorsa, haftalar geçmesine rağmen azalmıyorsa, işlev kaybı artıyorsa, yoğun kopukluk yaşanıyorsa veya kişi güvenliğini sürdüremiyorsa değerlendirme önemlidir. Aktif şiddet, istismar ya da tehdit sürüyorsa öncelik anıları çalışmak değil, güvenliği ve uygun destek ağını kurmaktır.</p>
          <p>Kendine ya da başkasına zarar verme riski, ağır yönelim bozukluğu veya acil tıbbi durum varsa çevrim içi içerikle yetinilmemeli; Türkiye’de 112 aranmalı ya da en yakın acil servise başvurulmalıdır. İlaçla ilgili başlama, bırakma veya doz kararları hekimle ele alınır.</p>
          <div class="article-sources"><h2>Kaynaklar ve ileri okuma</h2><ul>
            <li><a href="https://www.nice.org.uk/guidance/ng116/chapter/Recommendations" target="_blank" rel="noopener noreferrer">NICE NG116 — TSSB'yi tanıma, değerlendirme ve müdahale önerileri</a></li>
            <li><a href="https://www.nice.org.uk/guidance/ng116" target="_blank" rel="noopener noreferrer">NICE — Post-traumatic stress disorder: overview</a></li>
          </ul><p>Bu sayfa tanı ölçütü yerine genel bir belirti haritası sunar; kişisel değerlendirme yerine geçmez.</p></div>
        </section>''',
    },
    "travma-kacinma.html": {
        "published": "2026-05-19",
        "marker": '<section class="faq">\n            <h2>Sık Sorulan Sorular</h2>',
        "citations": [
            "https://www.nice.org.uk/guidance/ng116/chapter/Recommendations",
            "https://www.nice.org.uk/guidance/ng116",
        ],
        "html": '''<section data-quality-wave="2026-09-03-1">
          <h2>Travmada kaçınmayı azaltmak neden standart bir ödev değildir?</h2>
          <p>Kaçınma, travma sonrasında anlaşılır bir korunma girişimidir. Bazı davranışlar gerçek ve devam eden tehlikeden korur; bunları “kaçınma” diyerek kaldırmak güvenli değildir. Klinik çalışma önce tehdidin sürüp sürmediğini, kişinin yaşam koşullarını, kopukluk tepkilerini, bedensel sağlığı ve destek kaynaklarını değerlendirir.</p>
          <p>Tehlike geçmiş olsa bile alarm sistemi belirli anı, yer, koku, konuşma veya bedensel duyumları tehdit gibi işaretleyebilir. Uzaklaşmak o anda rahatlama sağladığında zihin “kaçmak işe yaradı” sonucunu öğrenebilir. Zamanla tetikleyici ağı büyüyebilir ve kişinin hareket alanı daralabilir. Bu işlevsel açıklama kişiyi suçlamaz; davranışın neden kalıcılaştığını anlamaya yardım eder.</p>
          <h2>Güvenli ilerleme hangi kapılardan geçer?</h2>
          <ul><li>Mevcut şiddet, istismar veya tehdit sona ermiş ve güvenlik planı kurulmuş olmalıdır.</li><li>Hedef, kişinin kendi yaşam amacıyla bağlantılı ve açık rızasına dayanmalıdır.</li><li>Adım küçük, kademeli ve durdurulabilir olmalıdır; “hazır olmadan anlatma” baskısı kurulmaz.</li><li>Yoğun kopukluk, kendine zarar riski, madde etkisi veya tıbbi risk varsa önce uygun değerlendirme yapılır.</li><li>İlerleme yalnız kaygının düşmesiyle değil, işlev ve yaşam alanının geri kazanılmasıyla izlenir.</li></ul>
          <p>NICE kılavuzu travma odaklı müdahalelerin eğitimli uygulayıcılarca, güvenlik planlaması ve uyarılmayı yönetme stratejileriyle sunulmasını; kaçınmayı aşma çalışmasının daha geniş bir tedavi çerçevesi içinde ele alınmasını önerir. Bu nedenle genel bir internet egzersizi, kişiselleştirilmiş travma değerlendirmesinin yerine konmamalıdır.</p>
          <div class="article-sources"><h2>Kaynaklar ve ileri okuma</h2><ul>
            <li><a href="https://www.nice.org.uk/guidance/ng116/chapter/Recommendations" target="_blank" rel="noopener noreferrer">NICE NG116 — Travma odaklı müdahaleler, güvenlik ve kaçınma önerileri</a></li>
            <li><a href="https://www.nice.org.uk/guidance/ng116" target="_blank" rel="noopener noreferrer">NICE — TSSB kılavuzuna genel bakış</a></li>
          </ul></div>
        </section>''',
    },
}


def update_article_schema(text: str, published: str, citations: list[str]) -> str:
    pattern = re.compile(r'<script type="application/ld\+json">([\s\S]*?)</script>')
    for match in pattern.finditer(text):
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if data.get("@type") != "Article":
            continue
        data["datePublished"] = published
        data["dateModified"] = MODIFIED
        data["author"] = {"@id": "https://www.atapamukcu.com/#person"}
        data["reviewedBy"] = {"@id": "https://www.atapamukcu.com/#person"}
        data["citation"] = citations
        block = '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'
        return text[:match.start()] + block + text[match.end():]
    raise RuntimeError("Article schema not found")


def add_visible_meta(text: str, published: str) -> str:
    if MARKER in text:
        return text
    meta = f'<p class="article-meta"><strong>Yazar ve editoryal sorumlu:</strong> <a href="/hakkimda">Psikolog Ata Pamukçu</a> · <strong>İlk yayın:</strong> {published[8:10]}.{published[5:7]}.{published[:4]} · <strong>İçerik ve kaynak güncellemesi:</strong> 03.09.2026 · <a href="/editorial-ilkeler">Editoryal ilkeler</a></p>'
    text, count = re.subn(r'(</h1>)', r'\1' + meta, text, count=1)
    if count != 1:
        raise RuntimeError("H1 not found")
    return text


def main() -> None:
    changed = 0
    for filename, spec in PAGES.items():
        path = ROOT / filename
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        text = add_visible_meta(text, spec["published"])
        if spec["marker"] not in text:
            raise RuntimeError(f"Insertion marker not found: {filename}")
        text = text.replace(spec["marker"], spec["html"] + "\n        " + spec["marker"], 1)
        text = update_article_schema(text, spec["published"], spec["citations"])
        path.write_text(text, encoding="utf-8")
        changed += 1
    print(f"batch1_pages_changed={changed}")


if __name__ == "__main__":
    main()
