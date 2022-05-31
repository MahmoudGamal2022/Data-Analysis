# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:32:45 2022

@author: MG
"""
# import libs
import time

# start time to calculate time of function
start_time = time.time()

# creat elinear Search function with two arguments arr and given element 
def LinearSearch(arr, x):  

    for pointer in range(len(arr)):
        if arr[pointer] == x:
            return print("Number" , x, "is at index" ,"%.0f"%pointer)
    return print("Number" , x, "is not exsist in array")
    

arr =[11, 12, 19, 24, 26, 30, 34, 37, 38, 40, 45, 49, 50, 54, 55, 62, 65, 73, 90, 91]
x = 2
LinearSearch(arr, x)
print("\nThis took %s seconds." % (time.time() - start_time))
