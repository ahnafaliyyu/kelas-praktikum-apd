nama= ['celio', "afrizal","shandy","ghazali","farrel","lian","jipa","fajar","dimas","rasyid"]

# matkul=["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]

# semua= nama + matkul

# print= (semua)


# print=type[nama]
# print(nama[3:5])\


# masukkan variabel
# print("sebelum:")
# print(nama)
# print("")
# print("sesudah:")
# nama.insert(2,"afrizal")


# ubah
# nama[4]="fufufafa"
# print(nama)

# hapus
# del nama[2]
# print ("nama")

# hapus
# hapus = nama.pop[2]
# print(nama)
# print(hapus)


# panggil dar- ke-
# print(nama[2:4])

# print(nama[0:8:2])

# data=["lian", "ridho",[1,2["halo", 23, 2.3, True]]]
# print(data[2][2][1])

# perulangan
# print menurun
# for i in nama:
#     print (i)

# print menyamping
# for i in nama:
#     print(i, end='*')

# angka = [[1,2,3][4,5,6][7,8,9]]

# for i in angka:
#     for j in i:
#         print(j)



# TUPLE
#Mendeklarasikan Tuple
# nama = ("rizky", "abdullah", "reza")
# #Mengakses nilai Tuple
# print (nama[1])
# print (nama[2])
# print (nama[3])

#mendeklarasikan tuple
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# #lalu kita unpacking
# absen, prodi, nim, nama = mahasiswa
# #maka ketiga variabel tersebut akan berisi data dari tuple mahasiswa
# #menampilkan variabel
# print(absen)


print(
    """
======================
|   DATA MAHASISWA   |
|   1. TAMBAH DATA
|   2. TAMBAHKAN DATA
|   3. UBAHA DATA
|   4. HAPUS DATA 
|   5. KELUAR      
======================""")
data_mahasiswa=[]
while True:
    pilih = int(input("pilih=:"))
    if pilih==1:
        nama = input("nama:")
        nim = input("nim:")
        kelas = input ("kelas:")
        data_mahasiswa.append([nama, nim, kelas])
    elif pilih==2:
        for i in range(len(data_mahasiswa)):
            