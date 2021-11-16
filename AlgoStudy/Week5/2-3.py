#K번째 큰 수
from itertools import combinations

n, k = map(int, input().split())
nums = list(map(int,input().split()))
result = list(combinations(nums,3))

sum_result=set()
for r0, r1, r2 in result:
    sum_result.add(r0+r1+r2)


sum_result = list(sum_result)
sum_result.sort(reverse=True)
print(sum_result[k-1])
