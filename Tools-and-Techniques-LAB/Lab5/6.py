# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:32:46 2022

@author: Rudrashis Dutta

6. Write a Python program to combine two dictionary adding values for common keys.
"""

from collections import Counter
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'d': 100, 'test': 200, 'for': 300}

Cdict = Counter(dict1) + Counter(dict2)
print(Cdict)
