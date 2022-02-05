# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:39:39 2021

실전문제2. 미래도시
P. 259
1차 시도: 플로이드 워셜 알고리즘인거 답지에서 힌트보고 시작함 + 중간중간 책 코드 참고 -> 양방향 조건 사용 X해서 TC 틀림 
"""

n, m = map(int, input().split())

INF = int(1e9)

graph = [ [INF] * (n+1) for _ in range(n+1)]


# 출발노드와 도착노드 같을 땐 거리 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 그래프 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

    
# X, K 입력받기
x, k = map(int, input().split())


for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min (graph[a][b], graph[a][i] + graph[i][b])
            

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)