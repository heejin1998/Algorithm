# 정다면체
n, m = map(int, input().split())

res = [0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1, m+1):
        tmp = i+j
        res[tmp] += 1

max_count = max(res)

for i in range(len(res)):
    if res[i]==max_count:
        print(i, end=' ')
