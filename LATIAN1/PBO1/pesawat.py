#muhammad iddar rajab
#R1
#210511028
class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")
pesawatA = PesawatTerbang("Garuda Indonesia", "Jakarta - Bali")
pesawatA.info()