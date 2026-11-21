# Nested classes = are classes that are defined within another class.
#                  class outer:
#                      class inner

# benefits = It logically allows you to group classes that are related
#            Encapsulates private details that aren't relevant outside the outer class
#            keeps the namespace clean; reducing naming conflicts


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_emp(self):
            return f"{self.name} {self.position}"

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def get_detail(self):
        return [employee.get_emp() for employee in self.employees]


company1 = Company("Apple")
company2 = Company("Samsung")

company1.add_employee("Ahmed", "manager")
company1.add_employee("Ali", "cook")
company1.add_employee("Husain", "Cashier")

for x in company1.get_detail():
    print(x)

