# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:01:57 2021

실전문제 4. 미로 탈출
P.153

최단 거리이므로 주변에 길이 없을 경우를 제외하면 오른쪽, 아래쪽으로만 이동해야 함.
아래쪽에 1이면 push


"""


from collections import deque

n, m = map(int, input().split())

graph = []
road  #스택 정의
for i in range(n):
    graph.append(list(map(int,input())))
    
def bfs(x,y):
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        
        
