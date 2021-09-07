# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:05:18 2021

@author: prince
"""
#Demonstrate get(), items() , values() and keys()
#get(key[,d])Returns the value of the key. If the key does not exist, returns d.
#items()	Return a new object of the dictionary's items in (key, value) format.
# keys()	Returns a new object of the dictionary's keys.
# values()	Returns a new object of the dictionary's values

#Can a set can hold duplicate Values? Demonstrate
#A Set is a Collection that cannot contain duplicate elements. It models the mathematical set abstraction. 

#Store 3 tuples in another tuple and print it in reverse
tup1=(1,2,3)
tup2=(4,5)
tup3=(6,7)
tupm=(tup1,tup2,tup3)
def Reverse(tuples):
    for i in tuples:
        i=i[::-1]
    new_tup = tuples[::-1]
    return new_tup
Reverse(tuples=tupm)

#Name 5 built-in function on list and tuples both
#len()	
#max()	
#min()
#sum()
#sorted()

#What are some properties of Frozen sets? Demonstrate

# If no parameters are passed to frozenset() function then it returns a empty frozenset type object.  
# Since frozenset object are immutable they are mainly used as key in dictionary or elements of other sets.
#If by mistake we want to change the frozenset object then it throws an error “‘frozenset’ object does not support item assignment“. 

#Slice a List and convert it to a set

# Initialize list
List = [50, 70, 20, 20, 90, 10, 50]
 
# Display list
a=List[1:4]
print(a)
list_to_set=set(a)
list_to_set

#Demonstrate d[1]='w'
# 1st item in list d will be w

#demonstrate built-in fun on Strings
#Function	Description
# chr()	Converts an integer to a character
# ord()	Converts a character to an integer
# len()	Returns the length of a string
# str()	Returns a string representation of an object

#Demonstrate slicing of tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
slice = tuplex[3:5]
slice

#Demonstrate unpacking of a tuple
#In Python, there is a very powerful tuple assignment feature that assigns the right-hand side of values into 
#the left-hand side. In another way, it is called unpacking of a tuple of values into a variable.
# In packing, we put values into a new tuple while in unpacking we extract those values into a single variable.

a = ("Allahabad", 5000, "delhi") 
(college, student, canteen) = a 
 
# print college name
print(college)