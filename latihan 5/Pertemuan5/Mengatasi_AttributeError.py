print('muhammad iddar rajab\n210511028\nT121A(R1)\n')

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
manusia = Manusia("tono", 20)
try:
    print(manusia.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")