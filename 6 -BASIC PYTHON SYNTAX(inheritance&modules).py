""""INHERITANCE in python is used to pass class atttributes onto another subclass hence it gains all the 
traits that the class had but also essentially if it has its own attributes it overwrites the initial code"""

#  First i create a Class Animals
#  then create a Mammal as a sub class 
#  a dog inherits all the attributes of the animal and the animal
class Animals:
    def __init__(self):
        self.breathing_system="all animals have a respiratory system that uses oxygen"
        self.digestion_system="All animals feed on food digest it to get energy for survival"
        self.locomotive_system="All animals have adapted a way of moving from one place to another"
    """def breathing(self):
        self.breathing_system=
        print(self.breathing_system)
    def digestion (self):
        self.digestion_system=
        print(self.digestion_system)
    def locomotion(self):
        self.locomotive_system="
        print(self.locomotive)"""
class Mammals(Animals):
    def respiratory(self):
        print(f"most mammals have a set of lungs and a nose hence",self.breathing_system) 
    def digest(self):
        print(f"most mammals have a digestive tract with teeth and chemicals hence",self.digestion_system)
    def movement(self):
        print(f"all mammals can move by the use of their four legs hence",self.locomotive_system)
class Dog(Mammals):
    def inherited_attributes(self):
        print("this are the general characteristics of a dog")
        return x
a=Mammals.respiratory(Dog())
b=Mammals.digest(Dog())
c=Mammals.movement(Dog())
print(a,b,c)
d=Dog()
print(f"this are the dogs general attributes",d)

