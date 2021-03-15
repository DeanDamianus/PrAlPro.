print("=====Piramida setengah / full=====")
baris = int(input("Silahkan memasukkan baris: "))
symbol = str(input("Masukkan simbol yang diinginkan (1 simbol untuk setengah piramida dan 2 simbol untuk full piramida: "))
jarak = baris - 1
for i in range (0,baris):
    for j in range (0,jarak):
        print(" ",end="")
    for k in range (0,i+1):
        print(symbol,end="")
    jarak = jarak - 1
    print ()
jarak = 1
for i in range (jarak-1,0,-1):
    for j in range (0,jarak):
        print("",end="")
    for k in range (0,i+1):
        print(symbol,end="")
    jarak = jarak - 1
    print()