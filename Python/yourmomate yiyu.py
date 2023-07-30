# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:52:57 2023

@author: Siddhant
"""
TalkingTom=["Tom","Ben","Angela","Hank","Hank","Ginger"]
Walt=["Mickey Mouse", "Minnie mouse","Donald Duck",]
TalkingTom.extend(Walt)
print(TalkingTom)
TalkingTom.remove("Hank")
print(TalkingTom)
TalkingTom.pop(-2)
print(TalkingTom)
del TalkingTom[2]
print(TalkingTom)
TalkingTom.clear()
print(TalkingTom)