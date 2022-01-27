# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:39:36 2022

@author: Rudrashis Dutta

WAP Add an element to a set,find the union ,intersection of elements in a set.
"""

a={"xyz",1,3,5,7,9,11}
b={1,2,3,4,5,5,"abc","xyz"}

a.add(100)
print(a)

c=a.union(b)
print(c)

d=a.intersection(b)
print(d)