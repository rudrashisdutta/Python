# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:36:59 2022

@author: Rudrashis Dutta
"""

test = [[(7, 2), (4, 5)], [(9, 6), (4, 3)]]
addVal = [3, 2]
modTouple = [[tuple(list(idx) + [val]) for idx in key] for key, val in zip(test, addVal)]
print(modTouple)