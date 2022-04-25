# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:59:41 2021

@author: p3813
"""

my_dict= {
    "fast":"in a quick way",
    "furious":"and a quick manner",
    "marks":[1,2,3],
    "another_dict":{"suraj":"adhikari"},
    1:2}

print(my_dict.keys(),)     #all the key like fast, furious etc will print
print("     \n")       # just for looks



print(type(my_dict.keys()))
print("     \n")
print("     \n")


print(list(my_dict.keys()))
print("     \n")
print("     \n")


print(my_dict.values())
print("     \n")
print("     \n")


print(my_dict.items())   # show everything from my_dict

update_dict= {"hard_work":"Success"}
my_dict.update(update_dict)
print(my_dict)