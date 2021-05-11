print('===SET===')
c = 0
lst = []
lst2 = []
while c == 0:
    print('==========DAFTAR ISI==========')
    print('1. Gabungan')
    print('2. Persamaan')
    print('3. Perbedaan')
    print('4. Exit')
    pil = int(input('silahkan masukkan pilihan anda: '))
    if pil == 1:
        print('====GABUNGAN====')
        kal1 = int(input('Masukkan mau berapa element: '))
        for i in range (kal1):
            element = int(input())
            lst.append(element)
        kal2 = int(input('Masukkan mau berapa element: '))
        for i in range(kal2):
            element = int(input())
            lst2.append(element)
        gabung = set(lst) | set(lst2)
        print('hasil dari gabungan list 1 dan 2 adalah',gabung)
    elif pil ==2:
        print('====PERSAMAAN====')
        kal1 = int(input('Masukkan mau berapa element: '))
        for i in range (kal1):
            element = int(input())
            lst.append(element)
        kal2 = int(input('Masukkan mau berapa element: '))
        for i in range(kal2):
            element = int(input())
            lst2.append(element)
        gabung = set(lst) & set(lst2)
        print('hasil dari persamaan list 1 dan 2 adalah',gabung)
    elif pil == 3:
        print('====PERBEDAAN====')
        kal1 = int(input('Masukkan mau berapa element: '))
        for i in range (kal1):
            element = int(input())
            lst.append(element)
        kal2 = int(input('Masukkan mau berapa element: '))
        for i in range(kal2):
            element = int(input())
            lst2.append(element)
        gabung = set(lst) ^ set(lst2)
        print('hasil dari perbedaan list 1 dan 2 adalah',gabung)
    else:
        print("Terimakasih sudah menggunakan program ini")
        break
        