# Nama   : muhammad iddar rajab
# NIM    : 210511028
# Kelas  : R1
# Matkul : Pemrogaman Berorientasi Objek 2


class Kendaraan:

    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna

    def berkendara(self):
        print("Kendaraan ini sedang berjalan.")


class SepedaMotor(Kendaraan):

    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc

    def belok(self):
        print("Sepeda motor ini sedang belok.")


motorA = SepedaMotor("Sepeda Motor", "Honda", "Merah", 150)
motorA.berkendara()  # Output: Kendaraan ini sedang berjalan.
motorA.belok()  # Output: Sepeda motor ini sedang belok.
