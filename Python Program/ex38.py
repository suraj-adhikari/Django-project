# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:11:30 2021

@author: p3813
"""
#here is the list of ten things  where ten things term is variable
#'' is the method of writing a list here

ten_things= 'apple, oranges, crows, telephone, light, sugar'

#we print first line of our program

print("wait  there is not a ten thing in this list ,lets fix that ")

#then, we create new variable stuff, assign it a job to spilt in ten things


stuff = ten_things.split(',')
#we provide new list  more stuff

more_stuff= ["day","night","song","frisbee","corn"," banana"," boy"," girl"]
#!= mean not equal to.. if stuff not equal to ten then...create new variable
#next one which perform pop(mean take from last) of more stuff list
#we print a line
#stuff append mean add one by one to the list
#then print a line...with 10 things


while len(stuff) != 10:
    next_one=more_stuff.pop()
    print("adding",next_one)
    stuff.append(next_one)
    print("there's %d items now." % len(stuff))
    
    
print("there we go:" , stuff)

print("let's do something with stuff.")

#stuff input secondmean 1 as liine start from 0, then -1, pop mean take last 
#one.join by complete line then join specific word 3 and 5


print (stuff[1])
print (stuff[-1])
print (stuff.pop())
print('>' .join (stuff))

print('#'.join(stuff[3:5]))