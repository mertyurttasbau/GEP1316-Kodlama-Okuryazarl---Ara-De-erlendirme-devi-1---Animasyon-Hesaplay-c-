# PROMPTLAR.md – YZ ile Çalışma Günlüğü

Bu dosyada, GEP1316 Kodlama Okuryazarlığı ödevim için Python ile ilk defa kod yazarken yapay zekâdan adım adım nasıl destek aldığımı, hatalarla nasıl başa çıktığımı ve kodu kendi kafama yatarak nasıl şekillendirdiğimi anlattım.

### Prompt 1: Temel İskelet ve Girdi Kısımları İçin Fikir Alma

* **Tarih:** 6 Kasım 2026

* **Kullandığım Araç:** Claude / Gemini

* **Prompt’um:**

  > *Selam, animasyon okuyorum ve ödevim için Python' da bir sahne süresi ve FPS hesaplayıcı yapmak istiyorum. Kullanıcıdan sahnesinin adı, süresi ve FPS’ ini almak istiyorum ama bunların sayı olup olmadığını kontrol etmesi lazım, aksi halde çökmemeli. Temel olarak bu yapıyı kurmama yardım eder misin, fonksiyonlar nasıl yazılır?*

* **YZ Yanıtı:** YZ, `while True` döngüsü ve `try-except` bloklarını kullanarak hatalı girişlerde programı çökertmeyen `veri_al_sayi` ve `veri_al_metin` fonksiyonlarının temel mantığını örnek bir kodla gösterdi.

* **Kararım ve Gerekçem:** **Düzenledim.** YZ'nin verdiği ilk örnek biraz karmaşık geldiği için bana en sade, en anlaşılır gelen kısımlarını aldım ve kendi anlayabileceğim şekilde değişken isimlerini düzenledim.

### Prompt 2: CSV Dosyasına Kaydetme ve Hata Ayıklama

* **Tarih:** 6 Kasım 2026

* **Kullandığım Araç:** Claude / Gemini

* **Prompt’um:**

  > *Kullanıcıdan verileri düzgünce alabiliyorum. Şimdi hocanın istediği gibi bu verileri bir sözlükte toplayıp bir CSV dosyasına (.csv) kaydetmem gerekiyor. Bunu nasıl yapabilirim? Kodun dosya kaydetme kısmını yazar mısın?*

* **YZ Yanıtı:** YZ, `csv` ve `os` kütüphanelerini kullanarak `animasyon_raporu.csv` dosyasına verileri ekleyen `sonucu_dosyaya_kaydet` fonksiyonunu yazdı.

* **Kararım ve Gerekçem:** **Düzenledim.** Kodu kendi dosyama ekleyip terminalden çalıştırdığımda `SyntaxError: invalid syntax` hatası aldım. Hata satırına baktığımda YZ'nin değişken adında boşluk bıraktığını fark ettim (`dosya_var mi`). Bunu hemen alt çizgiyle (`dosya_var_mi`) değiştirerek hatayı kendim çözdüm ve çalıştırdım.

### Prompt 3: İş Yükü Analizi ve Veda Mesajının Özelleştirilmesi

* **Tarih:** 6 Kasım 2026

* **Kullandığım Araç:** Claude / Gemini

* **Prompt’um:**

  > *Süper, şu an hesaplama yapıp dosyaya kaydediyor. Programın içine if/elif/else koyarak kare sayısına göre iş yükü yorumu yapmak istiyorum. Metinleri kendi sektörüme göre değiştirdim ama kodun mantığında bir yanlışlık var mı bakar mısın? Çıkış yazınca da kendi istediğim veda mesajını yazdırsın.*

* **YZ Yanıtı:** YZ, `is_yuku_analizi` fonksiyonundaki sınırları (`> 500`, `>= 200` vb.) kontrol edip onayladı ve menüdeki çıkış (`2`) seçeneğine istediğim veda mesajını eklemem için küçük bir kod bloğu önerdi.

* **Kararım ve Gerekçem:** **Kabul Ettim.** Yazdığım mantık doğru çıktı, sadece metinleri animasyon stüdyosu ortamına uygun hale getirdiğim için bu haliyle projeye dahil ettim.

### Süreçte Yaşadığım Zorluklar ve Çözümlerim

Bu ödevi yaparken en çok zorlandığım kısım, YZ'nin tek seferde kusursuz bir kod vermediğini, küçük yazım hatalarını benim yakalayıp düzeltmem gerektiğimi fark etmek oldu. Özellikle dosya kontrolü yaparken `dosya_var mi` şeklinde bıraktığı boşluk yüzünden terminalde hata aldığımda başta ne olduğunu anlamadım. Ama hata mesajını inceleyip Python'da değişken adlarında boşluk olamayacağını hatırlayınca `dosya_var_mi` yaparak sorunu çözdüm. Bu deneyim bana, YZ'yi bir "yardımcı geliştirici" olarak kullanmanın ve çıkan kodu mutlaka test edip okumanın ne kadar önemli olduğunu öğretti.