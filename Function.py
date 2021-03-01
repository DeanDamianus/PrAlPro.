print("===KONVERSI NILAI===")

def a (nilaia):
    nilaia = print("A")
    return nilaia
def aMin (nilaiamin):
    nilaiamin = print("A-")
    return nilaiamin
def bplus (nilaibplus):
    nilaibplus = print("B+")
    return bplus
def b (nilaib):
    nilaib = print("B")
    return nilaib
def bMin (nilaibmin):
    nilaibmin = print("B-")
    return nilaibmin
def cPlus (nilaicplus):
    nilaicplus = print("C+")
    return nilaicplus
def c (nilaic):
    nilaic = print("C")
    return nilaic
def cMin (nilaicmin):
    nilaicmin = print("C-")
    return nilaicmin
def d (nilaid):
    nilaid = print("D")
    return nilaid
def e (nilaie):
    nilaie = print("E")

nilai = float(input("Masukkan nilai anda: "))

if nilai >= 85:
    nilaia = a (nilai)
elif nilai >= 80:
    nilaiamin = aMin (nilai)
elif nilai >= 75:
    nilaibplus = bplus (nilai)
elif nilai >= 70:
    nilaib = b (nilai)
elif nilai >= 65:
    nilaibmin = bMin (nilai)
elif nilai >= 60:
    nilaicplus = cPlus (nilai)
elif nilai >= 55:
    nilaic = c (nilai)
elif nilai >= 50:
    nilaicmin = cMin (nilai)
elif nilai >= 40:
    nilaid = d (nilai)
elif nilai >= 0:
    nilaie = e (nilai)
else:
    print("salah input nilai")

