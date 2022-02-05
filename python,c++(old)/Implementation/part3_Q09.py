# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 05:45:50 2021

part3 구현
Q09 문자열 압축

1차 시도: 파이썬 문자열 다루는 실력미숙. cut할 문자 개수를 1개부터 s 문자열 전체까지 for문 돌리면서
s 문자열 내부에서도 for문을 통해 prev, now 리스트를 이용해서 비교 연산을 진행하려고 생각했음. 
그러나 구현 못 함. 또한 abab를 2ab로 바꾸기 위해 리스트를 어떻게 건드려야 할 지 모르겠음 
"""

s = 'abcabc'
s_len = len(s)

for i in range(s_len):
    cut = i # 문자열 잘라 읽는 개수 기준
    count = 1 # 문자가 반복되는 횟수
    start = 0
    prev = s[start:cut]
    for j in range(cut, s_len):
        now = s[j: j+ cut]
        if prev == now:
            count += 1
            prev = now
        else: 
            s[start:j] = str(count) + prev
            start = j
            break
        
print(s)