# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:40:57 2023

@author: Siddhant
"""

my_set = {"Farmer Cletus", "Baker", "Barbarian", "Vulcan", "Grim Reaper"}
p
rint(my_set)
print(type(my_set))
for elements in my_set:
    print(elements)
my_set.add("Adetunde")
print(my_set)
my_set.update(["Hannah", "Evellyn", "Lassy", "Builder", "Zenith"])
print(my_set)
my_set.discard("Hannah")
print(my_set)
my_set.remove("Builder")
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)
