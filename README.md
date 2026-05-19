# atapamukcu.com

Kişisel psikoloji websitesi. Squarespace'ten alınıp sade HTML/CSS/JS ile yeniden yazıldı.

## Klasör Yapısı

```
atapamukcu.com/
├── index.html        # Ana sayfa
├── css/
│   └── style.css     # Stiller
├── js/
│   └── script.js     # FAQ accordion + scroll efektleri
└── images/
    ├── hero-photo.jpg
    ├── about-photo.jpg
    ├── tech1.png
    └── tech2.png
```

## Yayına Alma (Vercel ile — en kolay yöntem)

### Adım 1: GitHub'a yükle
```bash
cd ~/atapamukcu.com
git init
git add .
git commit -m "İlk sürüm"
```

(sonra GitHub'da repo oluşturup push et — README'nin altında detay var)

### Adım 2: Vercel'e bağla
1. https://vercel.com adresine git
2. GitHub ile giriş yap
3. "Add New Project" → `atapamukcu.com` reposunu seç
4. "Deploy" butonuna bas (ayar değiştirmene gerek yok)
5. Bitti. Sana bir `atapamukcu.vercel.app` linki verir

### Adım 3: Domain bağla (isteğe bağlı)
- Vercel projenin "Domains" kısmına `atapamukcu.com` ekle
- Squarespace DNS ayarlarına CNAME kaydı ekle (Vercel'in verdiği hedefle)
- SSL sertifikası otomatik gelir

## Özellikler
- Mobil uyumlu (responsive)
- Soft yeşil tema (orijinal Squarespace ile aynı)
- Substack embed
- FAQ accordion
- WhatsApp üzerinden randevu linki
