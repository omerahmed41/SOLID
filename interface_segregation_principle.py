'''
Clients should not be forced to implement interfaces they do not use.
'''
# bad
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')


# Apply the Interface Segregation Principle
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flyable):
    def go(self):
        print("Taxiing")
        
    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")