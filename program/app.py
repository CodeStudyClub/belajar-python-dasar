import function

# List of dictionary
daftar_kontak = [
    {
        'nama': 'Alief Chandra Darmawan',
        'email': 'chandra13july@gmail.com',
        'telepon': '081331442778'
    }
]

# Menu program
while True:
    print("\nMenu:")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak_baru = function.new_kontak()
        daftar_kontak.append(kontak_baru)
        print("Kontak berhasil ditambahkan.")
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak valid.")

print("Program selesai berjalan, sampai jumpa!")
