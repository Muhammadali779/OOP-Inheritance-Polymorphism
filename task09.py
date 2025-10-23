class Notification:
    def __init__(self, name, name1, messege):
        self.name = name
        self.name1 = name1
        self.messege = messege

    def send(self):
        return f"Hurmatli {self.name} sizga {self.name1} tomonidan yangi {self.messege} bor"
    
class EmailNotification(Notification):
    def send(self):
        return f"Hurmatli {self.name} sizga {self.name1} tomonidan yangi email {self.messege} bor"
    
class SMSNotification(Notification):
    def send(self):
        return f"Hurmatli {self.name} sizga {self.name1} tomonidan yangi sms {self.messege} bor"

r = EmailNotification("Ali", "Vali", "bildirishnoma")
r1 = SMSNotification("Vali", "Ali", "bildirishnoma")

print(r.send())
print(r1.send())