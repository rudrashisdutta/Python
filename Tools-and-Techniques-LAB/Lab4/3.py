# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:55:24 2022

@author: Rudrashis Dutta
"""

list1 = [(32, 51), (22,13), (94, 65, 77), (70), (80, 61, 13, 17)]
k = 2

result_list = [element for element in list1 if len(element) != k]
print(result_list)