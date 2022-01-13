# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:14:33 2022

@author: Rudrashis Dutta
"""

l1 = [2, 45, 67, 5, 75]
l2 = []
for i in l1:
    if (i%5 != 0):
        l2.append(i)
print(l2)