# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 09:46:12 2021

@author: p3813
"""
#we can create function by using a word "def" mean define
''' here we create four function name using def are - print_two,print_two_again 
 print_one and print_none. anything begin with letter can be function name
 '''
 # we are giving argument in the same manner but argv change to args
 #here first line like a script with argv
 
 #*args always written within() with colon: to end the line
 #astreik * is used to take all the argument from the script
 
def print_two(*args):
    arg1,arg2 =args
    print("arg1:%r,arg2 %r" %(arg1,arg2))

#*args is  pointless , we can simply do this because we can directly use
#arg1 and arg 2 in() instead args

def print_two_again(arg1,arg2):
    print("arg1:%r,arg2 %r" %(arg1,arg2))
#
#this just takes only one argument

def print_one(arg1):
    print("arg1:%r" %arg1)
#no argument passes
def print_none():
    print("i got no error ")
# now, here  we provide value of argument according to our will.
print_two("suraj","adhikari")
print_two_again("raj","adhikari")
print_one("raj or suraj?")
print_none()