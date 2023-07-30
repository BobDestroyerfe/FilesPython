# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:23:07 2023

@author: Siddhant
"""
flag=True
Number=int(input("Enter a number"))
if Number==1:
    print("It's a unique number")
if Number%2==0 and Number!=2 :
    print("The number is composite")
else:
    divisor=3
    while divisor<=Number-1:
        if Number%divisor==0:
            flag=False
            break
        divisor+=1
    if flag==True:
        print("It is a prime number")
    else:
        print("It is a composite number")
    
          