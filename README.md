# 📊 Gate.io Hacme Göre Coin Listeleme Uygulaması

Bu Python masaüstü uygulaması, Gate.io API'si üzerinden **USDT ile işlem gören coinleri** çeker ve **günlük hacme göre filtreleyerek** listeler. Kullanıcı, belirli bir hacim aralığında coinleri görüntüleyebilir, sıralayabilir ve sayfa sayfa gezebilir.

## 🚀 Özellikler

- Gate.io Spot Market API ile veri çekme
- Günlük hacme göre filtreleme
- Fiyat, 24s en yüksek/düşük ve % değişim bilgisi
- Sayfalama (ileri / geri gezebilme)
- Sütunlara göre sıralama (isim, fiyat, hacim, değişim)
- Tkinter arayüzüyle kolay kullanım

---

## 🛠️ Kurulum Adımları

### 1. Bu repoyu klonla:
```bash
git clone https://github.com/ismailebci/Gateiopricevolume
cd gate-volume-app
2. Gerekli Python kütüphanelerini yükle:
bash
Kopyala
Düzenle
pip install -r requirements.txt
Eğer Linux kullanıyorsan, tkinter kurulu değilse şu komutu çalıştır:

bash
Kopyala
Düzenle
sudo apt install python3-tk
3. API Anahtarlarını Ayarla
Proje klasöründe yer alan config.py dosyasını aç ve kendi Gate.io API bilgilerini gir:

python
Kopyala
Düzenle
# config.py
API_KEY = "senin_api_key"
API_SECRET = "senin_api_secret"
🔒 Bu dosya .gitignore içinde olmalı, böylece GitHub'a yüklenmez ve gizli kalır.

▶️ Uygulamayı Başlat
bash
Kopyala
Düzenle
python app.py
Uygulama açıldıktan sonra:

Minimum ve maksimum hacim aralığını gir.

"Ara" butonuna bas.

USDT paritesine sahip coinler listelenir.

Coinleri sıralayabilir, sayfalar arasında geçiş yapabilirsin.
