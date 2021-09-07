# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:15:50 2021

@author: prince
"""

# Checking if a given number is an Armstrong number
#A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
number = int(input("Enter any Number: "))  
sum = 0  
temp = number 
  
while temp > 0:  
   digit = temp % 10  
   sum = sum+digit ** 3  
   temp //= 10  
  
if number == sum:  
   print(number,"is an Armstrong number")  
else:  
   print(number,"is not an Armstrong number")  

# Identifying Armstrong numbers within a given range
   
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
     
     
#Calculation and printing Fibonacci Series till nth term
#The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. 
     
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