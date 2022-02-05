# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:31:31 2022

@author: Rudrashis Dutta

2.Write a Python script to concatenate three dictionaries to create a new one
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
