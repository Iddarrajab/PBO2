# Nama   : muhammad iddar rajab
# NIM    : 210511028
# Kelas  : R1
# Matkul : Pemrogaman Berorientasi Objek 2

class Matematika:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c


mat = Matematika()
B = mat.add(5, 3, 4)
print(B)
mut = Matematika()
C = mut.add(7, 3)
print(C)
