import random

cekilis_min = 1
cekilis_max = 60
kolon_sayisi = 6
bilet_sayisi = 10
kac_tuttu = []

sayac = {i: 0 for i in range(kolon_sayisi + 1)}

def bilet_olustur(kolon_sayisi, bilet_sayisi):
    biletler = []
    for _ in range(bilet_sayisi):
        bilet = sorted(random.sample(range(cekilis_min, cekilis_max + 1), kolon_sayisi))
        biletler.append(bilet)
        print("Bilet:", bilet)
    return biletler

biletler = bilet_olustur(kolon_sayisi, bilet_sayisi)
