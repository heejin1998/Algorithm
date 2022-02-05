# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:25:14 2021

part3 구현
Q11 뱀

9:26~10:10
"""

flag = 0 # 1일시 종료
    

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수

dx = [0, 0, -1, 1]# 상하좌우
dy = [-1, 1, 0, 0]
direction = [0, 1, 2, 3] # 상하좌우

time = 0 # 시간

graph = []
for i in range(n+1):
    temp = []
    for j in range(n+1):
        if i == 0 or i==n or j==0 or j==n: # 벽
            temp.append(1)
        else:
            temp.append(0)
    graph.append(temp)
    
apple = [] # 사과 위치 저장
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    apple.append(temp)
    
    

for i in range(k):
    x, y = map(int, input().split())
    apple[x][y] = 1
    
graph[0][0] = 1 # 뱀 시작 위치 (0,0)
cur_x = 0
cur_y = 0

l = int(input()) # 뱀의 방향 변환 횟수



for i in range(l):
    x, c = map(str, input().split())
    
    for j in range(x):
        if c == 'L': # 왼쪽
            if direction == 0:
                # 여기부터 계속 반복되는 코드라서 함수로 만들면 좋을 거 같
                prev_x, prev_y = cur_x, cur_y
                cur_x += dx[direction]
                cur_y += dy[direction]
               
                if graph[cur_x][cur_y] == 1: # 벽이나 몸통에 부딪혔을 경우
                    flag = 1
                    time += 1
                    break
                else:
                    graph[cur_x][cur_y] = 1
                    
                if apple[cur_x][cur_y] == 1: # 이동한 칸에 사과가 있을 경우
                    apple[cur_x][cur_y] = 0 # 사과 사라짐
                    time += 1
                    
                    continue # 꼬리 안 움직임
                else: # 이동한 칸에 사과가 없을 경우
                    graph[prev_x][prev_y] = 0 # 꼬리 없애기
                    time += 1
                    
            elif direction == 1:
                prev_x, prev_y = cur_x, cur_y
                cur_x += dx[direction]
                cur_y += dy[direction]
               
                if graph[cur_x][cur_y] == 1: # 벽이나 몸통에 부딪혔을 경우
                    flag = 1
                    time += 1
                    break
                else:
                    graph[cur_x][cur_y] = 1
                    
                if apple[cur_x][cur_y] == 1: # 이동한 칸에 사과가 있을 경우
                    apple[cur_x][cur_y] = 0 # 사과 사라짐
                    time += 1
                    
                    continue # 꼬리 안 움직임
                else: # 이동한 칸에 사과가 없을 경우
                    graph[prev_x][prev_y] = 0 # 꼬리 없애기
                    time += 1
                    
                
                
            
                    
               
             
        
    
