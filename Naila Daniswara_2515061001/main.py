import naila001

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("PENJUMLAHAN MATRIKS")
hasil_tambah = naila001.penjumlahan_matriks(A, B)

for baris in hasil_tambah:
    print(baris)

print("\n PENGURANGAN MATRIKS")
hasil_kurang = naila001.pengurangan_matriks(A, B)

for baris in hasil_kurang:
    print(baris)
