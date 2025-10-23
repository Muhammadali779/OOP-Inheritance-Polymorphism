class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_delivery_method(self):
        return f"{self.name} dan {self.quantity} ta olib ketildi"

class PhysicalProduct(Product):
    def dowload(self):
        return f"{self.name} dan {self.quantity} yuklandi"

class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name} dan {self.quantity} ta olib kelindi"
    
r = PhysicalProduct("Olma", 23)
r1 = DigitalProduct("Fanta", 25)

print(r.get_delivery_method())
print(r1.get_delivery_method())
print(r.dowload())



 