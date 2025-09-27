class Vehiclе:
    def move(self):
        return "Vehicle is moving"

class Car(Vehiclе):
    def move(self):
        return "Car is driving"

class Bicyclе(Vehiclе):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicyclе()
print(move(car))
print(move(bike))