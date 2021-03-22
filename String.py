print("PENDETEKSI SOAL")
#71200569_Unguided01_Soal_01.py
soal = (str(input("Silahkan masukkan nama UG: ")))
nim = soal [0:8]
angkatan = soal [2:4]
angkatan1 = "20"
angkatan2 = angkatan1+angkatan
unguided = soal [17:19]
nomer = soal [26:27]
extensi = soal [-1]
extensi1 = soal [-2]
extensi2 = extensi1 + extensi
print("UG ini dimiliki oleh mahasiswa dengan NIM",nim)
print("UG ini dimiliki oleh mahasiswa angkatan",angkatan2)
print("Ini adalah Unguided ke-",unguided)
print("Soal ini adalah soal ke-",nomer)
extensi3 = print("File ini adalah file",extensi2)
if extensi3 == "py":
    print("Python")
