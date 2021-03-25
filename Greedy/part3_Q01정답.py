# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:17:41 2021

Part 3 그리디
Q01 모험가 길드

공포도를 기준으로 오름차순 정렬
공포도가 가장 낮은 모험가부터 하나씩 확인하며 그룹에 포함될 모험가 수 계산 가능
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1
        count = 0 # 현재 그룹에 포함된 모험가 수 초기화
print(count)