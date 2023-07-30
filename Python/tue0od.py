# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:13:48 2023

@author: Si
ddhant
"""
Constellations=["Scorpio","Torus","Toruk","The Big dipper"]
newlist=Constellations.copy()
print(newlist)
newlist2=list(Constellations)
print(newlist2)
newlist3= Constellations
print(newlist3)
print(id(Constellations))
print(id(newlist))
print(id(newlist2))
print(id(newlist3))
jki=[1,7,2,3,5,6,9,8,4]
jki.sort(reverse=True)
print(jki)
Constellations.sort(reverse=True)
print(Constellations)
result=jki+Constellations
print(result)