# 정수 삼각형
n = int(input())
dp = [[0] * (n+1) for _ in range(n+1)] # 최댓값 저장

nums = [[0] * (n) for _ in range(n)]
for i in range(n):
    nums[i] = list(map(int,input().split()))

dp[0][0] = nums[0][0]
for i in range(1, n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j-1] + nums[i][j], dp[i-1][j]+nums[i][j])
print(max(dp[n-1]))