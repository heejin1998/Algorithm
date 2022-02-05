# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:44:34 2021

실전 문제 2. 위에서 아래로
p. 178

1차 시도 (3/15): 출력 부분 숫자가 아닌 리스트 전체 출력해서 틀림
"""

n = int(input())
num = []

for i in range(n):
    num.append(int(input()))
    
num.sort()
num.reverse()
print(num, end= ' ')