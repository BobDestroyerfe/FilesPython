# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:25:41 2023

@author: Siddhant
"""

qggusau={}
qggusau["I dare u to lick ur toe"]=  input("Truth or Dare Type yes or no?")
print(qggusau)
qggusau["I dare u to stand on ur head"]= input("Truth or dare Type yes or no?")
print(qggusau)
#del qggusau["I dare u to lick ur toe"]
print(qggusau)
deletednote= qggusau.pop('I dare u to lick ur toe')
print(qggusau)
print(deletednote)
poti={1:"Hello",2:"Goodnight",3:"Bye",4:"Cook"}
for keys in poti.values():
    print(keys)
print(len(qggusau))
poti=qggusau.copy()
print(poti)
print(sorted(qggusau))