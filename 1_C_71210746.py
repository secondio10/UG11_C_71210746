#case1

def nilai(a):
    print("Nilai Tertinggi adalah: ", max(a))
    print("Nilai Terendah adalah: ", min(a))
    rumus = sum(a) / len(a)
    print("Rata-ratanya adalah: ", '{:5.2f}' .format(rumus))
    return sorted(a)

daftar_nilai1 = [10,40,30,53,50]
daftar_nilai2 = [99,78,89,85,46]
daftar_nilai3 = [57,90,76,85,78]
print(nilai(daftar_nilai1))