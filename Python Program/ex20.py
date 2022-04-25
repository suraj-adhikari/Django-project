# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:51:58 2021

@author: p3813
"""
#now once again we use system to import argument

from sys import argv
#script python ex20.py and input file test.txt 
script, input_file = argv
#here, we create three function using def or define 
#print all, rewind and print a line as afunction name,it is just a variable 
#and could be anything.

#f is a variable which connect to input_file by current file

def print_all(f):
    print (f.read())
#seek mean reach to back to line . here 0 mean zero line
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print(line_count,f.readline())
# now, we are giving value to our all argument, it is most important part of 
#program

#current file is a variabe and we assingn open input file value to it 
 
current_file= open(input_file)
print("first let's print the whole file :\n")

# the first function we create by def print_all(f)
#now we aasign a current file value = or to (f)

print_all(current_file)

#now, we rewind the f.seek and f= current file


print("let's rewind the file like a tape.")
rewind(current_file)
print("\n")
# in the third program, def we assing two argument to the function
#line count = current value (which assign above the para)
#f= current file
print("let's print these line one by one.\n")
current_line=1
print_a_line(current_line,current_file)
    
current_line = current_line+1
print_a_line(current_line,current_file)

current_line= current_line+1
print_a_line(current_line,current_file)    