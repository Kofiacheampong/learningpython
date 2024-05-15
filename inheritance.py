# class Animal:
#   alive = True

#   def eat (self):
#     print('This animal is eating')
#   def sleep(self):
#     print ('this animal is sleeping')
  
# class Rabbit (Animal):
#   pass
# class Fish (Animal):
#   pass
# class Hawk (Animal):
#   pass

# rabbit = Rabbit()

# print(rabbit.alive)

class Prey:
  def flee (self):
    print ('this nigga running')
class Predator:
  def hunt (self):
    print ('this nigga hunting')

class Fish(Prey,Predator):
  pass
class Rabbit(Prey):
  pass

fish= Fish()
rabbit= Rabbit()

fish.flee()
fish.hunt()
rabbit.flee()
  