# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:46:28 2021

@author: bobae
"""

import sys
import copy
from collections import deque



def bfs():
    global ans
    temp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2: # 바이러스인 경우
                q.append([i,j]) # queue에 좌표 추가
    while q:
        x, y = q.popleft()
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있을 경우
                if temp_graph[nx][ny] == 0: # 빈 칸
                    temp_graph[nx][ny] = 2 # 바이러스
                    q.append([nx, ny]) # queue에 좌표 추가
    cnt = 0
    for i in temp_graph:
        cnt += i.count(0)
    ans = max(ans, cnt)
 
def wall(x):
    if x == 3: # 벽을 다 세운 경우
        bfs() # BFS 수행
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 빈 칸일 경우
                graph[i][j] = 1 # 벽 세우기
                wall(x+1)
                graph[i][j] = 0 # 최근에 세운 벽을 초기화


               
n, m = map(int, input().split())
graph  = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
q = deque()
wall(0)
print(ans)