# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 23:45:36 2021

실전문제2. 1로 만들기
P. 217
1차 시도 - 문제 파악을 못 하겠다... 결국 TC 틀림 ㅜ
"""

x = int(input())

count = 0

d = [0] * 30000

while d[1] == 0:
    if x % 5 == 0:
        x /= 5
        print("a, x:",x)
        count += 1
        d[int(x)] = count
    if x % 3 == 0:
        x /= 3
        print("b, x:",x)
        count += 1
        d[int(x)] = count
        
    if x % 2 == 0:
        x /= 2
        print("c, x:",x)
        count += 1
        d[int(x)] = count
        
    else:
        x -= 1
        print("d, x:",x)
        count += 1
        d[int(x)] = count
        

print(d[1])

