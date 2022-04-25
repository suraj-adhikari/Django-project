# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:58:53 2021

@author: p3813
"""
#def mean define to make a function namme add ( a and b are argument)

def add(a,b):
    print("add %d + %d" %(a,b))
# a real action take place in return,it add value give output and retrn to 
#client or user
    return a+b
def sub(a,b):
    print("sub %d - %d" %(a,b))
    return a-b
def multiply(a,b):
    print ("multiply %d * %d" %(a,b))
    return a*b
def divide(a,b):
    print("divide %d / %d" %(a,b))
    return a/b

print("let's do some maths with function")
#here, we give value to variable
age =add(20,30)
height= sub(78,45)
weight=multiply(90,2)
iq = divide(90,2)

print("age %d height %d , weight %d and iq %d" %(age,height,weight,iq))
print("here, is a puzzle \n")
what = add(age,sub(height,multiply(weight,divide(iq,2))))
print("that becomes:", what,"can you do it by hand?")