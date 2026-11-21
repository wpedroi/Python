class car:
    country = "Yemen"
    num_cars = 0

    def __init__(self, model, colour, year, for_sale):
        self.model = model
        self.colour = colour
        self.year = year
        self.for_sale = for_sale
        car.num_cars += 1

    def driving(self):
        print(f"You are driving the {self.model}")

    def stopping(self):
        print(f"You are stopping the {self.model}")


car1 = car("Mercedes", "red", "2001", False)
car2 = car("BMW", "yellow", "2013", False)
car3 = car("Toyota", "black", "2015", True)
car4 = car("Hyundai", "red", "2001", False)

car1.driving()
car1.stopping()
print(car.num_cars)