# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 00:02:02 2021

실전문제2. 부품찾기
p.197

이진탐색 버전 정답 
"""

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result!=None:
        print('yes', end=' ')
    else:
        print('no', end=' ')