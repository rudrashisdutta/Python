# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:32:00 2022

@author: Rudrashis Dutta

4. Write a Python program to remove 2nd last key from a dictionary.
"""
d1 = {"Orange": 1, "Apple": 2, "Banana": 3, "Grape": 4}
l = list(d1.keys())
del d1[l[-2]]
print(d1)
