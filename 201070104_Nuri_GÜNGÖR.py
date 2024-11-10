import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri - Sözlük (Dictionary) olarak verilmiş
data = {
    'İsim': ['nuri', 'nazlı', 'esma', 'bekir'],
    'eğitim durumu': [25, 30, 22, 28],
    'Şehir': ['canik', 'atakum', 'ilkadım', 'tekkeköy']
}

# Veriyi DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Grafik penceresini oluştur
fig, ax = plt.subplots(figsize=(5, 2))  # Boyutları ayarlayın (Genişlik, Yükseklik)

# Tablomuzu matplotlib ile çiz
ax.axis('tight')  # Ekseni sıkılaştır (tablonun etrafında boşluk olmasın)
ax.axis('off')    # Ekseni gizle (sadece tabloyu göster)


# DataFrame'i tablo olarak matplotlib'e aktar
ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colColours=['#f1f1f1']*df.shape[1])

# Göster
plt.show()
