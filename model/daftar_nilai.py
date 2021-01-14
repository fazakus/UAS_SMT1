data = {}


def tambahdata():
    print("====================================================")
    print("============== Tambah Data Mahasiswa ===============")
    print("====================================================")
    print("Silahkan input data Mahasiswa yang ingin ditambahkan")


def hapus():
    print("==========================================================")
    print("================== Hapus Data Mahasiswa ==================")
    print("==========================================================")
    print("Silahkan masukkan Nama Mahasiswa yang akan dihapus datanya")
    nama = input(" Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("==========================================================")
        print("================= BERHASIL MENGHAPUS DATA ================")
        print("==========================================================")
    else:
        print("Data {0} tidak ada".format(nama))


def ubah():
    print("=================================================")
    print("=========== Edit Data Nilai Mahasiswa ===========")
    print("=================================================")
    print("Silahkan masukkan Nama Mahasiswa yang akan diubah")
    nama = input("Masukan Nama\t\t: ")
    print("===============================")
    if nama in data.keys():
        nim = input("NIM baru\t\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("=================================================")
        print("============ BERHASIL MENGUBAH DATA =============")
        print("=================================================")
    else:
        print("Data nilai {0} tidak ada ".format(nama))


def cari():
    print("=============================================")
    print("========= Cari Data Nilai Mahasiswa =========")
    print("=============================================")
    print("Silahkan input Nama Mahsiswa yang akan dicari")
