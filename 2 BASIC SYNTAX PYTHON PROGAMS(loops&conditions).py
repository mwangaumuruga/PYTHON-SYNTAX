""" This is the second python basic syntax program and it focuses strictly on loops with conditions by first 
showing the basic syntax then working with them in a program"""
""" there are types types of loops OR [CONDITIONS] in python the FOR ,IF & WHILE STATEMENTS.This conditions
 help us create  repeating loops untill they are fullfilled or ended """
"identation is essential in python it enhances code execution"

# 1- The "FOR" loop 
fruits=["mangoes","oranges","lemons","apples","bananas"]
for fruit in fruits:
    print("they are nutritious")

# 2- The IF loop
#if a conditon is fullfilled the code executed hence code moves to the next base
x=500
y=int(input("enter a number"))
if y>=x:
   print("its worth working for")
elif y<=x:
    print("that so little  cash can not be worked for")
else:
    print("enter a valid number")


#THE WHILE LOOP HELPS IN CONDITIONS THAT MUST BE FULLFILLED and executes untill its broken with break command
num1=input("enter any number to compare...")
num2=input("enter a number to be compared")
while num1==num2:
    print("those numbers are the same")
    break
else:
    print("those numbers are not equal")
