# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:28:26 2022

@author: MG
"""
# import libs
import time


# start time to calculate time of function
start_time = time.time()

# create linear Search search function 
def  InterpolationSearch(arr,  start, end, x):  

    if start <=end and x >= arr[start] and x <= arr[end]:
        mid = start +(((x-arr[start])*(end-start))//(arr[end]-arr[start]))
        if arr[mid] == x:
            return print("Number" , x, "is at index" ,"%.0f"%mid)
        elif x > arr[mid]:
            return InterpolationSearch(arr, mid + 1, end, x) 
        elif x < arr[mid]:
            return InterpolationSearch(arr, start, mid-1, x) 
    return print("Number" , x, "is not exsist in array")

arr =[11, 12, 19, 24, 26, 30, 34, 37, 38, 40, 45, 49, 50, 54, 55, 62, 65, 73, 90, 91]
x = 2
InterpolationSearch(arr,  0, len(arr)-1, x)

print("\nThis took %s seconds." % (time.time() - start_time))