print("=======BREAKING THE LAW=======")

def main():
    lst = []
    n = int(input("Masukkan mau berapa element yang ada pada tuple: "))
    for i in range(n):
        element = int(input())
        lst.append(element)
    convert = tuple(lst)
    print(convert)
    print(type(convert))
    hapus = str(input("Apakah ada element dalam tuple yang ingin anda hapus? (y/t): "))
    if hapus == 'y':
        remove = int(input("Hapus (1 element saja): "))
        try:
            lst.remove(remove)
            convert = tuple(lst)
            print(convert)
            print(type(convert))
        except:
            print("error")
    else:
        print("Oke.")
main()




