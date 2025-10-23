class User:
    def __init__(self, course: list):
        self.course = course

    def get_dashboard(self):
        return f"Kurslar: {self.course}"


class Student(User):
    pass
    

class Instructor(User):
    def __init__(self, course: str, price: int):
        self.course = course
        self.price = price

    def get_dashboard(self):
        return f"{self.course} -> {self.price} $"
    

r1 = Student(["Matematika", "Ona Tili", "Fizika"])
r2 = Instructor("Matematika", 200)
    
print(r1.get_dashboard())
print(r2.get_dashboard())