# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:26:07 2021

@author: p3813
"""
# fiiorst , we assign a variable i and define it

i =0
#then, number is a list variable
number =[]
# while works on logic, until and unless logic become False
#here logic with while

while i <8:
    #we print a statement
    print("at the top i is %d" %i)
#append mean add to the end
    number.append(i)
# here, we give logic i =i+1 then print it in way,as a bottom number
    
    
    i= i+1
# we use variable number in this line , from line 11, number is a list
# we use our new variable i here, i =i+1
    print("numbers now:",number)
    print("at the bottom i is %d" %i)

print ("the number:")
# here we use for loop using num as variable value to number
for num in number:
    print(num)