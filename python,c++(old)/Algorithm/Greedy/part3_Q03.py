# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:03:39 2021

part3_그리디
Q03. 문자열 뒤집기
"""

s = list(map(int, input()))
result = 0 # 최종 결과 저장하는 변수


array = [] # 문자열의 연속된 횟수 저장
count = 0 # 반복되는 횟수 저장

prev = s[0]

# 문자열의 0과 1의 개수 파악
for i in range(len(s)):
    if prev == s[i]:
        count += 1
    else:
        array.append(count)
        count = 1 # 횟수 0으로 초기화
        prev = s[i]
        #print(array)
    
        
array.append(count)

even = 0
odd = 0
# 홀수, 짝수를 기준으로 횟수 계산
for i in range(len(array)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(min(odd, even))