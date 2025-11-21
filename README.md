# ABD Şirketleri Halka Arz (IPO) Yaş Analizi (1975-2017) 📈

Bu proje, 1975 ile 2017 yılları arasında ABD borsalarında halka arz (IPO) olan şirketlerin verilerini analiz eden bir veri görselleştirme çalışmasıdır.

## 🎯 Projenin Amacı
Şirketlerin kuruluş tarihleri ile halka arz tarihleri arasındaki farkı (yani şirket yaşını) hesaplayarak, ekonominin farklı dönemlerindeki yatırımcı davranışlarını ve piyasa trendlerini incelemektir.

## 📊 Analiz Sonuçları ve Görselleştirme

Aşağıdaki grafik, Python kullanılarak elde edilmiştir:

![IPO Yaş Grafiği](https://github.com/Quadraxx/ipo-data-analysis/blob/main/IPO/IPOgrapics.png)

### 🔍 Grafikten Çıkarılan Önemli Bulgular:
* **Dot-com Balonu (1999-2000):** Grafikteki **çukur noktasına** dikkat edin. Bu yıllarda şirketlerin halka arz olma yaşı ortalama **10 yılın altına** düşmüştür. Bu, teknoloji çılgınlığı sırasında kurulan şirketlerin henüz "bebekken" borsaya girdiğini kanıtlar.
* **2008 Krizi Sonrası:** 2008 ekonomik krizinden sonra risk algısı değişmiş ve sadece daha yaşlı, oturmuş şirketler halka arz olabilmiştir (Ortalama yaş 20-25'e yükselmiştir).

## 🛠️ Kullanılan Teknolojiler
Bu projede **Python** programlama dili ve aşağıdaki kütüphaneler kullanılmıştır:

* **Pandas:** Veri temizleme, tarih formatı düzeltme ve yaş hesaplamaları için.
* **Matplotlib:** Veriyi çizgi grafiği (Line Chart) olarak görselleştirmek için.

## 🚀 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için:

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/ipo-data-analysis.git](https://github.com/KULLANICI_ADIN/ipo-data-analysis.git)
    ```
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pandas matplotlib
    ```
3.  Analiz kodunu çalıştırın:
    ```bash
    python halka_arz.py
    ```

## 📂 Veri Seti Kaynağı
Bu analizde kullanılan veri seti **Jay R. Ritter (University of Florida)** tarafından sağlanan "Founding dates for firms going public in the U.S. during 1975-2017" çalışmasından alınmıştır.

---
*Geliştirici: Hüseyin Akın*
