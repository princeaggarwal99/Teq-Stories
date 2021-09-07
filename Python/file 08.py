# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:45:50 2021

@author: prince
"""
#Write a program to copy from one file to another
with open(r"C:\Users\prince\Desktop\file1.txt") as f1:
    for line in f1:
        print(line)
with open(r"C:\Users\prince\Desktop\file2.txt") as f2:
    for line in f2:
        print(line)
        # BLANK
#NOW copying file 1 to file 2 :
with open(r"C:\Users\prince\Desktop\file1.txt") as f1, open(r"C:\Users\prince\Desktop\file2.txt","a") as f2:
    for line in f1:
        f2.write(line) 

with open(r"C:\Users\prince\Desktop\file2.txt") as f2:
    for line in f2:
        print(line)
        
#Write a program to count the number of times a character appears in the File#
file = open(r"C:\Users\prince\Desktop\filex.txt")
data = file.read()
occur= data.count("is")
print('Number of occurrences of the word :', occur)


# Opening a file in read mode which does not exist
file=open(r"C:\Users\prince\Desktop\filex.txt").read() #IT EXIST'S
file

file=open(r"C:\Users\prince\Desktop\file3.txt").read() #IT does not EXIST'S
file

#Rewrite program for factorial of a number with exception handling
import math  
def fact(n):  
    return(math.factorial(n))  
try:
    num = int(input("Enter a number: "))    
    factorial = 1    
       
    if num == 0:    
       print("The factorial of 0 is 1")    
    else:
        FACT=num * fact(num - 1);    
    print(FACT)
except ZeroDivisionError:
    print("Exception Handler for ZeroDivisionError")
