# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:27:22 2023

@author: Siddhant
"""

import random
People=["Don","Tyler","Walmart","Your mama"]
Things=["Seashells","home","Forks","Phone"]
Locations=["In a city","At the sea shore","In a house","At a restaurant"]
actions = ["found a treasure", "fell in love", "went on an adventure", "discovered a secret"]

character = random.choice(People)
setting = random.choice(Things)
action = random.choice(actions)
locate= random.choice(Locations)

print(f"{character} {action} {setting} {locate}.")