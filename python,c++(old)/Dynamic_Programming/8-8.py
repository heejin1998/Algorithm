# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 02:08:22 2021


1차 시도: DP 문제는 점화식을 세워야 하는데 못 세우겠다 ㅜㅜ 
"""

n, m = map(int, input())
array = []
for i in range(n):
    array.append(int(input()))
    
    
d = [0] * 10001

min_money = min(array)
d[min_money] = 1


