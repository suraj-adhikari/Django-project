# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:19:28 2021

@author: p3813
"""
# wheneverv you use \t symbol ,term "t" is ignored

tabby_cat = ("\tI'm tabbed in.")
# when you use\ it act as a entre and spilt a line into ywo parts.

persian_cat = ("I'm spilt\non a line")
#using \\ two times means apply \ once in a line


blacklash_cat = ("I'm\\a\\cat")

fat_cat = """
I'will do a list :
    \t* Cat food
    \t*Fishes
    \t*Catnip\n\t*Grass
    """
print (tabby_cat)
print (persian_cat)
print (blacklash_cat)
print (fat_cat)

"""

ESCAPE SEQUENCES AND THEIR MEANING

\\ = blacklash(\)
\' =SINGLE quote(')
\" = Double quote(")
\N{name}= character name in unicode data base

"""    
               