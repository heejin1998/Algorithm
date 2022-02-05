# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:09:25 2021

실전문제3. 떡볶이 떡 만들기
p. 204
1차 시도: 이진 탐색 문제이긴 한데 단순 구현으로 풀음. -> 입력 값이 매우 크기 때문에 시간 초과 판정받을 듯
"""
import time

n, m = map(int, input().split())

length = list(map(int, input().split()))

start = time.time()
length.sort(reverse = True) #가장 긴 길이의 떡 찾기 위한 정렬
max_length = length[0]

def binary_search(array, target, start, end):
    mid = (start + end) //2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        start = mid + 1
    elif array[mid] > target:
        end = mid - 1
    return None


length.sort() # 길이 리스트 다시 정렬
for i in range(max_length, 0, -1):
    temp = []
    for j in range(len(length)):
        result = length[j] - i
        if result <= 0:
            temp.append(0)
        elif result > 0:
            temp.append(result)
    print(temp)
    if m == sum(temp):
        print(i)
        break
        
end = time.time()
print("Time: ", end - start)
   
