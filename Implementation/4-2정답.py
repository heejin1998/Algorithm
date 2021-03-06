# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:06:47 2021

@author: bobae
"""


#모든 시각의 걍우를 하나씩 모두 세서 풀 수 있는 문제 -> 완전탐색
# 하루는 86,400초밖에 되지 않기 때문. 
# 일반적으로 데이터가 100만개 이하일 때 완전탐색 적

# H 입력 받기
H = int(input())


count = 0

for i in range(H+1):
    for j in range(60):
        for k in range(60):
            #매 시각 안에 '3'이 포함되면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)
                
                