# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:52:53 2021

part3_Q02 그리디
곱하기 혹은 더하기

1차 시도: TC 2개 맞음 
"""

s = list(map(int, input()))
result = 0 # 최종 결과를 저장할 변수

for i in range(len(s)):
    result = max(result + s[i], result * s[i])
    
print(result)