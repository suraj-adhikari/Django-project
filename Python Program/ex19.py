# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:22:22 2021

@author: p3813
"""
# def mean define is to make function and everything under def paragrah is script
# here, you give two argument cheese_count and number of box in function
#cheese and cracker
#then you write a script ,which will be repeated on passing argument values

def cheese_and_crackers(cheese_count,number_of_boxes):
    print("You have %d cheeses" %cheese_count)
    print("You have %d number of box" % number_of_boxes)
    print("that's enough for party")
    print("get a blanket.\n")
    # here we pass first argument value to our function , it can be number ,
#by variable a and b and can be both


# as we pass value under function cheese and cracker ,it pass too the prog
    print("we can give function number directly:")
cheese_and_crackers(20,30)

print("we can give variable to our script")
a=10
b=20
cheese_and_crackers(a,b)

print("we can do the maths inside to:")
cheese_and_crackers(10+20,5+6)

print("we can combine the two variables math")
cheese_and_crackers(a+10,b+20)