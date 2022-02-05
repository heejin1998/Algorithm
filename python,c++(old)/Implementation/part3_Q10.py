# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 02:07:07 2021

part3 구현
Q 10 자물쇠와 열쇠

1차 시도: 
    2차원 리스트 key를 회전 이동한다.
    그 다음 key와 lock 리스트를 합친 다음에 lock 리스트의 모든 요소가 1이면 true 반환
    
"""


key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]


N = len(lock)
M = len(key)

temp_lock = [] # 2차원 배열 선언
# 기존 자물쇠의 3배로 늘린 temp_lock 초기화 
for i in range(3*M):
    temp = []
    for j in range(3*M):
        if i >=M and i< 2*M: # 기존의 자물쇠
            if j>=M and j < 2*M:
                print(lock[i-M][j-M], i, j)
                temp.append(lock[i-M][j-M])
            else:
                temp.append(0)
        else:
            temp.append(0)
    temp_lock.append(temp)
    
# 완전 탐색(한 곳에서 회전을 해서 최종 결과 값이 전부 1이 아닐 경우 false)
for i in range(len(temp_lock)):
    for j in range(len(temp_lock[0])):
        # 시간 부족으로 못 풀음 ㅜㅜ 
        
            
print(temp_lock)