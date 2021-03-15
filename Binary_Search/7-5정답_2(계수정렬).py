# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 00:04:37 2021

실전문제2. 부품찾기
p.197

계수정렬 버전 정답 
"""

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x= list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')