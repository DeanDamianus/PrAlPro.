print("====================MENU====================")
menu = {'Ayam Goreng': 15000 , 'Nasi Goreng': 10000,'Magelangan': 13000,'Mie Goreng':1200,'Mie Rebus':13000,'Tempe':1000,'Tahu':1000}
inp = int(input("Berapa makanan / minuman yang akan ditambah ? : "))
for i in range (inp):
    ganti = str(input("Masukkan makanan / minuman yang ingin ditambah: "))
    harga = int(input("Masukkan harga: "))
    menu.update({ganti:harga})
print(menu)
hapus = str(input("Apakah ada menu yang ingin dihapus? (y/t): "))
if hapus == "y":
    print("Masukkan sesuai nama makanan / minuman!")
    hilang =(str(input("Masukkan makanan / minuman yang ingin dihapus: ")))
    menu.pop(hilang)
    print(menu)
elif hapus == "t":
    print(menu)
