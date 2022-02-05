# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:11:56 2021

실전문제3. 전보
p. 262

1차 시도: 다익스트라 알고리즘인 거 파악. 책 보고 참고해서 코드 구현 중.... -> TC 맞음. 맞게 구현함.
답은 sys.stdin.readline 이용해서 입력 받음. 다음에 구현할 땐 책 안 보고 다익스트라 구현하는 것이 좋을 듯 
"""
import heapq


n, m, c = map(int, input().split())

INF = int(1e9)

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]

# 최단거리 테이블 초기화
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    
    
def dijkstra(start): 
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                

dijkstra(c)
count = 0
result = 0
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
        
    elif distance[i] == 0:
        continue
    else:
        count += 1
        result = max(result, distance[i])
        
print(count, result)
        

