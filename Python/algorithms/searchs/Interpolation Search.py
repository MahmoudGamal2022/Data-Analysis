# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:46:42 2022

@author: MG
"""
# import libs
import time

# start time to calculate time of function
start_time = time.time()

# create Interpolaton Search search function with two arguments arr and given element 
def InterpolatonSearch(arr, x):  

    start = 0
    end = len(arr)-1
    # ensure that element in list
    while start <=end and x >= arr[start] and x <= arr[end]:
        # calculate of mid 
        mid = start +(((x-arr[start])*(end-start))//(arr[end]-arr[start]))
        if arr[mid] == x:
            return print("Number" , x, "is at index" ,"%.0f"%mid)
        elif x > arr[mid]:
            start = mid + 1
        elif x < arr[mid]:
            end = mid - 1
    return print("Number" , x, "is not exsist in array")
   
arr =[11, 12, 19, 24, 26, 30, 34, 37, 38, 40, 45, 49, 50, 54, 55, 62, 65, 73, 90, 91]
x = 2
# call function interpolation search 
InterpolatonSearch(arr, x)

print("\nThis took %s seconds." % (time.time() - start_time))