def ambil_dan_sisipkan(a1, a2=1, a3=2):
    kalimat = list(a1)
    return print(a1 + kalimat[a2-1] + kalimat[a3-1])

a = input("Masukkan Kalimat: ")
b = input("Masukkan Index 1: ")
c = input("Masukkan Index 2: ")

ambil_dan_sisipkan(a, int(b), int(c))