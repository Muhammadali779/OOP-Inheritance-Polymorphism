class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return 0


class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.1


class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.2



dev = Developer("Ali", 8000)
mgr = Manager("Vali", 12000)

print(f"{dev.name} bonusi: {dev.calculate_bonus()} so'm")
print(f"{mgr.name} bonusi: {mgr.calculate_bonus()} so'm")
