menu = (input("silahkan pilih bentuk 2D yang ingin dihitung luasnya (1)Persegi (2)Persegi Panjang (3)Segitiga (4)Lingkaran: "))

if menu == "1" or menu == "persegi":
    sp = (float(input("Masukkan sisi persegi : ")))
    hasil = round( sp * sp)
    print("Hasil dari luas persegi adalah",hasil)
elif menu == "2" or menu == "persegi panjang":
    ppp = (float(input("Masukkan panjang dari persegi panjang: ")))
    lpp = (float(input("Masukkan lebar persegi panjang: ")))
    hasil2 = round (ppp * lpp)
    print("Hasil dari luas persegi panjang adalah",hasil2)
elif menu == "3" or menu == "segitiga":
    a = (float(input("Masukkan alas segitiga: ")))
    ts = (float(input("Masukkan tinggi segitiga: ")))
    hasil3 = round (1/2 * a * ts)
    print("Hasil dari luas segitiga adalah",hasil3)
elif menu == "4" or menu == "lingkaran":
    r = (float(input("Masukkan ruas lingkaran: ")))
    hasil4 = round (3.14 * r * r)
    print("Hasil dari luas lingkaran adalah",hasil4)
else:
    print("Input yang anda masukkan salah, silahkan pilih salah satu dari bentuk diatas")
