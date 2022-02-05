# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:31:19 2022

@author: Rudrashis Dutta

1.Write a Python script to sort (ascending and descending) a dictionary by value.
"""

import operator as op
d = {1: 223, 3: 404, 4: 390, 2: 201, 0: 300}
ascending = dict(sorted(d.items(), key=op.itemgetter(1)))
print('Dictionary in ascending order by value : ', ascending)
descending = dict(sorted(d.items(), key=op.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ', descending)
