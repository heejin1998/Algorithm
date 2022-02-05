# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:41:33 2021

실전문제2. 팀 결성
p. 298
1차 시도: TC 맞음. 코드도 책 안보고 구현함. -> find_parent랑 union_parent 구현 잘못함 ㅋㅋㅋㅋㅋ 
"""

n, m = map(int, input().split())

parent = [[] for i in range(n+1)]

# 자기 자신의 부모 노드는 자기로 초기화
for i in range(1, n+1):
    parent[i] = i
    

    
def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    if find_parent(parent, a) != find_parent(parent, b):
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return parent


result = [] # 알고리즘 결과 저장하는 리스트   
for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_parent(parent, a, b)
    elif cal == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")
            
for i in result:
    print(i)