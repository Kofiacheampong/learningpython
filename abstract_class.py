#Template class, prevents the user from creating an object of that class, more like a ghost class, has a declaration but no implementation, compels a user to override abstract methods in parent class

from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def go (self):
    pass

class Motorcycle(Vehicle):
  def go(self):
    print ('Vroooom!!')

motorcycle = Motorcycle()

motorcycle.go()