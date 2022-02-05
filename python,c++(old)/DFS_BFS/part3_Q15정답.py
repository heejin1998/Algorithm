# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:37:31 2021

part3 Q15 특정 거리의 도시 찾기

그래프에서 모든 간선의 비용이 동일할 땐 너비우선탐색(BFS)를 이용하여 최단거리 찾을 수 있음
BFS 시간복잡도 O(N+M)
"""
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    
d = [-1] * (n+1)
d[x] = 0 

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시들 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if d[next_node] == -1:
            # 최단거리 갱신
            d[next_node] = d[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시 번호 오름차순 출력
check = False
for i in range(1, n+1):
    if d[i] == k:
        print(i)
        check = True
# 만약 최단거리가 k인 도시 없다면 -1 출력
if check == False:
    print(-1)            
