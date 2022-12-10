"""ERROR HANDLING this is piece of code ensures that all our codes are exited with 0 which is prove
 they were perfectly terminated with the all error considered and ensuring our programs do not crash due to an error of 
 input from the user"""
 #this code handles value errors when user enter input of wrong data type
try:
    age=int(input("enter your age--"))
    salary=20000
    credit_score=(salary/age)/100
    print(credit_score)
except ValueError:
    print("enter a numeric value for your age")
#handles if input is zero and as you know no value is divisible by zero
except ZeroDivisionError:
    print("your age can not be zero!!!!")

j

