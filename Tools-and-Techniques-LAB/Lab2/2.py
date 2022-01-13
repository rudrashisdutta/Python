# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:24:00 2022

@author: Rudrashis Dutta
"""

l = [2,1,4,5,8,7]
print("Original list: ", l)
for i in range(len(l)):
    l[i] = l[i]**3
print("Altered list: ", l)