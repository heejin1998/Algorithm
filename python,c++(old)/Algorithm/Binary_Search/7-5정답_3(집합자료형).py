# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 00:08:55 2021

실전문제2. 부품찾기
p.197

집합 자료형 버전 정답 

집합 자료형은 단순히 특정 데이터가 존재하는지 검사할 때 매우 효과적으로 사용할 수 있음.
"""

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')