# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:20:32 2021

@author: bobae
"""



N, K = map(int, input().split())
count = 0
# N이 K 이상이라면 K로 계속 나누
while N >= K:
    #N이 K로 나눠 떨어지지 않는다면 N에서 1씩 빼기
    while N%K !=0:
        N-=1
        count +=1
    #K로 나누기
    N//=K
    count +=1
    
while N>1 :
    N -=1
    count +=1
    
print(count)