# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:43:53 2021

실전문제4. 커리큘럼
P. 303

위상정렬 알고리즘 응용문제

위상정렬을 수행하면서, 매번 간선 정보를 확인하여 결과 테이블 갱신
리스트의 경우, 단순 대입연산을 하면 값이 변경될 때 문제가 발생할 수 있기 때문에,
리스트의 값을 복제해야 할 때는 deepcopy() 함수를 사용해야 한다

"""

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보 담기 위한 연결리스트 초기화
graph= [[] for i in range(v+1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫번째 수는 시간 정보
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과 리스트
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 뺴기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 수행 결과 출력
    for i in range(1, v+1):
        print(result[i])
    
topology_sort()
