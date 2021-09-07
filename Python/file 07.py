# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:37:29 2021

@author: prince
"""

#Writing program to demonstrate deep and shallow copy
# importing copy module
import copy
  
# initializing list 
list1 = [1, 2, [3,5], 4]
  
  
# using copy for shallow copy  
li2 = copy.copy(list1)
print("li2 is : " , li2) 
  
# using deepcopy for deepcopy  
li3 = copy.deepcopy(list1) 
print("li3 is : " , li3) 

#How to combine many series to form a dataframe?
# import pandas library
import pandas as pd
  
# create a series
a = pd.Series(["ABC", "DEF", 
               "GHI"])
  
# create a series
b = pd.Series(["JKL", "MNO", 
               "PQR"])
  
# combine two series then
# create a dataframe
df = pd.DataFrame(a.append(b, 
                  ignore_index = True))
# show the dataframe
df

#Replace items that satisfy a condition with another value in numpy array


import numpy as np
 
arr1 = np.array([49, 7, 44, 27, 13, 35, 71])
 
an_array = np.where(arr1 > 30, 0, arr1)
print(an_array)