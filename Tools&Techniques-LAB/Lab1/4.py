# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:45:11 2022

@author: Rudrashis Dutta
"""

a = 10
b = 13
c = 6

print("The greatest among the 3 numbers is", end=' ')
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    print(b)