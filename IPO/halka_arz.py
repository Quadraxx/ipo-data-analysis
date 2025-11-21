import pandas as pd
import matplotlib.pyplot as plt

# 1. Veri Setini Yükle
try:
    df = pd.read_csv('ipo-ages.csv')
    print("✅ CSV dosyası okundu.")
    
    # 2. Veri Temizliği (TARİH DÜZELTME)
    # ipo sütunu '19990521' gibi uzun sayıları, '1999' yılına çeviriyoruz
    # (Sayıyı 10000'e bölünce tam yıl kalır)
    df['IPO Year'] = df['ipo'] // 10000
    
    # Founding zaten yıl ise dokunmayalım, ama garanti olsun diye kontrol edelim
    # Eğer founding de uzun tarihse onu da böleriz, şimdilik sadece ismini değiştirelim
    df['Founding Year'] = df['founding']

    # Eksik verileri at
    df = df.dropna(subset=['IPO Year', 'Founding Year'])

    # 3. Yaş Hesaplama (Artık Yıl - Yıl yapıyoruz)
    df['Age'] = df['IPO Year'] - df['Founding Year']
    
    # Hatalı veri (0'dan küçük yaşlar) ve çok aşırı büyük yaşları temizle
    df = df[(df['Age'] >= 0) & (df['Age'] < 200)]

    # Yıllara göre ortalama yaşı hesapla
    avg_age = df.groupby('IPO Year')['Age'].mean()

    # 4. Grafiği Çiz
    plt.figure(figsize=(12, 6))
    plt.plot(avg_age.index, avg_age.values, marker='o', linestyle='-', color='r')
    
    plt.title('Yıllara Göre Şirketlerin Halka Arz Olma Yaşı (1975-2017)')
    plt.xlabel('Yıl')
    plt.ylabel('Ortalama Yaş (Yıl)')
    plt.grid(True)
    
    print("📊 Grafik çiziliyor...")
    plt.show()

except Exception as e:
    print(f"\n❌ HATA OLUŞTU: {e}")