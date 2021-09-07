# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:01:33 2021

@author: prince
"""


27
28
 # Re-write program for calculator application applying switch case functionality in Python
 def addition(num1,num2):
    num1 += num2
    return num1
def subtraction(num1,num2):
    num1 -= num2
    return num1
def mul(num1,num2):
    num1 *= num2
    return num1
def division(num1,num2):
    num1 /= num2
    return num1
switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division,
    }
def swith(operation, num1, num2):
  return switcher.get(operation)(num1, num2)

choice = int(input("Select operation from 1,2,3,4 : "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print (swith(choice, num1, num2))



#building a basic calculator application
def switch():
    a = int(input("Enter num1 : "))
    b = int(input("Enter num2 : "))
    
 
    option = int(input("your option : "))
 
 
    if option == 1:
        result = a+b
        print("\nAddition of a and b  = ",result)
 
    elif option == 2:
        result = a-b
        print("subtraction of a and b = ", result)
 
    elif option == 3:
        result = a*b
        print("multiplication of a and b = ", result)
    
    elif option == 4:
        result = a/b
        print("division of a and b = ", result)
    
    else:
        print("Incorrect option")
 
 
 
switch()

# Demonstrating one line if by writing a program for greatest of 3 numbers
num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
num3 = int(input("enter number3: "))
print(max(num1,num2,num3),"is the greatest")  