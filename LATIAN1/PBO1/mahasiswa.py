#muhammad iddar rajab
#R1
#210511028
class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")
mahasiswaB = Mahasiswa("muhammad iddar rajab", "210511028")
mahasiswaB.info()