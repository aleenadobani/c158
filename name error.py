# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:35:43 2023

@author: User
"""

# variable undefined error
a=10
b=20
try:
    print(a)
    print(b)
    print(x)
    
except NameError:
    
     print("variable x is not defined ")
     
print(a+b)