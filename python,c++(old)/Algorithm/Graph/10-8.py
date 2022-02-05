# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:33:58 2021

실전문제3. 도시 분할 계획
p. 300

1차 시도: 최소신장트리 책 코드 참고함. TC는 맞음. 코드도 거의 맞음. 다만 MST에서 간선을
하나씩 확인할 때 맨 마지막 간선이 가장 비용이 큰 거 이용하면 좀 더 코드가 간단해짐. 
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선 개수 입력 
v, e = map(int, input().split()) 
# 부모 테이블 초기화
parent = [0] * (v+1)
# 간선 정보 입력받기
edges = []
result = 0
max_edge = 0
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력 받기
for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # 비용을 첫 원소로 삽입
    


edges.sort()


# 간선을 하나씩 확인
for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않았으면 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        # 신장트리에서 가장 큰 간선 값 구하기 
        if c >= max_edge:
            max_edge = c
        

print(result-max_edge)        
    