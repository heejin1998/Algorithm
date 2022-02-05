
"""
Created on Tue Apr 27 00:04:29 2021

part3 Q13. 치킨 배달
1차 시도: 일반집의 모든 치킨 거리 구하고 나서, 치킨 
"""



INF = int(1e9)
n, m = map(int ,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split)))
    
chicken = [] # 치킨
chicken_cost = [[0] * n for _ in range(n)] # 치킨 집 장사하는 집 수
house = [] # 집


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집
            house.append((i, j))
        elif graph[i][j] == 2: # 치킨 집
            chicken.append((i, j))
            
chicken_distance = [[INF]*len(chicken)] # 최소 치킨 거리
count = 0
            
for i in house:
    for j in chicken:
        r_1 = i[0]
        c_1 = i[1]
        r_2 = j[0]
        c_2 = j[1]
        new_chicken_distance = abs(r_1 - r_2) + abs(c_1 - c_2)
        if new_chicken_distance < chicken_distance[count]:
            chicken_distance[count] = new_chicken_distance
    chicken_cost[r_2][c_2] += 1
    count += 1
    
# chicken_cost 가장 적은 집 찾기
chicken_cost.sort(reverse=True)
sum_chicken_cost = sum(chicken_cost)
for i in range(m):
    sum_chicken_cost -= chicken_cost[i]

print(sum_chicken_cost)


             
                
            
    



