# Nama   : muhammad iddar rajab
# NIM    : 210511028
# Kelas  : R1
# Matkul : Pemrogaman Berorientasi Objek 2


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog barks")


class Bulldog(Dog):

    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin

    def speak(self):
        print("The bulldog growls")