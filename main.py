print("TUGAS UTS")
print("Nama   : Nanda Eka Rostania")
print("NIM    : 04119020")
print("Prodi  : Sistem Komputer")
print("Semester : 4")
print("--------------------------")
print("masukkan kalimat anda :")
kalimat = input()
print(kalimat.split())
for kata in kalimat.split():
  print(kata)
print("Terdeksi Ada {} kata".format(len(kalimat.split())))
print("--------------------------")