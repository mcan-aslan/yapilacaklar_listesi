

yapilacaklar_listesi = []


print("""
(0) Çıkmak İçin
(1) Görevleri Görmek İçin
(2) Görev Eklemek İçin
(3) Görev Silmek İçin
""")


while True:
    soru = int(input("Yapılacak İşlemi Seçin (1-3):"))

    if soru==0:
        print("Çıkılıyor...")
        break

    if soru==1:
        if len(yapilacaklar_listesi)==0:
            print("Henüz Görev Eklenmemiş")
        else:
            for yapilacak in yapilacaklar_listesi:
                print("-", yapilacak)
            

    if soru==2:
        ekle = input("eklemek istediğinizi girin: ")
        yapilacaklar_listesi.append(ekle)

        print("başarı ile eklendi")


    if soru==3:
        sil = input("silmek istediğiniz görev: ")

        yapilacaklar_listesi.remove(sil)
        print("görev silindi")


        