# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:44:47 2021

@author: prince
"""

# How Interpreter execute programs ?
# The Interpreters translates one statement into machine language, executes it, and proceeds to next statement.

#Creating a hello world script to check interpretation
print("hello world")

# Assigning a value to a variable
# let x and y be the variable
x=45
x
y="hello"
y

#An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another
#Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _
#example :
x_y=90
x_y
#but,
x@y=40
x@y
# not valid

#Differentiating between a keyword and Identifier
#keyword= They help to identify a specific property that exists within a computer language.
 # example= int, char, if, while, do, class etc.

#identifier = They help to locate the name of the entity that gets defined along with a keyword.
  # example =Test, count1, high_speed, etc.
  
#Name some types of Values, what function to check the type of a variable

# value is one of the most basic things in any program works with.
# A value may be characters ‘Hello, World!’ or a number like 1,2.etc.
# Values belong to different types: 1 is an integer, 2 is a float and ‘Hello, World!’ is a string etc.
  
  #function to check the type of a variable
 x = 5
print(x, "is of type", type(x))

 z = "hello"
print(z, "is of type", type(z))

#Manual approach of bitwise operation

# Operator	Meaning
# &	           AND
# |	            OR
# ^	            XOR (exclusive OR)
# ~		      Bitwise NOT
# <<	a << n	Bitwise left shift
# >>	a >> n	Bitwise right shift


#Comparing output of '/' and '//'
a=9
b=2

a/b # divides
a//b # Floor Division

#Converting int to str and vice-versa

n = 10
 
print(type(n))
 
# converting the num into string
converted_n = str(n)
 
print(type(converted_n))

# converting the string into num
converted_n = int(n)
 
print(type(converted_n))

#Expressions vs Statements
# A statement is an instruction that the Python interpreter can execute.
#An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated.

age=20
limit=age/4
limit
#above, age/4 is the expression while limit=age/4 is the statement

#Predict output of '/' 
a=10
b=5
a/b

#