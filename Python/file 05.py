# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:56:36 2021

@author: prince
"""
#Rewriting Calculator program using method based approach

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
 
#Rewriting Fibonacci Series using method based approach
nterms = int(input("enter the nth number: "))

# first two terms
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count = count + 1
       
#Writing a boolean method and executing in loop to identify Armstrong numbers in an array
 lower = int(input("Enter lower range: ")) 
upper = int(input("Enter upper range: "))
print("The armstrong numbers are: ")    

#Calculates number of digits 
for i in range(lower, upper + 1):
    order = len(str(i))
    #Computes sum of nth power   
    sum_pow = 0

    temp = i
    while temp > 0:
     digit = temp % 10
     sum_pow+=digit ** order
     temp//=10
    # Checks if number is equal to 
    # the sum of nth power of its digits       
    if i == sum_pow:
     print(i)
     
#Changing default search path for modules
import sys
for path in sys.path:
         print(path)