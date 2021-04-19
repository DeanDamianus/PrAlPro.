print("======LIST BELANJA======")
belanja = []
a = True
while a == True:
    item = input("Masukkan barang yang ingin dibelanjakan: ")
    belanja.append(item)
    print("Belanjaan anda: ")
    for item in belanja:
        print("-",item)
    tambah = input("Apakah mau menambah lagi? (y/t): ")
    if tambah == "t":
        a = False
print("====BELANJAAN ANDA==== ")
for item in belanja:
    print(item)
print("-----------------------")