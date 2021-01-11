from model.daftar_nilai import tambah, ubah, hapus
from view.input_nilai import tambahnilai
from view.view_nilai import tampilkan

while True:
    print("")
    print("================================")
    print("======== DATA MAHASISWA ========")
    print("================================")
    x = input("(L)ihat (T)ambah (U)bah (H)apus (K)eluar \nPilih menu : ")
    if x.lower() == "l":
        tampilkan()
    elif x.lower() == "t":
        tambah()
        tambahnilai()
    elif x.lower() == "u":
        ubah()
    elif x.lower() == "h":
        hapus()
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
