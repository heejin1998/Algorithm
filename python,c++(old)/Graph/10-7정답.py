# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:08:45 2021

실전문제2. 팀 결성
p. 298

뭐지 입력하면서 동시에 YES, NO 출력하는데 이게 맞는 걸까..? 
1차 문제점:
    find_parent에서 parent[x]의 값을 루트 노드로 갱신 안하고 호출만 함...
    union_parent에서 a와 b의 루트 노드를 찾지 않음
    
"""

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속합 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [0] * (n+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i
    
# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else: 
            print("NO")