# -*- coding: utf-8 -*-
"""
4번 문제

"""

import heapq
import copy

n = 4
start = 1
end = 4
roads =[[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

def dijkstra(graph, d, start, traps):
    q = []
    heapq.heappush(q,(0,start))
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q) # now: 노드번호 dist: 간선 비용 
        #print("dist:", dist, "now:", now)
        if now in traps: # 현재 노드가 함정이라면
            for i in graph[now]:
                graph[now].remove((i[0],i[1]))
                graph[i[0]].append((now, i[1]))
                
               

        if d[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                                  
    



graph = [[] for _ in range(n+1)] # 그래프
INF = int(1e9)
d =[INF] * (n+1) # 최단 거리 테이블 모두 무한으로 초기화
 
for p, q, s in roads: # 간선 정보 입력받기
    graph[p].append((q,s))
dijkstra(graph, d, start, traps)

print(d) 
answer = d[end-1]                    
        
   
