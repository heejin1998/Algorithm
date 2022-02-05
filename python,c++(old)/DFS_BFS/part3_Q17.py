# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 00:57:55 2021

Q17 경쟁적 전염

1차: 시간초과남. tc 2개 맞음
"""
import sys
n, k = map(int, sys.stdin.readline().split())

data = []
temp = [[0] * n for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

s, x_in, y_in = map(int, sys.stdin.readline().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def virus():
    for l in range(1, k+1): # 바이러스 번호 작은 것부터 구현
        for i in range(n):
            for j in range(n):
                if temp[i][j] == l: # 바이러스 만났을 경우
                    dfs(i, j, l)
                    continue

def dfs(x, y, k):
    for i in range(4): # 상하좌우
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < n and nx >= 0 and ny < n and ny >= 0: # 영역 안 벗어날 경우
            if data[nx][ny] == 0: # 감염 안 되었을 경우
                data[nx][ny] = k 
                temp[nx][ny] = data[nx][ny]
   
            
for i in range(s):
    virus()
    

            
print(data[x_in-1][y_in-1])

