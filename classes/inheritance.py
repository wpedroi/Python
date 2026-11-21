# inheritance: Allows classes to inherent attributes and methods from another class
#              like a child inherent from his parent.

class Employees:
    def __init__(self, em_id, em_name, em_salary):
        self.em_id = em_id
        self.em_name = em_name
        self.em_salary = em_salary

    def receive_salary(self):
        print(f"Your salary is {self.em_salary}")


class Teacher(Employees):
    pass


employee1 = Employees(1, "mohammed", 1000.5)
employee2 = Employees(2, "Ali", 2000.6)

print(employee1.em_id)
print(employee1.em_name)
print(employee1.em_salary)

employee1.receive_salary()

teacher = Teacher(3, "shaif", 1000.9)

print(teacher.em_id)
print(teacher.em_name)
print(teacher.em_salary)

teacher.receive_salary()
