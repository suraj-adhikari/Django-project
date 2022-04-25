# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:50:23 2021

@author: p3813
"""

a=int(input("enter first number: \n"))
b=int(input("enter second number: \n"))
c=int(input("enter third number: \n"))
d=int(input("enter fourth number: \n"))

if (a>b):
    f1=a
else:
    f1=b
if(c>d):
    f2=c
else:
    f2=d
if (f1>f2):
    print("the greaytes number is:",f1)
else:
    print("the greatest number is :",f2)