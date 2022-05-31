# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:22:10 2022

@author: MG
"""
# import libs
import time


# start time to calculate time of function
start_time = time.time()

# creat recursive binary search function  
def BinarySearch(arr,  start, end, x):  

    if start <=end:
        mid = (start + end ) // 2
        if arr[mid] == x:
            return print("Number" , x, "is at index" ,"%.0f"%mid)
        elif x > arr[mid]:
            return BinarySearch(arr, mid + 1, end, x) 
        elif x < arr[mid]:
            # call function Binary search
            return BinarySearch(arr, start, mid-1, x) 
    return print("Number" , x, "is not exsist in array")

arr =[11, 12, 19, 24, 26, 30, 34, 37, 38, 40, 45, 49, 50, 54, 55, 62, 65, 73, 90, 91]
x = 2
BinarySearch(arr,  0, len(arr)-1, x)

print("\nThis took %s seconds." % (time.time() - start_time))