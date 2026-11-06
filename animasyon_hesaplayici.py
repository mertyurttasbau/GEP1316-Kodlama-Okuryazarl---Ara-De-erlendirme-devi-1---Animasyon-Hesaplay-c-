import csv
import os

def veri_al_sayi(mesaj):
    """Kullanıcıdan geçerli ve pozitif sayısal değer alan fonksiyon (Hata korumalı)."""
    while True:
        try:
            deger = float(input(mesaj))
            if deger <= 0:
                print("Hata: Değer 0'dan büyük olmalıdır. Lütfen tekrar deneyin.")
                continue
            return deger
        except ValueError:
            print("Hata: Geçersiz giriş! Lütfen sayısal bir değer girin.")


def veri_al_metin(mesaj):
    """Boş bırakılamayan metinsel girdi alan fonksiyon."""
    while True:
        deger = input(mesaj).strip()
        if deger == "":
            print("Hata: Bu alan boş bırakılamaz. Lütfen tekrar deneyin.")
            continue
        return deger


def is_yuku_analizi(toplam_kare):
    """Karar yapısı (if/elif/else) kullanarak kare sayısına göre iş yükü belirler."""
    if toplam_kare > 500:
        return "Çok yoğun bir iş yükü! Sahne için bu kadarının gerekli olduğuna emin misin?"
    elif toplam_kare >= 200:
        return "Orta yoğunlukta bir iş, ancak duruma göre dengelenmesi gerekebilir."
    else:
        return "Pratik ve olası. Hızlıca Tamamlanabilir."


def sonucu_dosyaya_kaydet(veri_sozlugu, dosya_adi="animasyon_raporu.csv"):
    """Sonuçları bir CSV dosyasına biçimli olarak kaydeder (Gereksinim 6)."""
    dosya_var_mi = os.path.exists(dosya_adi)
    
    with open(dosya_adi, mode="a", newline="", encoding="utf-8") as dosya:
        alanlar = ["Sahne Adi", "Sure (Saniye)", "FPS", "Toplam Kare", "Analiz Notu"]
        yazici = csv.DictWriter(dosya, fieldnames=alanlar)
        
        if not dosya_var_mi:
            yazici.writeheader()
        
        yazici.writerow(veri_sozlugu)
    print(f"\n[Bilgi] Rapor başarıyla '{dosya_adi}' dosyasına kaydedildi.")


def animasyon_hesapla():
    """Ana program akışını ve menü döngüsünü yöneten fonksiyon."""
    print("=" * 60)
    print("   ANİMASYON PROJE VE SAHNE SÜRESİ HESAPLAYICISI")
    print("=" * 60)
    
    # 1. Girdi: Proje / Sahne Adı (Metin doğrulama)
    sahne_adi = veri_al_metin("Sahne veya Proje Adını Giriniz: ")
    
    # 2. Girdi: Sahne Süresi (Saniye cinsinden)
    saniye = veri_al_sayi("Sahne Süresini Giriniz (Saniye cinsinden, örn: 5): ")
    
    # 3. Girdi: Kare Hızı / FPS (Örn: 12, 24, 30 vb.)
    fps = veri_al_sayi("Hedef Kare Hızını / FPS Seçiniz (Örn: 12, 24, 30): ")
    
    # Hesaplama: Toplam Kare Sayısı (Frame)
    toplam_kare = int(saniye * fps)
    
    # İş Yükü Analizi (Karar Yapısı - if/elif/else)
    analiz_notu = is_yuku_analizi(toplam_kare)
    
    # Veri Saklama (Gereksinim 5: Sözlük / Liste kullanımı)
    sahne_verisi = {
        "Sahne Adi": sahne_adi,
        "Sure (Saniye)": saniye,
        "FPS": fps,
        "Toplam Kare": toplam_kare,
        "Analiz Notu": analiz_notu
    }
    
    # Sonuçların Ekrana Biçimli Yazdırılması
    print("\n" + "-" * 45)
    print("TEKNİK ANALİZ VE İŞ YÜKÜ RAPORU")
    print("-" * 45)
    print(f"Proje Adı   : {sahne_verisi['Sahne Adi']}")
    print(f"Süre        : {sahne_verisi['Sure (Saniye)']} Saniye")
    print(f"Kare Hızı   : {sahne_verisi['FPS']} FPS")
    print(f"Toplam Kare : {sahne_verisi['Toplam Kare']} Frame")
    print(f"Analiz Notu : {sahne_verisi['Analiz Notu']}")
    print("-" * 45)
    
    # Sonucu dosyaya kaydetme fonksiyonu çağrısı
    sonucu_dosyaya_kaydet(sahne_verisi)
    
    # Döngü ve Menü Sistemi (Gereksinim 3)
    while True:
        print("\nİşlem Menüsü:")
        print("1. Yeni bir sahne hesapla")
        print("2. Programı kapat")
        
        secim = input("Seçiminiz (1/2): ").strip()
        
        if secim == "1":
            print("\n" + "="*60 + "\n")
            animasyon_hesapla()
            break
        elif secim == "2":
            print("İyi günler çizer dostum, bileğine kuvvet!")
            break
        else:
            print("Hata: Geçersiz seçim! Lütfen 1 veya 2 girin.")

if __name__ == "__main__":
    animasyon_hesapla()