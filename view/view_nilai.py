from model.daftar_nilai import data
from model.daftar_nilai import cari


def tampilkan():
    if data.items():
        print("================================== Daftar Nilai ======================================")
        print("======================================================================================")
        print("|  No  |      NAMA     |      NIM      |   TUGAS  |   UTS   |   UAS   | NILAI AKHIR  |")
        print("======================================================================================")
        i: int = 0
        for a in data.items():
            i += 1
            print(
                f"| {i:4} | {a[0]:13s} | {a[1][0]:13} | {a[1][1]:8d} |  {a[1][2]:6d} | {a[1][2]:7d} |    {a[1][4]:6.2f}    | ")
    else:
        print("===================================== Daftar Nilai ===================================")
        print("======================================================================================")
        print("|  No  |      NAMA     |      NIM      |   TUGAS  |   UTS   |   UAS   | NILAI AKHIR  |")
        print("======================================================================================")
        print("|                                    Tidak Ada Data                                  |")
    print("======================================================================================")


def tampilkancari():
    nama = input("Masukan Nama\t: ")
    if nama in data.keys():
        print("============================ Daftar Nilai ========================================")
        print("==================================================================================")
        print("====================| NAMA | (NIM, TUGAS, UTS, UAS, NILAI AKHIR) |================")
        print("==================================================================================")
        print("                    | {0} | {1} | ".format(nama, data[nama]))
        print("==================================================================================")
    else:
        print("Datanya {0} tidak ada ".format(nama))