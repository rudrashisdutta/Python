# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:32:52 2022

@author: Rudrashis Dutta

7.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
"""

from collections import Counter
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
k = Counter(my_dict)
high = k.most_common(3)

for i in high:
    print(i[0], " :", i[1], " ")
