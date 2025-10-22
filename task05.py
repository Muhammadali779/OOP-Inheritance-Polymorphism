class Appliance:
    def __init__(self):
        pass

    def turn_on(self):
        print("✅Yoqildi")
    
    def turn_off(self):
        print("❌ O`chirildi")


class TV(Appliance):
    def turn_on(self):
        print("✅ TV Yoqildi")

    def turn_off(self):
        print("❌ TV O`chirildi")

class Fridge(Appliance):
    def turn_on(self):
        print("✅ Fridge Yoqildi")

    def turn_off(self):
        print("❌ Fridge O`chirildi")

classes = [TV(), Fridge()]

for item in classes:
    item.turn_on()
    item.turn_off()
    print("-------")