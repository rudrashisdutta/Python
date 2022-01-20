# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:03:04 2022

@author: Rudrashis Dutta
"""



test = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
K = 1
res = 1
for ele in test:
    res *= ele[K]
print(res)