# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:59:08 2021

part3_그리디
Q04 만들 수 없는 금액

1차 시도: TC 맞긴한데 잘못 구현함. 
"""

n = int(input())
coin = list(map(int, input().split()))

max_money = sum(coin) # 동전으로 만들 수 있는 최대 금액
coin.sort() # 동전단위를 작은 순으로 정렬

result = 0 # 결과 적는 변수

if coin[0] != 1: # 가장 작은 단위가 1이 아닐 경우 최소 금액 1로 반환
    result = 1
    print(result)
    

d = [0] * (max_money+1)
'''
for i in range(n):
    result = 0 # result 변수 초기화
    for j in range(i, n-i):
        result += coin[j]
    print("result",result)
    d[result] = 1 
'''
for i in range(n):
    for j in range(i, n):
        result = 0
        for k in range(i, j):
            result += coin[k]
        print("result",result)
        d[result] = 1 
    
for i in range(1, len(d)):
    if d[i] == 0:
        print(i)

        break
        
    


