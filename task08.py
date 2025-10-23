class BankAccount:
    def __init__(self, owner, balance ):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <=self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi yangi balance {self.balance}")
        else:
            print("Hisobingizda mablag' yetarli emas")
        
    
    def get_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate

    def get_interest(self):
        interest = self.balance * self.interest_rate
        return f"Hisoblangan foiz {interest}"
    
class CheckingAccount(BankAccount):
    pass
        
r = SavingsAccount("Ali", 6000, 0.1)
r1 = CheckingAccount("Vali", 6000)

print(r.get_interest())
print(r1.withdraw(2000))