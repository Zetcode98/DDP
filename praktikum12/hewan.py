# Definisikan kelas induk 'Animal'
class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

# Definisikan kelas anak 'Rhinoceros' (Badak)
class Rhinoceros(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, 'Rumput', habitat, 'Viviparous') # Badak makan rumput dan berkembang biak viviparous

    def charge(self):
        return f"{self.name} sedang menyerang!"

# Definisikan kelas anak 'Fish' (Ikan)
class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, 'Plankton', habitat, 'Oviparous') # Ikan makan plankton dan berkembang biak oviparous

    def swim(self):
        return f"{self.name} sedang berenang!"

# Definisikan kelas anak 'Snake' (Ular)
class Snake(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, 'Tikus', habitat, 'Oviparous') # Ular makan tikus dan berkembang biak oviparous

    def slither(self):
        return f"{self.name} sedang melata!"

# Contoh penggunaan kelas-kelas yang telah dibuat
badak = Rhinoceros('Badak Jawa', 'Hutan Tropis')
print(badak.charge())  # Output: Badak Jawa sedang menyerang!
print(f"{badak.name} hidup di habitat {badak.habitat} dan makan {badak.food}.")

ikan = Fish('Ikan Koi', 'Kolam')
print(ikan.swim())  # Output: Ikan Koi sedang berenang!
print(f"{ikan.name} hidup di habitat {ikan.habitat} dan makan {ikan.food}.")

ular = Snake('Ular Sanca', 'Sawah')
print(ular.slither())  # Output: Ular Sanca sedang melata!
print(f"{ular.name} hidup di habitat {ular.habitat} dan makan {ular.food}.")
