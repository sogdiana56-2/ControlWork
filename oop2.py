class Animаl:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaking"

class Dog(Animаl):
    def speak(self):
        return "Гав"

class Сat(Animаl):
    def speak(self):
        return "Mяу"



dog = Dog("Бади")
cat = Сat("Кити")
print(dog.name, dog.speak())
print(cat.name, cat.speak())