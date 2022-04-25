# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:27:15 2021

@author: p3813
"""

#     it is inheritance, we have to avoid in class 
# inheritance change in base(parent)  cause change in all sub class(child)
#we create two class parent and child
#child class has inheritance function of parent class as class(parent)
#even though we did give specific implict function in child ,it will show in 
#output
class Parent():
    def implicit(self):
        print ("Parents implicit()")
        
class child(Parent):
    pass
#dad and son ae two variable which equal to parent() and child()

dad= Parent()
son=child()


dad.implicit()
son.implicit()

""" we write a 2nd program here to give seprate output of parent and child
"""
class Parents():
    def implicit(self):
        print("parents implicit")
class child(Parents):
    def override(self):
        print("child override")
        
dad= Parents()
son=child()

dad.implicit()
son.override()


# 3rd way of programming
class Parent(object):
    def altered(self):
        print("parent altered")
class child(Parent):
    
    def altered(self):
        print("child before Parent altered()")

#analyze output, we get parent altered two time, even we give command only once 
#due to present of super  function as child and self argument ... and altered      
        super(child,self).altered()
        print("child after parent altered()")

dad= Parent()
son=child()

dad.altered()
son.altered()















        