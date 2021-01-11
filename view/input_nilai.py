from model.daftar_nilai import data


def tambahnilai(nama=" "):
    print("Input Nilai")
    tugas = int(input("NIlai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = tugas, uts, uas, nilaiakhir
