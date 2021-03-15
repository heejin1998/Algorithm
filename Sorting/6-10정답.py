# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:46:06 2021

실전 문제 2. 위에서 아래로
p. 178
"""

n= int(input())

array = []

for i in range(n):
    array.append(int(input()))
    
array = sorted(array, reverse = True)

for i in array:
    print(i, end=' ')