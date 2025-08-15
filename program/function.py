def display_kontak(daftar_kontak):
    if not daftar_kontak:
        print("Tidak ada kontak yang tersedia.")
        return

    print("Daftar Kontak:")
    for i, kontak in enumerate(daftar_kontak, start=1):
        print("=====================================================")
        print(f"No      : {i}")
        print(f"Nama    : {kontak['nama']}")
        print(f"Email   : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")
        print("=====================================================")


def new_kontak():
    nama = input("Masukkan nama kontak: ")
    email = input("Masukkan email kontak: ")
    telepon = input("Masukkan nomor telepon kontak: ")

    return {
        'nama': nama,
        'email': email,
        'telepon': telepon
    }


def hapus_kontak(daftar_kontak):
    if not daftar_kontak:
        print("Tidak ada kontak yang tersedia untuk dihapus.")
        return

    display_kontak(daftar_kontak)
    pilihan = input("Masukkan nomor telepon atau email kontak yang ingin dihapus: ")

    for kontak in daftar_kontak:
        if kontak['telepon'] == pilihan or kontak['email'] == pilihan:
            daftar_kontak.remove(kontak)
            print("Kontak berhasil dihapus.")
            return

    print("Kontak tidak ditemukan.")


def cari_kontak(daftar_kontak):
    if not daftar_kontak:
        print("Tidak ada kontak yang tersedia.")
        return

    keyword = input("Masukkan nomor telepon atau email kontak yang ingin dicari: ")

    for kontak in daftar_kontak:
        if kontak['telepon'] == keyword or kontak['email'] == keyword:
            print("Kontak ditemukan:")
            print("=====================================================")
            print(f"Nama    : {kontak['nama']}")
            print(f"Email   : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
            print("=====================================================")
            return

    print("Kontak tidak ditemukan.")
