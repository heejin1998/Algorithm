# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:02:27 2021

실전문제4. 커리큘럼
P. 303
1차 시도: 책 위상정렬 코드 참고하고 만들었는데도 tc 틀림.... 
"""

from collections import deque
n = int(input())
# 모든 노드의 진입차수 0으로 초기화
indegree = [0] * (n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(n+1)]
# 각 과목의 시간 저장할 리스트
time = [0] * (n+1)


# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1,n+1):
    temp = list(map(int, input().split()))
    # temp 그래프에서 
    for j in range(len(temp)):
        if j == 0:
            time[i] = temp[j]
        elif temp[j] == -1:
            break
        else:
            graph[i].append(temp[j]) # 노드 j에서 노드 i로 이동 가능
            indegree[i] += 1
            
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행결과 담을 리스트
    q = deque() 
    
    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        total_time = 0
        now = q.popleft()
        total_time += time[now]
        print(now)
        result.append(total_time)
        
        # 해당 원소와 연결된 노드들의 진입차수에서 1 뺴기
        for i in graph[now+1]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    print(result)          
    # 위상 정렬 수행 결과
    for i in result:
        print(i)
            
topology_sort()
        
            
    
    
    