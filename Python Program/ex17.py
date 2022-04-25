# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:14:44 2021

@author: p3813
"""
# here we use two module sys for argv and os.path for exists

from sys import argv

#exists mean if file exist in system or not ,if file exist it say true 
from os.path import exists

script, from_file, to_file = argv
print("copying file from %s to %s" %(from_file,to_file))
#in_file variable is use to perform open function

in_file = open(from_file)
#in_data is used to read in file

indata = in_file.read()
# here len is used to read size of file
print("input file is %s long" %len(indata))

print("does the output file exist? %r" %exists(to_file))
print("ready,hit return to continue, CTRL-C to abort")
input()

out_file = open(to_file,'w')
out_file.write(indata)
print("done")

#here we close first out file open in line29 then in file open in line18
out_file.close()
in_file.close()

 