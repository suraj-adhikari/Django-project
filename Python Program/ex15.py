# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:00:18 2021

@author: p3813
"""
# firstly we import script in command line terminal by python ex15.py

from sys import argv


#we give two argv value to pass on the system
# script=python ex15.py and file_name= sample.txt


script , file_name = argv


#we assign txt variable to open file_name

txt =open(file_name)


# we print file _ name passed by argv
# we print text by using text.read() within larger ()


print("here is your file %s" %file_name)
print(txt.read())

# we want to print sample text again , so we again give first print command 
# raw value input as input()

print("type the file_name again:")
file_again = input(">")


#txt again to open file 
txt_again = open(file_again)

#print file text again
print(txt_again.read())
