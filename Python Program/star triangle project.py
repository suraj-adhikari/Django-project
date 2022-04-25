# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:39:59 2021

@author: p3813
"""

def triangle(a):
    b=a-1
    for i in range (0,a):
        for j in range(0,b):
            print(end = " ")
        b=b-1
        for j in range(0, i+1):
            print(" * ",end = "")
        print("\r")
n = 7
triangle(n)