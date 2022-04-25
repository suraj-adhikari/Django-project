# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:28:53 2021

@author: p3813
"""
# sys is a library to use argument "argv"
# import mean importing file from project location
from sys import argv
#script and user_name are two argument ,we are currently passing to system
script,user_name = argv
#prompt is use so input come in it
prompt = '>'
# now, you are aware of script %s ,%d and %r 
print("hi %s, I am %s script."%(user_name,script))
print("I would like you to ask few question")
print("do you like me %s?"%user_name)
likes = input(prompt)

print("where do you live %s" %user_name)
place = input(prompt)
 
print("what kind of software do you have?")
software = input(prompt)

print ("""
 Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
 And you have a %r computer. Nice.
 """ % (likes, place , software))
 #after complete a program , run it in command terminal not spyder terminal
