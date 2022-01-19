# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:54:59 2022

@author: Rudrashis Dutta
"""

limit_one, limit_two = 300, 500
result = [item for item in range(limit_one, limit_two+1)]
ans = []
for i in result:
    sum = 0
    for digit in str(i):
        sum += int(digit)
    if sum%2==0:
        ans.append(i)
print(ans)