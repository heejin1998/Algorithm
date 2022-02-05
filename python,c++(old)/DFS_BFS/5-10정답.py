# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:40:09 2021

실전문제 3. 음료수 얼려 먹기
정답 - DFS 문제, 재귀로 구현 

@author: bobae
"""

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))
    
#DFS로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문

def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] =1
    
        #상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x, y+1) #상
        dfs(x, y-1) #하
        dfs(x-1, y) #좌
        dfs(x+1, y) #우
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result +=1
                
print(result) #정답 출력
