# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:38:42 2022

@author: Rudrashis Dutta

WAP Check if a set a subset of another set.
"""

a = {1, 6, 2, 3, 4, 5}
b = {1, 2, 3, 6}
if b.issubset(a):
    print("Is a subset")
else:
    print("Is not a subset")