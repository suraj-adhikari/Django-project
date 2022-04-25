# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:38:41 2021

@author: p3813
"""
# we are familiar with sys and its argv.

from sys import argv
script, filename =argv
# script and filename are two argv that we pass to the system through command 
#terminal



# simple text printing....
print("we're going to erase %r" %filename)
print("if you do not want that,hit CTRL-C(C).")
print("if you do want that , hit RETURN.")
 
#we are taking input from user for example entre

input("?")
print("opening the file...")

#target as a variable to offer command open read write trubicate etc
#here we use character 'w' so that file open in notepad as a read and write mode

target= open(filename,'w')
# truncating mean empty the file....we open file and empty it

print("truncating the file, good bye")
target.truncate()
# line1,line2,line are input from user
print("now i am going to ask you three lines")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

#these 3 inputs ,now write in a file
print("I am going to write these lines on file")
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")
# here, we close the file
print("and finally we close it")
target.close()