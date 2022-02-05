# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 02:32:29 2021

실전문제5. 효율적인 화폐구성
p. 226
"""

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
    

d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j- array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]] +1)

#계산된 결과 출력
if d[m] == 10001: # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])