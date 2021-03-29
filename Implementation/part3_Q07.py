# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 00:45:44 2021

part3 구현
Q07 럭키 스트레이트

1차 시도: BOJ 제출 결과 정답
"""

n = list(map(int ,input()))
mid_len = int(len(n) / 2)

left = 0
right = 0

for i in range(mid_len):
    left += n[i]
    
for i in range(mid_len, len(n)):
    right += n[i]
    
if left == right:
    print("LUCKY")
else:
    print("READY")

    
    
