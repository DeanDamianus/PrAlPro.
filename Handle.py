print("====Text Identifier====")
inp = input("Masukkan lokasi file dan nama file txt contoh: (D:/Coding/Visual Studio Code/video 7/Menu.txt): ")
handle = open(inp,"r")

print("1. Membaca seluruh isi text")
print("2. Menghitung Baris pada file")
print("3. Menghitung Huruf pada file")
print("4. Exit")
menu = int(input("Silahkan pilih: "))
if menu == 1:
    a = handle.readlines()
    print(b)
elif menu == 2:
    count = 0
    for i in handle:
        count = count+1
    print("Baris dari text tersebut ada",count)
elif menu == 3:
    huruf = handle.read()
    huruf1 = print(len(huruf))
elif menu == 4:
    print("Terimakasih sudah menggunakan jasa kami.")