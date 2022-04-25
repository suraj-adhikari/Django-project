# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 10:50:47 2021

@author: p3813
"""
#animal is a class and object inherent in it..pass is a object

class Animal (object):
    pass
#dog is a class ,it is inherent animal , def is function in dog class
#self and name are variable , self.name is a ction to give object result

class Dog(Animal):
    
    def __init__(self,name):
        self.name=name
        
class cat(Animal):
    
    def __init__(self,name):
        self.name=name
        
class Person(object):
    def __init__(self,name):
#self.name for name of person and self. pet for pet of person       
        self.name=name
        self.pet=None
class Employee(Person):
    def __init__(self,name,salary):
        super(Employee, self).__init__(name)
        self.salary=salary
        
class Fish(object):
    pass

class salmon(Fish):
    pass
class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = salmon()
harry = Halibut()