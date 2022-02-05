# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:49:33 2021

part3_그리디
Q03. 문자열 뒤집기

전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중 더 적은 횟수를 가지는 경우를 계산

전체 리스트의 원소를 앞에서부터 하나씩 확인하며, 0에서 1로 변경하거나 1에서 0으로 변경하는
경우를 확인하는 방식으로 해결
"""

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
# 두번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i]!= data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))


