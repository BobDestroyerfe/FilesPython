# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:08:26 2023

@author: Siddhant
"""

days1={"Monday","Wednesday","Friday","Sunday"}
days2={"Tuesday","Monday","Thursday","Saturday"}
print(days1.difference(days2))
print(days2-days1)
print(days1.symmetric_difference(days2))
print(days1^days2)
print ("Monday" in days1)
day3={"Monday"}
print(day3<days2)