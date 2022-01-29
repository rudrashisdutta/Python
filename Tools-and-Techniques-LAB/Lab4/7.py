# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:54:20 2022

@author: Rudrashis Dutta

WAP Add all elements from another set to an existing set & display it.
"""

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

a.update(b)
print(a)