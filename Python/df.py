# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:47:42 2023

@author: Siddhant
"""

bock= int(input("Enter the first number"))
dock= int(input("Enter the second number"))
sum1=bock+dock
difference=bock-dock
product=bock*dock
quotient=bock/dock
remainder=bock%dock
result=sum1+difference+product+quotient+remainder
print(result)
if result%2==0:
    print("The number is even")
else:
    print("The number is odd")