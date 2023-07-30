# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:28:53 2023

@author: Siddhant
"""

A=15
if(A>10):
    print("A is greater than 10")
elif(A>0):
    print("A is greater than 0")    
Smiler=int(input("Enter a year")) 
if(Smiler%4==0):
    if(Smiler%100==0):
        if(Smiler%400==0):
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
             
    