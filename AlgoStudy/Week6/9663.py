# N-Queen -> 파이썬 시간초과, pypy 통과
# 퀸은 가로, 세로, 대각성 끝까지 이동 가능

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True


def dfs(x):
    global res
    global visited
    if x == n:
        res += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            dfs(x + 1)


n = int(input())
visited = [False for _ in range(n)]
col = [0] * n
res = 0

dfs(0)
print(res)
