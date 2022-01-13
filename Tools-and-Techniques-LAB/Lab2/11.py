# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:30:35 2022

@author: Rudrashis Dutta
"""

my_list = [82, 6, 32, 23, 6, 28]

print("The list is :")
print(my_list)

s = ' '.join([str(elem) for elem in my_list])
if s == s[::-1]:
   print("The list is a palindrome")
else:
   print("The list isn't a palindrome")