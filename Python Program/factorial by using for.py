# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:22:31 2021

@author: p3813
"""

num=int(input("enter number"))
factorial=1
for i in range (1,num+1):
    factorial=factorial*i
print(f"the factorial of this {num} is {factorial}")