# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:34:59 2021

실전문제3. 개미전사
P. 220

1차 시도: DP 테이블 만드는거 까먹음. TC 틀림 
"""

n = int(input())
food = list(map(int, input().split()))

result = 0
for i in range(len(food)-2):
    prev_result = result
    result += max(food[i], food[i+2])
    print(result)
    

print(result)