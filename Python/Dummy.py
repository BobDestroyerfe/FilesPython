# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:52:37 2023

@author: Siddhant
"""

Leap=int(input("Enter a year"))
if(Leap%4==0 and Leap%100==0 and Leap%400==0):
    print("The year is a leap year")
elif(Leap%4==0 and Leap%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")
