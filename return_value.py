def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total += angka
    return (list_angka, total)

list_angka, total = jumlahkan(1, 2, 3, 4, 5)

print(f"Total {list_angka} = {total}")
