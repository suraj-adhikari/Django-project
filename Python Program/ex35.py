# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:10:37 2021

@author: p3813
"""
#we import exit from sys , exit is a command use to exit program without error


from sys import exit
#here, we create three function by def- gold room, bear room and evil room

def gold_room():
    print("this room full of gold. how much do you want?")
#here, dead function later define by why    
    next = input(">")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
        dead("man , learn to type a number")
        
    if how_much<50:
        print("nice, you are not greedy,you win!")
        exit()
    else:
        print("you are a greedy man ,you lose!")
        
def bear_room():
    print("there is a bear here")
    print("the bear has a bunch of honey")
    print("the fat bear is in  front of another door")
    print("how are you going to move the bear")
    # a tricky line if bear moved false in this two statement
    
    bear_moved= False
    
    
    while True:
        
        next= input(">")
        
        if next =="take honey":
            dead("the bear looks at you then slap at your face off.")
        elif next=="taunt bear" and not bear_moved:
            print("The bear has moved from the door.You can go through now.")
            
    #bear_moved true in these two statement....all other statement get i dont 
#know        
            bear_moved=True
        elif next=="taunt bear" and bear_moved:
            dead ("The bear get pissed off and chews your leg")
        elif next== "open door"and bear_moved: 
            gold_room()
        else:
            print("i got no idea what that mean.")
def evil_room():
    print(" here you meet great evil dogra")
    print("he,it,whatever stares at you and you go insane")
    print("do you flee for your live or eat your head?")
    
    next= input(">")
    
    if "flee" in next:
        start()
    elif"head" in next:
        dead("well that was tasty")
    else:
        evil_room()
        
def dead(why):
    print (why,"good job!")
    exit(0)
  # from here function will start  
def start():
    print("you are in a dark room ")
    print("there is a door to your right and left")
    print("which one do you take?")
    
    next=input(">")
    
    if next=="left":
        bear_room()
    elif next=="right":
        evil_room()
    else:
        dead("you stumble around the room untill you strave")
        
start()
    
    