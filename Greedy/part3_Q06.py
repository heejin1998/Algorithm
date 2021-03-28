# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:36:18 2021

part3 그리디
Q06 무지의 먹방 라이브

1차 시도: TC 32개 중 3개 맞음/ 효율성 테스트 0 (4.0/100.0)
"""

def solution(food_times, k):
    i = 0 # 인덱스 초기화
    for _ in range(k):
        if i >= len(food_times)-1:
            i = 0 # 맨 처음 음식으로 돌아가기
        if food_times[i] == 0: # 음식을 다 먹었을 경우
            i+= 1
            continue # 다음 음식으로 넘어가기
        food_times[i] -= 1 # 음식 1초동안 먹기
        i+= 1
        
    return i