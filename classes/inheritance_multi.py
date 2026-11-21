class Animal:
    def eat(self):
        print("animal is eating")


class Pray(Animal):
    def flee(self):
        print("Animal Flees")

class Predator(Animal):
    def hunt(self):
        print("Animal Hunts")

class Rabbit(Pray):
    pass
class Lion(Predator):
    pass
class Fish(Pray, Predator):
    pass

rabbit = Rabbit()
lion = Lion()
fish = Fish()

rabbit.flee()
lion.hunt()
fish.flee()
fish.hunt()

