# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:56:11 2021

part3_그리디
Q05 볼링공 고르기

무게마다 볼링공이 몇 개 있는지 계산해야 함

"""

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
   
    n -= array[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    # n: A가 선택하는 경우의 수, array[i]: B가 선택하는 경우의 수
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기
    
print(result)
