# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:11:03 2021

@author: p3813
"""

""" 
here,we show how to import object from dictionary, module and class 
dict style
 mystuff['apples']
 
 
 # module style
 mystuff.apples()
 print mystuff.tangerine
 
 
 # class style
 thing = MyStuff()
 thing.apples()
 print thing.tangerine
 
 
 """
#class is a blueprint of a program ,with the help of class we can create many 
#function
#here, class name song and object is useless, hona na hona sa farak nahi padhta

class song(object):
 #here, we create our first function to get input for our class song'
#__init__ is used to get input in the form of argument self and lyrics
   # we always use self as first argument when ever we use class
    def __init__(self, lyrics):
        
#self.lyric = lyric is a actual function inside class
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)
#now , we give value of song that we used in class in line30,hbd and bulls are
#object
happy_birthday= song(['Happy birthday to you',
                      'May god bless you',
                      'live long'])

bulls_on_parade=song(["they rally around the family"
                       ,"with the pockets full of shells"])
#now, we check a function
#gdgg.gghgh(dot) function is used to check proper function and o/p of function
happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
    