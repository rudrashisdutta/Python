# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:36:59 2022

@author: Rudrashis Dutta
"""

tup1 = (10, 4, 5, 6)
tup2 = (5, 6, 7, 5)
res = tuple(ele1 % ele2 for ele1, ele2 in zip(tup1, tup2))
print(res)