import random

cekilis_min = 1
cekilis_max = 60
kolon_sayisi = 6
bilet_sayisi = 10
kac_tuttu = []

sayac = {i: 0 for i in range(kolon_sayisi + 1)}

cekilis_listesi = []

def cekilis():
    cekilis_listesi.extend(random.sample(range(cekilis_min, cekilis_max + 1), kolon_sayisi))
    cekilis_listesi.sort()

cekilis()
print("Çekiliş Listesi:", cekilis_listesi)

def bilet_olustur(kolon_sayisi, bilet_sayisi):
    biletler = []
    for _ in range(bilet_sayisi):
        bilet = sorted(random.sample(range(cekilis_min, cekilis_max + 1), kolon_sayisi))
        biletler.append(bilet)
        # print("Bilet:", bilet)
    return biletler

def kac_eleman_eslesiyor(cekilis_listesi, bilet):
    eslesme_sayisi = len(set(cekilis_listesi) & set(bilet))
    return eslesme_sayisi

def tum_kolonlar_eslesiyor(bilet, kolon_sayisi):
    return len(set(bilet) & set(cekilis_listesi)) == kolon_sayisi

biletler = bilet_olustur(kolon_sayisi, bilet_sayisi)

# Eşleşme sayıları hesapla
tebrik_mesajlari = []
for bilet_no, bilet in enumerate(biletler, start=1):
    eslesme_sayisi = kac_eleman_eslesiyor(cekilis_listesi, bilet)
    sayac[eslesme_sayisi] += 1
    
    if tum_kolonlar_eslesiyor(bilet, kolon_sayisi):
        tebrik_mesajlari.append(f"*** TEBRİKLER BÜYÜK İKRAMİYE KAZANDINIZ !!! *** Bilet No: {bilet_no}, {bilet}")

# Sonuçları yazdır
for eslesme, sayi in sayac.items():
    print(f"{eslesme} eşleşen bilet sayısı: {sayi}")

for tebrik_mesaji in tebrik_mesajlari:
    print(tebrik_mesaji)
