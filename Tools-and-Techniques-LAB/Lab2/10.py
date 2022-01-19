# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:55:07 2022

@author: Rudrashis Dutta
"""

list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45
result = -1
low = 0
high = len(list1) - 1
mid = 0
while low <= high:
    mid = (high + low)
    if list1[mid] < n:
        low = mid + 1
    elif list1[mid] > n:
        high = mid - 1
    else:  
        result = mid
        break
if result != -1:
    print("Present")
else:
    print("Not Present")