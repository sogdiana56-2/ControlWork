class Persоn:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            raise ValueError("возраст не может быть отрицательным")
        self.__age = age

    def get_age(self):
        return self.__age


p = Persоn()
p.set_age(25)
print(p.get_age())