# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:45:18 2022

@author: Rudrashis Dutta
"""
import cmath

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are", sol1, " and ", sol2)