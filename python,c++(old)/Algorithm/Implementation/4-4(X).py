# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:11:35 2021
P. 118
실전 3. 게임 개발

전형적인 시뮬레이션 문제로 삼성 전자 공채 코딩 테스트에 자주 출제되는 대표적 유형

방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
"""

N, M = map(int, input().split())
A, B, d = map(int, input().split())
game_map = []

move_dir = [0, 1, 2, 3]

def escape(A, B):
    if game_map[A][B] == 1:
        return 1
    else:
        return 0
    
for i in range(M):
    row = list(map(int, input().split()))
    game_map.append(row)
check = 0
count = 0 


while(1):
    if game_map[A-1][B] ==0: # 왼쪽에 가보지 않은 칸이 있으면
        d -= 1 # 왼쪽 방향으로 회전
        if d<0:  # 북 -> 서 예외처리
            d = 3 
        A = A-1
        game_map[A][B] = 1 #가본 곳으로 처리
        count += 1
    else : #왼쪽에 가보지 않은 칸이 없으면
        d -=1
        check += 1
        if d<0:
            d = 3
            
    if check ==4: # 4방향 모두 가본 칸이거나 바다로 되어 있는 칸
        if d == 0: #북쪽 바라보고 있을 경우
            B +=1
            if escape(A, B):
                break
        elif d ==1: #동쪽 바라보고 있을 경우
            A -= 1
            if escape(A, B):
                break
        elif d == 2: #남쪽 바라보고 있을 경우
            B -= 1
            if escape(A, B):
                break
            
        elif d ==3: #서쪽 바라보고 있을 경우
            A += 1
            if escape(A, B):
                break
        
        check = 0
        count+=1
        
        
print(count)       
    