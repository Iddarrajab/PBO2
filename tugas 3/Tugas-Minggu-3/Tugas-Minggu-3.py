# Nama   : muhammad iddar rajab
# NIM    : 210511028
# Kelas  : R1
# Matkul : Pemrogaman Berorientasi Objek 2

from playsound import playsound


class Animal:
    def __init__(self, sound_file):
        self.sound_file = sound_file

    def make_sound(self):
        playsound(self.sound_file)


class Cat(Animal):
    def __init__(self):
        super().__init__('cat.mp3')


class Dog(Animal):
    def __init__(self):
        super().__init__('dog.mp3')


class Cow(Animal):
    def __init__(self):
        super().__init__('cow.mp3')


class Horse(Animal):
    def __init__(self):
        super().__init__('horse.mp3')


class Sheep(Animal):
    def __init__(self):
        super().__init__('sheep.mp3')


class Pig(Animal):
    def __init__(self):
        super().__init__('pig.mp3')


class Rooster(Animal):
    def __init__(self):
        super().__init__('rooster.mp3')


class Duck(Animal):
    def __init__(self):
        super().__init__('duck.mp3')


class Elephant(Animal):
    def __init__(self):
        super().__init__('elephant.mp3')


class Lion(Animal):
    def __init__(self):
        super().__init__('lion.mp3')


if __name__ == '__main__':
    animals = [Cat(), Dog(), Cow(), Horse(), Sheep(), Pig(),
               Rooster(), Duck(), Elephant(), Lion()]

    for animal in animals:
        animal.make_sound()
