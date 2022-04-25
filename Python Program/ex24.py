# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:57:05 2021

@author: p3813
"""
''' this is a printing exercise where we use \' for just ' ,\n to next line,
\t fot tab or 5 space, we give poem as a variable asssign it a value and print 
it
'''

print("let's practice everything till,now")
print("you\'d need to know \'bout escape with\\that do\n new lines and \t tabs")
poem=(""" 
\t the lovely world
with logic so firmly planted
cannot discern \nthe needs of love
not comprehend passion from intuition
\and requires an explanation
\n\t where there is none.
""")
print("-----------------")
print (poem)
print("-----------------")
five = (10-2+3-6)
print(" this should be five: %s" %five)

"""
here define function under function name secret_formula and argument started
then, we make a logic with other variables like jellybeans , jars and crates
we, return all these value for action and output

we assign new variable start point, give it value 1000  and equal to perform 
function with our argument started
"""

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
start_point=1000
beans,jars,crates=secret_formula(start_point)


print("with a starting point of %d" %start_point)
print("we have %d beans,%d jars and %d crates" %(beans,jars,crates))

start_point=start_point/10
print("we can also do that this way:")
print("we'd have %d beans,%d jars and %d crates."% secret_formula(start_point))