# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:12:46 2022

@author: MG
"""

# Python program to display all the prime numbers within an interval

till = int(input("Enter The Till Number:"))

#make constrain that till is range(1,100)
if till >=1 and till <= 1000:
    for num in range(0, till + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num, end=" ")
       
else: 
    print("till is out constrian")