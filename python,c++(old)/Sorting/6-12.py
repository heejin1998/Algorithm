# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:43:23 2021

실전문제4. 두 배열의 원소 교체
p. 182

1차 시도: △ 금방 풀음. 예시 TC에선 맞으나 예외처리 못해서 틀림 
"""

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # a를 오름차순으로 정렬
b.sort()
b.reverse()


for i in range(k):
    a[i], b[i] = b[i], a[i]
    
result = 0
for i in a:
    result +=i
print(result)
