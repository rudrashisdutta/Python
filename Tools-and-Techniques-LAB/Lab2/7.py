# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:35:45 2022

@author: Rudrashis Dutta
"""

list1 = [6, 95, 47, 23, 71, 28]
for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
print(list1)