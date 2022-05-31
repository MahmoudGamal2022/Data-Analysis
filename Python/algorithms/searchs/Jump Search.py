# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:47:34 2022

@author: MG
"""
# import libs
import time
import math


# start time to calculate time of function
start_time = time.time()

# create jump search function with two arguments arr and given element 
def JumpSearch(arr, x):  

    # calculate block size to jumped
    jump_steps =  int(math.sqrt(len(arr)))
    
    # create two variable that represent the start and end index of block jump  
    left = 0
    right = 0
    
    while left < len(arr) and arr[left] <= x:
        
        right =min(left + jump_steps, len(arr)-1)
        
        if x >= arr[left] and x <= arr[right]:
            break
        
        left += jump_steps
        
    if left >= len(arr) or arr[left] > x:
        
        return print("Number" , x, "is not exsist in array")
    
    
    # Doing a linear search for x in block beginning with prev.
    pointer = left
    right = min(left + jump_steps, len(arr)-1)
    
    while pointer <= right and arr[pointer] <= x:
        
        if arr[pointer]==x:
            return print("Number" , x, "is at index" ,"%.0f"%pointer)
        pointer+=1
        
    return  print("Number" , x, "is not exsist in array")

arr =[11, 12, 19, 24, 26, 30, 34, 37, 38, 40, 45, 49, 50, 54, 55, 62, 65, 73, 90, 91]
x = 2
JumpSearch(arr, x)
print("\nThis took %s seconds." % (time.time() - start_time))
