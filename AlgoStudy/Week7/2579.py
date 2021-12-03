# 계단 오르기 (다시 풀어보기)
n = int(input())
dp = [0] * (n+1)

stairs = [0]
for i in range(n):
    stairs.append(int(input()))
if n==1:
    print(stairs[1])
else:
    dp[0] = 0
    dp[1] = stairs[1]
    dp[2] = stairs[1]+ stairs[2]

    for i in range(3, n+1):
        dp[i] = max(stairs[i]+ stairs[i-1]+ dp[i-3], stairs[i]+ dp[i-2])

    print(dp[n])