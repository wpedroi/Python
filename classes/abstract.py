from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        print("Go")
    @abstractmethod
    def stop(self):
        print("stop")

class Car(Vehicle):
    pass

car = Car()

car.stop()