#Single inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"Sound made by {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barked!")

d = Dog("Tommy", "Lebra")
d.make_sound()

a = Animal("dog", "Dog")
a.make_sound()