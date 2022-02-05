# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:39:26 2021

실전문제3. 도시 분할 계획
p. 300

전체 그래프에서 2개의 최소 신장 트리를 만들어야 함.
크루스칼 알고리즘으로 MST 만든 다음 MST에서 가장 큰 간선을 제거하면 됨 
"""

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        parent[a] = b
        
# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int ,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선 정보 입력받기
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.add((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

# 간선 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
        
print(result - last)