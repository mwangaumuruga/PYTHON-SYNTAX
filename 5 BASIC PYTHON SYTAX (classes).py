"""CLASSES are used to create a series of  functions with objects with the same attributes and Visualize objects as true life items with characteristics and also have a special relation with 
each other or what they generally do"""

#function is the action that can happen
#class blueprint that makes an object
#object collection of information that represents a thing or two
#the first letter is usually uppercase to the convention
#this class shows some examples of animals i.e mammals
#Basic python class
class Tweet:
    pass
#A PROGRAM TO SHOW CLASSES
class student:
     def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
a=student("moses",21,"male")
print(a.name)
print(a.age)
print(a.sex)


#program to show instant object
class Fruits:
    pass
a=Fruits()
b=Fruits()
print(a)
a.message="fruits are sweet and nutritious"
print(a.message)
b.message="this instance class coexists with other hence fruits are healthy"
print(b.message)

#program with initialiser which is part of the double under score method.self refers to particular instant
class Pet:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def method(self):
        print(self.name,self.sound)
        

a=Pet("dog","barks")
a.method()
b=Pet("cat","purrs")
b.method()





#THE CODE ABOVE IS TRYING TO SHOW HOW WE USE PYTHON CLASSES BASICALLY BUT  MUST CORRECT AND KNOW HOW HOW CLASSES WORK


# A CODE TO SHOW THE BASIC WORKING OF A MONEY CALCULATOR
class BankAccount:
    def __init__(self,balance):
         self.balance=1000
        
       
    def deposit(self,amount):
     self.balance+=amount
     return self.balance
    def withdraw(self,amount):
     self.balance-=amount
     return self.balance

a=BankAccount(0)
print(a.deposit(1000000))
