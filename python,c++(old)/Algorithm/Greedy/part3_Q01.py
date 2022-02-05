# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:34:14 2021

Part 3 그리디
Q01 모험가 길드
1회: ㅜㅜㅜ 어렵다...... 난이도 1인데 왜 못 푸렁!! 
"""

n = int(input())
array = list(map(int, input().split()))

# 모험가들을 공포도 순으로 정렬
array.sort()

count = 0
result = 0 # 결과 출력
flag = 1
while flag:
    standard = array[0]
    print(standard)
    
    for i in range(standard):
        if array[i] <= standard:
            print("if문", standard)
            continue
        else:
            standard = array[i]
            print("else문", standard)
            print("array 길이", len(array))
            
    for i in range(standard):
        if len(array) < standard:
            flag = 0
            break
        else:
            print("삭제")
            del array[0]
        
        
    count += 1
    print("증가")
    
    
            
    
print(count)