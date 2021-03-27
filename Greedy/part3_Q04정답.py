# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:29:21 2021

part3_그리디
Q04 만들 수 없는 금액

정렬을 이용한 그리디 알고리즘. 
그리디 알고리즘에 익숙하지 않으면 문제 해결이 쉽지 않음

화폐 단위를 기준으로 옮차순 정렬
1부터 차례대로 특정금액을 만들수 있는지 확인

"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
print(target)