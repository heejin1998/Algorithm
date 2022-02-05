"""
Created on Tue Apr 27 00:04:29 2021

part3 Q13. 치킨 배달
치킨집은 최대 13개로 13개에서 M개를 선택하는 조합과 동일.
이는 100,000을 넘지 않고, 집의 개수 또한 최대 100개이기 때문에 모든 경우의 수
다 계산하더라도 시간 초과 없음

파이썬에선 조합 라이브러리 제공함.

"""
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1: # 일반 집
            house.append((r,c))
        elif data[c] == 2: # 치킨 집
            chicken.append((r,c))
            
# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산
def get_sum(candidates):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집 찾기
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result
# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)

