# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:27:33 2022

@author: Rudrashis Dutta
"""

l = ['hello', 'hi', 'how are you', 'Rudrashis', 'Dutta']
size = []
for i in l:
    size.append(len(i))
print(l, size, sep='\n')