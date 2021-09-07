# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:05:25 2021

@author: prince
"""
# storing and Loading data from databases
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prince@99",
  database="pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#