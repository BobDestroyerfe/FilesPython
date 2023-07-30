# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:14:36 2023

@author: Siddhant
"""

Marks=int(input("Enter your marks"))
if(Marks>97):
    print("You got an A+")
elif(Marks>93):
    print("You got an A-")  
elif(Marks>85):
    print("You got a B+")
elif(Marks>75):
    print("You got a B-")
elif(Marks>65):
    print("You got a C+")
elif(Marks>55):
    print("You got a C-")  
elif(Marks>45):
    print("You got a D+")
elif(Marks>38):
    print("You got a D-")
elif(Marks>35):
    print("You got an E+")
elif(Marks>35):
    print("You got an E-")
elif(Marks>23):
    print("You got a F+")
elif(Marks<10):
    print("You got a F- You failed")
else:
    print("You have entered a wrong value please enter a number")
   