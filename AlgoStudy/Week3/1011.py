#Fly me to the Alpha Centauri
# 수학 공식 찾는 문제 -> 숫자 여러개 나열해서 규칙성 찾아야함
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
