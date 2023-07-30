# -*- coding: utf-8 -*-
"""
created on sat mar  4 15:33:55 2023

@author: siddhant
"""

i=1
while (i<=200):
    if(i%2!=0):
        print(i)
    i+=1
rows=5
randomman=69
while(rows>=1):
   count=1
   while(count<=rows):
    print(chr(randomman),end=" ")
    count+=1
   randomman-=1
   rows-=1
   print(" ")
