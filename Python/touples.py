# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:08:23 2023

@author: Siddhant
"""

# create a tuple
my_tuple=(578,18,1.2,10990)
print(my_tuple)
my_tuple[2]
print(my_tuple[-1::-1])
tuple1=(8,3,4,5,["A","B","D","E","Z"])
print(tuple1)
print(tuple1[4][1:4])
tuple1=tuple1*3
print(tuple1)
print(tuple1.count(5))
print(tuple1[4].count("A"))
print(tuple1.index(3,5))
print(8 in tuple1)
print(103 not in tuple1 )
tuple1[4][0]=100
print(tuple1)