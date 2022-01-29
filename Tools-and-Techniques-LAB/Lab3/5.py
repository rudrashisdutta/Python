# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:37:09 2022

@author: Rudrashis Dutta
"""
def count_digs(tup):
    return sum([len(str(ele)) for ele in tup ])

test_list = [(3, 4, 6, 723), (1, 2), (12345), (134, 234, 34)]
test_list.sort(key = count_digs)
print(test_list)