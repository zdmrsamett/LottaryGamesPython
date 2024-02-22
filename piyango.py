import random

def cekilis_listesi_olustur(basamak=6):
    ilk_basamak = random.randint(0, 6)
    diger_basamaklar = [random.randint(0, 9) for _ in range(basamak - 1)]
    return [ilk_basamak] + diger_basamaklar

def eslesen_rakamlari_goster(cekilis_sonucu, bilet):
    eslesen_adet = sum(1 for i in range(len(bilet)) if cekilis_sonucu[i] == bilet[i])
    return eslesen_adet

# Başamak değerini istediğiniz gibi değiştirebilirsiniz.
basamak = 6
bilet_sayisi = 20

try:
    cekilis_sonucu = cekilis_listesi_olustur(basamak)
    print(f"Çekiliş Sonucu: {cekilis_sonucu}")

    eslesen_sayilari = [0] * (basamak + 1)

    kazanan_bilet_sirasi = []  # Kazanan biletlerin sıralarını takip etmek için liste

    # Bilet oluşturma ve kontrol döngüsü
    for i in range(bilet_sayisi):  # Belirtilen sayıda bilet oluştur
        bilet = cekilis_listesi_olustur(basamak)

        eslesen_adet = eslesen_rakamlari_goster(cekilis_sonucu, bilet)
        eslesen_sayilari[eslesen_adet] += 1

        if eslesen_adet == basamak:
            kazanan_bilet_sirasi.append(i + 1)

    # Eşleşme sayılarını yazdırma
    for i in range(basamak + 1):
        print(f"{i} bilen bilet: {eslesen_sayilari[i]}")

    if eslesen_sayilari[basamak] > 0:
        print(f"**********  TEBRİKLER BÜYÜK İKRAMİYE KAZANDINIZ !!!  **********")
        print("Kazanan biletlerin sıraları:", ', '.join(map(str, kazanan_bilet_sirasi)))

except KeyboardInterrupt:
    print("\nProgram sonlandırıldı.")
