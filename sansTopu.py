import random
import time

biletSayisi = 1000

def cekilis_yap():
    cekilis_listesi = sorted(random.sample(range(1, 61), 5)) + [random.randint(1, 14)]
    return cekilis_listesi

def bilet_olustur():
    bilet = cekilis_yap()
    return bilet

def eslesme_sayisi(bilet, cekilis_listesi):
    eslesme_sayisi = sum(1 for num in set(bilet[:5]) & set(cekilis_listesi[:5]) if num in cekilis_listesi[:5])
    return eslesme_sayisi

def tebrik_mesaji():
    print("\n*** TEBRİKLER BÜYÜK İKRAMİYEYİ KAZANDINIZ !!! ***")
    print("Büyük İkramiyeyi Kazanan Biletin Sırası:")

def takip_et_ve_sonucu_yazdir(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nProgramın Çalışma Süresi: {:.5f} saniye".format(elapsed_time))

def main():
    start_time = time.time()
    cekilis_listesi = cekilis_yap()

    print("cekilis_listesi:", cekilis_listesi)

    biletler = [bilet_olustur() for _ in range(biletSayisi)]
    # print("Oluşturulan biletler:")
    # for bilet in biletler:
    #     print(bilet)

    eslesme_sayilari = [0, 0, 0, 0, 0, 0]

    for bilet in biletler:
        if bilet[5] != cekilis_listesi[5]:
            eslesme = eslesme_sayisi(bilet, cekilis_listesi)
            eslesme_sayilari[eslesme] += 1

    print("\n Biletlerde tutturulan kolon sayıları:")
    print("0 eşleşen bilet sayısı:", eslesme_sayilari[0])
    print("1 eşleşen bilet sayısı:", eslesme_sayilari[1])
    print("2 eşleşen bilet sayısı:", eslesme_sayilari[2])
    print("3 eşleşen bilet sayısı:", eslesme_sayilari[3])
    print("4 eşleşen bilet sayısı:", eslesme_sayilari[4])
    print("5 eşleşen bilet sayısı:", eslesme_sayilari[5])

    eslesme_6_sayisi = [0, 0, 0, 0, 0, 0]

    for bilet in biletler:
        if bilet[5] == cekilis_listesi[5]:
            eslesme_6 = eslesme_sayisi(bilet[:5], cekilis_listesi[:5])
            eslesme_6_sayisi[eslesme_6] += 1

    # print("\n Biletlerde tutturulan kolon sayıları:")
    print("0+1 eşleşen bilet sayısı:", eslesme_6_sayisi[0])
    print("1+1 eşleşen bilet sayısı:", eslesme_6_sayisi[1])
    print("2+1 eşleşen bilet sayısı:", eslesme_6_sayisi[2])
    print("3+1 eşleşen bilet sayısı:", eslesme_6_sayisi[3])
    print("4+1 eşleşen bilet sayısı:", eslesme_6_sayisi[4])
    print("5+1 eşleşen bilet sayısı:", eslesme_6_sayisi[5])


    if eslesme_6_sayisi[5] > 0:
        tebrik_mesaji(eslesme_6_sayisi[5])

    takip_et_ve_sonucu_yazdir(start_time)


if __name__ == "__main__":
    main()
