# K번째 수
t = int(input())

for l in range(1, t+1):
    n, s, e, k = map(int, input().split())

    nums = list(map(int,input().split()))
    nums = nums[s-1:e]

    nums.sort()
    print("#%d %d" %(l, nums[k-1]))
    