#Fly me to the Alpha Centauri
# x + k <= y-1이기만 하면 계속 크게 간다.
# 근데 x + k > y-1 보다 커진다? 그러면 이제 + 1만 시킨다
# 마지막에 x+1 == y 이다? 그러면 그냥 1만 더하고 break
t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    d = y-x
    n = 0

    while True:
        if d <= n*(n+1):
            break
        n += 1
    # 총 이동거리가 n의 제곱보다 작거나 같을 때
    if d <= n**2:
        print(n*2-1)
    # 총 이동거리가 n의 제곱보다 클 때
    else:
        print(n*2)
