# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:02:44 2021

@author: p3813
"""
# these are there variable known as list due to [] bracket.

the_count= [1,2,3,4,5]
fruits=['apple','orange','banana','pears','grapes']
change= [1,'pennies',2,'dimes',3,'quarters']
#this is first kind of for loop goes into a series.
#number fruit and i are there variable getting value of above variable
# you can write any word instead of number fruit and i 
#"for" is used for a loop
for number in the_count:
    print("this is the %d" %number)
for fruit in fruits:
    print("A Fruit of type: %s" %fruit)
for i in change:
    print(" I got i %r" % i)

print (type(the_count))

# here , we are using a range in a loop
# fo 0 to 5 we take (0,6)



element= []
for i in range(0,6):
    print("adding %d to the list." %i)
    element.append(i)

for i in element:
    print("element was : %d" %i)