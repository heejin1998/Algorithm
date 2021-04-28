# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:58:17 2021

part3 Q15 특정 거리의 도시 찾기

단일정점에서 여러곳까지의 최단거리네. 머리속에 떠오르는건 다익스트라다...

1차 시도: 시간초과 ㅋㅋㅋㅋㅋㅋㅋㅋ
"""
import heapq

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]
INF = int(1e9)
# 최단거리 테이블
d = [INF] * (n+1)

def dijkstra(start):
    d[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
    
    
    
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    
    
dijkstra(x)

answer = []

for i in range(len(d)):
    if d[i] == k:
        answer.append(i)
        
if len(answer)==0:
    answer.append(-1)
sorted(answer)

for i in answer:
    print(i)
    
    
    
    