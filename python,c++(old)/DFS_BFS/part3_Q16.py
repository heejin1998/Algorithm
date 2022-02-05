# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:58:04 2021

part3_Q16 연구소
전수 조사 가즈아~
0인 부분들 개수 C 3 계산해야 할듯
"""
from sys import stdin
import itertools
import copy
def spread_virus(x, y, temp_graph):
    if 0<
    
    
    
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

zeros = [] # 빈칸인 부분 좌표 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeros.append((i,j))

candidates = list(itertools.permutations(zeros,3))
result = 0
for  i, way in enumerate(candidates):
    temp_graph = copy.deepcopy(graph)
    
    # 벽 세우기
    for x, y in way:
        temp_graph[x][y] = 1
        
    # 바이러스 퍼뜨리기
    for x, y in way:
        spread_virus(x, y, temp_graph)
   
    
    



        