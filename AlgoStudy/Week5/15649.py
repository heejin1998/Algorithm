from itertools import permutations

n, m = map(int, input().split())
nums = list(range(1,n+1))

result = list(permutations(nums,m))

for r in result:
   for x in r:
       print(x, end=' ')
   print()

