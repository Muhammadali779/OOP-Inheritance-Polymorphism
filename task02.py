class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h")

class Bike(Vehicle):
    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h")

vehicles = [
    Car("BMW X7", 150),
    Bike("Zokos", 25)
]

for i in vehicles:
    i.move()