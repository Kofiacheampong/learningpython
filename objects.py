#instance of a class
#attributes what an object is or has
#methods what an object can do


class Car:

  wheels = 4 #class variable

  def __init__(self, make, model, year , color):
   self.make = make #instance variable
   self.model = model
   self.year = year
   self.color = color


  def drive (self):
     print('This',self.model, 'is moving')
     return self

  def stop (self):
    print('This',self.model, 'has stopped')
    return self
  
  def turn_off (self):
    print('This',self.model, 'has stopped')
    return self

## passing objects as arguments

class Bike:

      color = None

def change_color (bike,color):
   bike.color = color

bike1 = Bike()
bike2 = Bike()
bike3 = Bike()

change_color(bike1,'blue')
change_color(bike2,'white')
change_color(bike3,'red')

print(bike1.color)
print(bike2.color)



   
   
