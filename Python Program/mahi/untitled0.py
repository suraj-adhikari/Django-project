# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:35:25 2021

@author: p3813
"""

my_name ='Suraj Addhikari'
my_age = 24
my_height = 167 # centimeter
my_weight = 70 #kilogram
my_eyes = 'Blue'
my_hair = 'black'
my_teeth = 'white'


#everything is under () is a code and everything under "" is print
# %s is a string format .  it is must to  run the function
print ("let's talk about %s." %my_name)
#observe the use of % before variable
# %d is use for numerical
#where as %s is used for alphabets


print("he's %d cm tall." %my_height)
print("he is %d kg heavy." %my_weight)
print ("he is got %s eyes and %s hair." %(my_eyes,my_hair))
print("his teeth are usually %s in colour." %my_teeth)
print("if i had %d,%d,and %d I get %d" %( my_age, my_height, my_weight, my_age + my_height + my_weight))