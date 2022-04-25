# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:48:56 2021

@author: p3813
"""

people =100
cars=20
buses=8
# difference between if ,elif and else
# if mean a divide like a branch two roads on a highway
#elif mean if one road is wrong accoding to data then we go to this road
#else  mean if their is same data or incorrect data ..show this lines
if cars>people:
    print("we have more cars than people")
elif cars<people:
    print("we need a more cars .")
else:
    print("we can't decide")

if buses>cars:
    print("we have more buses than cars")
elif buses<cars:
    print("we need more buses as compare to cars")
else:
    print("we can't decide")
    
if people>buses:
    print("we have more people than buses")
elif people<buses:
    print("we have a sufficent number of buses")
else:
    print("we can't decide")