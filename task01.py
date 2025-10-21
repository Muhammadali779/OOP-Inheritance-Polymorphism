class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} aytadi: Vov - Vov !"

class Cat(Animal):
    def speak(self):
        return f"{self.name} aytadi: Miyov-miyov!"

dog = Dog("Rex")
cat = Cat("Mosh")

print(dog.speak())
print(cat.speak())