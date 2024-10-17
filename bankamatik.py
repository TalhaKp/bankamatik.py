import random

hesaplar = {"Talha Kx" :{ #ileri düzeltmeler. 1) ek bakiyenin tamamı bakiyeye eklenmesin
    "ad": "Talha Kx",
    "HesapNo": 1234567,
    "şifre": 1234,
    "bakiye": 3000,
    "ekbakiye": 2000},}

def hesapac(ad,şifre, hesapno=None):
    if hesapno is None:
        hesapno = random.randint(1000000, 9999999)
    hesaplar[ad] = {"ad": ad, "HesapNo": hesapno,"şifre":şifre, "bakiye": 0, "ekbakiye": 1000}

def yatır(ad, miktar):
        hesapno = hesaplar[ad]["HesapNo"]
        hesaplar[ad]["bakiye"] += miktar
        print(f"{miktar} TL, hesap numarası {hesapno} olan hesaba yatırıldı.")
        print(f"Güncel bakiye: {hesaplar[ad]['bakiye']}, Ekbakiye: {hesaplar[ad]['ekbakiye']}")

def çek(ad,miktar):
    hesapno= hesaplar[ad]["HesapNo"]
    if miktar <= hesaplar[ad]["bakiye"]:
        hesaplar[ad]["bakiye"]-=miktar
        print(f"{miktar} TL, hesap numarası {hesapno} olan hesaptan çekildi.")
        print(f"Güncel bakiye: {hesaplar[ad]['bakiye']}, Ekbakiye: {hesaplar[ad]['ekbakiye']}\n")
    elif miktar<= hesaplar[ad]["bakiye"]+hesaplar[ad]["ekbakiye"]:
        hesaplar[ad]["bakiye"]+= hesaplar[ad]["ekbakiye"]
        hesaplar[ad]["ekbakiye"]-=hesaplar[ad]["ekbakiye"]
        hesaplar[ad]["bakiye"]-=miktar
        print(f"{miktar} TL, hesap numarası {hesapno} olan hesaptan çekildi.")
        print(f"Güncel bakiye: {hesaplar[ad]['bakiye']}, Ekbakiye: {hesaplar[ad]['ekbakiye']}\n")

def gönder(ad, gönderilenAd, miktar):
    hesaplar[gönderilenAd]["bakiye"]+=miktar
    hesaplar[ad]["bakiye"]-=miktar
    print(f"{hesaplar[gönderilenAd]['HesapNo']} nolu hesaba {miktar} TL, {hesaplar[ad]['HesapNo']} tarafından gönderilmiştir.")
    print(f"Güncel bakiye: {hesaplar[ad]['bakiye']}, Ekbakiye: {hesaplar[ad]['ekbakiye']}\n")

while True:
    print("Merhaba bankamatiğe hoşgeldiniz.\n")
    a = input("Bir banka hesabınız var mı? (e/h): ")
    if a == "h":
        a = input("Hesap açmak ister misiniz? Yeni açılan hesaplara özel 1000TL hoşgeldin ekbakiyesi veriyoruz! (e/h): ")
        if a == "e":
            hesapac(input("Adınız ve soyadınız: "),int(input("4 Haneli bir şifre belirleyin: ")))
            print(f"Hesaplar: {hesaplar}\n")  # Unuturum diye koydum xd
            break
        else:
            print("İyi günler dilerim.\n")
            break
    else:
        break

while True:
    a = input("Devam etmek ister misiniz? (e/h): ")
    if a.lower() == "e":
        ad = input("Adınızı ve soyadınızı giriniz: ")
        hesapno = int(input("Hesap numaranızı giriniz: "))
        şifre = int(input("Şifrenizi giriniz: "))

        if ad in hesaplar and hesaplar[ad]["HesapNo"] == hesapno and hesaplar[ad]["şifre"] == şifre:
            print("Giriş başarılı.\n")
            print("Hesap detayları: \n")
            print(f"Ad: {hesaplar[ad]['ad']}")
            print(f"Hesap No: {hesaplar[ad]['HesapNo']}")
            print(f"Bakiye: {hesaplar[ad]['bakiye']}")
            print(f"Ek Bakiye: {hesaplar[ad]['ekbakiye']}\n")

            while True:
                işlem = input("Hangi işlemi yapmak istersiniz? (Çek, Yatır, Gönder,Çık,Bilgi(hesap_detayları_gösterir)): ")
                if işlem.lower() == "çek":
                    tekrar = 0
                    while True:
                        miktar = float(input("Çekmek istediğiniz para miktarını giriniz: "))
                        a = input(f"Çekmek istediğiniz miktar: {miktar}. Emin misiniz? (e/h): ")
                        if a.lower() in ["e", "evet"] and tekrar < 3:
                            if miktar>hesaplar[ad]["bakiye"]:
                                print("Yetersiz bakiye")
                                if ((hesaplar[ad]["ekbakiye"]) + (hesaplar[ad]["bakiye"]))>=miktar:
                                    b= input("Ekbakiye ile beraber limitiniz yetiyor para çekme işlemine devam edilsin mi?(e/h): ")
                                    print("Bilgilendirme: Ekbakiyenizin tamamı bakiyenize eklenecektir.")
                                    if b.lower()=="e" or b.lower()=="evet":
                                        çek(ad, miktar)
                                        print("Para çekme işlemi başarılı.\n")
                                        break
                                else:
                                    print(f"Çekmek istediğiniz miktar: {miktar} Hesap bakiyesi (ekbakiye+bakiye): {hesaplar[ad]['bakiye']+hesaplar[ad]['ekbakiye']}")
                                    print("Olmayan parayı çekemezsiniz :( \n)")
                                    break
                            else:
                                çek(ad, miktar)
                                print("Para çekme işlemi başarılı.\n")
                                break
                        elif tekrar >= 3:
                            print("Çok fazla yanlış giriş yaptınız. İşlem iptal edildi.\n")
                            break
                        else:
                            print("Lütfen miktarı tekrar giriniz.")
                            tekrar += 1
                elif işlem.lower() == "yatır":
                    tekrar = 0
                    while True:
                        miktar = float(input("Yatırmak istediğiniz para miktarını giriniz: "))
                        a = input(f"Yatırmak istediğiniz miktar: {miktar}. Emin misiniz? (e/h): ")
                        if a.lower() in ["e", "evet"] and tekrar < 3:
                            yatır(ad, miktar)
                            print("Para yatırma işlemi başarılı.\n")
                            break
                        elif tekrar >= 3:
                            print("Çok fazla yanlış giriş yaptınız. İşlem iptal edildi.\n")
                            break
                        else:
                            print("Lütfen miktarı tekrar giriniz.")
                            tekrar += 1


                elif işlem.lower() == "gönder":
                    a=input("Bilgilendirme: Para göndereceğiniz kişinin adı ve hesapnumarasına ihtiyacınız var. Devam etmek istiyor musunuz?(e/h): ")
                    if a.lower()=="e" or a.lower() =="evet":
                        gönderilenAd=input("Para göndereceğiniz kişinin adı ve soyadı: ")
                        gönderilenHN= int(input("Para göndereceğiniz kişinin hesap numarası: "))
                        if gönderilenAd in hesaplar and gönderilenHN == hesaplar[gönderilenAd]["HesapNo"]:
                            tekrar=0
                            while True:
                                miktar=float(input("Göndermek istediğiniz miktar: "))
                                a= input(f"Göndermek istediğiniz miktar {miktar} emin misiniz?(e/h)")
                                if (a.lower()== "e" or a.lower()== "evet") and tekrar < 3:
                                    if hesaplar[ad]["bakiye"]>miktar:
                                        gönder(ad, gönderilenAd, miktar)
                                        print("Gönderme işlemi başlatılıyor \n")
                                        break
                                    elif hesaplar[ad]["bakiye"]+hesaplar[ad]["ekbakiye"]>=miktar:
                                        b= input("Ekbakiye ile beraber limitiniz yetiyor para gönderme işlemine devam edilsin mi?(e/h): ")
                                        print("Bilgilendirme: Ekbakiyenizin tamamı bakiyenize eklenecektir.")
                                        if b.lower()=="e" or b.lower()=="evet":
                                            hesaplar[ad]["bakiye"] += hesaplar[ad]["ekbakiye"]
                                            hesaplar[ad]["ekbakiye"] = 0
                                            gönder(ad, gönderilenAd, miktar)
                                            print("Para gönderme işlemi başlatılıyor.\n")
                                            break
                                elif tekrar >= 3:
                                    print("Çok fazla yanlış giriş yaptınız. İşlem iptal edildi.\n")
                                    break
                                else:
                                    print("Lütfen miktarı tekrar giriniz.")
                                    tekrar += 1
                        else:
                            print("Geçersiz kullanıcı adı veya hesap numarası.")
                elif işlem.lower()=="çık":
                    print("Hoşçakalın...")
                    break
                elif işlem.lower()=="bilgi":
                    print("Hesap detayları: \n")
                    print(f"Ad: {hesaplar[ad]['ad']}")
                    print(f"Hesap No: {hesaplar[ad]['HesapNo']}")
                    print(f"Bakiye: {hesaplar[ad]['bakiye']}")
                    print(f"Ek Bakiye: {hesaplar[ad]['ekbakiye']}\n")
                    break

                else:
                    print("Geçersiz işlem.\n")
        else:
            print("Hesap numarası veya şifre yanlış.\n")
    else:
        print("Bizi tercih ettiğiniz için teşekkürler. İyi günler dilerim.\n")
        break