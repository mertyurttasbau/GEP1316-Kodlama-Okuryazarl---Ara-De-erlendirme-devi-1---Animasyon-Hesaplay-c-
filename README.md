# Animasyon Proje ve Süre Hesaplayıcı

Bu proje, GEP1316 Kodlama Okuryazarlığı dersi için geliştirdiğim, animasyon projelerinde süre ve kare hızı (FPS) hesaplamayı sağlayan basit bir Python aracıdır.

## Projenin Amacı

Animasyon yaparken (özellikle stop-motion veya geleneksel cel/kağıt animasyonda) planlama aşamasında kaç kare çizilmesi gerektiğini ya da saniye hesabını hızlıca yapmak istedim. Storyboard aşamasında sahne sürelerini ve iş yükünü öngörmek için bu küçük aracı kodladım.

## Özellikler

* **Kullanıcı Girdi Koruması:** Harf veya negatif sayı girildiğinde program çökmez, uyarı vererek tekrar sorar.

* **İş Yükü Analizi:** Toplam kare sayısına göre sahnenin yoğunluğunu (hafif, orta, yoğun) otomatik yorumlar.

* **CSV Raporlama:** Hesaplanan tüm verileri otomatik olarak `animasyon_raporu.csv` dosyasına kaydeder.

* **Döngü ve Menü:** Program kapanmadan birden fazla hesaplama yapmanıza olanak tanır.

## Nasıl Çalıştırılır?

Bilgisayarınızda Python yüklüyse terminal veya komut istemcisini açıp şu komutu yazmanız yeterlidir:

python animasyon_hesaplayici.py
