# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:54:51 2022

@author: Rudrashis Dutta
"""

from collections import Counter

tupList = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
freqTuple = [(key, val) for key, val in Counter(tupList).items()]
print(freqTuple)