# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:50:52 2021

@author: p3813
"""

dictionary= {
    "pankha":"fan",
    "kurshi":"chair"
    ,"ladka":"boy"}

print("available words in dictionary",dictionary.keys())

a= input("enter the hindi word \n")

print(" the meaning of your word is:", dictionary.get(a))
