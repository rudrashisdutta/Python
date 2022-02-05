# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:32:19 2022

@author: Rudrashis Dutta

5. Write a Python program to square the keys in odd position in a  Dictionary.
"""

d = {1: 100, 2: 200, 3: 300}
print(str(d))
for i in d:
    if (i % 2 != 0):
        d[i] = d[i] ** 2
print(str(d))
