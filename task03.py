class User:
    def __init__(self):
        pass
    
    def access_level(self):
        return "No specific access"

class Admin(User):
    def access_level(self):
        return "Full access — tizimni to`liq boshqarish mumkin"

class Guest(User):
    def access_level(self):
        return "Limited access — faqat ma`lumotni ko`rish mumkin"

admin = Admin()
guest = Guest()

print("Admin:", admin.access_level())
print("Guest:", guest.access_level())
