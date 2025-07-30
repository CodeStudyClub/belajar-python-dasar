banyak = int(input("Masukkan banyak data: "))

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i}")
    input_nama = input("Masukkan nama: ")
    input_umur = int(input("Masukkan umur: "))  
    
    nama.append(input_nama)
    umur.append(input_umur) 
    
for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"Data ke {i} adalah {data_nama} berumur {data_umur} tahun.")