# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 16:25:57 2023

@author: Siddhant
"""

set2={"Eldertree","Crypt","Warden","Wizard","Pirate Dave"}
action={"Eldertree" ,"Eldertree Collect Souls","Collect orbs to increase health","Use a frozen hammer","Use an orb to kill enemies","Use cannons"}
print(set2|action)
print(set2&action)
print(set2.union(action))
print(set2.intersection(action
                        ))
