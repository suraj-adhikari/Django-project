# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:55:19 2021

@author: p3813
"""

num=int(input("enter any number \n"))
prime=True

for i in range(2,num):
    if(num%i ==0):
        prime = False
        break
if prime:
    print("it is a prime number")
else:
    print("it is not a prime number")