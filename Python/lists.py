# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:58:42 2023

@author: Siddhant
"""
import random
Subjects = ["Maths","Science","SST","Computer","Englsih","Hindi"]
print ( Subjects [2:6] )
for elements in Subjects : 
    print(elements)
for i in range(len(Subjects)):
    print(Subjects [ i ])
for j in range(len(Subjects)-1,-1,-1):
    print(Subjects [ j ])
Games = ["Bedwars", "Among us", "Fall guys" , "Garten of Banban" , "DOORS"]
ACTIONS = ["Break others beds","Who is the imposter?","FALL OR SURVIVE","Survive the kintergarten","Survive through the hotel"]    
Devs = ["Easy.gg Bedwars","Among us Innersloth games", "Fall guys Mediatonic","Euphoric Brothers Garten", "LSPLASH"]    
print("The following developing team"+random.choice(Devs)+"Has developed this game"+random.choice(Games)+"And in that we were"+random.choice(ACTIONS))
    
    