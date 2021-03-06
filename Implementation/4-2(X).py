# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:20:43 2021

@author: bobae
"""

N = int(input())
valids = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
count =0
for h in range(N+1):
    for valid in valids:
        if h == valid:
            count +=1
            continue
    for m in range(60):
        for valid in valids:
            if m == valid:
                count +=1
                continue
        for s in range(60):
            for valid in valids:
                if s == valid:
                    count +=1
                    continue

            
print(count)
    