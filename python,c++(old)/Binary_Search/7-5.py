# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:49:20 2021

실전문제2. 부품찾기
p.197
1차 시도: TC와는 똑같이 출력됨.
"""

n = int(input())
item = list(map(int, input().split()))

m = int(input())
request_item = list(map(int, input().split()))

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
    
    

# 데이터 sort
item.sort() 

for target in request_item:
    result = binary_search(item, target, 0, n-1)
    if(result):
        print("yes", end=' ')
    else:
        print("no", end=' ')






    

