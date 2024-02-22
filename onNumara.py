import random
import time

# Bilet sayısı
bilet_sayisi = 10  # İstediğiniz sayıyı buraya yazabilirsiniz.

# Program başlangıcını kaydet
baslangic_zamani = time.time()

# 80 sayı arasından rasgele 22 farklı sayı seçme
selected_numbers = random.sample(range(1, 81), 22)

# Seçilen sayıları küçükten büyüğe sıralama
selected_numbers.sort()

# selected numbers ı yazdır
print(selected_numbers)

def generate_ticket():
    # 10 adet küçükten büyüğe sıralı, birbirinden farklı rasgele 10 sayı seçme
    ticket_numbers = sorted(random.sample(range(1, 81), 10))
    return ticket_numbers

# Fonksiyon: Bilette kaç bilen olduğunu sayıp çıktı verme
def count_matching_numbers(ticket, selected_numbers):
    matching_count = sum(num in selected_numbers for num in ticket)
    return matching_count

# Çıktıyı oluşturma
bilet_sayilari = [0] * 11

# Özel mesaj yazdırma
tebrik_mesaji_yazildi = False
tebrik_mesajlari = []

for i in range(bilet_sayisi):
    bilet = generate_ticket()
    bilen_sayisi = count_matching_numbers(bilet, selected_numbers)
    bilet_sayilari[bilen_sayisi] += 1

    if bilen_sayisi == 10 :
        tebrik_mesajı=f" *** TEBRİKLER BÜYÜK İKRAMİYE KAZANDINIZ !!! *** Bilet Sırası: {i+1}, Bilet Numarası: {bilet}"
        tebrik_mesajlari.append(tebrik_mesajı)
        tebrik_mesaji_yazildi = True  # Özel mesaj yazıldı

# Sonuçları yazdırma
for i, bilet_sayisi in enumerate(bilet_sayilari):
    print(f"{i} bilen bilet sayısı: {bilet_sayisi}")
    
# Özel mesajı yazdırma
if tebrik_mesaji_yazildi:
    for tebrik_mesajı in tebrik_mesajlari:
        print(tebrik_mesajı)

# Program sonlanış zamanını kaydet
bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

# Sonucu yazdır
print(f"Programın çalışma süresi: {gecen_sure} saniye")
