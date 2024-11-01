import matplotlib.pyplot as plt
# Verileri tanımla
x = [1, 2, 3, 4, 5]  # X ekseni verileri
y = [2, 3, 5, 7, 11]  # Y ekseni verileri

# Çizgi grafiğini oluştur
plt.plot(x, y, marker='o')

# Başlık ve etiketler ekle
plt.title('Basit Çizgi Grafiği')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')

# Grafiği göster
plt.grid()  # Izgara ekle
plt.show()