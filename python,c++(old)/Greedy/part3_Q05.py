# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:38:29 2021

part3_그리디
Q05 볼링공 고르기

1차시도: TC 2개 다 맞음 . 하지만 정답 코드가 더 효율적인 코드임 ㅜㅜ 
"""

n, m =map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(n):
    first = data[i]
    for j in range(i, n):
        second = data[j]
        if first != second:
            #print("("+str(i+1)+",", str(j+1)+")")
            result += 1
    
print(result)

