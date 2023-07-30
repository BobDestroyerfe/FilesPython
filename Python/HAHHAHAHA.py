# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:23:04 2023

@author: Siddhant
"""

list1=[1,3,6,9]
list1[2]=100
print(list1)
guns=["Revolver","AK-47","Krige RGL","Hollingsworth 1894","DB Shotgun"]
books=["Harry Pot","Diary of a wimpy kid","Geronimo Sliton","Your mom","The LEGEND OF the dragon"]
guns.append(books)
guns[1:3]=["Webley"]
guns.append("Barret")
guns.insert(1,"Kolibri")
print("Your mom")
print(guns)
print(guns[6])