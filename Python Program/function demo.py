# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:30:39 2021

@author: p3813
"""

def percentage(marks):
    p=((marks[0]+marks[1]+marks[2])/300)*100
    return p
marks1= [40,56,66]
percentage1=percentage(marks1)
print(percentage1)
    