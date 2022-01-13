# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:24:16 2022

@author: Rudrashis Dutta
"""

l = ['hello', '', '', 'bye', '', 'hi']
print("Original list: ", l)
while('' in l) :
    l.remove('')
print("After removing empty spaces: ", l)