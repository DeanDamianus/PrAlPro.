print("===DADU RANDOM===")

import random

dadu1 = random.randint(1,6)
dadu2 = random.randint(1,6)
dadu3 = random.randint(1,6)

nama = (input("Masukkan nama anda: "))
print("Halo!",nama,"Game ini sangat simpel, cukup dengan melempar dadu 3 kali dengan angka dadu 6 secara berturut - turut maka anda menang")
lempar1 = (input("Apakah anda siap? (ya): "))
if lempar1 == "ya":
    print("dadu anda adalah",dadu1)
    if dadu1 == 6:
        print("Wuihh kerenn ayo 2 kali lagii!")
        lempar2 = (input("sudah siapp?? (ya): "))
        if lempar2 == "ya":
            print("dadu anda adalah",dadu2)
            if dadu2 == 6:
                print("Wihhhh selamatt 1 lagii! kamu pasti bisa",nama,"!")
                lempar3 = (input("Ayooo 1 lagi, sudah siap? (ya): "))
                if lempar3 == "ya":
                    print("dadu anda adalah",dadu3)
                    if dadu3 == 6:
                        print("WIHHH SELAMATT!, Hadiah bisa diambil di rumah saya")
                    else:
                        print("WAHHH SDIKITL LAGIII!")
                else:
                    print("yasudah kesempatan tidak datang lagi")
            else:
                print("yahh kamu pasti bisa",nama,"ayo coba lagi")
        else:
                    print("yasudah kesempatan tidak datang lagi")
    else:
        print("yahhh coba lagi ayoo")
else:
    print("yasudah nanti lagi")