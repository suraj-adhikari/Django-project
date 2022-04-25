# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:31:28 2021

@author: p3813
"""

num= int(input("enter any number \n"))

for i in range(1,11):
    print(str(num) + " X " + str(i) + " = " + str(i*num))    
    
    print(f"{num} X {i}= {num*i}")