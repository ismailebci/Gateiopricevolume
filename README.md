# 📊 Gate.io Hacme Göre Coin Listeleme Uygulaması

Bu Python masaüstü uygulaması, Gate.io API'si üzerinden **USDT ile işlem gören coinleri** çeker ve **günlük hacme göre filtreleyerek** listeler. Kullanıcı, belirli bir hacim aralığında coinleri görüntüleyebilir, sıralayabilir ve sayfa sayfa gezebilir.

---

## 🚀 Özellikler

- 🔄 Gate.io Spot Market API ile canlı veri çekme
- 📈 Günlük hacme göre filtreleme
- 💰 Fiyat, 24 saatlik en yüksek/düşük değerler ve % değişim bilgisi
- 📄 Sayfalama (ileri / geri geçiş)
- 🔍 Sıralama: Coin adı, fiyat, hacim, değişim gibi sütunlara göre

---

## 🛠️ Kurulum

### 1. Bu repoyu klonla:
```bash
git clone https://github.com/ismailebci/Gateiopricevolume.git
cd Gateiopricevolume
```

### 2. Gerekli Python kütüphanelerini yükle:
```bash
pip install -r requirements.txt
```

> Eğer Linux kullanıyorsan ve `tkinter` yoksa:
```bash
sudo apt install python3-tk
```

### 3. API Anahtarlarını Ayarla

içine aşağıdaki şekilde **kendi Gate.io API bilgilerini** gir:

```python
# config.py
API_KEY = "senin_api_key"
API_SECRET = "senin_api_secret"
```

---

## ▶️ Kullanım

```bash
python app.py
```

Uygulama çalıştığında:

- Minimum ve maksimum hacim aralığını gir
- "Ara" butonuna tıkla
- USDT paritesine sahip coinler sıralanır
- İleri/Geri butonlarıyla sayfalar arası geçiş yapabilirsin
- Başlıklara tıklayarak sıralama yapabilirsin (örn: fiyat, hacim)

---

## 📁 Dosya Yapısı

```
gate-volume-app/
├── app.py           # Ana uygulama dosyası
├── config.py        # API anahtar bilgileri 
├── requirements.txt # Gerekli kütüphaneler
└── README.md        # Bu döküman
```

---

## 🔧 Kullanılan Kütüphaneler

- `gate-api`
- `tkinter` (Python GUI modülü)
- `ttk` (gelişmiş arayüz bileşenleri için)

---

## 📌 Gereksinimler

- Python 3.8 veya üzeri
- Gate.io'dan alınmış API anahtarı

---

## 📝 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
