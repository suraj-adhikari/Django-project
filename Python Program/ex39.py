# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:18:59 2021

@author: p3813
"""

#here,states and cities are two dictionary  with element and abbrevation
#[ these bracket  shows list] and {} bracket shows dictionary
#the way to write element in dictionay 'hhhh':'kkjj', and so on....


states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York':'NY',
'Michigan': 'MI'
}

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}
"""we try to add list in dictionary , type dictionary name cities ,open list
['fhfhhf']="jsk" done! that simple
"""

cities['NY']="New York"
cities['OR']="Portland"

#we start printing from taking word from dictionary cities and later 
#states from its abbrevation
#main trick is that 'a':'b' , if you type a it show b and vice versa




print ('- ' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])



print ('- ' * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])


#observe here, state michingam=mi=detroit city ...so it will print detroit
#it is a planning and organizing ability of programmer

print ('- ' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])
print ('- ' * 10)

#we create loop in state and abbrev as a variable and states.items(): as list

for state, abbrev in states.items():
    print ("%s is abbreviated %s" %(state, abbrev))


#similar as above now cities and abbrev as variable
print ('- ' * 10)
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city))
    print ('- ' * 10)


for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" 
           % (state, abbrev, cities[abbrev]))
#if not then print this one.......get is used to check a list
print ('- ' * 10)
state = states.get('Texas', None)
if not state:
    print ("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)