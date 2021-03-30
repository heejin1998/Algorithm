# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:36:18 2021

part3 그리디
Q06 무지의 먹방 라이브

1차 시도: TC 32개 중 21개 맞음/ 효율성 테스트 0 (28.1/100.0)
"""

def solution(food_times, k):
    food_len = len(food_times)
    if sum(food_times) <= k: # 더 섭취해야 할 음식이 없다면
        return -1

    i = 0 # 음식 번호 인덱스 초기화

    while k:
        if food_times[i] == 0: # 음식을 다 먹었을 경우
            i += 1 # 다음 음식으로 이동
        else: # 음식을 먹어야 할 경우
            food_times[i] -= 1 # 음식 시간 감소
            k -= 1
            i += 1 # 다음 음식으로 이동
        if i == food_len:
            i = 0
    return i+1