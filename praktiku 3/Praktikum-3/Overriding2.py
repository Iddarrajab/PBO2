# Nama   : muhammad iddar rajab
# NIM    : 210511028
# Kelas  : R1
# Matkul : Pemrogaman Berorientasi Objek 2

class Runnable:
    def run(self):
        pass


class Car(Runnable):
    def run(self):
        print("Mobil berjalan.")


class Bike(Runnable):
    def run(self):
        print("Sepeda berjalan.")


class Bus(Runnable):
    def run(self):
        print("Bus berjalan.")


def run_all(objects):
    for obj in objects:
        obj.run()


objects = [Car(), Bike(), Bus()]
run_all(objects)
