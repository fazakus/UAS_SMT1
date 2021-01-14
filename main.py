from model.daftar_nilai import ubah, hapus, cari, tambahdata
from view.input_nilai import inputdata
from view.view_nilai import tampilkan, tampilkancari

while True:
    print("")
    print("====================================================")
    print("================== DATA MAHASISWA ==================")
    print("====================================================")
    x = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar \nPilih menu : ")
    if x.lower() == "l":
        tampilkan()
    elif x.lower() == "t":
        tambahdata()
        inputdata()
    elif x.lower() == "u":
        ubah()
    elif x.lower() == "h":
        hapus()
    elif x.lower() == "c":
        cari()
        tampilkancari()
    elif x.lower() == "k":
        print()
        print("=================================")
        print("====== KELUAR DARI PROGRAM ======")
        print("=================================")
        break

    else:
        print()
        print("==================================")
        print("== Pilihan Anda Tidak Tersedia ==")
        print("== Pilihlah Menu Yang Tersedia ==")
        print("==================================")
